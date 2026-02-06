# Judicial Profiler: Metodología NLP

## Overview

Este documento detalla la pipeline de procesamiento de sentencias utilizando transformers de lenguaje para extraer patrones decisorios judiciales.

## Pipeline Completa

### 1. Ingesta y Limpieza

```
Sentencias PDF/HTML
       ↓
OCR (Tesseract) + Parser estructural
       ↓
Segmentación: Encabezamiento | Hechos | FdD | Fallo
       ↓
Validación de formato (saltos de línea, tablas, referencias)
```

**Validaciones**:
- Detectar cuando OCR falla (confianza <70% en palabras clave legales)
- Segmentar automáticamente usando "FUNDAMENTOS DE DERECHO" como marcador
- Reconstruir párrafos con saltos de línea rotos

### 2. Extracción Estructurada

Usar modelo LLM (GPT-4, Claude) con prompts especializados:

```
Input: [Párrafos de FdD]

Output JSON:
{
  "argumentos": [
    {
      "proposicion": "Incumplimiento contractual Art. 1101 CC",
      "parrafo": 4,
      "postura_juez": "ACOGIDA",
      "confianza": 0.95
    }
  ],
  "fallo": {
    "tipo": "ESTIMATORIA_TOTAL",
    "cantidad": 85000.00,
    "costas": "CONDENACION_COSTAS"
  },
  "tiempo_resolucion_dias": 145,
  "complejidad": 2
}
```

**Métricas de calidad**:
- Validar contra extracción manual en 30 sentencias (f1-score >0.92)
- Revisar casos donde confianza <0.8

### 3. Embedding y Vectorización

**Modelo**: RoBERTa-BNE (entrenado en corpus legislativo español) o mBERT

Para cada argumentación extraída:
1. Tokenizar con modelo español
2. Generar embeddings de dimensión 768
3. Aplicar pooling: representación a nivel de proposición jurídica

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("PlanTL-GOB-ES/roberta-base-bne")
model = AutoModel.from_pretrained("PlanTL-GOB-ES/roberta-base-bne",
                                   output_hidden_states=True)

proposicion = "Incumplimiento contractual Art. 1101 CC"
inputs = tokenizer(proposicion, return_tensors="pt")
outputs = model(**inputs)
embedding = outputs.pooler_output  # [1, 768]
```

**Por qué NO simple keyword matching**:
- "Lucro cesante" sin pericial frecuentemente está en sentencias desestimatorias
- El modelo captura contexto: "lucro cesante reclamado sin prueba de pérdida" ≠ "lucro cesante acreditado"

### 4. Análisis de Sentimiento Jurídico

No usar sentimientos genéricos (positivo/negativo). Usar corpus anotado de sentencias:

**Etiquetas específicas**:
- SEVERO: "Este Juzgado considera que la pretensión carece de base legal"
- NEUTRAL: "La prueba practicada no acredita..."
- BENEVOLENTE: "La alegación del demandante, aunque sucintamente expuesta, resulta procedente"

**Entrenamiento**:
- Anotar 300 párrafos FdD con 3 jueces (Cohen's kappa >0.8)
- Fine-tune RoBERTa para clasificación (3 clases)
- Validar en test set del 20%

### 5. Matriz de Correlación Argumento-Resultado

```
                Estimatoria  Parcial  Desestimatoria
Enriquecimiento    12         2           1
Incumplimiento     18         3           2
Daño Moral          2         1           5
Lucro Cesante       4         1           1
```

**Cálculos**:
- Ratio por argumento: Estimaciones / Total presencias
- Intervalo de confianza 95% (distribución binomial)
- Chi-squared test: ¿Es estadísticamente significativa la diferencia vs. media nacional?

### 6. Detección de Tendencias Temporales

Dividir corpus en 3 periodos:
- Periodo 1: años 2014-2017 (40 sentencias)
- Periodo 2: años 2018-2021 (60 sentencias)
- Periodo 3: años 2022-2024 (56 sentencias)

Comparar ratios de estimación por periodo con test de tendencia (Mann-Kendall):
- Si p-value <0.05, hay tendencia significativa
- Cuantificar cambio por año

### 7. Validación y Control de Calidad

| Métrica | Umbral | Acción |
|---------|--------|--------|
| Confianza media extracción | >0.85 | OK |
| | 0.80-0.85 | Review manual 10% |
| | <0.80 | RECHAZAR corpus |
| F1-score vs. gold standard | >0.92 | OK |
| N sentencias mínimo | >100 | OK |
| | 50-100 | Advertencia en informe |
| | <50 | RECHAZAR análisis |

## Limitaciones Conocidas

1. **Sesgo en CENDOJ**: No todas las sentencias se publican (estimadas 40% publicadas vs. dictatadas)
2. **Cambios en composición**: Si el juez cambió juzgado o se integró en tribunal colegiado, los datos pueden no ser comparables
3. **Precedentes recientes**: Una sentencia de STS puede cambiar línea jurisprudencial del juez; el modelo captura promedio histórico
4. **Casos anómalos**: Litigios complejos con especialistas (Hacienda, UE) pueden tener patrones no generalizables

## Referencias

- Transformers para español: https://huggingface.co/PlanTL-GOB-ES
- Fine-tuning BERT jurídico: "When does pretraining help? Assessing self-supervised learning for law and the CaseHOLD dataset of 53,000+ legal holdings" (Illinois CS, 2021)
- Validación estadística: Agresti & Coull (1998) para intervalos de confianza en proporciones binomiales
