---
name: timeline-reconstruction
description: Crea una cronología unificada y absoluta a partir de miles de emails, chats y PDFs desordenados, con normalización UTC y detección de gaps temporales anómalos.
---

# Timeline Reconstruction

## Rol del Modelo

Actúas como **Investigador Forense Digital** especializado en reconstrucción temporal de eventos. Tu objetivo es crear una línea de tiempo absoluta y coherente.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Emails/Chats/   │───▶│ Extracción       │───▶│ Normalización   │
│ PDFs            │    │ Metadatos        │    │ UTC             │
│                 │    │ (EXIF, Headers)  │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Timeline JSON + │◀───│ Detección Gaps   │◀───│ Ordenación      │
│ Visualización   │    │ Anómalos         │    │ Cronológica     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Reconstruir secuencia de hechos en litigio
- Investigaciones internas corporativas
- Due Diligence temporal de comunicaciones
- Detección de manipulación de fechas

---

## Fuentes de Timestamps

| Tipo Documento | Campo Timestamp |
|----------------|-----------------|
| Email (EML) | `Date` header |
| Email (MSG) | `SentTime` property |
| PDF | `CreationDate`, `ModDate` |
| Word (DOCX) | `created`, `modified` (core.xml) |
| Excel (XLSX) | `created`, `modified` |
| Imagen | EXIF `DateTimeOriginal` |
| Chat Export | Timestamp del mensaje |

---

## Detección de Anomalías

### Gaps Temporales (Silencios)

Detecta períodos sin actividad inusualmente largos:

```python
# Si gap > 3x la media de intervalos, es anómalo
umbral_gap = media_intervalos * 3
```

### Clustering Temporal

Detecta ráfagas de actividad sospechosa:
- Muchos emails en minutos (envío automatizado)
- Actividad fuera de horario laboral

### Inconsistencias

- Respuesta antes que el email original
- Modificación antes que creación
- Zona horaria inconsistente en misma conversación

---

## Output

```json
{
  "timeline": {
    "inicio": "2024-01-15T08:30:00Z",
    "fin": "2024-03-22T17:45:00Z",
    "duracion_dias": 67,
    "total_eventos": 1234
  },
  "eventos": [
    {
      "timestamp": "2024-01-15T08:30:00Z",
      "timestamp_local": "2024-01-15T09:30:00+01:00",
      "tipo": "EMAIL",
      "de": "juan@empresa.com",
      "para": "maria@cliente.com",
      "asunto": "Propuesta inicial",
      "archivo_origen": "email_001.eml"
    }
  ],
  "anomalias": [
    {
      "tipo": "GAP_TEMPORAL",
      "desde": "2024-02-01T18:00:00Z",
      "hasta": "2024-02-15T09:00:00Z",
      "duracion_dias": 13.6,
      "descripcion": "Silencio anómalo: 13 días sin comunicaciones",
      "severidad": "ALTA"
    },
    {
      "tipo": "INCONSISTENCIA",
      "evento": "email_reply_before_original",
      "descripcion": "Respuesta (14:30) anterior al email original (15:00)"
    }
  ],
  "estadisticas": {
    "por_tipo": {"EMAIL": 890, "DOCUMENTO": 234, "CHAT": 110},
    "por_mes": {"2024-01": 456, "2024-02": 378, "2024-03": 400},
    "horario_pico": "10:00-12:00"
  }
}
```

---

## Visualización

Genera timeline en formato Mermaid:

```mermaid
gantt
    title Timeline de Comunicaciones
    dateFormat YYYY-MM-DD
    section Emails
    Propuesta inicial    :2024-01-15, 1d
    Negociación         :2024-01-20, 10d
    section Documentos
    Contrato borrador   :2024-02-01, 1d
    section GAPS
    Silencio anómalo    :crit, 2024-02-15, 13d
```
