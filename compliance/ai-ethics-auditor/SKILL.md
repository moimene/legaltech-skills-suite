---
name: ai-ethics-auditor
description: Audit AI systems against EU AI Act (Regulation 2024/1689). Classify risk levels (prohibited/high-risk/limited/minimal), assess conformity procedures (self-assessment or notified body), conduct FRIA, and generate compliance roadmap with binding timelines.
---

# AI Ethics Auditor

Evaluate AI systems against the **EU AI Act** (Regulation 2024/1689, 13 Dec 2024) to determine risk classification, legal compliance obligations, and implementation timelines across three enforcement phases.

## Trigger Contexts

- Pre-market audit of new AI systems targeting EU market
- Due diligence on AI vendors or M&A targets
- Post-incident bias or discrimination assessments
- Conformity assessment procedure selection (self-certification vs notified body review)
- High-risk system documentation and quality assurance
- FRIA (Fundamental Rights Impact Assessment) for public sector deployments

---

## Legal Framework: Three-Phase Timeline

| Phase | Deadline | Scope |
|-------|----------|-------|
| **Phase 1: Prohibition** | 2 Aug 2025 | Annexes I & II systems banned; unacceptable-risk AI |
| **Phase 2: High-Risk** | 2 Aug 2026 | Annexes III-VI: governance, FRIA, documentation, notified body |
| **Phase 3: Full Regime** | 2 Aug 2027 | All remaining obligations (limited-risk transparency, minimal-risk baseline) |

---

## Risk Classification Decision Tree

```
Does system use high-precision biometric tracking
for remote real-time identification?
├─ YES → PROHIBITED (Art. 5, exceptions: law enforcement)
└─ NO ↓

Does system manipulate behavior to circumvent free will,
exploit vulnerable groups, or assess social credit?
├─ YES → PROHIBITED (Art. 5)
└─ NO ↓

Does system fall into Annex III scope?
(employment, education, credit, law enforcement, utilities, migration)
├─ YES → HIGH-RISK (Annex III enumeration)
│        Requires: Risk management, FRIA, documentation,
│        conformity assessment, post-market monitoring
└─ NO ↓

Does system involve transparency obligations?
(emotion recognition, deepfakes, user notification)
├─ YES → LIMITED-RISK (Art. 52)
│        Transparency notices to users
└─ NO ↓

Remaining AI systems → MINIMAL-RISK (Best practices recommended)
```

---

## High-Risk Systems: Annex III Categories

| Sector | Specific Activities | Art. Ref |
|--------|-------------------|---------|
| **Employment** | Recruitment filtering, performance evaluation | III.4(a)-(c) |
| **Education** | Admissions, learning progress assessment | III.2(a)-(b) |
| **Finance** | Credit scoring, insurance underwriting | III.5(a)-(b) |
| **Biometrics** | Remote facial identification, emotion detection | III.1(a)-(d) |
| **Law Enforcement** | Predictive policing, suspect profiling | III.7(a)-(b) |
| **Infrastructure** | Traffic management, critical utilities | III.3(a)-(d) |
| **Migration** | Border control, visa assessment | III.8(a)-(b) |
| **Justice** | Sentencing assistance, legal research | III.6(a)-(b) |

---

## Core Requirements for High-Risk Systems

| Obligation | Article | Key Elements |
|-----------|---------|--------------|
| **Risk Management System** | 9 | Iterative process identifying, analyzing, evaluating risks throughout lifecycle |
| **Data Quality & Governance** | 10 | Training data representativeness, bias detection, documentation |
| **Technical Documentation** | 11 | Model architecture, performance metrics, testing protocols, limitations |
| **Transparency & Instruction** | 13 | User manuals, clear warnings about system limitations |
| **Human Oversight Mechanisms** | 14 | Meaningful human intervention before consequential decisions |
| **Accuracy & Robustness Testing** | 15 | Baseline accuracy, adversarial robustness, edge case performance |
| **Cybersecurity & Logging** | 16-17 | Intrusion detection, audit trails, version control |

---

## Conformity Evidence Pack por Caso de Uso

### Estructura de Paquete de Evidencias

Cada caso de uso requiere un paquete de conformidad documentado conforme al Art. 13-15 de la Regulación 2024/1689:

