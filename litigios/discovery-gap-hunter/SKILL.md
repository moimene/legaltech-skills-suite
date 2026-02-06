---
name: discovery-gap-hunter
description: Detecta sistemáticamente documentos referenciados pero no aportados mediante análisis estructurado de referencias cruzadas, matching fuzzy multilingüe y cotejo de hashes. Aplicable en discovery bilateral (M&A, arbitraje internacional), exhibición documental (Art. 328-334 LEC), compliance con Hague Convention (solicitudes transfronterizas), GDPR Article 6/17 (cross-border requests). Incluye chain of custody validation, privilege log integration, soporte EN/ES/FR, y detección de duplicados deduplicación mediante MD5/SHA-256.
---

# Discovery Gap Hunter

## Descripción General

Una auditoría forense de documentación requiere identificar:
1. **Documentos referenciados pero no entregados** (ocultación probable)
2. **Documentos entregados bajo nombre diferente** (matching inteligente)
3. **Duplicados y versiones** (deduplicación para evitar solicitudes redundantes)
4. **Cadena de custodia rotos** (metadata faltante, saltos temporales)

Esta skill automatiza lo que un magic circle firm realiza manualmente: rastrear 5.000+ documentos contra 1.000+ referencias en múltiples idiomas, con precisión legal.

**Contextos de aplicación**:
- **M&A discovery**: Seller reclama haber entregado "todos" los documentos
- **Arbitraje internacional** (Hague Convention): Solicitudes de documentos transfronterizas
- **GDPR cross-border** (Reg. UE 2020/1783): Transferencias de datos entre jurisdicciones
- **Litigio mercantil** (Art. 328-334 LEC): Apercibimiento por ocultación

---

## Topología de Aplicación

```
┌──────────────────────────────────────────┐
│ Corpus Documental + Metadata             │
│ - PDFs, docx, xls, eml (1.000-50.000)    │
│ - Metadata: Fechas, remitentes, asunto   │
└────────────────┬─────────────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
  ┌──────────┐      ┌──────────────┐
  │Extracción│      │MD5/SHA-256   │
  │Referencias│      │Deduplicación │
  │(Multilin)│      │              │
  └──────┬───┘      └────────┬─────┘
         │                   │
         └────────┬──────────┘
                  ▼
         ┌─────────────────┐
         │Graph de Refs    │
         │(Doc → Mención)  │
         └────────┬────────┘
                  │
                  ▼
     ┌────────────────────────┐
     │Matching Fuzzy (BM25)   │
     │- Referencias vs. Docs  │
     │- Multilingüe (EN/ES/FR)│
     │- Ranking confianza     │
     └────────┬───────────────┘
              │
         ┌────┴────┐
         ▼         ▼
    ┌────────┐ ┌──────────┐
    │  Gaps  │ │Possibles  │
    │Críticos│ │ Matches   │
    └────────┘ └──────────┘
         │         │
         └────┬────┘
              ▼
    ┌──────────────────┐
    │Reporte Forense   │
    │+ Privilege Log   │
    │+ Chain Custody   │
    └──────────────────┘
```

---

## Cuándo Usar (Triggers Específicos)

### Discovery Bilateral / M&A
- Seller entrega "todos" los documentos
- Buyer necesita validar completitud
- Ejecutar skill para detectar gaps antes de cierre

### Exhibición Documental (Art. 328-334 LEC)
- Recibimos entrega de contraparte bajo apercibimiento
- Auditar: ¿entregó realmente lo que debe?
- Documentar gaps para requerimiento bajo Art. 329 LEC

### Solicitud Transfronteriza (Hague Convention, GDPR)
- Autoridad extranjera solicita documentos específicos
- Validar que cumplimos listado exhaustivamente
- Generar certificado de completitud (chain of custody)

### Compliance Interno (Litigation Hold)
- Gestión de documentación en procedimiento activo
- Verificar no hay referencias sin soporte documental
- Identificar duplicados para reducir volumen

---

## Metodología

### Fase 1: Ingesta y Indexación de Documentos

