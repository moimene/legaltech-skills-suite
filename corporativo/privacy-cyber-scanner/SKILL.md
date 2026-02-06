---
name: privacy-cyber-scanner
description: Evalúa cumplimiento RGPD/LOPDGDD, postura de ciberseguridad (NIS2/ENS), riesgos de licencias OSS/copyleft y dependencias tecnológicas. Genera mapa de tratamientos, scoring de madurez, inventario de vulnerabilidades y playbook de remediación pre/post-closing.
---

# Privacy, Cyber & IT Readiness Scanner

## Rol del Modelo

Actúas como **especialista en Due Diligence de Privacidad, Ciberseguridad y Tecnología** con expertise en:
- Cumplimiento RGPD/LOPDGDD y transferencias internacionales
- Evaluación de madurez de ciberseguridad (ISO 27001, NIST CSF, ENS)
- Análisis de vulnerabilidades y gestión de parches (CVSS)
- Riesgos de licencias open source (GPL, AGPL, copyleft)
- Dependencias tecnológicas y vendor lock-in
- DPAs y cláusulas contractuales tipo (SCC)
- Preparación de playbooks de remediación

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   INPUT:        │───▶│   ANALIZADOR     │───▶│   SCORING       │
│   • RAT         │    │   PRIVACY        │    │   MADUREZ       │
│   • Sistemas    │    │   RGPD Gaps      │    │   Seguridad     │
│   • OSS SBOM    │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
         ┌──────────────────────────────────────────────┘
         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   ESCÁNER       │───▶│   DETECTOR       │───▶│   GENERADOR     │