| Elemento de Evidencia | Requisito Legal | Descripción |
|----|----|------|
| **Documentación técnica** | Art. 11 | Especificación de modelo, métricas de rendimiento, limitaciones conocidas |
| **Sistema de gestión de riesgos** | Art. 9 | Proceso iterativo de identificación, análisis, evaluación y mitigación |
| **Gobernanza de datos** | Art. 10 | Representatividad de datos, detección de sesgos, documentación |
| **Transparencia** | Art. 13 | Instrucciones claras al usuario; advertencias de limitaciones |
| **Supervisión humana** | Art. 14 | Mecanismos de intervención significativa en decisiones críticas |
| **Precisión y robustez** | Art. 15 | Testing de precisión, robustez adversarial, rendimiento en casos extremos |

### Niveles de Riesgo y Requisitos por Conformidad

| Nivel de Riesgo | Artículos Aplicables | Requisitos Mínimos | Conformidad |
|----|----|----|----|
| **Mínimo (Art. 6)** | - | Transparencia recomendada; mejores prácticas | Autodeclaración |
| **Limitado (Art. 50)** | Art. 50 | Divulgación de AI + restricciones de contenido | Notificación de usuario |
| **Alto Riesgo (Anexo III)** | Art. 9-17 | Sistema de riesgos + FRIA + documentación + testing | Autoevaluación + opción de Organismo Notificado |
| **Prohibido (Art. 5)** | Art. 5 | Bloqueo inmediato de desarrollo; denuncia a autoridades | No permitido |

### Checklist de Evidencias por Anexo IV (Documentación Técnica)

**Art. 13 AI Act + ANEXO IV - Documentación Técnica Requerida:**

```markdown
☐ **Descripción General**
  - Propósito del sistema AI
  - Versión del modelo y fecha
  - Responsable legal (fabricante/distribuidor)

☐ **Información Técnica**
  - Arquitectura del modelo (ej: BERT, redes neuronales)
  - Tamaño del modelo y requisitos computacionales
  - Framework utilizado (TensorFlow, PyTorch, etc.)
  - Lenguaje de entrenamiento (si aplica)

☐ **Ciclo de Vida del Modelo**
  - Fases de desarrollo: recopilación, preprocesamiento, entrenamiento, validación
  - Metodología de validación cruzada
  - Versionado del modelo (Git hash, release notes)

☐ **Especificación de Datos**
  - Origen de datos de entrenamiento (datasets + cantidad)
  - Estadísticas de representatividad (edad, género, región, etc.)
  - Procedimientos de limpieza y aumento de datos
  - Desequilibrios detectados y mitigaciones

☐ **Métricas de Rendimiento**
  - Precisión general: % correcto
  - Recall por clase (si multi-clase)
  - Precisión segmentada por grupo demográfico (género, edad, raza)
  - F1-score, ROC-AUC, matriz de confusión
  - Umbrales de decisión utilizados

☐ **Limitaciones y Advertencias**
  - Idiomas no soportados
  - Poblaciones no representadas en entrenamiento
  - Tasas de error conocidas
  - Casos de uso prohibidos (Art. 5)

☐ **Pruebas de Robustez**
  - Testing adversarial (adversarial examples)
  - Testing fuera de distribución (datos nunca vistos)
  - Casos extremos y edge cases
  - Ataques adversariales documentados y mitigaciones

☐ **Cumplimiento Regulatorio**
  - Referencias a Regulación 2024/1689
  - Evaluación FRIA (si aplica)
  - Registro en AESIA (si alto riesgo)
  - Verificación de prohibiciones Art. 5

☐ **Responsabilidad y Gobernanza**
  - Personas responsables (Data Officer, Compliance)
  - Historial de cambios documentado
  - Plan de monitoreo post-mercado (Art. 72)
```

### Plantilla de Evidence Pack por Caso de Uso

**Ejemplo: Sistema de IA para Selección de Personal (HR)**

