# Discovery Gap Hunter: Matching con BM25

## Algoritmo BM25 (Best Matching 25)

Es el estándar industrial en información retrieval para encontrar documentos relevantes dado una query (referencia).

## Fórmula

```
score(Q, D) = Σ_i IDF(q_i) * (f(q_i, D) * (k1 + 1)) / (f(q_i, D) + k1 * (1 - b + b * |D| / avgdl))

Donde:
  Q = Query (referencia a documento)
  D = Documento candidato
  q_i = término i-ésimo de Q
  f(q_i, D) = frecuencia de q_i en D
  |D| = longitud de D en tokens
  avgdl = longitud media de documentos en corpus
  IDF(q_i) = log((N - n(q_i) + 0.5) / (n(q_i) + 0.5))
    donde N = total documentos, n(q_i) = documentos con q_i
  k1 = parámetro tuning (típicamente 1.2-1.5)
  b = parámetro tuning (típicamente 0.75)
```

## Intuición

```
IDF(término):
  - Palabras comunes ("de", "el", "contrato"): IDF bajo
  - Palabras raras ("suministro", "Juan"): IDF alto

f(término, doc) / (f(término, doc) + k1 * ... ):
  - Saturación: 100 apariciones de "suministro" no vale 100× más que 1 aparición
  - Normalización por longitud: documentos largos no penalizados
```

## Ejemplo Práctico

### Caso 1: Match Perfecto

```
Query (referencia): "Contrato de Suministro Exclusivo de 15/03/2023"
Tokens: [contrato, suministro, exclusivo, 15/03/2023]

Documento candidato 1:
Nombre: "2023-03-15_suministro_contrato_exclusivo.pdf"
Contenido (primeras líneas):
  "CONTRATO DE SUMINISTRO EXCLUSIVO
   Celebrado en Madrid, 15 de marzo de 2023
   Entre [empresa A] y [empresa B]..."

Cálculo:
  - IDF(contrato) = log(4320 / 287) ≈ 2.4
  - f(contrato, doc) = 5 (apariciones en documento)
  - IDF(suministro) = log(4320 / 142) ≈ 3.1
  - f(suministro, doc) = 12
  - IDF(exclusivo) = log(4320 / 89) ≈ 3.6
  - f(exclusivo, doc) = 8
  - IDF(15/03/2023) = log(4320 / 1) ≈ 8.4 (muy raro)
  - f(15/03/2023, doc) = 2

Score = 2.4*(5*2.2)/(5+1.2*...) + 3.1*(12*2.2)/(12+1.2*...) + 3.6*(8*2.2)/(8+1.2*...) + 8.4*(2*2.2)/(2+1.2*...)
      ≈ 0.91 (MATCH FUERTE)
```

### Caso 2: Match Parcial

```
Query: "Email de Juan García de 12/01/2024 confirmando incumplimiento"

Documento candidato 2:
Nombre: "email_j_garcia_12_01_2024.eml"
Contenido:
  "From: juan.garcia@empresa.es
   Date: 2024-01-12
   Subject: Problema en suministro
   Body: ...como te mencione ayer, hay un problema con el suministro..."

Análisis:
  - Query tiene: [email, juan, garcía, 12/01/2024, confirmando, incumplimiento]
  - Documento tiene: [juan, 12/01/2024] (2 de 6 términos)
  - FALTA: "incumplimiento" (hay "problema" como sinónimo, pero BM25 no lo captura)
  - Asunto dice "Problema" no "Incumplimiento"

Score = 3.8*(2*2.2)/(2+1.2*...) + 8.3*(1*2.2)/(1+1.2*...) ≈ 0.72 (MATCH DÉBIL)

Conclusión: Probablemente match correcto, pero requiere revisión manual
```

## Mejoras: Normalización Semántica

Para reducir falsos negativos (matches que se pierden por sinónimos), añadir:

### 1. Normalización de Entidades Nombradas

```python
# Extender query expandiendo entidades
query_original = "Email de Juan García de 12/01/2024"
entities = extract_ner(query_original)
  # → [PERSONA: Juan García, DATE: 12/01/2024]

# Variaciones:
query_expandida = [
  "Email de Juan García de 12/01/2024",
  "Email de juan.garcia de 2024-01-12",
  "Email juan garcía 2024-01-12",
  "Email j.garcía 12-01-2024"
]

# Buscar con cada variación, tomar max score
scores = [bm25_score(q, doc) for q in query_expandida]
mejor_score = max(scores)
```

### 2. Sinonimia Jurídica

```python
# Diccionario de sinónimos legales (ES)
sinonimos = {
  "incumplimiento": ["falta de cumplimiento", "violación", "quebrantamiento"],
  "contrato": ["acuerdo", "convenio", "pacto"],
  "documento": ["archivo", "fichero", "escrito"],
  "email": ["correo", "mensaje de correo", "comunicación por mail"]
}

# Expandir query con sinónimos
query_expandida = expand_with_synonyms(query_original, sinonimos)
# → [email, correo, mensaje correo, ...] ∪ [incumplimiento, violación, ...]
```

### 3. Embeddings Semánticos

Para máxima precisión, usar modelo de embeddings (complementario a BM25):

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

query_embedding = model.encode("Email de Juan García confirmando incumplimiento")
doc_embeddings = [model.encode(doc_text) for doc in corpus]

# Cosine similarity (captura significado, no solo palabras)
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
```

**Ventaja**: Captura que "incumplimiento" ≈ "problema" semánticamente
**Desventaja**: Más lento; usar solo si BM25 < 0.75

## Validación de Matches

### Scoring Multidimensional

No usar solo score BM25. Combinador:

```
score_final = 0.7 * score_bm25
            + 0.2 * score_fecha_match
            + 0.1 * score_extensión_archivo

Donde:
  score_fecha_match: 1.0 si fechas coinciden exactas, 0.5 si ±7 días, 0.1 si ±3 meses
  score_extensión: 1.0 si extensión esperada (PDF para "contrato"), 0.7 si neutral
```

### Umbrales de Decisión

| Score Final | Decisión | Acción |
|---|---|---|
| > 0.85 | MATCH confirmado | Reportar como match |
| 0.70-0.85 | Match probable | Revisar manualmente; incluir en "posibles matches" |
| 0.50-0.70 | Incierto | Ignorar a menos que sea documento crítico |
| < 0.50 | No match | No reportar |

## Validación Contra Inventario Declarado

Si contraparte proporcionó inventario CSV:

```
Inventario declarado:
  nombre_doc, hash_md5, fecha, tipo
  "contrato_suministro.pdf", "a1b2c3d4", "2023-03-15", "CONTRATO"
  "email_juan.eml", "e5f6g7h8", "2024-01-12", "EMAIL"

Para cada match en corpus:
  1. Buscar documento en inventario por hash_md5
  2. Si no encontrado → Gap (documento entregado pero no declarado)
  3. Si encontrado → Confirmado (documento declarado y efectivamente entregado)
  4. Documento en inventario pero no en corpus → Gap crítico
```

## Referencias

- Robertson, S., & Zaragoza, H. (2009). "The Probabilistic Relevance Framework: BM25 and Beyond"
- Okapi BM25 library: https://github.com/dorianbrown/rank_bm25
- SentenceTransformers: https://www.sbert.net/
- Legal AI: "Latent Dirichlet Allocation for Contract Understanding" (NeurIPS 2021)
