---
name: judicial-profiler
description: Analiza sistemáticamente el perfil decisorio de jueces específicos mediante procesamiento predictivo de sentencias. Identifica patrones argumentativos, predilecciones por tipos de prueba, tendencias en estimación/desestimación y tiempo de resolución medio. Aplicable en: preparación de estrategia litigiosa previa a asignación judicial, optimización de argumentos tras designación de juez, planificación de recursos en apelación, identificación de jueces con sesgo manifiesto. Utiliza transformers NLP, análisis estadístico de 150+ sentencias, y referencias a jurisprudencia consolidada (STS, CGPJ base de datos CENDOJ).
---

# Judicial Profiler

## Descripción General

Construir el perfil decisorio de un juez requiere análisis sistemático de su jurisprudencia histórica. Esta skill automatiza tres tareas que una Magic Circle firm realiza manualmente:

1. **Extracción estructurada**: Fallos, argumentos clave, materia, tiempos de resolución
2. **Análisis de patrones**: Correlación entre tipos de argumentos y estimación (transformers-based NLP, no simple keyword matching)
3. **Generación de recomendaciones tácticas**: Cómo argumentar ante este juez específico

**Límites legales**: Análisis de datos públicos (sentencias disponibles en CENDOJ). No constituye predicción de casos individuales sino descripción estadística de tendencias históricas. Respeta Art. 24 CE (tutela judicial efectiva) y Ley Orgánica del Poder Judicial.

---

## Topología de Aplicación

```
┌─────────────────────────┐
│ Sentencias PDF/HTML     │  Fuentes: CENDOJ, Poder Judicial,
│ (CENDOJ + Poder Jud.)   │  Boletín Oficial Judicial
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Extracción Estructura   │  - Párrafos de FdD
│ (OCR + Parser)          │  - Fallo, Materia, Dinámica
│                         │  - Fechas (entrada/resolución)
└────────────┬────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│ NLP Sentiment + Transformers             │  RoBERTa/mBERT español
│ (Token-level embeddings)                 │  - Argumentos pro/contra
│                                          │  - Tono sentenciador
└────────────┬─────────────────────────────┘
             │
        ┌────┴────┬──────────┐
        ▼         ▼          ▼
   ┌────────┐ ┌────────┐ ┌──────────┐
   │Matriz  │ │Temporal│ │Sensibilidad
   │Correlatoria Trend │ (Cambios juez)
   └────────┘ └────────┘ └──────────┘
        │         │          │
        └────┬────┴──────┬───┘
             ▼
    ┌─────────────────────┐
    │ Perfil JSON + Recs. │
    │ Tácticas Litigiosas │
    └─────────────────────┘
```

---

## Cuándo Usar (Triggers Específicos)

### Preparación de Demanda / Reconvención
- Juez ya asignado: optimizar estructura argumentativa
- Identificar argumentos con máxima ratio de éxito ante este juez
- Evitar líneas argumentativas donde el juez historicamente desestima

### Planificación de Recursos en Apelación
- Evaluar viabilidad de recurso según antecedentes del Juzgado de lo Comercial
- Detectar temas donde este juez sistematicamente pierde en superior
- Priorizar prueba pericial (vs. documental) según predilecciones del juez

### Asignación de Juez (Recursos de Nulidad, Art. 102.2 LOPJ)
- Documentar sesgo manifiesto o desviación extrema vs. jurisprudencia consolidada
- Datos: si juez estima <5% en materia mercantil vs. 40% de media, requiere análisis

### Negociación y BATNA
- Dato objetivo: estimar probabilidad de éxito ante este juez específico
- Fundamentar oferta en predicción estadística, no intuición

---

## Metodología

### Fase 1: Ingesta y Validación

Recolectar sentencias del juez desde CENDOJ y Poder Judicial (últimos 10-15 años):
- Mínimo 100 sentencias de la materia (ideal 150+)
- Validar identificación del juez (NIF contra base CGPJ)
- Descartar resoluciones interlocutorias, recobros cautelares

### Fase 2: Extracción Estructurada (LLM-Assisted)