```
Entrada: Carpeta con documentos (PDF, DOCX, XLS, EML, etc.)

Extracción de metadata:
  - Nombre archivo
  - Fecha creación / modificación
  - Tamaño (bytes)
  - Remitente (si email)
  - Asunto/Título
  - Texto completo (OCR si PDF)

Generación de identificadores:
  - MD5: Hash para deduplicación de contenido
  - SHA-256: Hash para cadena de custodia
  - Nombre normalizado: lowercase, eliminar caracteres especiales
```

### Fase 2: Extracción de Referencias (Multilingüe)

**Patrones en ESPAÑOL**:
```
- "Ver Anexo ([A-Z]|\d+)"
- "(?:según|conforme|tal)\s+(?:el|la|los)\s+(\w+)\s+de\s+fecha"
- "(?:documento|doc\.?|archivo)\s+nº?\s*(\d+)"
- "(?:adjunto|acompaño)\s+(?:original|copia)\s+de"
- "como consta en (?:el|la)\s+(\w+ de \d{1,2}[-/]\d{1,2}[-/]\d{4})"
```

**Patrones en INGLÉS**:
```
- "Exhibit ([A-Z]|\d+)"
- "attached ([A-Za-z\s]+) dated"
- "(?:document|doc\.?)\s+nº?\s*(\d+)"
- "as evidenced in the (?:email|letter|agreement)"
```

**Patrones en FRANCÉS**:
```
- "Annexe ([A-Z]|\d+)"
- "(?:selon|conformément|par)\s+(?:le|la)\s+(\w+)"
- "pièce jointe"
```

**Extracción estructurada** (LLM-assisted):
```json
{
  "referencia": "Ver Anexo A - Contrato de Suministro",
  "tipo_documento": "CONTRATO",
  "fecha_aproximada": "2023-03-15",
  "contexto_completo": "Párrafo 8 de la demanda",
  "criticidad_inferida": "ALTA",
  "palabras_clave": ["suministro", "contrato", "partes", "marzo"]
}
```

### Fase 3: Deduplicación de Documentos

```
Algoritmo:
1. Agrupar documentos por MD5 (contenido idéntico)
   → Ejemplos: Contrato original + copia = 1 grupo
2. Detectar versiones (MD5 similar, cambios menores)
   → Usar Levenshtein distance en embeddings de contenido
3. Generar "documento canónico" por grupo (la primera versión)
4. Mapear todas las versiones a documento canónico
```

**Output**: Reducir 5.000 documentos a 4.200 únicos (800 duplicados detectados).

### Fase 4: Matching Fuzzy (BM25 + Embeddings)

Para cada referencia, buscar matches en corpus documental:

```
Método BM25 (información retrieval):
  score(referencia, documento) =
    Σ IDF(término) × (f(término,doc) × (k1+1)) /
    (f(término,doc) + k1 × (1 - b + b × |doc|/avgdoclen))

Ejemplo:
  Referencia: "Contrato de Suministro de 15/03/2023"
  Matches:
    1. "2023-03-15_suministro_contrato.pdf" (score: 0.92)
    2. "Acuerdo_suministro_marzo_2023.docx" (score: 0.85)
    3. "Email_confirmacion_suministro.eml" (score: 0.61)
```

**Umbrales de confianza**:
- Score > 0.85: Match confirmado (incluir en "posibles matches")
- Score 0.70-0.85: Revisar manualmente (baja confianza)
- Score < 0.70: No reportar (ruido)

### Fase 5: Análisis de Cadena de Custodia

Para documentos críticos, validar:
```
1. ¿Metadata de creación/modificación sensata?
   - Fecha creación posterior a evento ≠ documento original
   - ¿Modificación después de "litigation hold"?
2. ¿Hay saltos en secuencia temporal?
   - Emails: ¿existe thread completo sin saltos?
   - Contratos: ¿versiones intermedias desaparecidas?
3. ¿Hash consistente con archivo digital?
   - Si cliente entregó "original" pero metadata contradice
```

### Fase 6: Clasificación de Gaps

| Tipo Gap | Ejemplos | Criticidad | Acción Legal |
|---|---|---|---|
| **Documento Central** | Contrato principal, correo de decisión | ALTA | Art. 329 LEC - Requerimiento bajo apercibimiento |
| **Prueba Clave** | Email que contradice alegación | ALTA | Moción de completitud en audiencia previa |
| **Documento Secundario** | Confirmación de envío, acuse de recibo | MEDIA | Citar en alegaciones, no obligatorio conseguir |
| **Referencia Ambigua** | "el documento mencionado" sin especificar | BAJA | Documentar para contra-argumentación si contraparte lo cita |

