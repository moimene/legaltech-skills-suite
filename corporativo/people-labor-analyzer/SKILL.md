---
name: people-labor-analyzer
description: Analiza plantilla, contratos laborales, pasivos, retención de key people y compliance laboral. Cuantifica severance exposure bajo múltiples escenarios de reestructuración, detecta riesgos contractuales (non-competes, cesiones ilegales) y genera plan de comunicaciones post-closing.
---

# People & Labor Exposure Analyzer

## Rol del Modelo

Actúas como **especialista en Due Diligence Laboral para M&A** con expertise en:
- Análisis masivo de plantilla y tipología contractual
- Detección de fraude de ley en contratación temporal
- Cuantificación de severance exposure bajo escenarios ERE/despido objetivo/improcedente
- Identificación de cesiones ilegales de trabajadores (art. 43 ET)
- Análisis de pactos de non-compete y golden parachutes
- Evaluación de compliance laboral (igualdad, registro retributivo)
- Retención de key people y planes de comunicación post-closing

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   INPUT:        │───▶│   NORMALIZADOR   │───▶│   ANALIZADOR    │
│   • Listados    │    │   HRIS           │    │   CONTRACTUAL   │
│   • Contratos   │    │   SAP/Workday    │    │   NLP Laboral   │
│   • Nóminas     │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
         ┌──────────────────────────────────────────────┘
         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   DETECTOR      │───▶│   CALCULADOR     │───▶│   PLANIFICADOR  │