Para cada sentencia extraer con precisión:
- **Fallo**: Estimatoria total / Parcial (%) / Desestimatoria
- **Materia**: Civil, Mercantil, Laboral, Contencioso, Penal (subsistema)
- **Argumentos clave en FdD**: Identificar proposiciones jurídicas que aparecen en párrafos 3-8
- **Dinamismo probatorio**: ¿Requería prueba pericial? ¿La solicitó de oficio?
- **Tiempo de resolución**: entrada - sentencia en días
- **Complejidad**: número de partes, litigios relacionados

### Fase 3: NLP con Transformers

Aplicar modelo de lenguaje español (RoBERTa-BNE o mBERT) a Fundamentos de Derecho:
- **Token embeddings**: Capturar contexto de argumentos específicos, no simple keyword matching
- **Sentiment en lenguaje jurídico**:
  - Severidad hacia litigante (usar corpus de sentencias anotado)
  - Nivel de exigencia probatoria implícito
- **Extracción de relaciones argumentativas**: "A pesar de que [contraparte], este Juzgado considera que..."

### Fase 4: Correlación Estadística

Matriz N x M:

| Tipo de Argumento | Frecuencia | Estimaciones | Ratio | Intervalo Confianza (95%) |
|---|---|---|---|---|
| Enriquecimiento Injusto | 15 | 12 | 80% | [63%, 97%] |
| Incumplimiento Contractual | 23 | 18 | 78% | [65%, 91%] |
| Daño Moral | 8 | 2 | 25% | [7%, 43%] |
| Lucro Cesante (con pericial) | 6 | 4 | 67% | [33%, 100%] |

Cálculos adicionales:
- **Tendencia temporal**: ¿Ha cambiado la tasa de estimación últimos 3 años?
- **Ratio por materia**: Si es mercantil, diferencial vs. litigios civiles
- **Efecto escala**: ¿Estima mejor cuantías <50k? >200k?

---

### Fase 5: Análisis de Sensibilidad Temporal

Detectar cambios en el perfil del juez:
- Comparar ratios de estimación: primeros 50 casos vs. últimos 50
- ¿Ha endurecido criterio con reformas legales?
- ¿Hay correlación con cambios de composición del juzgado?

---

## Inputs

| Parámetro | Tipo | Descripción | Validación |
|-----------|------|-------------|---|
| `juez_id` | string | NIF del juez o código CGPJ-Poder Judicial | Validar contra base CGPJ |
| `sentencias_dir` | directory | Carpeta con PDFs/HTML de sentencias (CENDOJ export) | Mín. 100 sentencias |
| `materia_filter` | string (optional) | Mercantil/Civil/Laboral/etc. | Normalizar nomenclatura |
| `anos_minimos` | integer | Años atrás a analizar (default: 10) | 5-15 recomendado |

---

## Output

```json
{
  "metadata": {
    "juez": "D. Juan García López",
    "juzgado": "Juzgado Mercantil 3 de Madrid",
    "codigo_cgpj": "280500012",
    "sentencias_analizadas": 156,
    "periodo_analisis": "2014-2024",
    "fecha_informe": "2025-02-06"
  },
  "perfil_decisorio": {
    "tasa_estimacion_global": 0.62,
    "tasa_estimacion_parcial": 0.18,
    "tasa_desestimacion": 0.20,
    "tiempo_medio_resolucion_dias": 145,
    "tendencia_temporal": "ESTABLE_LEVE_ENDURECIMIENTO"
  },
  "argumentos_por_eficacia": [
    {
      "tipo": "Enriquecimiento Injusto",
      "frecuencia": 15,
      "estimaciones": 12,
      "ratio": 0.80,
      "ic_95": [0.63, 0.97],
      "observaciones": "Funciona bien si hay prueba documental clara"
    },
    {
      "tipo": "Incumplimiento Contractual",
      "frecuencia": 23,
      "estimaciones": 18,
      "ratio": 0.78,
      "ic_95": [0.65, 0.91],
      "observaciones": "Requiere pericial en daños"
    },
    {
      "tipo": "Daño Moral",
      "frecuencia": 8,
      "estimaciones": 2,
      "ratio": 0.25,
      "ic_95": [0.07, 0.43],
      "observaciones": "EVITAR: juez exigente con daño moral"
    }
  ],
  "recomendaciones_tacticas": [
    "Enfatizar hechos sobre derecho: juez con ratio 0.95 en estimaciones con prueba documental directa",
    "Evitar argumentos sobre daño moral a menos que sea extremo (STS 2187/2022 como piso mínimo)",
    "Incluir pericial en daños cuantitativos: correlaciona con +15% estimación",
    "Tiempo: presupuestar 140-150 días; si supera 200, requiere investigación de incidencias"
  ],
  "referencias_legales": [
    "Art. 24 CE: derecho a tutela judicial efectiva",
    "Art. 316 LEC: carga de prueba en acciones de daño",
    "STS 2187/2022: estándar mínimo para reconocimiento daño moral",
    "Directiva 2019/1937 (denuncia de irregularidades): aplicada en 3 sentencias del juez"
  ],
  "metodologia_detalle": "Ver /references/judicial-profiler-metodologia-nlp.md"
}
```