---

## Inputs

| Parámetro | Tipo | Descripción | Validación |
|-----------|------|-------------|---|
| `corpus_dir` | directory | Carpeta con documentos entregados (PDF, DOCX, XLS, EML, etc.) | Mín. 10 documentos |
| `texto_principal` | file | Demanda, reconvención o escrito que contiene referencias | Requerido |
| `idiomas` | string array | Idiomas a analizar (ej. ["es", "en", "fr"]) | Defecto: ["es"] |
| `inventario_csv` | file (optional) | Inventario declarado por contraparte (para cotejo) | Formato: nombre_doc, hash, fecha |
| `excluir_patrones` | string (optional) | Regex de archivos a excluir (ej. logs, temp) | Defecto: ninguno |

**Validación de calidad**:
- Documentos no indexables (corrupto, imagen baja resolución) → Señalar para revisión manual
- Ficheros > 500 MB → Dividir en chunks para análisis

---

## Output

```json
{
  "metadata_analisis": {
    "corpus_size_bytes": 4200000000,
    "documentos_totales": 5127,
    "documentos_unicos": 4320,
    "duplicados_detectados": 807,
    "referencias_detectadas": 1.023,
    "tasa_completitud": "0.68 (68%)",
    "fecha_analisis": "2025-02-06",
    "duracion_procesamiento_min": 12
  },
  "analisis_deduplicacion": {
    "duplicados_por_md5": 807,
    "versiones_detectadas": 34,
    "espacio_recuperado_mb": 850,
    "documentos_canonicos": 4320
  },
  "gaps_criticos": [
    {
      "id_gap": "G001",
      "referencia": "Ver Anexo A - Contrato de Suministro Exclusivo",
      "ubicacion_en_texto": "Hecho Tercero, párrafo 8, línea 45",
      "contexto": "\"...según consta en el Contrato de Suministro Exclusivo de fecha 15/03/2023, cuya copia adjunta como Anexo A...\"",
      "fecha_aproximada": "2023-03-15",
      "criticidad": "ALTA",
      "razon": "Documento contractual central no aportado; prueba esencial de existencia de obligación",
      "matches_parciales": [],
      "accion_legal": "Art. 329 LEC: Requerimiento de exhibición bajo apercibimiento de sanción",
      "referencia_normativa": "Art. 24 CE (derecho a prueba); Art. 316 LEC (carga dinámica)",
      "recomendacion": "Incluir en moción de completitud con orden de depositar en 5 días"
    },
    {
      "id_gap": "G002",
      "referencia": "Email de Juan García de 12/01/2024 confirmando incumplimiento",
      "ubicacion_en_texto": "Hecho Quinto, párrafo 12, línea 78",
      "fecha_aproximada": "2024-01-12",
      "criticidad": "ALTA",
      "razon": "Email que contiene confesión de incumplimiento por la otra parte",
      "matches_parciales": [
        {
          "documento": "email_j_garcia_12_01_2024.eml",
          "confianza": 0.88,
          "motivo_no_matching_perfecto": "Asunto ligeramente diferente ('incumplimiento' vs 'problema')"
        }
      ],
      "accion_legal": "Revisar si el match parcial corresponde; si no, requiere bajo Art. 329",
      "recomendacion": "Validar hash SHA-256 del match parcial contra original contraparte"
    }
  ],
  "gaps_menores": [
    {
      "referencia": "Acta de reunión de 20/02/2024",
      "ubicacion": "Hecho Octavo, línea 102",
      "criticidad": "MEDIA",
      "matches_parciales": [
        {"documento": "reunion_feb_2024.docx", "confianza": 0.72}
      ],
      "recomendacion": "Solicitar aclaración en audiencia previa"
    }
  ],
  "posibles_matches_alto_valor": [
    {
      "referencia": "Contrato de 15/03/2023",
      "matches": [
        {
          "documento": "2023-03-15_suministro_contrato.pdf",
          "score_bm25": 0.91,
          "confianza": 0.91,
          "metadata": {
            "fecha_creacion": "2023-03-15",
            "tamaño_kb": 450,
            "hash_md5": "a1b2c3d4e5f6g7h8i9j0",
            "remitente": "abogada.contraparte@empresa.es"
          },
          "recomendacion": "Confirmar con contraparte que este documento satisface referencia"
        }
      ]
    }
  ],
  "chain_of_custody_findings": [
    {
      "tipo_hallazgo": "SALTO_TEMPORAL_EN_THREAD",
      "documento_afectado": "email_chain_julio_2023.eml",
      "descripcion": "Thread de emails con salto de 8 días entre mensajes 5-6; versión intermedia probablemente existía",
      "criticidad": "MEDIA",
      "accion": "Investigar si thread completo fue aportado"
    },
    {
      "tipo_hallazgo": "METADATA_INCONSISTENTE",
      "documento_afectado": "contrato_final.docx",
      "inconsistencia": "Creación: 2023-03-10, pero texto referencia a 'reunión de 2023-03-20'",
      "criticidad": "BAJA",
      "accion": "Probablemente documento borradores antes de fecha final"
    }
  ],
  "privilege_log_integration": {
    "documentos_potencialmente_privilegiados": 3,
    "recomendacion": "Validar que no fueron entregados bajo privilegio abogado-cliente",
    "detalles": [
      {
        "documento": "email_abogado_interno_04_2024.eml",
        "razon": "Comunicación entre client y su counsel externo",
        "accion": "Verificar si está correctamente reclamado como privilegiado"
      }
    ]
  },
  "estadisticas_resumen": {
    "tasa_completitud_global": 0.68,
    "gaps_criticos": 2,
    "gaps_medianos": 4,
    "gaps_menores": 12,
    "posibles_matches_revisar": 8,
    "confianza_media_matching": 0.84
  },
  "recomendaciones_tacticas": [
    "Priorizar requerimiento de G001 (Contrato central) bajo Art. 329 LEC con plazo de 5 días",
    "Validar matches parciales G002 comparando hashes SHA-256 antes de dar por satisfecho",
    "Investigar saltos temporales en threads de emails (chain of custody)",
    "Solicitar certificado de completitud firmado por contraparte con listado exhaustivo de documentos entregados"
  ],
  "referencias_legales": [
    "Art. 24 CE: Derecho a la tutela judicial efectiva y a la prueba",
    "Art. 316 LEC: Carga dinámica de prueba (quien mejor acceso a documento debe aportarlo)",
    "Art. 328-334 LEC: Procedimiento de exhibición documental (objeto, alcance, apercibimientos)",
    "Art. 329 LEC: Apercibimiento por incumplimiento (multa coercitiva)",
    "Convención de La Haya de 1970: Procedimiento para obtención de prueba en extranjero (Art. 23-27)",
    "Reglamento (UE) 2020/1783: Procedimiento de solicitud de documentos transfronterizo",
    "GDPR Art. 6(1)(c), Art. 17: Obligaciones de cumplimiento y derechos de acceso a información personal",
    "STS 1148/2017: Criterios de relevancia en discovery; no es admisible pedir 'todos los documentos'"
  ],
  "metodologia_detalle": "Ver /references/discovery-matching-bm25.md para técnica de búsqueda"
}
```