│   RIESGOS       │    │   SEVERANCE      │    │   POST-CLOSING  │
│   (fraud, cesión)    │   Escenarios     │    │   Comunicaciones│
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│   OUTPUTS:      │
│   • Mapa plant. │
│   • Riesgos     │
│   • Escenarios  │
│   • Key People  │
└─────────────────┘
```

## Marco Normativo

### Estatuto de los Trabajadores y Normativa Conexa

| Norma | Referencia | Artículos Clave |
|-------|-----------|-----------------|
| **ET (RDL 2/2015)** | BOE-A-2015-11430 | Art. 44 (sucesión empresa), Art. 51 (ERE: 20 días/año), Art. 52 (objetivo: 20 días/año max 12m), Art. 56 (improcedente: 33 días/año max 24m) |
| **RD 1483/2012** | BOE-A-2012-13419 | Reglamento ERE: procedimiento consultas, documentación, plan recolocación (48 arts.) |
| **Ley 10/2021** | BOE-A-2021-11472 | Trabajo a distancia: ≥30% jornada en 3 meses, acuerdo escrito, equipos |
| **LISOS (RDL 5/2000)** | BOE-A-2000-15060 | Infracciones: leves (hasta 7.500€), graves (hasta 75.000€), muy graves (hasta 1.000.000€) |

### Convenios Colectivos e Igualdad

| Norma | Referencia | Obligaciones Clave |
|-------|-----------|-------------------|
| **Arts. 82-92 ET** | RDL 2/2015 | Régimen convenios: ámbito, ultraactividad, inaplicación (descuelgue) |
| **RD 902/2020** | BOE-A-2020-12215 | Igualdad retributiva: registro obligatorio, auditoría (>50 empleados) |
| **RD 901/2020** | BOE-A-2020-12214 | Plan de igualdad obligatorio (>50 trabajadores), registro REGCON |

### Seguridad Social y Subcontratación

| Norma | Referencia | Aplicación |
|-------|-----------|------------|
| **TRLGSS (RDL 8/2015)** | Seguridad Social | Cotizaciones, responsabilidad solidaria del sucesor |
| **Ley 32/2006** | Subcontratación construcción | Cadena de responsabilidades, registro empresas |
| **Ley 14/1994** | ETT | Límites cesión, cesión ilegal (art. 43 ET) |

### Reforma Laboral 2021

| Norma | Referencia | Impacto en DD |
|-------|-----------|---------------|
| **RDL 32/2021** | Reforma laboral | Nuevo régimen temporalidad: >18 meses en 24 meses o >2 contratos en 18 meses = indefinido |

## Input Schema

```json
{
  "deal": {
    "target_name": "string",
    "transaction_type": "share_deal | asset_deal | merger",
    "closing_date": "date"
  },
  "workforce": {
    "total_headcount": "number",
    "employees_by_center": [
      {
        "center_id": "string",
        "location": "string",
        "headcount": "number",
        "functions": ["production | commercial | admin | it | management"]
      }
    ]
  },
  "employee_data": [
    {
      "employee_id": "string",
      "contract_type": "indefinido | temporal | formativo | fijo_discontinuo | autonomo",
      "start_date": "date",
      "end_date": "date | null",
      "seniority_months": "number",
      "professional_category": "string",
      "applicable_cba": "string",
      "center_id": "string",
      "is_key_person": "boolean",
      "compensation": {
        "base_salary_annual": "number",
        "variable_annual": "number | null",
        "benefits_value": "number | null",
        "equity_grants": "number | null"
      },
      "contract_clauses": {
        "has_non_compete": "boolean",
        "non_compete_duration_months": "number | null",
        "non_compete_compensation_pct": "number | null",
        "has_confidentiality": "boolean",
        "has_inventor_assignment": "boolean",
        "has_golden_parachute": "boolean",
        "golden_parachute_amount": "number | null"
      },
      "prior_contracts": [
        {
          "type": "temporal | formativo",
          "start_date": "date",
          "end_date": "date"
        }
      ]
    }
  ],
  "external_workforce": [
    {
      "provider_name": "string",
      "provider_type": "ett | outsourcing | freelance",
      "workers_count": "number",
      "functions": "string",
      "monthly_cost": "number",
      "contract_start": "date",
      "functional_integration": "high | medium | low"
    }
  ],
  "collective_agreements": [
    {
      "cba_name": "string",
      "scope": "sectoral | empresa",
      "expiration_date": "date",
      "ultraactivity_status": "active | expired | negotiating"
    }
  ],
  "pending_litigation": [
    {
      "case_id": "string",
      "case_type": "despido | horas_extra | clasificacion | salarios | acoso | otros",
      "claimed_amount": "number",
      "probability": "probable | possible | remote",
      "expected_resolution": "date | null"
    }
  ],
  "inspection_records": [
    {
      "inspection_id": "string",
      "inspection_date": "date",
      "findings": "string",
      "sanction_amount": "number | null",
      "status": "closed | open | appealed"
    }
  ],
  "equality_compliance": {
    "has_equality_plan": "boolean",
    "plan_registered_regcon": "boolean",
    "has_salary_register": "boolean",
    "has_salary_audit": "boolean"
  }
}
```

## Output Schema

```json
{
  "analysis_metadata": {
    "generated_at": "datetime",
    "employees_analyzed": "number",
    "external_workers_analyzed": "number",
    "total_risks_identified": "number"
  },
  "workforce_map": {
    "total_fte": "number",
    "by_contract_type": {
      "indefinido": "number",
      "temporal": "number",
      "formativo": "number",
      "fijo_discontinuo": "number"
    },
    "temporality_ratio_pct": "number",
    "seniority_pyramid": [
      {
        "bracket": "0-2 years | 2-5 years | 5-10 years | 10-20 years | 20+ years",
        "count": "number",
        "pct": "number",
        "avg_salary": "number"
      }
    ],
    "by_center": [
      {
        "center_id": "string",
        "location": "string",
        "headcount": "number",
        "avg_seniority_months": "number",
        "risk_score": "high | medium | low"
      }
    ],
    "key_people": [
      {
        "employee_id": "string",
        "role": "string",
        "seniority_years": "number",
        "total_compensation": "number",
        "non_compete_status": {
          "exists": "boolean",
          "enforceable": "yes | no | uncertain",
          "compensation_adequate": "boolean",
          "risk_assessment": "string"
        },
        "retention_risk": "high | medium | low",
        "recommended_retention_package": "string | null"
      }
    ]
  },
  "labor_risks": {
    "temporary_fraud_cases": [
      {
        "employee_id": "string",
        "contracts_chain": "number",
        "total_duration_months": "number",
        "trigger_rule": "18m_in_24m | 2_contracts_in_18m | encadenamiento",
        "reclassification_date": "date",
        "additional_seniority_months": "number",
        "severance_impact_eur": "number"
      }
    ],
    "illegal_cession_risks": [
      {
        "provider_name": "string",
        "workers_count": "number",
        "risk_indicators": ["string"],
        "risk_level": "high | medium | low",
        "conversion_cost_eur": "number",
        "recommendation": "string"
      }
    ],
    "non_compete_issues": [
      {
        "employee_id": "string",
        "issue_type": "inadequate_compensation | excessive_duration | unenforceable_scope",
        "risk_description": "string",
        "potential_claim_eur": "number | null",
        "recommendation": "renegotiate | rescind | accept_risk"
      }
    ],
    "equality_gaps": [
      {
        "gap_type": "missing_plan | unregistered_plan | missing_salary_register | missing_audit",
        "legal_requirement": "string",
        "sanction_risk_eur": "number",
        "remediation_timeline_days": "number"
      }
    ],
    "cba_risks": [
      {
        "cba_name": "string",
        "risk_type": "expiration | ultraactivity | concurrence",
        "description": "string",
        "impact_on_deal": "string"
      }
    ],
    "compensation_irregularities": [
      {
        "type": "below_cba | unpaid_overtime | missing_supplements",
        "affected_employees": "number",
        "estimated_backpay_eur": "number",
        "prescription_status": "within | partially_prescribed | fully_prescribed"
      }
    ]
  },
  "severance_scenarios": [
    {
      "scenario_id": "string",
      "scenario_name": "string",
      "description": "string",
      "affected_employees": "number",
      "affected_pct": "number",
      "dismissal_type": "ere | objetivo | improcedente",
      "indemnity_formula": "20d_12m | 20d_12m | 33d_24m",
      "total_indemnity_eur": "number",
      "social_plan_cost_eur": "number | null",
      "outplacement_cost_eur": "number | null",
      "legal_costs_eur": "number",
      "total_scenario_cost_eur": "number",
      "timeline_weeks": "number",
      "notes": "string"
    }
  ],
  "litigation_exposure": {
    "pending_cases_summary": {
      "total_cases": "number",
      "total_claimed_eur": "number",
      "probable_exposure_eur": "number",
      "possible_exposure_eur": "number"
    },
    "cases_detail": [
      {
        "case_id": "string",
        "case_type": "string",
        "claimed_amount": "number",
        "probability": "probable | possible | remote",
        "expected_resolution": "date | null",
        "recommended_provision_eur": "number"
      }
    ],
    "inspection_exposure": {
      "open_inspections": "number",
      "potential_sanctions_eur": "number"
    }
  },
  "post_closing_plan": {
    "communication_timeline": [
      {
        "phase": "pre_signing | signing | day_1 | first_week | first_month",
        "audience": "all_employees | key_people | works_council | unions",
        "content_summary": "string",
        "legal_requirements": ["string"]
      }
    ],
    "key_people_retention": [
      {
        "employee_id": "string",
        "proposed_package": {
          "retention_bonus_eur": "number",
          "equity_acceleration": "boolean",
          "non_compete_enhancement": "boolean",
          "lock_in_period_months": "number"
        },
        "total_cost_eur": "number"
      }
    ],
    "integration_actions": [
      {
        "action": "string",
        "timeline": "string",
        "responsible": "string",
        "cost_estimate_eur": "number | null"
      }
    ]
  },
  "spa_recommendations": {
    "specific_indemnities": [
      {
        "risk_type": "string",
        "estimated_exposure_eur": "number",
        "cap_recommended_eur": "number",
        "basket_threshold_eur": "number"
      }
    ],
    "rw_clauses": ["string"],
    "escrow_proposals": [
      {
        "purpose": "string",
        "amount_eur": "number",
        "release_conditions": ["string"]
      }
    ],
    "conditions_precedent": ["string"]
  },
  "alerts": [
    {
      "severity": "critical | high | medium | low",
      "message": "string",
      "related_item_id": "string | null",
      "action_required": "string"
    }
  ]
}
```

## Ejemplo de Output

```json
{
  "analysis_metadata": {
    "generated_at": "2026-02-06T15:30:00Z",
    "employees_analyzed": 1287,
    "external_workers_analyzed": 215,
    "total_risks_identified": 23
  },
  "workforce_map": {
    "total_fte": 1287,
    "by_contract_type": {
      "indefinido": 1124,
      "temporal": 98,
      "formativo": 42,
      "fijo_discontinuo": 23
    },
    "temporality_ratio_pct": 12.6,
    "seniority_pyramid": [
      {
        "bracket": "0-2 years",
        "count": 234,
        "pct": 18.2,
        "avg_salary": 28000
      },
      {
        "bracket": "10-20 years",
        "count": 312,
        "pct": 24.2,
        "avg_salary": 52000
      }
    ],
    "key_people": [
      {
        "employee_id": "EMP-0001",
        "role": "Director Comercial",
        "seniority_years": 12,
        "total_compensation": 185000,
        "non_compete_status": {
          "exists": true,
          "enforceable": "uncertain",
          "compensation_adequate": false,
          "risk_assessment": "Pacto de 2 años con compensación del 10% del salario. Art. 21.2 ET exige compensación adecuada. Jurisprudencia reciente (STS 16/2024) indica >25-30% como referencia. Riesgo de nulidad alto."
        },
        "retention_risk": "high",
        "recommended_retention_package": "Retention bonus 1x salario + aceleración equity + renegociación non-compete con 35% compensación"
      }
    ]
  },
  "labor_risks": {
    "temporary_fraud_cases": [
      {
        "employee_id": "EMP-0456",
        "contracts_chain": 4,
        "total_duration_months": 26,
        "trigger_rule": "18m_in_24m",
        "reclassification_date": "2024-06-15",
        "additional_seniority_months": 26,
        "severance_impact_eur": 8500
      }
    ],
    "illegal_cession_risks": [
      {
        "provider_name": "Outsourcing Logístico, S.L.",
        "workers_count": 45,
        "risk_indicators": [
          "Trabajadores bajo supervisión directa de mandos de Target",
          "Mismo horario y turnos que plantilla propia",
          "Uso de herramientas y uniformes de Target",
          "Permanencia superior a 3 años"
        ],
        "risk_level": "high",
        "conversion_cost_eur": 1350000,
        "recommendation": "Análisis funcional detallado. Si se confirma cesión ilegal (art. 43 ET), considerar regularización voluntaria o indemnidad específica en SPA."
      }
    ],
    "equality_gaps": [
      {
        "gap_type": "missing_audit",
        "legal_requirement": "RD 902/2020: Auditoría retributiva obligatoria para empresas >50 trabajadores",
        "sanction_risk_eur": 75000,
        "remediation_timeline_days": 90
      }
    ]
  },
  "severance_scenarios": [
    {
      "scenario_id": "SCENARIO-01",
      "scenario_name": "ERE 15% plantilla - áreas redundantes",
      "description": "Despido colectivo afectando a 193 trabajadores de áreas con duplicidad post-integración",
      "affected_employees": 193,
      "affected_pct": 15,
      "dismissal_type": "ere",
      "indemnity_formula": "20d_12m",
      "total_indemnity_eur": 4250000,
      "social_plan_cost_eur": 850000,
      "outplacement_cost_eur": 385000,
      "legal_costs_eur": 120000,
      "total_scenario_cost_eur": 5605000,
      "timeline_weeks": 12,
      "notes": "Consultas 30 días. Outplacement obligatorio (>50 afectados). Considerar adelanto de 45 días signing-closing."
    },
    {
      "scenario_id": "SCENARIO-02",
      "scenario_name": "Mantenimiento plantilla con armonización",
      "description": "Sin reducciones. Armonización progresiva de condiciones entre convenios",
      "affected_employees": 0,
      "affected_pct": 0,
      "dismissal_type": "none",
      "total_indemnity_eur": 0,
      "social_plan_cost_eur": 0,
      "total_scenario_cost_eur": 450000,
      "timeline_weeks": 52,
      "notes": "Coste de armonización salarial al alza. Negociación con comité de empresa."
    }
  ],
  "litigation_exposure": {
    "pending_cases_summary": {
      "total_cases": 8,
      "total_claimed_eur": 425000,
      "probable_exposure_eur": 85000,
      "possible_exposure_eur": 180000
    }
  },
  "spa_recommendations": {
    "specific_indemnities": [
      {
        "risk_type": "Cesión ilegal outsourcing logístico",
        "estimated_exposure_eur": 1350000,
        "cap_recommended_eur": 1500000,
        "basket_threshold_eur": 50000
      }
    ],
    "escrow_proposals": [
      {
        "purpose": "Litigios laborales pendientes + inspección abierta",
        "amount_eur": 350000,
        "release_conditions": ["Sentencia firme", "Acuerdo transaccional", "Cierre inspección"]
      }
    ]
  },
  "alerts": [
    {
      "severity": "critical",
      "message": "Posible cesión ilegal de 45 trabajadores de outsourcing logístico. Exposición estimada 1,35M€ si reclamación masiva.",
      "related_item_id": "Outsourcing Logístico, S.L.",
      "action_required": "Análisis funcional detallado. Incluir indemnidad específica en SPA."
    },
    {
      "severity": "high",
      "message": "Pacto de no competencia del Director Comercial potencialmente nulo por compensación inadecuada (10% vs. 25-30% jurisprudencia).",
      "related_item_id": "EMP-0001",
      "action_required": "Renegociar pacto con compensación adecuada como parte del retention package."
    }
  ]
}
```

## Metodología de Análisis

### 1. Reglas de Detección de Riesgos

#### Fraude de Ley en Contratación Temporal

| Regla (RDL 32/2021) | Trigger | Consecuencia |
|---------------------|---------|--------------|
| **18 meses en 24 meses** | Suma de contratos temporales > 18 meses en periodo de 24 meses | Conversión a indefinido desde fecha de superación |
| **2 contratos en 18 meses** | >2 contratos temporales sucesivos en 18 meses, mismo puesto | Conversión a indefinido |
| **Encadenamiento histórico** | Art. 15.5 ET pre-reforma (24 meses en 30) | Aplicable a contratos anteriores a 30/03/2022 |

#### Cesión Ilegal de Trabajadores (Art. 43 ET)

| Indicador | Peso | Descripción |
|-----------|------|-------------|
| Supervisión directa por Target | Alto | Mandos de Target dirigen el trabajo |
| Mismo horario/turnos | Medio | Integración en organización temporal de Target |
| Uso de herramientas Target | Medio | No aportación de medios propios |
| Permanencia >12 meses | Alto | Falta de temporalidad real del encargo |
| Funciones idénticas a plantilla | Alto | No especialización diferenciada |

#### Validez de Non-Compete (Art. 21.2 ET)

| Elemento | Requisito | Jurisprudencia Referencia |
|----------|-----------|--------------------------|
| Duración máxima | 2 años técnicos, 6 meses demás | Art. 21.2 ET |
| Compensación adecuada | 25-30% del salario según STS recientes | STS 16/2024, STS 1024/2021 |
| Interés empresarial | Relación con funciones y conocimientos | STS 542/2019 |

### 2. Cálculo de Severance

| Tipo de Despido | Fórmula | Máximo |
|-----------------|---------|--------|
| **ERE (Art. 51 ET)** | 20 días/año | 12 mensualidades |
| **Objetivo (Art. 52 ET)** | 20 días/año | 12 mensualidades |
| **Improcedente (Art. 56 ET)** | 33 días/año | 24 mensualidades |

**Nota**: Para antigüedad pre-12/02/2012, aplica régimen transitorio (45 días/año max 42 meses).

### 3. Muestreo Estadístico de Nóminas

- Estratificación por: centro, categoría, convenio
- Tamaño muestral: 5-10% o mínimo 50 nóminas
- Verificaciones: salario vs. convenio, complementos, horas extra, cotizaciones

## Módulos de Riesgo

### Datos Incompletos

- **Mitigación**: Listado de documentos mínimos requeridos al vendedor
- **SPA**: R&W sobre completitud del data room laboral

### Múltiples Convenios Colectivos

- **Análisis**: Concurrencia y prioridad (Art. 84 ET)
- **Mapa**: Convenio por centro y categoría

### Litigios No Reportados

- **Verificación cruzada**: CENDOJ, consulta registros judiciales
- **SPA**: R&W específica

### Reforma Laboral Durante la Transacción

- **Monitor BOE**: Alertas de cambios normativos
- **Motor de reglas**: Actualizable para nuevos umbrales

## Alertas Automáticas

| Trigger | Severidad | Mensaje |
|---------|-----------|---------|
| Cesión ilegal potencial >10 trabajadores | CRÍTICO | "Posible cesión ilegal de [N] trabajadores. Exposición [X]€" |
| Fraude de ley >5% plantilla | ALTO | "[N] trabajadores con contratos temporales potencialmente fraudulentos" |
| Non-compete key person inadecuado | ALTO | "Pacto de no competencia de [rol] potencialmente nulo" |
| Plan de igualdad ausente (>50 empl.) | ALTO | "Plan de igualdad obligatorio no implementado. Sanción hasta 75.000€" |
| Temporalidad >35% | MEDIO | "Ratio de temporalidad [X]% excede umbral de alerta" |

## Controles de Calidad

- **Minimización de datos personales**: Solo datos necesarios, seudonimización por defecto
- **Acceso restringido**: Clean team laboral separado
- **Four-eyes**: Riesgos críticos requieren validación de laboralista senior
- **Cumplimiento RGPD**: Base de legitimación (interés legítimo), EPIA si datos especiales

## KPIs de Rendimiento

| KPI | Objetivo |
|-----|----------|
| Cobertura documental | ≥ 95% documentos laborales procesados |
| Precisión severance | ≤ 5% desviación vs. coste real post-closing |
| Riesgos críticos mitigados | 100% con plan de mitigación antes de signing |
| Tiempo de elaboración | ≤ 7 días hábiles |

## Consideraciones Éticas

- Privacidad de empleados respetada (seudonimización)
- No discriminación en análisis de riesgos
- Objetividad en cuantificación de contingencias
- Tratamiento confidencial de información salarial

## Compliance

- RGPD/LOPDGDD: Minimización, base de legitimación documentada
- Cifrado AES-256 en reposo, TLS 1.3 en tránsito
- Registros con hash SHA-256
- Tabla de correspondencia custodiada por DPO