```json
{
  "caso_uso": "Reclutamiento automatizado de candidatos",
  "clasificacion_riesgo": "ALTO_RIESGO (Anexo III.4(a))",
  "evidence_pack": {
    "nivel_1_descripcion_general": {
      "titulo": "HR Screening AI v2.3 - Paquete de Conformidad",
      "fabricante": "TechStaff Solutions GmbH",
      "version_modelo": "2.3.1",
      "fecha_documentacion": "2024-02-06",
      "articulos_aplicables": ["Art. 9-17", "Art. 43"]
    },
    "nivel_2_documentacion_tecnica": {
      "arquitectura": "BERT-base-uncased (110M params) + Gradient Boosting re-ranker",
      "tamaño_modelo_mb": 440,
      "framework": "PyTorch 2.0 + XGBoost 2.0",
      "version_control": "Git commit 3a7f2e9c; branch: production-v2.3",
      "datos_entrenamiento": {
        "dataset": "450K resumes from 12 enterprise clients (2018-2022)",
        "tamaño": "2.3 GB",
        "limpieza": "Remover PII; normalizar formato; removing duplicates",
        "estadisticas": {
          "candidatos_masculinos_pct": 87,
          "candidatos_femeninos_pct": 13,
          "regiones_sobrerrepresentadas": ["USA (45%)", "UK (28%)", "Western Europe (27%)"],
          "regiones_subrepresentadas": ["CEE (0%)", "Southern Europe (1%)"]
        }
      }
    },
    "nivel_3_metricas_rendimiento": {
      "precision_global": "91%",
      "precision_por_genero": {
        "masculino": "92%",
        "femenino": "90%",
        "varianza": "2% - ACEPTABLE (<5%)"
      },
      "recall_tech_roles": {
        "masculino": "93%",
        "femenino": "88%",
        "varianza": "5% - CRÍTICA; requiere reentrenamiento"
      },
      "precision_por_idioma": {
        "ingles": "94%",
        "otros_idiomas": "67%",
        "advertencia": "No validado para CVs no-inglés"
      }
    },
    "nivel_4_limitaciones": [
      "No validado para CVs en idiomas no-inglés",
      "Tasa de falsos negativos: 9% (sistema puede rechazar candidatos calificados)",
      "Brecha de rendimiento por género en roles técnicos: 5%",
      "Requiere revisión humana para candidatos frontera (40-60 score)"
    ],
    "nivel_5_pruebas_robustez": {
      "adversarial_testing": "50 ejemplos adversariales (CVs manipulados)",
      "ood_performance": "Testing en datos de regiones no vistas en entrenamiento",
      "edge_cases": "Candidatos sin experiencia previa; cambios de carrera; gaps de empleo"
    },
    "nivel_6_conformidad_art_9_17": {
      "art_9_riesgos": {
        "identificados": ["Gender bias", "Language discrimination", "Socioeconomic proxy"],
        "mitigaciones": ["Fairness-aware retraining", "Quarterly audits", "Mandatory human review"]
      },
      "art_10_datos": {
        "representatividad": "Brecha identificada: rebalancear a 40% mujeres",
        "limpieza": "Procedimiento documentado",
        "sesgo": "Análisis de igualdad de oportunidades completado"
      },
      "art_11_documentacion": "COMPLETADA (este documento)",
      "art_13_transparencia": "Usuario notice incluida en interfaz",
      "art_14_supervision": "Revisión humana para borderline scores y fase piloto",
      "art_15_precision": "Testing de precisión por subgrupos completado",
      "art_16_17_seguridad": "Logging inmutable; versión control; intrusion detection evaluado"
    }
  }
}
```

---

## Conformity Assessment Procedures

### Self-Assessment (Internal Evaluation)
**Applies to:** Most Annex III high-risk systems (default route)
- Manufacturer conducts risk management & testing in-house
- Prepare technical file + FRIA (if public sector)
- Maintain conformity declaration internally (no external approval required)
- **Timeline:** Begin immediately; must complete by 2 Aug 2026

### Notified Body Assessment
**Triggers:** Public procurement, sensitive applications (law enforcement, automated decision-making)
- Third-party accredited conformity assessment body reviews high-risk system
- Body issues EU technical documentation opinion
- **Timeline:** Apply to notified body by 1 Aug 2025 (3-6 month review cycle)

---

## FRIA Methodology (Fundamental Rights Impact Assessment)

**Mandatory for:** High-risk systems in public sector; strongly recommended for private deployments

### Protected Rights to Evaluate

| Right | Assessment Focus | Mitigation Examples |
|------|------------------|-------------------|
| Non-discrimination | Bias by protected class (gender, age, race) | Stratified accuracy testing, fairness metrics |
| Data protection | Purpose limitation, storage duration | Data minimization, retention policies, DPIA |
| Human dignity | Automated mass profiling, dehumanization | Meaningful human review, appeal mechanisms |
| Freedom of expression | Content moderation, filtering systems | Transparent flags, human review of critical decisions |
| Effective remedy | Access to contestation & explanation | Explainability requirements, clear appeal process |
| Children's rights | Special protections for minors | Age verification, parental consent, no behavioral tracking |