---

## Ejemplo Práctico: M&A Discovery (5.000+ Documentos)

**Caso de Uso**: Adquisición de empresa. Seller afirma haber entregado "todos" los documentos. Buyer necesita auditar completitud.

**Entrada**:
- Corpus: 5.127 archivos (4,2 GB) - PDFs, emails, hojas de cálculo
- Texto principal: Documento de diligencia (request list de 1.000+ referencias)

**Proceso**:

1. **Ingesta y deduplicación**
   - Identificar 807 duplicados (16% del corpus)
   - Reducir a 4.320 documentos únicos
   - Ganancia: No solicitar duplicados

2. **Extracción de referencias**
   - 1.023 referencias detectadas en documento de diligencia
   - Clasificar por tipo: contratos (340), emails (410), actas (105), financieros (168)

3. **Matching**
   - 695 referencias con match > 0.85 (baja confianza)
   - 230 referencias con match 0.70-0.85 (revisar)
   - 98 referencias SIN match (gaps)

4. **Análisis de gaps**
   - **2 críticos**: Contrato principal, autorización de accionista
   - **8 medianos**: Emails clave entre ejecutivos
   - **88 menores**: Referencias secundarias

5. **Acción**
   - Requerir bajo apercibimiento (Art. 329 LEC equivalent en otras jurisdicciones)
   - Plazo: 5-10 días
   - Resultado: Seller aporta 12 documentos faltantes, justifica 86 como irrelevantes (carga dinámica)

