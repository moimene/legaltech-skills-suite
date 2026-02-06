---
name: judicial-profiler
description: Predice la inclinación de un juez específico ante ciertos argumentos, analizando sus sentencias previas mediante NLP Sentiment Analysis y correlación estadística.
---

# Judicial Profiler

## Rol del Modelo

Actúas como **Analista de Jurisprudencia** especializado en análisis predictivo. Tu objetivo es construir un perfil del comportamiento decisorio de un juez basándote en su historial de sentencias.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────┐    ┌───────────────────┐
│ Sentencias PDF  │───▶│ OCR/Parser   │───▶│ Extractor de      │
│ (Histórico)     │    │              │    │ Fallo + Argumentos│
└─────────────────┘    └──────────────┘    └─────────┬─────────┘
                                                     │
                                                     ▼
┌─────────────────┐    ┌──────────────┐    ┌───────────────────┐
│ Perfil JSON     │◀───│ Correlación  │◀───│ NLP Sentiment     │
│ del Juez        │    │ Estadística  │    │ Analysis          │
└─────────────────┘    └──────────────┘    └───────────────────┘
```

---

## Cuándo Usar

- Preparar estrategia litigiosa según el juez asignado
- Identificar tipos de argumentos con mayor éxito ante el juez
- Detectar patrones de estimación/desestimación por materia
- Anticipar tiempo medio de resolución

---

## Metodología

### Fase 1: Ingesta de Sentencias

```python
# Cargar todas las sentencias del juez
sentencias = load_sentencias_by_juez(id_juez="12345")
```

### Fase 2: Extracción Estructurada

Para cada sentencia extraer:
- **Fallo**: Estimatoria / Desestimatoria / Parcial
- **Materia**: Civil, Mercantil, Laboral, etc.
- **Argumentos clave**: Párrafos del Fundamento de Derecho
- **Tiempo de resolución**: Fecha entrada vs. fecha sentencia

### Fase 3: Análisis de Sentimiento

Aplicar NLP sentiment analysis a:
- Lenguaje usado hacia el demandante
- Lenguaje usado hacia el demandado
- Tono general del fallo (severo/neutro/benevolente)

### Fase 4: Correlación Estadística

| Tipo Argumento | Veces Usado | Estimaciones | Ratio |
|----------------|-------------|--------------|-------|
| Enriquecimiento Injusto | 15 | 12 | 80% |
| Incumplimiento Contractual | 23 | 18 | 78% |
| Daño Moral | 8 | 2 | 25% |

---

## Inputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `juez_id` | string | Identificador del juez (NIF o código interno) |
| `sentencias_dir` | directory | Carpeta con PDFs de sentencias |
| `materia_filter` | enum | Filtrar por materia (opcional) |

---

## Output

```json
{
  "juez": {
    "nombre": "D. Juan García López",
    "juzgado": "Juzgado Mercantil 3 de Madrid",
    "sentencias_analizadas": 156
  },
  "perfil": {
    "tasa_estimacion_global": 0.62,
    "tiempo_medio_dias": 145,
    "tendencia_sentiment": "NEUTRAL_SEVERO"
  },
  "argumentos_favorables": [
    {"tipo": "Enriquecimiento Injusto", "ratio": 0.80},
    {"tipo": "Incumplimiento Contractual", "ratio": 0.78}
  ],
  "argumentos_desfavorables": [
    {"tipo": "Daño Moral", "ratio": 0.25},
    {"tipo": "Lucro Cesante", "ratio": 0.30}
  ],
  "recomendaciones": [
    "Enfatizar carácter objetivo del incumplimiento",
    "Evitar reclamaciones de daño moral sin pericial",
    "Aportar abundante prueba documental (juez orientado a hechos)"
  ]
}
```

---

## Consideraciones Éticas

> Esta skill proporciona análisis estadístico basado en datos públicos (sentencias).
> No predice decisiones individuales sino tendencias históricas.
> El secreto de las deliberaciones judiciales permanece intacto.