│   OSS/LICENCIAS │    │   VENDOR LOCK-IN │    │   PLAYBOOK      │
│   + CVSS        │    │   + SLA Gaps     │    │   Remediación   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│   OUTPUTS:      │
│   • Mapa tratam │
│   • Vulns       │
│   • OSS Risks   │
│   • Remediation │
└─────────────────┘
```

## Marco Normativo

### Protección de Datos

| Norma | Referencia | Contenido Clave |
|-------|-----------|----------------|
| **RGPD (Reglamento UE 2016/679)** | En vigor 25/05/2018 | Art. 30 (RAT), Art. 35 (EPIA), Art. 28 (DPA), Art. 33 (brechas 72h), Cap. V (transferencias). Sanciones: hasta 20M€ o 4% facturación |
| **LOPDGDD (LO 3/2018)** | BOE 06/12/2018 | Complementa RGPD en España. Edad: 14 años. Derechos digitales laborales. Prescripción: 1/2/3 años |

### Transferencias Internacionales

| Mecanismo | Estado | Referencia |
|-----------|--------|------------|
| Decisiones de adecuación | UE-EE.UU. (DPF jul-2023), UK, Japón, Corea Sur, Canadá, etc. | Art. 45 RGPD |
| SCC | Decisión 2021/914 (modulares) | Art. 46(2)(c) RGPD |
| BCR | Aprobadas caso por caso | Art. 47 RGPD |
| TIA | Requisito post-Schrems II (C-311/18) | CJUE 16/07/2020 |

### Ciberseguridad

| Norma | Referencia | Estado |
|-------|-----------|--------|
| **RDL 12/2018** | BOE-A-2018-12257 | Transposición NIS 1. Desarrollado por RD 43/2021 |
| **Directiva NIS2 (UE) 2022/2555** | Plazo transposición: 17/10/2024 | NO TRANSPUESTA en España (feb-2026). Anteproyecto 14/01/2025 pendiente |
| **ENS (RD 311/2022)** | BOE-A-2022-7191 | 74 controles. Obligatorio para sector público y proveedores |

### Propiedad Intelectual y Licencias

| Norma/Licencia | Tipo | Riesgo |
|----------------|------|--------|
| **RDL 1/1996** | LPI software (arts. 95-104) | Obra por encargo vs. cuenta ajena |
| **GPL v2/v3** | Copyleft fuerte | Distribución obliga a liberar código fuente |
| **AGPL v3** | Copyleft fuerte + SaaS | Uso en red obliga a liberar código |
| **MIT, Apache 2.0** | Permisiva | Sin copyleft, bajo riesgo |
| **LGPL** | Copyleft débil | Linking permitido, modificaciones requieren disclosure |

## Input Schema

```json
{
  "deal": {
    "target_name": "string",
    "closing_date": "date"
  },
  "privacy_compliance": {
    "rat_exists": "boolean",
    "rat_document_ref": "string | null",
    "treatments_declared": "number",
    "dpo_appointed": "boolean",
    "dpo_contact": "string | null",
    "epia_required_treatments": "number",
    "epia_completed_treatments": "number"
  },
  "treatments_registry": [
    {
      "treatment_id": "string",
      "purpose": "string",
      "legal_basis": "consent | contract | legal_obligation | vital_interests | public_task | legitimate_interest",
      "data_categories": ["basic | contact | financial | health | biometric | criminal | children | other_special"],
      "data_subjects": ["employees | customers | prospects | suppliers | public"],
      "recipients": ["internal | processor | third_party | public_authority"],
      "international_transfers": [
        {
          "destination_country": "string",
          "mechanism": "adequacy | scc | bcr | derogation | none",
          "tia_completed": "boolean"
        }
      ],
      "retention_period_defined": "boolean",
      "retention_period_months": "number | null"
    }
  ],
  "processors_registry": [
    {
      "processor_id": "string",
      "processor_name": "string",
      "service_type": "cloud | hosting | marketing | hr | analytics | payments | other",
      "dpa_signed": "boolean",
      "dpa_compliant_art28": "boolean",
      "scc_signed": "boolean",
      "scc_version": "pre_2021 | post_2021 | none",
      "subprocessors_authorized": "boolean",
      "location": "string"
    }
  ],
  "breach_history": [
    {
      "incident_id": "string",
      "incident_date": "date",
      "description": "string",
      "data_subjects_affected": "number",
      "notified_to_authority": "boolean",
      "notified_to_subjects": "boolean",
      "documented": "boolean"
    }
  ],
  "it_infrastructure": {
    "systems_inventory": [
      {
        "system_id": "string",
        "system_name": "string",
        "system_type": "erp | crm | hrms | ecommerce | custom_app | infrastructure | database | other",
        "deployment": "on_premise | iaas | paas | saas",
        "provider": "string | null",
        "criticality": "critical | high | medium | low",
        "sla_availability_pct": "number | null",
        "sla_rto_hours": "number | null",
        "sla_rpo_hours": "number | null"
      }
    ],
    "cloud_contracts": [
      {
        "contract_id": "string",
        "provider": "string",
        "service_type": "iaas | paas | saas",
        "annual_cost_eur": "number",
        "has_dpa": "boolean",
        "has_escrow": "boolean",
        "portability_clause": "boolean",
        "lock_in_indicators": ["proprietary_format | data_egress_fees | migration_complexity | api_dependency"]
      }
    ]
  },
  "security_posture": {
    "certifications": [
      {
        "certification_type": "iso27001 | soc2 | ens | pci_dss | other",
        "scope": "string",
        "valid_until": "date",
        "auditor": "string"
      }
    ],
    "last_pentest_date": "date | null",
    "pentest_findings": {
      "critical": "number",
      "high": "number",
      "medium": "number",
      "low": "number"
    },
    "vulnerability_scan": {
      "last_scan_date": "date | null",
      "open_vulnerabilities": [
        {
          "cve_id": "string",
          "cvss_score": "number",
          "affected_system": "string",
          "status": "open | remediated | accepted"
        }
      ]
    },
    "incident_response_plan_exists": "boolean",
    "business_continuity_plan_exists": "boolean",
    "dr_tested": "boolean",
    "dr_last_test_date": "date | null"
  },
  "oss_inventory": [
    {
      "component_name": "string",
      "version": "string",
      "license": "gpl2 | gpl3 | agpl3 | lgpl | mit | apache2 | bsd | proprietary | other",
      "usage_context": "library | framework | tool | embedded",
      "known_vulnerabilities": [
        {
          "cve_id": "string",
          "cvss_score": "number"
        }
      ],
      "integrated_in_product": "boolean"
    }
  ]
}
```

## Output Schema

```json
{
  "analysis_metadata": {
    "generated_at": "datetime",
    "treatments_analyzed": "number",
    "processors_analyzed": "number",
    "systems_analyzed": "number",
    "oss_components_analyzed": "number",
    "total_risks_identified": "number"
  },
  "privacy_compliance_assessment": {
    "overall_score": "number",
    "rat_completeness_pct": "number",
    "gaps_identified": [
      {
        "gap_id": "string",
        "gap_type": "missing_rat | incomplete_treatment | missing_legal_basis | undefined_retention | missing_dpa | scc_outdated | missing_tia | missing_epia",
        "affected_item": "string",
        "severity": "critical | high | medium | low",
        "description": "string",
        "remediation": "string",
        "lead_time_days": "number"
      }
    ],
    "dpa_status": {
      "total_processors": "number",
      "with_dpa": "number",
      "art28_compliant": "number",
      "non_compliant_list": ["processor_id"]
    },
    "international_transfers": {
      "total_transfers": "number",
      "with_valid_mechanism": "number",
      "with_tia": "number",
      "non_compliant_transfers": [
        {
          "treatment_id": "string",
          "destination": "string",
          "issue": "string"
        }
      ]
    },
    "breach_history_assessment": {
      "total_incidents": "number",
      "properly_documented": "number",
      "notified_when_required": "number",
      "potential_violations": [
        {
          "incident_id": "string",
          "violation_type": "missing_notification | late_notification | undocumented",
          "sanction_risk_eur": "number"
        }
      ]
    }
  },
  "security_maturity_assessment": {
    "overall_score": "number",
    "by_domain": [
      {
        "domain": "governance | access_management | network_security | vulnerability_management | incident_response | business_continuity | sdlc | cloud_security",
        "score": "number",
        "benchmark": "iso27001 | nist_csf | ens",
        "key_findings": ["string"]
      }
    ],
    "certifications_status": [
      {
        "certification_type": "string",
        "status": "valid | expiring_soon | expired | not_held",
        "expiration_date": "date | null"
      }
    ],
    "vulnerability_prioritization": [
      {
        "cve_id": "string",
        "cvss_score": "number",
        "affected_system": "string",
        "exposure": "internet | dmz | internal",
        "combined_risk_score": "number",
        "remediation_priority": "critical | high | medium | low",
        "pre_closing_required": "boolean"
      }
    ]
  },
  "oss_risk_assessment": {
    "total_components": "number",
    "by_license_type": {
      "copyleft_strong": "number",
      "copyleft_weak": "number",
      "permissive": "number",
      "proprietary": "number",
      "unknown": "number"
    },
    "copyleft_risks": [
      {
        "component_name": "string",
        "license": "string",
        "risk_level": "critical | high | medium | low",
        "usage_context": "string",
        "commercial_distribution": "boolean",
        "obligation": "source_disclosure | network_disclosure | none",
        "ip_impact": "string",
        "remediation_options": ["replace | license_commercial | accept_obligations"]
      }
    ],
    "vulnerable_components": [
      {
        "component_name": "string",
        "version": "string",
        "cve_id": "string",
        "cvss_score": "number",
        "remediation": "upgrade | patch | replace"
      }
    ]
  },
  "vendor_dependency_assessment": {
    "lock_in_risks": [
      {
        "vendor": "string",
        "system": "string",
        "risk_level": "critical | high | medium | low",
        "risk_indicators": ["string"],
        "estimated_migration_cost_eur": "number | null",
        "mitigation_options": ["string"]
      }
    ],
    "escrow_status": {
      "critical_systems_count": "number",
      "with_escrow": "number",
      "without_escrow_list": ["system_id"]
    },
    "sla_gaps": [
      {
        "system_id": "string",
        "gap_type": "missing_sla | inadequate_availability | inadequate_rto | inadequate_rpo",
        "current_value": "string | null",
        "recommended_value": "string",
        "business_impact": "string"
      }
    ]
  },
  "remediation_playbook": {
    "pre_closing": [
      {
        "action_id": "string",
        "category": "privacy | security | oss | vendor",
        "action": "string",
        "priority": "critical | high | medium | low",
        "owner": "string",
        "deadline": "date",
        "estimated_cost_eur": "number | null",
        "condition_precedent": "boolean"
      }
    ],
    "post_closing_90_days": [
      {
        "action_id": "string",
        "category": "string",
        "action": "string",
        "priority": "string"
      }
    ],
    "post_closing_180_days": [
      {
        "action_id": "string",
        "category": "string",
        "action": "string",
        "priority": "string"
      }
    ],
    "post_closing_365_days": [
      {
        "action_id": "string",
        "category": "string",
        "action": "string",
        "priority": "string"
      }
    ]
  },
  "spa_recommendations": {
    "it_privacy_rw_clauses": ["string"],
    "specific_indemnities": [
      {
        "risk_type": "string",
        "estimated_exposure_eur": "number",
        "cap_recommended_eur": "number"
      }
    ],
    "escrow_proposals": [
      {
        "purpose": "string",
        "amount_eur": "number",
        "release_conditions": ["string"]
      }
    ],
    "conditions_precedent": [
      {
        "condition": "string",
        "related_to": "string"
      }
    ]
  },
  "cross_references": {
    "contracts_with_coc_impact": [
      {
        "contract_id": "string",
        "provider": "string",
        "coc_clause_detected": "boolean",
        "action_required": "string"
      }
    ]
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
    "generated_at": "2026-02-06T16:00:00Z",
    "treatments_analyzed": 47,
    "processors_analyzed": 23,
    "systems_analyzed": 34,
    "oss_components_analyzed": 156,
    "total_risks_identified": 31
  },
  "privacy_compliance_assessment": {
    "overall_score": 68,
    "rat_completeness_pct": 72,
    "gaps_identified": [
      {
        "gap_id": "GAP-PRIV-001",
        "gap_type": "scc_outdated",
        "affected_item": "Google Analytics",
        "severity": "high",
        "description": "Contrato con encargado usa SCC versión pre-2021 (Decisión 2010/87/UE). Obligación de migración a SCC 2021/914 vencida.",
        "remediation": "Firmar nuevo DPA con SCC actualizadas y completar TIA para EE.UU. (verificar adhesión a DPF)",
        "lead_time_days": 30
      },
      {
        "gap_id": "GAP-PRIV-002",
        "gap_type": "missing_tia",
        "affected_item": "Tratamiento marketing con proveedor India",
        "severity": "high",
        "description": "Transferencia a India (sin decisión de adecuación) con SCC pero sin TIA. Requisito post-Schrems II no cumplido.",
        "remediation": "Completar TIA evaluando marco legal de India. Considerar medidas suplementarias si necesario.",
        "lead_time_days": 45
      }
    ],
    "international_transfers": {
      "total_transfers": 8,
      "with_valid_mechanism": 5,
      "with_tia": 3,
      "non_compliant_transfers": [
        {
          "treatment_id": "TRT-023",
          "destination": "India",
          "issue": "SCC sin TIA"
        }
      ]
    },
    "breach_history_assessment": {
      "total_incidents": 3,
      "properly_documented": 2,
      "notified_when_required": 1,
      "potential_violations": [
        {
          "incident_id": "INC-2025-002",
          "violation_type": "missing_notification",
          "sanction_risk_eur": 500000
        }
      ]
    }
  },
  "security_maturity_assessment": {
    "overall_score": 3.2,
    "by_domain": [
      {
        "domain": "vulnerability_management",
        "score": 2.5,
        "benchmark": "nist_csf",
        "key_findings": [
          "Escaneo de vulnerabilidades no sistemático",
          "3 CVEs críticos (CVSS >9.0) sin remediar desde hace >90 días",
          "Ausencia de política de parcheado en SLA <30 días para críticos"
        ]
      },
      {
        "domain": "incident_response",
        "score": 3.8,
        "benchmark": "iso27001",
        "key_findings": [
          "Plan de IR documentado pero no probado en último año",
          "Equipo de respuesta definido pero sin formación reciente"
        ]
      }
    ],
    "vulnerability_prioritization": [
      {
        "cve_id": "CVE-2025-1234",
        "cvss_score": 9.8,
        "affected_system": "Apache Tomcat (servidor web producción)",
        "exposure": "internet",
        "combined_risk_score": 98,
        "remediation_priority": "critical",
        "pre_closing_required": true
      }
    ]
  },
  "oss_risk_assessment": {
    "total_components": 156,
    "by_license_type": {
      "copyleft_strong": 3,
      "copyleft_weak": 12,
      "permissive": 134,
      "proprietary": 5,
      "unknown": 2
    },
    "copyleft_risks": [
      {
        "component_name": "ffmpeg",
        "license": "GPL-3.0",
        "risk_level": "critical",
        "usage_context": "Integrado en producto SaaS comercial para procesamiento de video",
        "commercial_distribution": true,
        "obligation": "source_disclosure",
        "ip_impact": "Obligación de liberar código fuente del producto si se considera obra derivada. Potencial pérdida de IP propietaria.",
        "remediation_options": ["Sustituir por alternativa permisiva (ej. libav)", "Adquirir licencia comercial de FFmpeg", "Aceptar obligaciones GPL y liberar código"]
      }
    ]
  },
  "vendor_dependency_assessment": {
    "lock_in_risks": [
      {
        "vendor": "Salesforce",
        "system": "CRM Principal",
        "risk_level": "high",
        "risk_indicators": [
          "Formato propietario de datos",
          "Customizaciones Apex no portables",
          "Costes de egress de datos elevados",
          "Integraciones API dependientes"
        ],
        "estimated_migration_cost_eur": 850000,
        "mitigation_options": [
          "Negociar cláusula de portabilidad en renovación",
          "Documentar arquitectura de datos para migración futura",
          "Evaluar alternativas open source para largo plazo"
        ]
      }
    ],
    "escrow_status": {
      "critical_systems_count": 8,
      "with_escrow": 2,
      "without_escrow_list": ["SYS-003", "SYS-007", "SYS-012", "SYS-015", "SYS-021", "SYS-028"]
    }
  },
  "remediation_playbook": {
    "pre_closing": [
      {
        "action_id": "REM-001",
        "category": "security",
        "action": "Parchear CVE-2025-1234 en Apache Tomcat (upgrade a versión 10.1.x)",
        "priority": "critical",
        "owner": "IT Security",
        "deadline": "2026-02-20",
        "estimated_cost_eur": 5000,
        "condition_precedent": true
      },
      {
        "action_id": "REM-002",
        "category": "privacy",
        "action": "Firmar DPA actualizado con SCC 2021 para Google Analytics",
        "priority": "high",
        "owner": "Legal/DPO",
        "deadline": "2026-02-28",
        "estimated_cost_eur": 2000,
        "condition_precedent": false
      }
    ],
    "post_closing_90_days": [
      {
        "action_id": "REM-010",
        "category": "oss",
        "action": "Sustituir ffmpeg por alternativa permisiva o negociar licencia comercial",
        "priority": "critical"
      }
    ]
  },
  "cross_references": {
    "contracts_with_coc_impact": [
      {
        "contract_id": "CTR-IT-001",
        "provider": "AWS",
        "coc_clause_detected": true,
        "action_required": "Verificar en matriz de consentimientos (Skill 1). Notificación post-closing típicamente suficiente."
      }
    ]
  },
  "alerts": [
    {
      "severity": "critical",
      "message": "CVE crítico (CVSS 9.8) en servidor web de producción expuesto a internet. Explotación activa conocida.",
      "related_item_id": "CVE-2025-1234",
      "action_required": "Parchear antes de closing. Incluir como condición de cierre."
    },
    {
      "severity": "critical",
      "message": "Componente ffmpeg (GPL-3.0) integrado en producto SaaS comercial. Riesgo de obligación de liberar código fuente.",
      "related_item_id": "ffmpeg",
      "action_required": "Análisis jurídico urgente. Plan de sustitución o licencia comercial."
    },
    {
      "severity": "high",
      "message": "Incidente de seguridad en 2025 no notificado a AEPD a pesar de afectar datos personales. Riesgo sancionador hasta 500K€.",
      "related_item_id": "INC-2025-002",
      "action_required": "Valorar notificación extemporánea. Incluir indemnidad específica en SPA."
    }
  ]
}
```

## Metodología de Análisis

### 1. Reglas de Compliance RGPD

| Artículo | Verificación | Severidad si Gap |
|----------|--------------|------------------|
| **Art. 30 (RAT)** | ¿Existe registro? ¿Todos los tratamientos documentados? ¿Campos completos? | Alta |
| **Art. 28 (DPA)** | ¿DPA firmado? ¿Instrucciones, confidencialidad, medidas seguridad, subencargados, asistencia, destrucción, auditoría? | Alta |
| **Cap. V (Transferencias)** | ¿Decisión adecuación, SCC, BCR? ¿TIA completada (post-Schrems II)? | Alta |
| **Art. 35 (EPIA)** | ¿Tratamiento alto riesgo? ¿EPIA realizada? | Media |
| **Art. 33 (Brechas)** | ¿Incidentes notificados en 72h? ¿Documentados? | Crítica si incumplimiento |

### 2. Scoring de Madurez de Seguridad

| Nivel | Score | Descripción |
|-------|-------|-------------|
| **Inicial** | 1 | Procesos ad-hoc, no documentados |
| **Gestionado** | 2 | Procesos definidos pero no consistentes |
| **Definido** | 3 | Procesos documentados y estandarizados |
| **Gestionado cuantitativamente** | 4 | Métricas y KPIs de seguridad |
| **Optimizado** | 5 | Mejora continua, benchmark industria |

### 3. Priorización de Vulnerabilidades

```
Risk Score = CVSS Base × Factor de Exposición × Factor de Criticidad del Sistema