---

## Plantillas Automatizadas de Oficios LEC

### Template 1: Requerimiento Art. 328 LEC (Exhibición Documental entre Partes)

**Contexto**: Demandado no aportó documentos que constan en la demanda; requiere su exhibición.

**Plantilla automática**:

```
ESCRITO DE REQUERIMIENTO DE EXHIBICIÓN DOCUMENTAL
Art. 328 LEC - Solicitud de documentos específicos

Al Ilmo. Sr. Juez del Juzgado de lo Mercantil [NÚMERO] de [CIUDAD]

De [DEMANDANTE O DEMANDADO], representado por el procurador [NOMBRE],
asistido del letrado [ABOGADO],

EXPONE:

En el litigio que se tramita ante V.I. con número [AUTOS], y en uso de los
derechos que me reconoce el Art. 328 de la Ley de Enjuiciamiento Civil,
**REQUIERO** al demandado [NOMBRE] para que en el plazo de **5 días hábiles**
aporte los documentos siguientes que obran en su poder y resultan imprescindibles
para la prueba de los hechos controvertidos:

DOCUMENTOS REQUERIDOS:
1. [DOCUMENTO 1] - Referencia en demanda: [PÁRRAFO/LÍNEA]
   Descripción: [Título, fecha aproximada, relevancia legal]

2. [DOCUMENTO 2] - Referencia en demanda: [PÁRRAFO/LÍNEA]
   Descripción: [...]

[... continuar con cada documento del análisis de Discovery Gap Hunter ...]

JUSTIFICACIÓN:
- Estos documentos resultan esenciales para la resolución del asunto
- Obran en poder del demandado (conforme a Art. 328.1 LEC)
- La controversia sobre su autenticidad/existencia justifica requerimiento
- Se citaron en la demanda pero no fueron aportados en contestación

APERCIBIMIENTO:
De conformidad con Art. 329 LEC, apercibo al demandado que, de incumplir
el presente requerimiento sin justa causa, podrá incoarse procedimiento
de apremio, con multa coercitiva hasta €600 por día de incumplimiento.

Por todo ello, pido se curse el presente requerimiento.

[FIRMA DEL LETRADO]
[FECHA]
```

**Campos que rellena automáticamente Discovery Gap Hunter**:
- `[DOCUMENTO N]`: Cada referencia detectada como "Gap crítico"
- `[PÁRRAFO/LÍNEA]`: Ubicación exacta en demanda
- `[Descripción]`: Contexto jurídico de por qué es crítico
- Número de documentos, duración plazo, cita jurisprudencial

### Template 2: Requerimiento Art. 332 LEC (Exhibición por Terceros)

**Contexto**: Un tercero (no parte en litigio) tiene documentos necesarios. Ejemplo: Banco, asegurador, agencia.

**Plantilla automática**:

```
ESCRITO DE REQUERIMIENTO DE EXHIBICIÓN A TERCERO
Art. 332 LEC - Documentos en poder de persona ajena al litigio

Al Ilmo. Sr. Juez del Juzgado de lo Mercantil [NÚMERO] de [CIUDAD]

De [PARTE DEMANDANTE], representado por procurador [NOMBRE], asistido de letrado [ABOGADO],

EXPONE:

En el procedimiento mercantil que se tramita ante V.I. con número [AUTOS],
he detectado la necesidad de obtener documentos que obran en poder de tercero
[NOMBRE DEL TERCERO - Empresa/Institución], utilizando el procedimiento
establecido en Art. 332 LEC.

TERCERO REQUERIDO:
- Denominación social: [RAZÓN SOCIAL]
- NIF: [NIF]
- Domicilio: [DIRECCIÓN COMPLETA]
- Relación con litigio: [Bancario/Asegurador/Transportista/etc.]

DOCUMENTOS SOLICITADOS:
1. [DOCUMENTO] - Relevancia: [...]
2. [DOCUMENTO] - Relevancia: [...]

El tercero podrá presentar objeción al requerimiento (Art. 332.3 LEC) si
acredita que los documentos están protegidos por secreto profesional o legal.

PLAZO: **10 DÍAS HÁBILES** contados desde notificación del requerimiento.

Por todo ello, REQUIERO:
1. Se curse requerimiento al tercero [NOMBRE]
2. Se oficie al tercero a depositar documentos en Juzgado

[FIRMA DEL LETRADO]
[FECHA]
```