---

## Ejemplo Práctico: Preparación de Demanda Mercantil

**Caso de Uso**: Demanda por incumplimiento de contrato de suministro. Juzgado Mercantil 3 de Madrid asignado. Cuantía: 85.000€.

**Proceso**:

1. **Extracción de perfil** (ejecutar skill)
   - Recopilar 156 sentencias del juez (últimos 12 años, materia Mercantil)
   - Ejecutar NLP sobre Fundamentos de Derecho
   - Generar matriz de argumentos

2. **Análisis de resultados**
   - Tasa de estimación global: 62% (vs. 58% media española en mercantil)
   - Argumentos con éxito: Incumplimiento Contractual (78%), Lucro Cesante con pericial (67%)
   - Argumentos débiles: Daño Moral (25%), Reclamación de costas sin cuantificar (30%)

3. **Recomendaciones aplicadas a nuestro caso**
   - **Estructura de demanda**: Iniciar con hechos objetivos (fechas de incumplimiento, emails de comunicación)
   - **Argumento principal**: Incumplimiento contractual Art. 1101 CC (ratio 78% ante este juez)
   - **Cuantificación**: Incluir pericial de daños (correlaciona +15% estimación) → presupuestar €1.200
   - **Evitar**: Argumentos sobre daño moral, reclamaciones difusas de costas sin detallar
   - **Prueba**: Acopiar correspondencia completa; juez estima 95% si hay email trail claro

4. **Estimación de resultado**
   - BATNA = Valor Esperado considerando este juez específico
   - Probabilidad de estimación total: 78% (vs. 62% media)
   - EV = (0.78 × €85.000) - €15.000 (costes) = €51.300
   - Esto mejora el BATNA en +€3.300 vs. juez "medio"

---

## Marco Legal y Ético

**Responsabilidad civil** (Art. 24 CE, tutela judicial efectiva):
- Este análisis es estadístico, no predictivo de caso concreto
- Complementa (no reemplaza) análisis jurídico del fondo
- Se basa en datos públicos disponibles en CENDOJ

**Ley Orgánica del Poder Judicial**:
- Art. 6: imparcialidad de jueces
- Identificar juez con sesgo manifiesto (ratio <10% en materia donde media es 50%) puede justificar Art. 102.2 LOPJ (recusación por causa legal)

**GDPR / Ley Orgánica 3/2018**:
- Las sentencias son datos públicos, no datos personales
- Si se incluye NIF juez, aplicar minimización según AEPD criterios

---

## Inputs

| Parámetro | Tipo | Descripción | Validación |
|-----------|------|-------------|---|
| `juez_id` | string | NIF o código CGPJ del juez | Validar contra base CGPJ oficial |
| `sentencias_dir` | directory | Carpeta con sentencias PDF/HTML (CENDOJ) | Mín. 100 sentencias |
| `materia_filter` | string | Mercantil/Civil/Laboral (opcional) | Normalizar |
| `anos_minimos` | integer | Años atrás a analizar | Defecto: 10 años |

---

