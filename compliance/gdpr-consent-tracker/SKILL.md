---
name: gdpr-consent-tracker
description: Analiza formularios y DBs para verificar que los consentimientos tienen base legal válida, fecha, alcance y revocabilidad conforme a RGPD y LOPDGDD, generando informe de gaps.
---

# GDPR Consent Tracker

## Rol del Modelo

Actúas como **DPO (Data Protection Officer)** especializado en gestión de consentimientos. Tu objetivo es auditar la validez legal de los consentimientos recabados.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Formularios     │───▶│ Extracción de    │───▶│ Validación      │
│ Web/App         │    │ Textos Legales   │    │ RGPD Art. 7     │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
┌─────────────────┐                                     │
│ Base de Datos   │───▶│ Análisis de      │─────────────┤
│ Consentimientos │    │ Estructura DB    │             │
└─────────────────┘    └──────────────────┘             │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Gap Analysis     │◀───│ Matriz de       │
│ Compliance      │    │                  │    │ Consentimientos │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Auditoría RGPD periódica
- Preparación para inspección AEPD
- Due Diligence de plataformas digitales
- Migración de sistemas legacy

---

## Requisitos del Consentimiento Válido (RGPD Art. 7)

| Requisito | Descripción | Verificación |
|-----------|-------------|--------------|
| **Libre** | Sin condicionamiento | No vinculado a servicio |
| **Específico** | Por finalidad | Checkbox separado por uso |
| **Informado** | Información clara | Texto comprensible |
| **Inequívoco** | Acción afirmativa | No pre-marcado |
| **Revocable** | Fácil retirada | Mecanismo disponible |
| **Demostrable** | Prueba de obtención | Log con timestamp |

---

## Bases Legales (Art. 6 RGPD)

| Base Legal | Código | Cuándo Aplica |
|------------|--------|---------------|
| Consentimiento | 6.1.a | Marketing, newsletters |
| Contrato | 6.1.b | Prestación del servicio |
| Obligación Legal | 6.1.c | PBC, fiscal |
| Interés Vital | 6.1.d | Emergencias salud |
| Interés Público | 6.1.e | Sector público |
| Interés Legítimo | 6.1.f | Fraud prevention, analytics |

---

## Inputs

### Formularios

```json
{
  "formularios": [
    {
      "id": "registro_web",
      "url": "https://empresa.com/registro",
      "campos_consentimiento": [
        {
          "id": "marketing",
          "texto": "Acepto recibir comunicaciones comerciales",
          "pre_marcado": false,
          "obligatorio": false
        },
        {
          "id": "cesion_terceros",
          "texto": "Acepto la cesión de mis datos a empresas del grupo",
          "pre_marcado": true,
          "obligatorio": false
        }
      ],
      "politica_privacidad": "https://empresa.com/privacidad"
    }
  ]
}
```

### Base de Datos

```json
{
  "tabla_consentimientos": {
    "estructura": [
      {"campo": "user_id", "tipo": "int"},
      {"campo": "consent_type", "tipo": "varchar"},
      {"campo": "granted", "tipo": "boolean"},
      {"campo": "timestamp", "tipo": "datetime"}
    ],
    "tiene_revocacion": false,
    "tiene_version_texto": false
  }
}
```

---

## Output

```json
{
  "auditoria": {
    "fecha": "2024-02-06",
    "formularios_analizados": 5,
    "tratamientos_identificados": 12
  },
  "hallazgos": [
    {
      "id": "GDPR-001",
      "severidad": "CRITICA",
      "elemento": "formulario:registro_web.cesion_terceros",
      "problema": "Checkbox pre-marcado",
      "requisito_incumplido": "Art. 7.1 - Consentimiento inequívoco",
      "evidencia": "Campo 'cesion_terceros' tiene pre_marcado=true",
      "remediacion": "Desmarcar por defecto, requerir acción afirmativa"
    },
    {
      "id": "GDPR-002",
      "severidad": "ALTA",
      "elemento": "db:consentimientos",
      "problema": "No se registra versión del texto legal",
      "requisito_incumplido": "Art. 7.1 - Demostrar consentimiento",
      "remediacion": "Añadir campo 'legal_text_version' con hash del texto aceptado"
    },
    {
      "id": "GDPR-003",
      "severidad": "ALTA",
      "elemento": "db:consentimientos",
      "problema": "Sin mecanismo de revocación",
      "requisito_incumplido": "Art. 7.3 - Retirada fácil",
      "remediacion": "Implementar endpoint de revocación + UI en área cliente"
    },
    {
      "id": "GDPR-004",
      "severidad": "MEDIA",
      "elemento": "formulario:registro_web",
      "problema": "Información de cesión insuficiente",
      "requisito_incumplido": "Art. 13 - Derecho información",
      "remediacion": "Especificar qué empresas del grupo y para qué finalidad"
    }
  ],
  "matriz_consentimientos": {
    "tratamientos": [
      {
        "tratamiento": "Newsletter marketing",
        "base_legal": "Consentimiento",
        "consentimiento_valido": true,
        "revocable": true
      },
      {
        "tratamiento": "Cesión a grupo",
        "base_legal": "Consentimiento",
        "consentimiento_valido": false,
        "problema": "Pre-marcado"
      },
      {
        "tratamiento": "Prestación servicio",
        "base_legal": "Contrato",
        "consentimiento_requerido": false
      }
    ]
  },
  "resumen_gaps": {
    "criticos": 1,
    "altos": 2,
    "medios": 3,
    "bajos": 1,
    "compliance_score": 0.58
  },
  "plan_remediacion": [
    {
      "prioridad": 1,
      "hallazgo": "GDPR-001",
      "responsable": "Desarrollo Web",
      "deadline": "2024-02-20",
      "esfuerzo": "Bajo"
    },
    {
      "prioridad": 2,
      "hallazgo": "GDPR-003",
      "responsable": "Backend + Frontend",
      "deadline": "2024-03-15",
      "esfuerzo": "Medio"
    }
  ],
  "riesgo_sancion": {
    "nivel": "ALTO",
    "base": "Infracciones Art. 7 pueden suponer hasta 20M€ o 4% facturación",
    "atenuantes": ["Buena fe", "Primera infracción"],
    "agravantes": ["Datos de menores", "Tratamiento masivo"]
  }
}
```

---

## Checklist de Auditoría

```markdown
☐ Consentimientos separados por finalidad
☐ Sin checkboxes pre-marcados
☐ Información clara y comprensible
☐ Identificación clara del responsable
☐ Referencia a derechos ARCO
☐ Mecanismo de revocación accesible
☐ Registro con timestamp de obtención
☐ Versión del texto legal almacenada
☐ Renovación periódica si aplica
☐ Consentimiento específico para menores (LOPDGDD Art. 7)
```