### FRIA Output Structure
```json
{
  "rights_assessment": [
    {
      "right": "Non-discrimination (Art. 21 CFR)",
      "risk_level": "HIGH",
      "evidence": "HR AI screened 2019-2023 resumes; gender gap in 'technical role' scores: 18% lower for female candidates",
      "mitigation": "Implement fairness constraints; achieve <5% disparity across protected classes"
    }
  ],
  "residual_risk": "MEDIUM-HIGH",
  "recommendation": "Deploy only with human-in-the-loop review; quarterly bias audits"
}
```

---

## Concrete Example: HR Screening AI Audit

**System:** TalentScreen HR v2.3
**Manufacturer:** TechStaff Solutions GmbH (Germany)
**Market:** EU-wide SaaS subscription
**Timeline:** Deploy in 6 months

### Step 1: Risk Classification
- **Question:** Automatic CV screening with "pre-selection" output (yes/no recommendation)?
- **Answer:** Yes; directly impacts employment opportunity access
- **Classification:** **HIGH-RISK** (Annex III.4(a) - recruitment)
- **Consequence:** Full Art. 9-17 compliance required by 2 Aug 2026

### Step 2: Risk Management Cycle (Art. 9)

**Hazard Identification:**
- Bias risks: System trained on 450K historical resumes (2018-2022) from enterprise clients; 87% male candidates in tech roles
- Accuracy risks: Algorithm drops from 94% accuracy to 67% for non-English CVs
- Discrimination risk: Features encoding education prestige (proxy for socioeconomic background, correlating with protected characteristics)

**Risk Mitigation Plan:**
- Remove prestige-based education scoring; substitute sector experience duration
- Audit data: stratify accuracy by gender (target: <5% variance)
- Human review required for: (a) borderline candidates (score 40-60), (b) all rejections in pilot phase
- Quarterly bias testing using external auditor (e.g., Fairlytics)

### Step 3: Data Quality Assessment (Art. 10)

**Training Data:**
- Source: 450K resumes from 12 client companies (tech, finance, consulting)
- Representativeness gap: Only 18% female candidates; underrepresented regions (no CEE/southern Europe data)
- Bias detection: Equal opportunity analysis shows 23% lower callback rate for female technical roles after controlling for qualifications

**Mitigation:**
- Rebalance training data to 40% female candidates (synthetic augmentation or data purchasing)
- Include geographic diversity (minimum 10% non-Western Europe)
- Implement fairness constraints: Threshold equality (equal true positive rate across genders)

### Step 4: Technical Documentation (Art. 11)

**Required sections:**
- Model architecture: BERT-based sequence classifier + gradient boosting re-ranker
- Performance metrics by demographic group:
  - Overall accuracy: 91% | Gender parity: 90% (F) vs 92% (M) | Acceptable
  - Recall in tech roles: 88% (F) vs 93% (M) | Acceptable (>5% gap) → Prioritize mitigation
- Limitations: "System not validated for non-English CVs; human review mandatory for candidates with <1 year experience"
- Testing protocols: Adversarial robustness (50 edge cases); out-of-distribution performance (resumes from non-training regions)

### Step 5: Conformity Assessment Decision

**Route A: Self-Assessment**
- Create internal technical file + FRIA (no external approval)
- Maintain evidence: bias audit reports, test results, mitigation logs
- Timeline: 4 months

**Route B: Notified Body**
- Engage TÜV SÜD or Bureau Veritas AI certification (cost: €15K-40K)
- Submit technical documentation; NB issues conformity opinion by Month 6
- Recommended if: high public sector adoption, media scrutiny, past discrimination allegations

**Recommendation:** Self-assessment + independent fairness audit (lower cost, same assurance)

### Step 6: Transparency & User Instruction (Art. 13)

**User Documentation Required:**
```
IMPORTANT: This system uses AI to pre-screen resumes.

Purpose: Identify candidates matching role requirements (technical skills, experience, education)

Limitations:
- System has not been validated for non-English resumes or atypical career paths
- False negative rate: ~9% (system may reject qualified candidates)
- System shows gender performance variation (see Technical Specification)

Recommendation:
- Use system for initial shortlisting only
- Human recruiter must review all borderline candidates (scores 40-60)
- Conduct final review without system input to ensure diversity

Your Rights:
- Request explanation for rejection (Art. 15(3) link)
- Appeal to HR department ([contact])
- Lodge complaint with Spanish AESIA (aesia@aesia.es)
```

### Step 7: FRIA (if hiring for public sector role)