## Controles de Sesgo y Explicabilidad

### Detección de Sesgos en el Modelo NLP

El corpus CENDOJ puede contener sesgos sistémicos que distorsionan el análisis:

**Sesgos de género**:
- Análisis de frecuencia de estimación según género de las partes
- Palabras clave género-específicas en Fundamentos: "señor/señora", profesiones estereotipadas
- Métrica: Diferencial de ratio estimación según género de demandante

**Sesgos geográficos**:
- Comparar tasas estimación por Comunidad Autónoma
- Identificar juzgados que sistemáticamente favorecen partes locales
- Normalizar por tamaño de mercado y litigiosidad regional

**Sesgos temporales**:
- Detectar cambios en criterio del juez correlacionados con reforma legal
- Comparar primeros 50 casos vs. últimos 50 años del juez
- Alertar si cambio > 15 pp (puntos porcentuales) en corto plazo

### Explicabilidad mediante SHAP (SHapley Additive exPlanations)

Para cada clasificación de sentimiento/estimación:

```python
# Calcular importancia de features
import shap

explainer = shap.TreeExplainer(modelo_estimacion)
shap_values = explainer.shap_values(features)

# Output: Qué tokens/argumentos causaron predicción
# Ej: "Argumento 'lucro cesante' contribuyó +0.23 a probabilidad de estimación"
```

**Aplicación práctica**: Usuario puede consultar "¿Por qué dice que este argumento tiene 80% de éxito?" → Sistema muestra SHAP breakdown.

### Intervalos de Confianza (No Estimaciones Puntuales)

**Nunca reportar**: "Probabilidad de éxito: 78%"

**Siempre reportar**: "Probabilidad de éxito: 78% [IC95: 65%-91%]"

- Calcular IC mediante bootstrapping de corpus (remuestreo aleatorio 1.000 iteraciones)
- Si IC muy amplio (>25 pp), advertencia: "Confianza baja por muestra pequeña"
- Número mínimo de casos por argumento: 8 (si <8 ocurrencias, no reportar probabilidad)

### Programa de Auditoría Periódica de Sesgos

| Frecuencia | Acción | Responsable |
|---|---|---|
| Trimestral | Análisis de sesgo género/geografía en corpus actualizado | Data science team |
| Semestral | Validación de SHAP consistency (¿mismos argumentos tienen misma importancia?) | Chief Data Officer |
| Anual | Auditoría externa independiente de sesgo (ex. Deloitte / AEPD) | Cumplimiento |
| Evento | Si ratio estimación cambia >15 pp en 6 meses → investigación inmediata | Product |

---

## Logs de Auditoría y Trazabilidad

### Esquema de Audit Log Obligatorio

Cada análisis ejecutado debe generar registro inmutable:

```json
{
  "audit_id": "JP-2025-02-06-001",
  "timestamp_inicio": "2025-02-06T14:30:15Z",
  "timestamp_fin": "2025-02-06T14:35:42Z",
  "usuario_id": "abogado@bufete.es",
  "juez_analizado": "D. Juan García López (280500012)",
  "sentencias_procesadas": 156,
  "modelo_version": "judicial-profiler-v2.3.1",
  "configuracion": {
    "anos_minimos": 10,
    "materia_filter": "Mercantil",
    "umbral_confianza_minimo": 0.70
  },
  "resultados_generados": {
    "tasa_estimacion_global": 0.62,
    "argumentos_procesados": 23,
    "gaps_confianza_baja": 2
  },
  "controles_ejecutados": {
    "deteccion_sesgo_genero": "OK",
    "deteccion_sesgo_geografico": "OK",
    "shap_values_calculados": true,
    "intervalos_confianza_incluidos": true
  },
  "alertas": [
    "ADVERTENCIA: Ratio 'daño moral' basado en solo 8 casos (confianza baja)"
  ],
  "usuario_descargo": {
    "timestamp": "2025-02-06T14:35:42Z",
    "confirmacion": "Usuario reconoce que herramienta es apoyo, no predicción de fallo"
  }
}
```

### Política de Retención de Logs (RGPD Art. 5(1)(e))

