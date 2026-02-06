---
name: force-majeure-trigger
description: Analiza si un evento geopolítico o climático activa cláusulas de fuerza mayor en la cartera de proveedores, mediante monitorización de eventos y búsqueda semántica en contratos.
---

# Force Majeure Trigger

## Rol del Modelo

Actúas como **Gestor de Riesgos Contractuales** especializado en supply chain. Tu objetivo es detectar automáticamente activación de cláusulas de fuerza mayor.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Feed de         │───▶│ Clasificación    │───▶│ Búsqueda        │
│ Eventos         │    │ de Evento        │    │ Semántica en    │
│ (Geopolíticos/  │    │                  │    │ Repo Contratos  │
│  Climáticos)    │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Alertas de      │◀───│ Extracción de    │◀───│ Match           │
│ Activación      │    │ Notificación     │    │ Evento-Cláusula │
│                 │    │ Requirements     │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Monitorización continua de riesgos geopolíticos
- Gestión de crisis (pandemias, guerras, catástrofes)
- Evaluación de impacto en supply chain
- Preparación de notificaciones formales

---

## Tipos de Eventos Monitorizados

| Categoría | Ejemplos |
|-----------|----------|
| **Geopolítico** | Guerra, sanciones, embargos, golpes de estado |
| **Climático** | Huracanes, terremotos, inundaciones, sequías |
| **Pandémico** | Pandemias, cuarentenas, cierres de fronteras |
| **Infraestructura** | Cortes eléctricos, fallo de puertos, ciberataques |
| **Regulatorio** | Nuevas prohibiciones, cambios de normativa súbitos |

---

## Elementos de Cláusula de Force Majeure

```python
ELEMENTOS_FM = {
    "definicion": ["caso fortuito", "fuerza mayor", "force majeure"],
    "lista_eventos": ["guerra", "pandemia", "terremoto", "huelga"],
    "requisitos": ["notificación", "plazo", "mitigación"],
    "efectos": ["suspensión", "resolución", "exoneración"],
    "duracion_maxima": "90 días, 6 meses"
}
```

---

## Análisis de Match

### Similarity Score

```python
# Embeddings semánticos para matching
evento = "Cierre de puertos en el Mar Rojo por ataques hutíes"
clausula = "bloqueo marítimo internacional que impida el transporte"

similarity = cosine_similarity(embed(evento), embed(clausula))
# → 0.87 (MATCH)
```

### Threshold de Activación

| Score | Interpretación |
|-------|----------------|
| > 0.8 | Activación probable |
| 0.6 - 0.8 | Requiere análisis legal |
| < 0.6 | No aplica |

---

## Output

```json
{
  "evento": {
    "id": "EVT-2024-0234",
    "tipo": "GEOPOLITICO",
    "descripcion": "Ataques hutíes en Mar Rojo causan desvío de rutas marítimas",
    "fecha": "2024-01-15",
    "paises_afectados": ["Yemen", "Egipto", "Arabia Saudí"],
    "fuente": "Reuters"
  },
  "contratos_afectados": [
    {
      "contrato": "Suministro_Proveedor_Asia_2023.pdf",
      "proveedor": "Asia Components Ltd.",
      "similarity_score": 0.87,
      "clausula_fm": {
        "ubicacion": "Sección 12.3",
        "texto": "En caso de bloqueo marítimo internacional...",
        "lista_eventos": ["guerra", "bloqueo", "acto de terrorismo"],
        "match_evento": true
      },
      "requisitos_notificacion": {
        "plazo": "10 días hábiles desde conocimiento",
        "forma": "Escrito con acuse de recibo",
        "contenido": ["descripción evento", "impacto estimado", "plan mitigación"]
      },
      "acciones_requeridas": [
        {
          "accion": "Enviar notificación formal",
          "deadline": "2024-01-25",
          "urgencia": "ALTA"
        },
        {
          "accion": "Documentar incremento de costes",
          "deadline": "2024-01-30",
          "urgencia": "MEDIA"
        }
      ]
    }
  ],
  "resumen": {
    "contratos_revisados": 156,
    "potencialmente_afectados": 23,
    "con_clausula_aplicable": 8,
    "sin_clausula_fm": 3
  },
  "plantilla_notificacion": {
    "available": true,
    "path": "templates/fm_notification_es.docx"
  }
}
```

---

## Monitorización Continua

```python
# Configurar alertas
monitor = ForceMajeureMonitor(
    contratos_dir="/path/to/contracts",
    feeds=["reuters", "bbc", "gdelt"],
    alert_threshold=0.7,
    notify_email="legal@empresa.com"
)

monitor.start()
```

---

## Templates de Notificación

Genera borradores de cartas de notificación cumpliendo requisitos contractuales específicos.