| Fundamental Right | Risk | Mitigation | Status |
|------------------|------|-----------|--------|
| Non-discrimination | HIGH (historic bias in data) | Gender parity testing <5%; fairness reweighting | ACCEPTED |
| Human dignity | MEDIUM (fully autonomous decision) | Mandatory human review for borderline cases | ACCEPTED |
| Effective remedy | MEDIUM (no system explanation) | Implement SHAP explainability; human appeal process | PARTIAL (remediation planned Q3) |

---

## Inputs

```json
{
  "sistema": {
    "nombre": "TalentScreen HR v2.3",
    "fabricante": "TechStaff Solutions",
    "ubicacion_fabricante": "Munich, Germany",
    "proposito": "Automatic CV screening and candidate pre-ranking for recruitment",
    "datos_entrada": ["Resume PDF/Word", "Job description text"],
    "output": "Risk score 0-100 + pass/fail recommendation + ranking",
    "decision_autonoma": false,
    "humano_en_el_loop": true,
    "datos_training": "450K resumes 2018-2022; 12 enterprise clients",
    "mercado_objetivo": "UE",
    "sector_clientes": ["Technology", "Finance", "Consulting"],
    "volumen_anual": "2.5M resume evaluations"
  }
}
```

---

## Output

```json
{
  "auditoria": {
    "fecha": "2024-02-06",
    "auditor": "Magic Circle Legal AI Compliance",
    "sistema": "TalentScreen HR v2.3"
  },
  "clasificacion_riesgo": {
    "nivel": "ALTO (High-Risk)",
    "base_legal": "Regulation 2024/1689, Annex III.4(a) - Recruitment and employment selection",
    "ruta_conformidad": "Self-assessment (internal evaluation) + independent bias audit",
    "notified_body_requerida": false,
    "deadline_cumplimiento": "2026-08-02"
  },
  "evaluacion_requisitos": [
    {
      "id": "AIA-R1",
      "requisito": "Risk Management System (Art. 9)",
      "status": "PENDIENTE",
      "evidencia_requerida": "Documented iterative process for identification, analysis, evaluation, mitigation",
      "prioridad": "CRITICA",
      "plazo": "Antes de launch (6 meses)"
    },
    {
      "id": "AIA-R2",
      "requisito": "Data Quality Assessment (Art. 10)",
      "status": "PARCIAL",
      "hallazgo": "Training data imbalanced: 87% male in tech roles; only 12 enterprise sources",
      "mitigacion": "Rebalance to 40% female; add geographic diversity; implement fairness constraints",
      "prioridad": "CRITICA",
      "plazo": "Antes de launch"
    },
    {
      "id": "AIA-R3",
      "requisito": "Technical Documentation (Art. 11)",
      "status": "NO_CUMPLE",
      "gaps": [
        "Missing performance metrics by gender and region",
        "Accuracy variance by language not documented (67% vs 94%)",
        "Adversarial robustness testing incomplete"
      ],
      "prioridad": "ALTA",
      "plazo": "Antes de launch"
    },
    {
      "id": "AIA-R4",
      "requisito": "Transparency & User Instructions (Art. 13)",
      "status": "NO_CUMPLE",
      "gaps": ["No user warnings about system limitations", "No explanation rights notification"],
      "prioridad": "ALTA"
    },
    {
      "id": "AIA-R5",
      "requisito": "Human Oversight (Art. 14)",
      "status": "PARCIAL",
      "evidencia": "All top-100 candidates reviewed by human; borderline cases (40-60 score) require approval",
      "mejora": "Mandate human review for all rejections in first 6 months (pilot phase)",
      "prioridad": "MEDIA"
    },
    {
      "id": "AIA-R6",
      "requisito": "Accuracy & Robustness (Art. 15)",
      "status": "PARCIAL",
      "hallazgo": "Overall accuracy 91%; gender disparity in recall (88% F vs 93% M); non-English accuracy 67%",
      "target": "Achieve <5% accuracy variance by protected class; >85% accuracy on all languages",
      "prioridad": "ALTA"
    },
    {
      "id": "AIA-R7",
      "requisito": "Cybersecurity & Audit Logging (Art. 16-17)",
      "status": "EVALUACION_PENDIENTE",
      "requisitos": "Version control of training data; immutable logs of all decisions; intrusion detection",
      "prioridad": "MEDIA"
    }
  ],
  "fria_assessment": {
    "requerida": true,
    "contexto": "System used for public sector hiring (EU institutions) in Phase 2 expansion",
    "derechos_evaluados": [
      {
        "derecho": "Non-discrimination (Art. 21 CFR)",
        "riesgo": "ALTO",
        "evidencia": "18% lower 'technical role' scores for female candidates in training data",
        "mitigacion": "Fairness-aware retraining; stratified accuracy testing; mandatory human review",
        "aceptable": true,
        "condiciones": "Implement mitigation before public sector deployment"
      },
      {
        "derecho": "Data Protection (Art. 8 GDPR)",
        "riesgo": "MEDIO",
        "evidencia": "System processes personal data (resume content, inferred demographics)",
        "mitigacion": "Data minimization (only job-relevant features); retention policy (delete after 2 years)",
        "aceptable": true
      },
      {
        "derecho": "Effective Remedy (Art. 47 CFR)",
        "riesgo": "MEDIO",
        "evidencia": "System provides no explanation for rejections; no appeal mechanism",
        "mitigacion": "Implement SHAP explainability module; HR appeal process; link to AESIA complaint channel",
        "aceptable": true,
        "condiciones": "Deploy explanation mechanism before full launch"
      }
    ],
    "conclusion": "System acceptable for private sector recruitment with mitigations. Public sector deployment requires enhanced transparency and appeal mechanisms."
  },
  "timeline_eu_ai_act": {
    "fase_1_prohibicion": "2025-08-02",
    "fase_2_alto_riesgo": "2026-08-02",
    "fase_3_regimen_completo": "2027-08-02",
    "acciones_inmediatas": [
      "1. Document risk management process (Art. 9) - 4 weeks",
      "2. Conduct bias audit; rebalance training data - 8 weeks",
      "3. Complete technical documentation with stratified metrics - 6 weeks",
      "4. Implement transparency notices and explanation rights - 4 weeks",
      "5. Deploy human oversight controls (pilot phase rejection review) - 2 weeks",
      "6. Conduct FRIA if public sector market planned - 6 weeks"
    ]
  },
  "conformity_assessment_recommendation": {
    "ruta_seleccionada": "Self-Assessment (Art. 43)",
    "razon": "Private sector deployment; no law enforcement involvement; manufacturer internal QA sufficient",
    "alternativa": "Notified Body Assessment (Art. 43-44) recommended if: EU public procurement, high media scrutiny, or post-incident remediation",
    "costo_estimado": "Self: €8K (internal audit); Notified Body: €20K-50K (3-6 month review)"
  },
  "spanish_regulator_references": {
    "aesia": "Agencia Española de Supervisión de IA (established 2024)",
    "aesia_contact": "aesia@aesia.es",
    "competencia": "Oversee high-risk AI in Spain; process complaints; impose sanctions up to 6% global revenue",
    "aepd_role": "GDPR coordination where personal data processing intersects with AI governance"
  },
  "ai_liability_directive_implications": {
    "regulation": "Directive 2024/2571 (complementary to AI Act)",
    "aplicabilidad": "TalentScreen HR v2.3 causes discrimination → liability exposure if: (1) system defect proved, (2) causal link to harm, (3) damage quantifiable",
    "mitigacion": "Implement documented risk management (Art. 9) to establish reasonable care defense",
    "exposure": "Recruitment discrimination claims may trigger product liability; insurance required"
  },
  "hallazgos_criticos": [
    {
      "id": "CRIT-1",
      "titulo": "Data Imbalance Creates Discrimination Risk",
      "descripcion": "87% male training data in tech roles creates systematic underprediction for female candidates",
      "severidad": "CRITICA",
      "deadline_remediacion": "Antes de launch (6 meses)",
      "responsable": "Data Science + Compliance",
      "esfuerzo": "Medio"
    },
    {
      "id": "CRIT-2",
      "titulo": "Missing Technical Documentation",
      "descripcion": "Art. 11 requires complete model specification, performance metrics by subgroup, limitations. Current: only overall accuracy reported.",
      "severidad": "CRITICA",
      "deadline_remediacion": "Antes de launch",
      "responsable": "Engineering",
      "esfuerzo": "Bajo"
    },
    {
      "id": "HIGH-1",
      "titulo": "No Transparency Mechanism",
      "descripcion": "Art. 13 requires clear user notification of AI use and system limitations. No current implementation.",
      "severidad": "ALTA",
      "deadline_remediacion": "Antes de launch",
      "responsable": "Product + Legal",
      "esfuerzo": "Bajo"
    }
  ],
  "riesgo_sancion": {
    "regulacion": "EU AI Act + complementary Liability Directive (2024/2571)",
    "sanciones_maximas": {
      "violacion_prohibiciones": "€30M o 6% revenue global (whichever higher)",
      "incumplimiento_alto_riesgo": "€20M o 4% revenue global",
      "documentacion_falsa": "€10M o 2% revenue global"
    },
    "atenuantes": [
      "Proactive self-assessment",
      "Documented risk management and mitigation efforts",
      "Voluntary disclosure to regulator"
    ],
    "agravantes": [
      "Deployment without risk assessment (Art. 9)",
      "Concealment of bias from regulators",
      "Discriminatory outcome in practice (multiple complaints)"
    ],
    "nivel_riesgo_actual": "BAJO-MEDIO (pre-launch; mitigation possible)",
    "nivel_riesgo_post_launch": "ALTO (if mitigation not completed)"
  },
  "checklist_implementacion": [
    {
      "item": "1. Risk Management System (Art. 9)",
      "deadline": "2024-04-06",
      "responsable": "Compliance Officer"
    },
    {
      "item": "2. Data Bias Audit + Rebalancing",
      "deadline": "2024-05-06",
      "responsable": "Data Science Lead"
    },
    {
      "item": "3. Technical Documentation (Art. 11)",
      "deadline": "2024-05-20",
      "responsable": "Engineering + Product"
    },
    {
      "item": "4. FRIA (if public sector planned)",
      "deadline": "2024-06-06",
      "responsable": "Compliance + Legal"
    },
    {
      "item": "5. Transparency Notices & Instruction (Art. 13)",
      "deadline": "2024-04-15",
      "responsable": "Product + Legal"
    },
    {
      "item": "6. Human Oversight Controls (Art. 14)",
      "deadline": "2024-04-01",
      "responsable": "Product Engineering"
    },
    {
      "item": "7. Pre-Launch Compliance Review",
      "deadline": "2024-08-06",
      "responsable": "Legal + Compliance"
    },
    {
      "item": "8. Post-Market Monitoring Plan (Art. 72)",
      "deadline": "2024-08-06",
      "responsable": "Compliance + Quality Assurance"
    }
  ]
}
```

