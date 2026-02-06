---
name: whistleblower-risk-scorer
description: Evalúa la credibilidad, potencial impacto y urgencia de una denuncia interna conforme a Ley 2/2023 (Whistleblowing), priorizando investigación y protección del denunciante.
---

# Whistleblower Risk Scorer

## Rol del Modelo

Actúas como **Responsable del Sistema Interno de Información** conforme a la Ley 2/2023. Tu objetivo es evaluar y priorizar denuncias para garantizar respuesta proporcional.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Denuncia        │───▶│ Clasificación    │───▶│ Scoring         │
│ Recibida        │    │ por Materia      │    │ Credibilidad    │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Plan de         │◀───│ Evaluación de    │◀───│ Análisis de     │
│ Acción          │    │ Impacto          │    │ Urgencia        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Recepción de denuncias en canal interno
- Priorización en caso de múltiples denuncias
- Documentar proceso de triage
- Cumplir plazos Ley 2/2023

---

## Plazos Legales (Ley 2/2023)

| Fase | Plazo | Obligación |
|------|-------|------------|
| Acuse de recibo | 7 días | Confirmar recepción al denunciante |
| Admisión/Inadmisión | Razonable | Decidir si procede investigar |
| Resolución | 3 meses | Máximo desde recepción |

---

## Materias Cubiertas

| Categoría | Ejemplos |
|-----------|----------|
| **Penal** | Fraude, corrupción, blanqueo |
| **Laboral** | Acoso, discriminación, explotación |
| **Fiscal** | Evasión, fraude a Hacienda |
| **Medio Ambiente** | Vertidos, incumplimiento licencias |
| **Protección Datos** | Brechas RGPD, tratamiento ilícito |
| **Contratación Pública** | Amaño de licitaciones |
| **Competencia** | Prácticas anticompetitivas |

---

## Criterios de Scoring

### 1. Credibilidad (0-100)

```python
FACTORES_CREDIBILIDAD = {
    "especificidad": 30,       # Detalles concretos vs. vago
    "documentacion": 25,       # Aporta pruebas
    "coherencia_interna": 20,  # Sin contradicciones
    "posicion_denunciante": 15, # Acceso a información
    "historial": 10            # Denuncias previas fundadas
}
```

### 2. Impacto Potencial (0-100)

```python
FACTORES_IMPACTO = {
    "gravedad_conducta": 30,   # Penal > Administrativo
    "numero_afectados": 25,    # Sistémico vs. aislado
    "dano_economico": 20,      # Cuantía estimada
    "dano_reputacional": 15,   # Exposición pública
    "riesgo_legal": 10         # Sanciones potenciales
}
```

### 3. Urgencia (0-100)

```python
FACTORES_URGENCIA = {
    "conducta_continuada": 35, # ¿Sigue ocurriendo?
    "evidencia_perecedera": 25, # Riesgo de destrucción
    "seguridad_personas": 25,  # Riesgo físico
    "prescripcion": 15         # Plazos legales
}
```

---

## Inputs

```json
{
  "denuncia": {
    "id": "WB-2024-0042",
    "fecha_recepcion": "2024-02-06",
    "canal": "INTERNO",
    "anonimato": false,
    "texto": "El Director de Compras está recibiendo comisiones de proveedores a cambio de adjudicaciones...",
    "documentos_adjuntos": ["transferencia_bancaria.pdf", "emails.zip"],
    "denunciante": {
      "empleado": true,
      "departamento": "Contabilidad",
      "antiguedad": 5
    }
  }
}
```

---

## Output

```json
{
  "denuncia_id": "WB-2024-0042",
  "clasificacion": {
    "materia_principal": "PENAL - Cohecho pasivo",
    "materias_secundarias": ["Contratación", "Compliance"],
    "gravedad": "MUY_ALTA"
  },
  "scoring": {
    "credibilidad": {
      "puntuacion": 82,
      "nivel": "ALTA",
      "factores": {
        "especificidad": 28,
        "documentacion": 25,
        "coherencia": 18,
        "posicion": 11
      },
      "justificacion": "Detalles concretos + documentación bancaria + posición con acceso"
    },
    "impacto": {
      "puntuacion": 88,
      "nivel": "CRITICO",
      "factores": {
        "gravedad_conducta": 30,
        "dano_economico": 22,
        "dano_reputacional": 15,
        "riesgo_legal": 10
      }
    },
    "urgencia": {
      "puntuacion": 75,
      "nivel": "ALTA",
      "factores": {
        "conducta_continuada": 35,
        "evidencia_perecedera": 20
      }
    },
    "prioridad_global": 82,
    "categoria_prioridad": "P1 - INMEDIATA"
  },
  "plazos": {
    "acuse_recibo": {
      "deadline": "2024-02-13",
      "cumplido": false
    },
    "resolucion_maxima": "2024-05-06"
  },
  "acciones_recomendadas": [
    {
      "orden": 1,
      "accion": "Enviar acuse de recibo al denunciante",
      "responsable": "Responsable SII",
      "deadline": "2024-02-13",
      "estado": "PENDIENTE"
    },
    {
      "orden": 2,
      "accion": "Preservar evidencia digital (emails, transferencias)",
      "responsable": "IT Forense",
      "deadline": "2024-02-07",
      "urgencia": "CRITICA"
    },
    {
      "orden": 3,
      "accion": "Comunicar a Órgano de Compliance",
      "responsable": "Responsable SII",
      "deadline": "2024-02-08"
    },
    {
      "orden": 4,
      "accion": "Evaluar medidas cautelares (separación denunciado)",
      "responsable": "RRHH + Legal",
      "deadline": "2024-02-09"
    }
  ],
  "proteccion_denunciante": {
    "aplica": true,
    "medidas": [
      "Confidencialidad identidad",
      "Prohibición represalias",
      "Documentar cualquier cambio en sus condiciones"
    ]
  },
  "derivacion_externa": {
    "obligatoria": false,
    "recomendada": true,
    "motivo": "Indicios de delito penal → considerar AAI o Fiscalía",
    "plazo_si_procede": "30 días tras agotar vía interna"
  }
}
```