- **Retención mínima**: 3 años (para auditoría legal)
- **Retención máxima**: 5 años (principio de minimización RGPD)
- **Destrucción segura**: Borrado criptográfico (no restaurable)
- **Acceso restringido**: Solo administrador + Chief Data Officer; auditoría de acceso mensual

### Controles de Acceso

| Acción | Quién | Autorización |
|---|---|---|
| Ver perfil judicial (lectura) | Cualquier abogado autenticado | Nivel 1 |
| Descargar informe JSON | Abogado + Cliente (titular caso) | Nivel 2 |
| Modificar parámetros NLP | Solo Data Science team | Nivel 3 |
| Ver audit logs | Chief Data Officer + General Counsel | Nivel 4 |
| Ejecutar reentrenamiento modelo | Solo CEO + CTO | Nivel 4 |

---

## Políticas de Uso Ético

### Descargo de Responsabilidad (Obligatorio en Cada Uso)

**Texto que usuario debe aceptar antes de generar análisis**:

> **DESCARGO DE RESPONSABILIDAD - JUDICIAL PROFILER**
>
> 1. **Herramienta de apoyo, no predicción**: Este análisis constituye una descripción estadística de patrones históricos del juez, basada en sentencias públicas (CENDOJ). **NO es predicción del fallo en su caso concreto**, ni sustituye el análisis jurídico profesional de su abogado.
>
> 2. **Art. 24 CE - Límites legales**:
>    - Independencia judicial garantizada: El uso de este análisis para solicitar recusación requiere causa legal específica (Art. 102.2 LOPJ), no puede basarse únicamente en estadísticas.
>    - Prohibición de listas negras: Bajo ninguna circunstancia se crearán listas de jueces a "evitar". Cada caso es único.
>    - Publicidad de criterios: Los parámetros y algoritmo son públicos y auditables (no "caja negra").
>
> 3. **Limitaciones del análisis**:
>    - Sesgo histórico: Si juez ha resuelto mal históricamente, modelo lo captura (pero no predice mejor comportamiento futuro).
>    - Cambios legislativos: Reformas legales pueden cambiar criterio; modelo no predice adaptación judicial.
>    - Complejidad del caso: Variables no cuantificables (habilidad de abogados, prueba sorpresa) no están en modelo.
>
> 4. **Certificación**: He leído y entiendo que esta herramienta es **solo orientativa**.
>
> □ Acepto términos y condiciones de uso ético

### Límites Legales Específicos (Art. 24 CE + LOPJ)

**Prohibido**:
- ❌ Crear "ranking de jueces favorables/desfavorables" para distribución de demandas
- ❌ Solicitar cambio de juez basado solo en estadísticas sin causa legal específica
- ❌ Usar perfil para intimidar a contraparte ("este juez nunca estima daño moral")
- ❌ Vender "reporte de sesgo de juez" a terceros sin certificación AEPD

**Permitido**:
- ✅ Orientar argumentación interna (preparación demanda)
- ✅ Calcular BATNA con probabilidades sustentadas en Judicial Profiler
- ✅ Documentar sesgo extremo (ratio <5% en materia con media 50%) como elemento probatorio en recurso de recusación (Art. 102.2 LOPJ)
- ✅ Usar en mediación/arbitraje como base de negociación racional

### Cumplimiento RGPD

Los datos de entrada (sentencias) son **públicos**; sin embargo:

- **Minimización**: No almacenar datos de partes/abogados del juez; solo análisis agregado
- **Propósito limitado**: Análisis jurídico; prohibido vender perfiles de jueces a terceros
- **Derechos de datos**: Si usuario solicita borrar su análisis de logs, cumplir en 30 días
- **No categorías especiales**: Nunca procesar datos sobre origen étnico, religión, etc. del juez (aunque sean públicos)

---

## Referencias y Metodología Detallada

Para profundizar en la metodología NLP y referencias jurisprudenciales, consultar:
- `/references/judicial-profiler-metodologia-nlp.md`: Pipeline de transformers, validación estadística
- `/references/jurisprudencia-consolidada.md`: STS, CGPJ resoluciones sobre análisis predictivo