**Ventaja**: Automatiza identificación de terceros (ej., emails de contraparte mencionan banco X; sistema propone requerimiento).

### Template 3: Prueba Documental Pública (Art. 330 LEC)

**Contexto**: Documentos públicos (registros, licencias municipales, actas notariales) que tercero público debe aportar.

**Plantilla automática**:

```
REQUERIMIENTO DE DOCUMENTACIÓN PÚBLICA
Art. 330 LEC - Documentos en archivos públicos

Al Ilmo. Sr. Juez del Juzgado de lo Mercantil [NÚMERO] de [CIUDAD]

De [PARTE], representado por procurador [NOMBRE], asistido de letrado [ABOGADO],

EXPONE:

Requiero al [ÓRGANO/ARCHIVO PÚBLICO] para que aporte los documentos públicos
siguientes que resultan imprescindibles en el litigio:

DOCUMENTOS PÚBLICOS SOLICITADOS:
1. Acta notarial de [FECHA Y TIPO] - Protocolo notarial del Notario [NOMBRE]
   Relevancia: [Prueba de consentimiento, fecha cierta, etc.]

2. Inscripción registral de [PROPIEDAD/MERCANTIL] - Registro [ESPECIFICAR]
   Descripción: [...]

3. Licencia municipal de [ACTIVIDAD] - Ayuntamiento de [CIUDAD]
   Referencia: [...]

PLAZO: **5 DÍAS HÁBILES** (excepto documentos en archivos históricos: 10 días).

La aportación de documentos públicos es **obligatoria y sin potestad de negarse**
(Art. 330.2 LEC).

[FIRMA DEL LETRADO]
[FECHA]
```

**Integración Discovery Gap Hunter**: Si referencia en demanda menciona "según consta en protocolo notarial de fecha X", sistema genera automáticamente requerimiento al Colegio Notarial.

### Template 4: Exhortos Internacionales (Convenio La Haya 1970)

**Contexto**: Documentos ubicados en extranjero. Solicitud via "letters rogatory" bajo Convenio de La Haya de 1970.

**Plantilla automática** (Compatible con Autoridad Central española - Ministerio de Justicia):

```
DEMANDA INTERNACIONAL DE OBTENCIÓN DE PRUEBA
Convención de La Haya de 14 de marzo de 1970
(Art. 1-27 - Toma de Prueba en el Extranjero)

REMITENTE:
- Juzgado: Juzgado de lo Mercantil [NÚMERO] de [CIUDAD], ESPAÑA
- Asunto: [REFERENCIA DEL LITIGIO]
- Juez Rogante: D./Dña. [NOMBRE JUEZ], NIF [...]

PARTE SOLICITANTE:
[Datos demandante/demandado según corresponda]

DOCUMENTOS SOLICITADOS:
1. [DOCUMENTO] - Ubicación: [País/Empresa/Archivo]
   Descripción detallada: [...]
   Relevancia jurídica: [...]

2. [DOCUMENTO] - Ubicación: [...]

ESTADO EN QUE DEBE CUMPLIRSE LA DILIGENCIA:
- Idioma: [Español/Inglés/Francés/etc.]
- Certificación: SHA-256 + declaración autenticidad por Autoridad Central
- Formato: Original + copia electrónica con sello tiempo

AUTORIDAD CENTRAL DESTINATARIA:
País: [Ej. Francia, Alemania, Italia]
Autoridad Central: [Ej. "Ministère de la Justice - Bureau de l'Entraide Pénale et de l'Exécution des Peines"]

Conforme al Art. 3 del Convenio, requiero que la Autoridad Central designe
persona competente para obtener la prueba documental en el plazo **máximo 60 días**.

[CERTIFICACIÓN JUZGADO]
[SELLO OFICIAL]
[FIRMA JUEZ]

---

NOTA: Esta demanda de prueba será remitida vía Ministerio de Justicia (Autoridad
Central Española) conforme protocolo. Plazo estimado: 90-180 días.
```