Factor de Exposición:
- Internet: 1.0
- DMZ: 0.8
- Interno: 0.5

Factor de Criticidad:
- Crítico: 1.0
- Alto: 0.8
- Medio: 0.5
- Bajo: 0.3
```

### 4. Análisis de Licencias OSS

| Licencia | Tipo | Obligación | Riesgo para Producto Comercial |
|----------|------|------------|-------------------------------|
| **GPL v2/v3** | Copyleft fuerte | Source disclosure en distribución | CRÍTICO si integrado |
| **AGPL v3** | Copyleft fuerte + SaaS | Source disclosure incluso en uso de red | CRÍTICO para SaaS |
| **LGPL** | Copyleft débil | Solo modificaciones del componente | MEDIO |
| **MIT, Apache 2.0** | Permisiva | Atribución | BAJO |

## Módulos de Riesgo

### Shadow IT

- **Detección**: Análisis de gastos IT (facturas cloud, SaaS)
- **Cuestionario**: Management sobre herramientas no autorizadas

### Informes de Auditoría Desactualizados

- **Verificación**: Fecha último informe >12 meses = flag
- **Recomendación**: Nueva evaluación como condición de cierre

### Transposición NIS2 Durante el Deal

- **Monitor legislativo**: BOE, tramitación parlamentaria
- **Evaluación proactiva**: Cumplimiento NIS2 anticipado
- **SPA**: Cláusula de ajuste para cambios normativos

### Zero-Day en Componentes Detectados

- **Monitorización continua**: NVD/CVE durante período DD
- **Alerta inmediata**: Nuevo CVE crítico en componente inventariado

## Alertas Automáticas

| Trigger | Severidad | Mensaje |
|---------|-----------|---------|
| CVSS ≥9.0 en sistema expuesto | CRÍTICO | "CVE [id] crítico en [sistema]. Parchear antes de closing" |
| GPL/AGPL en producto comercial | CRÍTICO | "Componente [nombre] con [licencia] en producto comercial. Riesgo IP" |
| Brecha no notificada | ALTO | "Incidente [id] no notificado a AEPD. Riesgo sancionador [X]€" |
| SCC pre-2021 sin migrar | ALTO | "Encargado [nombre] con SCC obsoletas. Migración obligatoria" |
| TIA ausente para transferencia | ALTO | "Transferencia a [país] sin TIA. Requisito Schrems II" |
| Escrow ausente en sistema crítico | MEDIO | "[N] sistemas críticos sin escrow de código fuente" |

## Controles de Calidad

- **Pruebas de proporcionalidad**: Solo metadata y configuraciones, no datos de producción
- **Cadena de custodia**: Informes clasificados "Confidencial — DD" con hash
- **Exclusión de entornos productivos**: No tests intrusivos sin autorización escrita
- **NDA reforzado**: Destrucción de hallazgos técnicos al cierre del mandato

## KPIs de Rendimiento

| KPI | Objetivo |
|-----|----------|
| % DPAs adecuados identificados | 100% de encargados verificados |
| Vulnerabilidades CVSS ≥9.0 remediadas pre-closing | 100% |
| Cobertura inventario OSS | ≥ 95% componentes identificados |
| Tiempo a propuesta remediación para riesgo crítico | ≤ 48 horas |
| Precisión scoring madurez | ≤ 0.5 puntos vs. evaluación externa |

## Consideraciones Éticas

- No acceso a datos personales de producción
- Confidencialidad de arquitectura de seguridad
- Disclosure responsable de vulnerabilidades
- Respeto a propiedad intelectual de terceros

## Compliance

- Cifrado AES-256 en reposo, TLS 1.3 en tránsito
- Seudonimización de identificadores de usuarios en logs
- Registros inmutables con hash SHA-256
- Destrucción segura al cierre del mandato