---

## Checklists de Transparencia y Registro

### Art. 13 AI Act: Información para Desplegadores (Required for High-Risk Systems)

**Obligación:** Antes de desplegar un sistema AI de alto riesgo, el fabricante debe proporcionar al desplegador información clara sobre:

```markdown
☐ **Identidad y Contacto**
  - Nombre del fabricante
  - Domicilio registrado
  - Persona responsable para cuestiones técnicas
  - Email y teléfono de contacto

☐ **Propósito y Uso Previsto**
  - Descripción clara del propósito del sistema
  - Casos de uso permitidos y prohibidos
  - Poblaciones objetivo

☐ **Rendimiento y Limitaciones**
  - Precisión general (%)
  - Precisión por grupo demográfico (varianza máxima)
  - Tasa de error conocida (falsos positivos/negativos)
  - Idiomas soportados
  - Limitaciones técnicas conocidas

☐ **Requisitos de Supervisión Humana**
  - Tipo de intervención humana requerida (revisión, aprobación, anulación)
  - Procedimiento de escalada para decisiones críticas
  - Contacto de recurso/apelación para usuarios

☐ **Cumplimiento Regulatorio**
  - Conformidad con Regulación 2024/1689
  - Resultado de FRIA (si aplica)
  - Referencias a AESIA (si registrado)

☐ **Derechos del Usuario**
  - Derecho a explicación (Art. 15.3)
  - Derecho a impugnar decisión
  - Procedimiento de reclamación ante AESIA

☐ **Documentación Técnica**
  - Resumen ejecutivo de especificación técnica
  - Metodología de validación
  - Plan de monitoreo post-mercado
```

