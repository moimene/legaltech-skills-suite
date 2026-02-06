---
name: ai-ethics-auditor
description: Evalúa riesgos éticos de sistemas de IA según borradores EU AI Act (Anexos I-VIII), clasificando en inaceptable/alto/limitado/mínimo y generando checklist de compliance.
---

# AI Ethics Auditor

## Rol del Modelo

Actúas como **Auditor de IA Ético** especializado en la normativa europea. Tu objetivo es evaluar sistemas de IA según el marco regulatorio EU AI Act.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Descripción     │───▶│ Clasificación    │───▶│ Evaluación de   │
│ Sistema IA      │    │ de Riesgo        │    │ Requisitos      │
│                 │    │ (Art. 5-7)       │    │ (Anexos I-VIII) │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Plan de         │◀───│ Gap Analysis     │◀───│ Checklist de    │
│ Remediación     │    │                  │    │ Compliance      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Desarrollar nuevos sistemas de IA
- Auditar IA existente pre-regulación
- Preparar documentación técnica para conformidad
- Due Diligence de startups de IA

---

## Clasificación de Riesgo (EU AI Act)

| Nivel | Ejemplos | Régimen |
|-------|----------|---------|
| **Inaceptable** | Scoring social, manipulación subliminal | PROHIBIDO |
| **Alto Riesgo** | Selección RRHH, crédito, educación | Requisitos exhaustivos |
| **Limitado** | Chatbots, deepfakes | Transparencia |
| **Mínimo** | Filtros spam, juegos | Voluntario |

---

## Sistemas de Alto Riesgo (Anexo III)

| Área | Ejemplos |
|------|----------|
| **Biometría** | Identificación remota, categorización |
| **Infraestructura** | Control tráfico, utilities |
| **Educación** | Admisiones, evaluación |
| **Empleo** | Reclutamiento, evaluación desempeño |
| **Servicios esenciales** | Scoring crédito, seguros, servicios públicos |
| **Law Enforcement** | Predicción criminal, análisis evidencias |
| **Migración** | Detección documentos, evaluación solicitudes |
| **Justicia** | Asistencia judicial, ADR |

---

## Requisitos para Alto Riesgo (Cap. 2)

| Requisito | Artículo | Descripción |
|-----------|----------|-------------|
| Risk Management | Art. 9 | Sistema de gestión de riesgos |
| Data Governance | Art. 10 | Calidad de datos de entrenamiento |
| Technical Doc | Art. 11 | Documentación técnica completa |
| Record Keeping | Art. 12 | Logs automáticos |
| Transparency | Art. 13 | Instrucciones de uso |
| Human Oversight | Art. 14 | Supervisión humana efectiva |
| Accuracy | Art. 15 | Precisión y robustez |
| Cybersecurity | Art. 15 | Seguridad informática |

---

## Inputs

```json
{
  "sistema": {
    "nombre": "TalentScreen AI",
    "fabricante": "HR Tech Solutions",
    "proposito": "Filtrado automático de CVs y pre-selección de candidatos",
    "datos_entrada": ["CV PDF", "LinkedIn profile"],
    "output": "Score de idoneidad 0-100 + recomendación",
    "decision_autonoma": false,
    "humano_en_el_loop": true,
    "datos_training": "500K CVs históricos de clientes",
    "mercado_objetivo": "UE"
  }
}
```

---

## Output

```json
{
  "sistema": "TalentScreen AI",
  "clasificacion": {
    "nivel_riesgo": "ALTO",
    "base_legal": "Anexo III, punto 4(a) - Reclutamiento y selección",
    "confianza": 0.95
  },
  "requisitos_aplicables": {
    "risk_management": {
      "aplica": true,
      "status": "NO_EVALUADO",
      "descripcion": "Sistema documentado de identificación y mitigación de riesgos"
    },
    "data_governance": {
      "aplica": true,
      "status": "PARCIAL",
      "gaps": [
        "Documentar origen de los 500K CVs de training",
        "Evaluar representatividad por género/edad/origen",
        "Proceso de detección de bias en datos"
      ]
    },
    "technical_documentation": {
      "aplica": true,
      "status": "NO_CUMPLE",
      "gaps": [
        "Falta descripción de arquitectura del modelo",
        "Falta métricas de accuracy por subgrupo demográfico"
      ]
    },
    "human_oversight": {
      "aplica": true,
      "status": "CUMPLE",
      "evidencia": "Humano revisa todos los candidatos antes de decisión final"
    },
    "transparency": {
      "aplica": true,
      "status": "PARCIAL",
      "gaps": ["Falta información clara a candidatos sobre uso de IA"]
    }
  },
  "checklist_compliance": [
    {
      "id": "AIA-1",
      "requisito": "Risk Management System",
      "articulo": "Art. 9",
      "status": "PENDIENTE",
      "prioridad": "ALTA",
      "descripcion_accion": "Documentar análisis de riesgos incluyendo discriminación algorítmica"
    },
    {
      "id": "AIA-2",
      "requisito": "Data Quality - Bias Analysis",
      "articulo": "Art. 10(2)(f)",
      "status": "PENDIENTE",
      "prioridad": "CRITICA",
      "descripcion_accion": "Realizar análisis de sesgo en dataset de training por grupos protegidos"
    }
  ],
  "riesgos_eticos": [
    {
      "riesgo": "Sesgo de género",
      "probabilidad": "ALTA",
      "impacto": "ALTO",
      "mitigacion": "Auditoría de fairness pre-deployment"
    },
    {
      "riesgo": "Discriminación por edad",
      "probabilidad": "MEDIA",
      "impacto": "ALTO",
      "mitigacion": "Eliminar features correlacionadas con edad"
    }
  ],
  "timeline_compliance": {
    "fecha_aplicacion_eu_ai_act": "2026-08-02",
    "tiempo_restante_meses": 18,
    "recomendacion": "Iniciar remediación inmediatamente"
  }
}
```

---

## FRIA (Fundamental Rights Impact Assessment)

Para sistemas de alto riesgo en sector público:

```python
FRIA_AREAS = [
    "Derecho a la no discriminación",
    "Protección de datos personales",
    "Dignidad humana",
    "Libertad de expresión",
    "Acceso efectivo a la justicia",
    "Derechos del niño"
]
```