**Función Discovery Gap Hunter**:
- Si documento referenciado está en empresa alemana → automáticamente genera Template 4 con Autoridad Central Alemania
- Incluye tiempos estimados (La Haya es lenta; usuario ve 120+ días de espera)

---

## Límites de Acceso: Secreto y Datos Reservados

### Art. 24.2 CE: Derecho a No Declarar Contra Sí Mismo

El descubrimiento de documentos tiene límite constitucional:

**Prohibido solicitar**:
- ❌ Documentos donde demandado confiesa su responsabilidad (derecho a no autoinculparse)
- ❌ Comunicaciones internas donde abogado de demandado asesoró sobre ocultación
- ❌ Emails que demuestran destrucción de prueba (obstruction of justice)

**Permitido solicitar**:
- ✅ Contratos entre partes (aunque desfavorables)
- ✅ Emails donde demandado ofrece solución/reconoce incumplimiento parcial
- ✅ Facturas/recepciones (datos factuales)

**En Discovery Gap Hunter**: Marcar documentos "potencialmente problemáticos" y recomendar consulta al abogado antes de solicitar.

### Secreto Profesional Abogado-Cliente (Arts. 416-417 LEC)

**Protección absoluta**:

| Comunicación | Protegida | Por Qué |
|---|---|---|
| Email cliente → abogado: "Tengo estos hechos ¿qué hago?" | SÍ | Art. 416 LEC |
| Email abogado → cliente: "Recomiendo no enviar documento X a contraparte" | SÍ | Consejo legal |
| Email abogado → abogado de contraparte: "Propongo transacción por €50k" | **NO** | No es secreto |
| Nota interna abogado: "Cliente miente sobre fecha" | SÍ | Opinión legal |
| Email cliente → abogado: "Transferí dinero a cuenta Z el 15/03" | **PARCIALMENTE** | Hecho es descobertible; consejo es secreto |

**En Discovery Gap Hunter**:
- Detectar emails marcados "CONFIDENCIAL - LEGAL ADVICE"
- Marcar como "Privilege Log Entry" (no debe entregarse, pero listar en log)
- Advertencia: Si cliente entregó sin querer, pierde secreto

### Secretos Comerciales (Ley 1/2019 de Secretos Empresariales)

**Definición**: Información que propietario mantiene secreta, con valor económico real, acceso restringido.

| Tipo Documento | Secreto Comercial | Obligación |
|---|---|---|
| Fórmula de producto | SÍ | No descubrimiento; solo abogados + peritos |
| Proceso manufacturación | SÍ | Idem |
| Lista de clientes + precios | SÍ | Idem |
| Estructura de costes | PARCIALMENTE | Pericia comparativa; no divulgar públicamente |
| Estrategia de precios | SÍ | Producción bajo acuerdo de confidencialidad |
| Estudio de mercado (externo) | NO si pagó tercero | Sí si es propio análisis |

**Procedimiento LEC**:
- Art. 328.2 LEC permite demandado "alegar" secreto comercial
- Juez evalúa si realmente es secreto + valor económico
- Si válido, limita descubrimiento a "necessary in interest of justice"

**Discovery Gap Hunter**:
- Si documento que detecta como "Gap" contiene secreto (ej. "Estudio competitivo H1 2025")
- Marcar: "POSIBLE SECRETO COMERCIAL - Verificar con demandado si válido"
- No insistir en requerimiento si defensa es justificada

### Límites RGPD en Solicitudes Transfronterizas (Reglamento 2020/1783)

Si litigio involucra datos personales (nombres, emails, DNIs):

**Prohibido solicitar sin limitación**:
- ❌ Acceso a lista completa de clientes (datos personales masivos)
- ❌ Salarios individuales de empleados (datos sensibles)
- ❌ Información de contacto de testigos (privacidad)

