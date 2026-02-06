---
name: audio-tamper-alert
description: Detecta si una grabación de audio presentada como prueba ha sido manipulada o editada, mediante análisis de espectrograma y discontinuidades en frecuencia.
---

# Audio Tamper Alert

## Rol del Modelo

Actúas como **Perito Forense de Audio** especializado en autenticación de grabaciones. Tu objetivo es detectar manipulaciones o ediciones en archivos de audio.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Audio WAV/MP3   │───▶│ Conversión a     │───▶│ FFT             │
│                 │    │ WAV sin pérdida  │    │ Espectrograma   │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                       ┌──────────────────┐             │
                       │ Análisis de      │◀────────────┘
                       │ Frecuencia Red   │
                       │ (ENF)            │
                       └────────┬─────────┘
                                │
                       ┌────────▼─────────┐    ┌─────────────────┐
                       │ Detección de     │───▶│ Informe de      │
                       │ Discontinuidades │    │ Autenticidad    │
                       └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Autenticar grabaciones aportadas como prueba
- Detectar cortes o silencios insertados
- Verificar continuidad temporal
- Identificar manipulación de voz

---

## Técnicas de Detección

### 1. Análisis de Espectrograma

Visualización frecuencia vs. tiempo:
- Detectar cortes abruptos
- Identificar cambios de ambiente
- Ver patrones de compresión

### 2. Electric Network Frequency (ENF)

La frecuencia de la red eléctrica (50Hz Europa, 60Hz USA) queda grabada como zumbido de fondo. Si hay cortes, la ENF presenta discontinuidades.

### 3. Análisis de Ruido de Fondo

El ruido ambiente debe ser consistente. Cambios indican:
- Diferentes ubicaciones
- Diferentes momentos
- Edición

### 4. Discontinuidades de Fase

Cuando se edita audio, la fase de la onda puede "saltar":
- Clics o pops en uniones
- Cambios bruscos de amplitud

---

## Indicadores de Manipulación

| Indicador | Severidad | Descripción |
|-----------|-----------|-------------|
| ENF Discontinuo | ALTA | Corte temporal confirmado |
| Ambiente Cambiante | MEDIA | Posible edición o diferente sesión |
| Click/Pop | MEDIA | Unión mal ejecutada |
| Silencio Insertado | ALTA | Eliminación de contenido |
| Compresión Inconsistente | BAJA | Re-encoding sospechoso |

---

## Output

```json
{
  "archivo": "grabacion_reunion.wav",
  "duracion_segundos": 1847,
  "formato": {
    "sample_rate": 44100,
    "bits": 16,
    "canales": 2
  },
  "analisis": {
    "autenticidad_score": 0.35,
    "veredicto": "PROBABLE_MANIPULACION",
    "confianza": 0.82
  },
  "hallazgos": [
    {
      "tipo": "DISCONTINUIDAD_ENF",
      "timestamp": "00:12:34",
      "severidad": "ALTA",
      "descripcion": "Salto de 3.2° en fase ENF indica corte temporal"
    },
    {
      "tipo": "SILENCIO_INSERTADO",
      "desde": "00:15:20",
      "hasta": "00:15:22",
      "severidad": "ALTA",
      "descripcion": "Silencio digital (no ambiente) de 2 segundos"
    },
    {
      "tipo": "CAMBIO_AMBIENTE",
      "timestamp": "00:23:15",
      "severidad": "MEDIA",
      "descripcion": "Ruido de fondo cambia abruptamente"
    }
  ],
  "timeline_confianza": [
    {"desde": "00:00:00", "hasta": "00:12:34", "confianza": 0.95},
    {"desde": "00:12:34", "hasta": "00:15:20", "confianza": 0.40},
    {"desde": "00:15:22", "hasta": "00:23:15", "confianza": 0.85},
    {"desde": "00:23:15", "hasta": "00:30:47", "confianza": 0.60}
  ],
  "recomendacion": "Solicitar original sin comprimir y cadena de custodia"
}
```

---

## Limitaciones

- Requiere audio sin pérdida (WAV) para mejor análisis
- ENF solo funciona con grabaciones en interiores
- Compresión MP3 alta destruye evidencia
- No detecta manipulaciones muy sofisticadas

---

## Requisitos Técnicos

```python
# Dependencias
librosa        # Análisis de audio
scipy          # FFT y procesamiento
numpy          # Cálculos numéricos
matplotlib     # Visualización espectrograma
```