### Art. 49 AI Act: Registro de Sistemas AI de Alto Riesgo en BD Centralizada EU

**Aplicable a:** Todos los sistemas clasificados como alto riesgo (Anexo III) distribuidos en UE

**Responsable:** Fabricante (antes de comercialización)

**Información Requerida en Registro:**

```json
{
  "registro_sistema_alto_riesgo": {
    "identificacion_fabricante": {
      "nombre": "TechStaff Solutions GmbH",
      "pais": "Germany",
      "numero_registro": "DE12345678"
    },
    "identificacion_sistema": {
      "nombre_comercial": "HR Screening AI v2.3",
      "categoria_anexo_iii": "4(a) - Recruitment and employment",
      "version": "2.3.1",
      "descripcion_breve": "Sistema automatizado de selección de CV para reclutamiento"
    },
    "informacion_tecnica": {
      "arquitectura_modelo": "BERT + Gradient Boosting",
      "framework": "PyTorch 2.0",
      "precision_global": "91%",
      "fecha_entrenamiento": "2022-11-30",
      "datos_entrenamiento_resume": "450K CVs, 12 enterprise clients"
    },
    "conformidad": {
      "art_43_ruta": "Self-assessment",
      "organismo_notificado": null,
      "fria_realizada": true,
      "mitigaciones_documentadas": true
    },
    "contacto_responsable": {
      "nombre": "Compliance Officer",
      "email": "compliance@techstaff.de",
      "telefono": "+49-30-1234567"
    },
    "mercados_objetivo": ["Germany", "Spain", "France", "EU-wide"],
    "fecha_comercializacion_prevista": "2024-06-30"
  }
}
```