**Permitido con restricción**:
- ✅ Datos imprescindibles para probar hechos litigiosos
- ✅ Nombre + email de ejecutivos que firmaron contrato
- ✅ Datos anonimizados (sin identificar individuos)

**Aplicación en Discovery Gap Hunter**:
```json
{
  "referencia_detectada": "Lista de empleados asignados a proyecto X",
  "tipo_dato": "DATOS PERSONALES (names, emails, salarios)",
  "criticidad": "MEDIA",
  "posicion_rgpd": {
    "permitido": "Nombres + rol (para probar asignación proyecto)",
    "prohibido": "Salarios, datos bancarios, información familiar"
  },
  "recomendacion": "Requiere DATOS ANONIMIZADOS o con consentimiento (Art. 6 RGPD)"
}
```

### Test de Proporcionalidad para Solicitudes de Discovery

Juez puede rechazar solicitud si es **desproporcionada** (Art. 329 LEC):

**Criterios**:
- Número de documentos solicitados (si >5.000 sin justificación = desproporcionado)
- Relevancia (documento debe ser "reasonably calculated to lead to admissible evidence")
- Carga en demandado (costo de búsqueda > beneficio demandante)
- Confidencialidad (afecta terceros, información sensible)

**Ejemplo rechazable**:
- "Aporte TODOS los emails de los últimos 5 años" → DESPROPORCIONADO
- "Aporte emails del 01/03/2023 al 30/06/2023 que mencionen 'contrato suministro'" → PROPORCIONAL

**Discovery Gap Hunter** informa sobre proporcionalidad:
```json
{
  "solicitud_propuesta": "100 documentos críticos",
  "analisis_proporcionalidad": {
    "numero_documentos": "PROPORCIONAL (100 < 1000)",
    "relevancia": "CLARA (cada documento citado en demanda)",
    "carga_demandado": "LEVE (documentos digitales, búsqueda por palabras clave)",
    "confidencialidad": "NINGUNA (documentos comerciales, no secretos)",
    "veredicto": "DEFENSA SOLIDA ante rechazo por desproporción"
  }
}
```

---

## Guías de la Autoridad Central para Convenio La Haya 1970

**Referencia oficial**: Ministerio de Justicia (España) publica guía de procedimiento para solicitudes La Haya:

- **Documento**: "Guía de Procedimiento de Obtención de Prueba en el Extranjero conforme Convenio de La Haya de 1970"
- **URL oficial**: [Ministerio de Justicia - Cooperación Judicial Civil]
- **Autoridad Central española**: Subdirección General de Cooperación Judicial Civil (Ministerio de Justicia)
- **Email**: [cooperacion.judicial@justicia.gob.es]
- **Contacto**: Teléfono +34-91-390-6500

### Procedimiento Práctico

1. **Preparar demanda según Template 4** (arriba)
2. **Remitir al Juzgado** (juez firma certificación)
3. **Juzgado envía a Ministerio de Justicia** (Autoridad Central)
4. **Ministerio transmite a Autoridad Central país destino** (vía canales diplomáticos)
5. **Autoridad Central destino nombra ejecutor** (abogado/comisionado)
6. **Ejecutor obtiene documentos** (plazo típico 60-180 días)
7. **Retorna a Autoridad Central destino** (con sello/certificación)
8. **Remite a Ministerio Justicia España** (via diplomático)
9. **Ministerio entrega a Juzgado** (traduce si necesario, Art. 4 Convenio)
10. **Juzgado notifica a partes** (documentos ingresan en procedimiento)

**Tiempo total**: 4-6 meses (no acelerable; proceso burocrático)

### Casos Especiales

- **USA**: Usa "Letters Rogatory" bajo Convenio La Haya (similar)
- **Reino Unido/UE**: Post-Brexit, verificar si aplicable Reglamento 2020/1783 o La Haya
- **Países no suscritos La Haya**: Requiere cooperación diplomática ad-hoc (aún más lento)

---

## Referencias Metodológicas

Para detalle en:
- Algoritmo BM25: Ver `/references/discovery-matching-bm25.md`
- Deduplicación y chain of custody: Ver `/references/chain-of-custody-validation.md`
- Privilege log integration: Ver `/references/privilege-log-management.md`