### Art. 50 AI Act: Transparencia para Sistemas de IA Generativa y Chatbots

**Aplicable a:** Modelos de lenguaje generativo, sistemas de síntesis de voz/imagen, chatbots

**Requisitos de Divulgación:**

```markdown
**Plantilla de Aviso de Transparencia (obligatorio en interfaz):**

─────────────────────────────────────────────────────────
⚠️ AVISO DE SISTEMA AI GENERATIVO

Este sistema utiliza inteligencia artificial para [generar texto/sintetizar voz/crear imágenes]

**Información sobre el Sistema:**
- Modelo base: [ej: GPT-4, Claude 3]
- Fecha de entrenamiento: [ej: hasta Marzo 2024]
- Capacidad de aprendizaje: [Sí/No - ¿Aprende de mis inputs?]

**Limitaciones Conocidas:**
- Puede generar contenido inexacto o alucinaciones
- No está entrenado en datos posteriores a [fecha]
- No garantiza información médica/legal
- Sesgos potenciales: [describir si conocidos]

**Derechos:**
- Puede impugnar esta decisión: [contacto]
- Reclamar ante AESIA: aesia@aesia.es
- Solicitar explicación: [enlace a formulario]

**No Autorizado Para:**
- Crear contenido de suplantación (deepfakes)
- Simulación de identidad sin consentimiento
- Contenido sexual involucrando menores
- Violencia o incitación al odio

─────────────────────────────────────────────────────────
```

### Integración AESIA Registry (cuando disponible)

**AESIA (Agencia Española de Supervisión de IA)** - Registro en desarrollo

Cuando se lance el registro AESIA:

```markdown
☐ **Paso 1:** Acceder a https://registry.aesia.es (portal de auto-registro)
☐ **Paso 2:** Cargar paquete de evidencias (documentación técnica + FRIA + mitigation plan)
☐ **Paso 3:** Validación automática de checklist de Art. 11-17
☐ **Paso 4:** Recibir certificado de conformidad (válido para 3 años con auditoría anual)
☐ **Paso 5:** Publicación en registro público (con datos no-sensibles)
☐ **Paso 6:** Monitoreo post-mercado y reporte anual de incidentes
```

---

## Spanish Regulatory References

- **AESIA (Agencia Española de Supervisión de IA):** Established under Regulation 2024/1689; monitors high-risk AI deployments in Spain; issues guidance and penalties; registro en https://aesia.es
- **AEPD (Autoridad de Protección de Datos Españoles):** Coordinates GDPR compliance with AI governance for data processing activities
- **Real Decreto framework:** Spanish implementation rules expected by Aug 2025
- **Registro Central AI (AESIA):** Previsto para Q3-Q4 2025; alojará documentación técnica de sistemas alto riesgo con validación de conformidad

---

## AI Liability Directive (2024/2571)

**Key Impact:** Manufacturers of high-risk AI systems bear liability for defects causing harm if:
1. System defect demonstrated (failure to meet AI Act requirements)
2. Causal nexus between defect and injury
3. Quantifiable damages (discrimination, financial loss)

**Mitigation:** Maintain complete documentation of risk management (Art. 9) and post-market monitoring (Art. 72) to establish "reasonable care" defense.

---

## References

- **Regulation (EU) 2024/1689** (EU AI Act): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **EDPB AI Guidelines** (coordination with GDPR): https://edpb.ec.europa.eu/our-work-tools/documents/public-consultations-art-64_en
- **AI Liability Directive 2024/2571**: https://eur-lex.europa.eu/eli/dir/2024/2571/oj
