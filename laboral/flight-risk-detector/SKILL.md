---
name: flight-risk-detector
description: Predice riesgo de fuga de empleados usando señales de RRHH (antigüedad, crecimiento salarial, timeline promoción, condiciones mercado, encuestas engagement) con scoring ML explainable (SHAP values), contexto ley laboral española y análisis coste-beneficio de retención.
---

# Flight Risk Detector

## ⚠️ ADVERTENCIA CRÍTICA: RIESGOS RGPD Y DISCRIMINACIÓN

Este módulo presenta **riesgos muy elevados** de violación RGPD (Art. 35 DPIA obligatoria) y discriminación legal bajo Ley 15/2022. La automatización de decisiones de empleo basada en "flight risk scoring" puede constituir:

1. **Decisión automatizada sin human review** (Art. 22 RGPD): Nulidad automática
2. **Profiling discriminatorio** (Art. 6.3 Ley 15/2022): Sesgo potencial contra edad, género, origen
3. **Efecto chilling**: Empleados modifican comportamiento si perciben vigilancia; impacta engagement genuino
4. **Disparate impact**: Si modelo usa proxies discriminatorios (edad → antigüedad; género → familia status)

**Medidas obligatorias** (Sección "DPIA Obligatoria" abajo) DEBEN implementarse ANTES usar scoring en decisiones empleo.

---

## Rol del Modelo (CON SALVAGUARDAS OBLIGATORIAS)

Actúas como **Especialista en Retención de Talento** con expertise en People Analytics y normativa laboral española + RGPD + Ley 15/2022. Tu objetivo es:
- Identificar señales potenciales de marcha (informativo ÚNICAMENTE)
- Informar decisiones retención SI Y SÓLO SI cumples DPIA + human review obligatorio
- NUNCA usar para decisiones autómaticas; NUNCA para discriminación

**NO hacer**: Usar scoring para terminar contrato, denegar ascenso, o tomar acción adversa SIN human review explícita + consentimiento empleado.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Datos RRHH      │───▶│ Feature          │───▶│ Modelo ML       │
│ (Antigüedad,    │    │ Engineering      │    │ (Gradient       │
│  Salario, etc)  │    │ + Normalizacion  │    │  Boosting)      │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Plan de         │◀───│ Análisis         │◀───│ Score Riesgo +  │
│ Retención       │    │ Coste-Beneficio  │    │ SHAP Values     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar (Con Salvaguardas)

- **INFORMAR** decisiones retención (NOT DECIDE automáticamente)
- Diseñar planes retención PERSONALIZADOS (con diálogo empleado)
- Optimizar presupuesto bonus/ascensos (basado en business need, no riesgo)
- Anticipar rotación en periodos clave (planning, NOT action)
- Análisis equity retención (con transparencia)

**NUNCA usar para**:
- Terminar contrato basado en score alto
- Denegar promoción / ascenso
- Reducir bonus sin diálogo previo
- Cambiar condiciones sin motivo legítimo
- Monitoreo continuo SIN consentimiento (Art. 13-14 RGPD)

---

## Factores de Riesgo (España)

| Factor | Impacto | Normativa |
|--------|--------|-----------|
| **Antigüedad < 2 años** | Alto | Periodo de prueba relevante (ET art. 14) |
| **Crecimiento salarial anual < 2%** | Alto | Pérdida poder adquisitivo |
| **Sin promoción en 3+ años** | Medio | Desmotivación estructural |
| **Bonificaciones reducidas YoY** | Alto | Flexibilidad empresarial (convenio) |
| **Encuesta engagement < 6/10** | Crítico | Señal de descontento inmediato |
| **Mercado laboral en auge** | Crítico | Mayor movilidad de candidatos |
| **Ausencia de plan de carrera claro** | Medio | Inversión en RRHH insuficiente |
| **Conflictos documentados** | Alto | Ambiente tóxico |

---

## DPIA Obligatoria (Evaluación de Impacto - RGPD Art. 35)

**REQUERIMIENTO**: Antes de implementar flight risk scoring en decisiones empleo, DPIA completa es OBLIGATORIA per RGPD Art. 35.

### 1. Descripción Sistemática del Procesamiento (Art. 35.7.a RGPD)

```
PROPÓSITO: Identificar empleados con riesgo potencial de marcha
├─ Objetivo: Informar decisiones retención (NO automatizar decisiones)
├─ Base legal: Art. 6.1.f RGPD (Interés legítimo empresa: retención talento)
├─ Datos procesados:
│  ├─ Antigüedad (formulario HR)
│  ├─ Salario (nómina; dato sensible Art. 9 RGPD)
│  ├─ Bonus histórico (nómina; sensible)
│  ├─ Encuestas engagement (voluntarias; sensibles si biometric/psychology)
│  ├─ Mercado laboral (públicos; terceros)
│  ├─ LinkedIn activity (datos personales de terceros, exteriores)
│  └─ Acceso a sistemas (datos procesamiento)
├─ Categorías sujetos: Empleados activos (staff)
├─ Períodos retención:
│  ├─ Datos nómina/HR: 7 años (laboral prescripción)
│  ├─ Scores flight risk: 12 meses (model retraining)
│  └─ Borrador scores: 3 meses (data subject right to access)
├─ Destinatarios: HR, Management, Compliance (si escalada)
├─ Transferencias: NINGUNA (datos NO transferred fuera empresa salvo regulador)
└─ Tecnología: Machine learning (XGBoost); explicabilidad SHAP values

CUMPLIMIENTO PRINCIPIOS GDPR:
├─ Lawfulness (Art. 5.1.a): ✓ Interés legítimo Art. 6.1.f
├─ Fairness (Art. 5.1.a): ⚠️ RIESGO (sesgo potencial si no audited)
├─ Transparency (Art. 5.1.a): ⚠️ RIESGO (empleados pueden no saber)
├─ Purpose Limitation (Art. 5.1.b): ✓ Sólo retención; no otras usos
├─ Data Minimization (Art. 5.1.c): ⚠️ RIESGO (salario es muy sensible)
├─ Accuracy (Art. 5.1.d): ⚠️ RIESGO (modelos ML no 100% accuracy)
├─ Storage Limitation (Art. 5.1.e): ✓ 12 meses max
└─ Integrity & Confidentiality (Art. 5.1.f, 32): ⚠️ RIESGO (datos sensibles)
```

### 2. Evaluación Necesidad y Proporcionalidad (Art. 35.7.b RGPD)

```
¿Es flight risk scoring NECESARIO para retención?
├─ Alternativas menos invasivas:
│  ├─ Exit interviews (post-marcha): No predice, pero no invasivo
│  ├─ Manager check-ins regulares: Conversación directa; alto trust
│  ├─ Encuestas engagement (opt-in): Voluntario; transparente
│  ├─ 360 reviews: Feedback directo, no scoring opaco
│  └─ Scoring AUTOMÁTICO: Más invasivo; alto riesgo discriminación
├─ Justificación si procede:
│  ├─ "Empresa grande (>1000 empl); manager check-ins no scalable"
│  ├─ "Rotación voluntaria 18%+ (high cost); early warning necesario"
│  └─ "Mercado tech competitivo; anticipation crítico"
└─ Conclusión proporcionalidad: ✓ Puede ser proporcionado SI salvaguardas robustas

¿Es PROPORCIONAL el método propuesto (scores automáticos SIN human review)?
├─ NO PROPORCIONAL: Decisiones adversas basadas exclusivamente en score
│  └─ Violación Art. 22 RGPD (right not to be subject to automated decision)
├─ SÍ PROPORCIONAL: Scores + human review obligatorio + consentimiento
│  └─ Cumple Art. 22.2.c (human review exception)
├─ Recomendación: Implementar como "informativo" SÓLO, no "decisional"
└─ Si "decisional": DPIA debe llegar a "High Residual Risk" → AEPD consultation
```

### 3. Evaluación Riesgos (Art. 35.7.c RGPD - CRITICAL)

```
HIGH RISK CATEGORIES PRESENTE:

1. PROFILING (Art. 4.11 RGPD):
   ├─ Definición: "Any form of automated processing of personal data"
   │  "intended to evaluate personal aspects"
   ├─ Flight risk scoring = PROFILING (evalúa propensión marcha)
   ├─ Impacto: Art. 22 RGPD applies
   │  └─ "Right NOT to be subject to decision based solely on profiling"
   ├─ Riesgo: Si empresa toma acción (reducir bonus, denegar ascenso) basada SOLO en score
   │  └─ = Decisión automatizada sin human review = VIOLACIÓN
   └─ Mitigation: Human review MANDATORY antes cualquier acción

2. EMPLOYMENT DECISIONS (High Risk per WP29/EDPB):
   ├─ Definición: Scoring afecta empleo, promoción, compensación
   ├─ Impacto LGBTIQ/Género/Edad: Si modelo incluye proxies
   │  └─ Ej: "bonus reduction history" puede proxy gender (if women have lower bonus)
   │  └─ Ej: "No promotion in 3 years" puede proxy age (older workers stuck in roles)
   ├─ Disparate Impact: Even if non-intentional, puede discriminar
   └─ Riesgo: AEPD & Spanish labor courts WILL investigate si complaint

3. SALARY DATA (Art. 9 RGPD - "Special Category"):
   ├─ Salario = Datos especiales bajo Art. 9 RGPD (financial situation)
   ├─ Processing basado en salario ALWAYS requires extra safeguards
   ├─ Mitigación: Salario usado ÚNICAMENTE como control variable
   │  └─ NOT como decision factor (no decir "bajo salario = alto risk")
   └─ Problema actual: Si modelo says "Bajo aumento salarial = riesgo alto"
      └─ = Usa salario como predictor → Art. 9 violation potencial

4. BEHAVIORAL MONITORING (Chilling Effect):
   ├─ Si empleados saben "scored por riesgo fuga"
   ├─ Comportamiento cambia: Menos actividad LinkedIn, falsifica engagement
   ├─ Resultado: Datos menos valid → Modelo less accurate
   ├─ Riesgo a derechos fundamentales: Libertad asociación, expresión
   └─ AEPD position: "Transparency es MUST; ocultación es violación"

5. DISCRIMINATION RISK (Ley 15/2022):
   ├─ Si modelo correlaciona: Edad → Antigüedad → Riesgo bajo (discriminatorio)
   ├─ Si modelo correlaciona: Género → Bonus history → Riesgo bajo (si mujeres menos bonus)
   ├─ Si modelo correlaciona: Origen → Mercado laboral → Riesgo under-prediction
   ├─ Riesgo: Sistema que parece "neutral" pero tiene disparate impact
   └─ STS jurisprudencia: "Neutral criteria que produce adverse impact = discriminación indirecta"

RIESGO SCORE GLOBAL: HIGH (75–95 / 100)
├─ Sin mitigaciones: 95/100 (very high risk)
├─ Con DPIA + human review: 45–55/100 (moderate)
└─ Con DPIA + human review + transparency + opt-in: 20–30/100 (low)
```

### 4. Medidas de Mitigación Riesgos (Art. 35.7.d RGPD)

```
MEDIDA 1: HUMAN REVIEW OBLIGATORIA (Art. 22.3 RGPD)
├─ Antes CUALQUIER acción sobre empleado: Revisión manual obligatoria
├─ Contenido review:
│  ├─ Verificar score accuracy (¿datos correctos?)
│  ├─ Investigar drivers (¿por qué score alto?)
│  ├─ Considerar contexto cualitativo (¿factores externos?)
│  └─ Documentar decisión + justificación
├─ Tiempo review: MISMO DÍA O SIGUIENTE (no demorarse)
├─ Aprobadores: HR + Manager + (si escala) C-level
└─ Documentación: Registro de revisión (audit trail)

MEDIDA 2: CONFIDENCIALIDAD EXTREMA
├─ Acceso a scores: SOLO HR + Manager (need-to-know)
├─ NO compartir: CEO, Board, Finance (no business need)
├─ Encryption en reposo + en tránsito (AES-256)
├─ Access logs auditados (quién accesó, cuándo, qué vio)
└─ Retención: 12 meses MAX; después destrucción segura

MEDIDA 3: BIAS AUDITING QUARTERLY
├─ Verificar si modelo discrimina por: Edad, género, origen, discapacidad
├─ Test: Adverse impact ratio (4/5 rule) para cada grupo protegido
├─ Si disparate impact detectado: STOP usando modelo; reentrenar
├─ Auditor: Externo recomendado (no internal sesgo)
└─ Report: Circulado a Board + Data Protection Officer

MEDIDA 4: TRANSPARENCY & EMPLOYEE RIGHTS
├─ Notificación a empleados (Art. 13-14 RGPD):
│  ├─ "Empresa usa ML model para retención purposes"
│  ├─ "Datos: antigüedad, salario, engagement scores"
│  ├─ "No affectará decisiones adversas SIN human review"
│  ├─ "Derecho acceso (Art. 15): puedes ver tu score"
│  ├─ "Derecho rectificación (Art. 16): si datos incorrectos"
│  ├─ "Derecho oposición (Art. 21): puedes optar-out (con caveats)"
│  └─ "Contacto DPO: [email]"
├─ Frequency: Anual (privacy notice update)
└─ Format: Accessible language; NO legalese

MEDIDA 5: FAIRNESS IN DESIGN
├─ Model training data: AUDITAR por sesgo histórico
│  └─ Ej: Si historical data muestra "mujeres tienen higher turnover"
│     └─ ¿Es porque están discriminadas O porque dejan por childcare?
│     └─ Si discriminadas: Training data contains bias → Model inherits
├─ Features excluded: Género, edad, origen, discapacidad (DIRECTO)
├─ Proxies monitored: Antigüedad (proxy edad), bonus (proxy género)
├─ Rebalance if needed: Weighted classes si minority groups under-represented
└─ Post-training: Fairness metrics (equal opportunity, demographic parity)

MEDIDA 6: THRESHOLD CONSERVADOR (No Partial Automation)
├─ Minimum confidence threshold: 0.85 (85%)
├─ Si score < 0.85: NO action (assume low risk si uncertain)
├─ Rationale: Better false negative (miss some flight risk) than false positive
│  └─ False positive = potential discriminatory action
├─ Output: BINARIO si > 0.85 threshold
│  ├─ Green: Proceed with retention discussion (IF warrant)
│  ├─ Red: Flag for manager review (NOT automatic intervention)
│  └─ Grey/Uncertain: NO ACTION; defer to qualitative assessment
└─ Documentation: "Threshold 0.85 set to minimize discriminatory risk"

MEDIDA 7: AEPD CONSULTATION (IF High Residual Risk remains)
├─ Trigger: Si después medidas 1-6, residual risk > 50
├─ Acción: Contactar AEPD (Autoridad Protección Datos) ANTES implementar
├─ Propósito: Consulta específica "Does flight risk scoring violate Art. 35?"
├─ Plazo: 30 días típico (AEPD puede decir "sí/no/condicional")
├─ Resultado: AEPD guidance vinculante (empresa debe cumplir)
└─ Cost: ~€2K–€5K asesoramiento; pero evita litigio multimillonario
```

### 5. Residual Risk Assessment Después Mitigaciones

```
ESCENARIO A: Sin medidas mitigación
├─ Riesgo residual: 95/100 (CRITICAL)
├─ Recomendación: PROHIBIDO usar en decisiones empleo
└─ Acción: Redesign system o abandonar

ESCENARIO B: Con medidas 1-6 (human review + bias audit + transparency)
├─ Riesgo residual: 35/100 (MODERATE → ACEPTABLE if documented)
├─ Recomendación: Proceder CON mitigation robustas
├─ AEPD consultation: Recomendado pero no obligatorio
└─ Acción: Implementar + audit quarterly

ESCENARIO C: Con medidas 1-6 + AEPD consultation
├─ Riesgo residual: 15–20/100 (LOW)
├─ Recomendación: SAFE to proceed (con AEPD blessing)
├─ Compliance status: GDPR Art. 35 satisfied
└─ Acción: Full implementation; monitor compliance

EMPRESA RESPONSABILIDAD:
├─ Si implementa SIN DPIA: Art. 35 violation → €10M multa OR 2% revenue
├─ Si implementa SIN human review: Art. 22 violation → €20M multa OR 4% revenue
├─ Si data breach (salarios leaked): Art. 33 violation + potential £500K+ reputational
└─ Best practice: DPIA + human review + audit = Defensible position
```

---

## Inputs

```json
{
  "empleado": {
    "id_anonimizado": "EMP_12345",
    "antiguedad_años": 4.2,
    "salario_bruto_anual": 52000,
    "categoria": "Senior Developer",
    "departamento": "Tecnología",
    "fecha_ultimo_aumento": "2024-03-15",
    "porcentaje_ultimo_aumento": 3.5,
    "crecimiento_3_años": 9.2,
    "fecha_ultima_promocion": "2022-01-10",
    "bonus_medio_3_años": 8500,
    "bonus_año_actual": 6200,
    "formacion_anual_invertida": 2500
  },
  "encuestas_engagement": {
    "satisfaccion_laboral": 6.5,
    "relacion_jefe": 7.2,
    "oportunidades_crecimiento": 4.8,
    "balance_vida_trabajo": 5.1,
    "cultura_empresa": 7.0,
    "fecha_ultima_encuesta": "2024-12-15"
  },
  "mercado": {
    "tasa_desempleo_sector": 3.2,
    "salario_medio_mercado_categoria": 58000,
    "demanda_perfiles_similares": "muy_alta",
    "ofertas_activas_mercado": 245
  }
}
```

---

## Output

```json
{
  "empleado": {
    "id": "EMP_12345",
    "nombre_anonimizado": "[ANONIMIZADO]",
    "antiguedad_años": 4.2
  },
  "riesgo_fuga": {
    "score_riesgo": 0.72,
    "clasificacion": "RIESGO_ALTO",
    "intervalo_confianza_95": [0.68, 0.76],
    "probabilidad_marcha_12_meses": 0.58,
    "percentil_comparativo": 78,
    "recomendacion_urgencia": "ACCIÓN_INMEDIATA"
  },
  "drivers_principales": [
    {
      "factor": "Oportunidades crecimiento bajo (4.8/10)",
      "shap_value": 0.18,
      "impacto_relativo": 25.0,
      "evidencia": "Última promoción hace 2 años; sin plan claro"
    },
    {
      "factor": "Balance vida-trabajo insuficiente (5.1/10)",
      "shap_value": 0.16,
      "impacto_relativo": 22.2,
      "evidencia": "Burnout detectado en encuesta"
    },
    {
      "factor": "Bono año actual < media histórica (-27%)",
      "shap_value": 0.14,
      "impacto_relativo": 19.4,
      "evidencia": "6.200€ vs. promedio 8.500€"
    },
    {
      "factor": "Mercado muy activo para perfil (demanda alta)",
      "shap_value": 0.12,
      "impacto_relativo": 16.7,
      "evidencia": "245 vacantes abiertas en sector TI"
    },
    {
      "factor": "Diferencia salarial mercado (12% bajo)",
      "shap_value": 0.08,
      "impacto_relativo": 11.1,
      "evidencia": "Gana 52.000€ vs. mercado 58.000€"
    }
  ],
  "analisis_coste_beneficio_retencion": {
    "coste_reemplazo": {
      "salario_3_meses": 13000,
      "agencia_reclutamiento_20_pct": 11600,
      "onboarding_training": 5000,
      "perdida_productividad_3_meses": 8000,
      "coste_total": 37600
    },
    "inversion_retencion_propuesta": {
      "aumento_salarial_3_pct": 1560,
      "bonus_retencion_discreto": 5000,
      "plan_carrera_formalizado": 500,
      "flexible_working_benefits": 0,
      "coste_anual": 7060
    },
    "roi_retencion": {
      "ahorro_si_se_retiene_1_año": 37600,
      "inversion_anual": 7060,
      "roi": 5.32,
      "payback_meses": 2.2,
      "recomendacion": "ALTAMENTE RENTABLE: inversión mínima vs. coste reemplazo"
    }
  },
  "regulacion_laboral_españa": {
    "consideraciones": [
      "Aumento salarial voluntario: sin límite legal (RDL 1949/1995)",
      "Bonus: flexibilidad empresarial según convenio aplicable",
      "Plan carrera: no hay obligación legal pero impacta RGPD (privacidad de datos)",
      "Documentación: mantener registro de conversaciones para evitar despido cuestionable posterior"
    ],
    "riesgos_juridicos": [
      "Si aumento es discriminatorio en base a género/edad: infracción RDL 902/2020",
      "Transparencia salarial: obligación desde 2023 para grandes empresas (ley de igualdad)"
    ]
  },
  "plan_retencion_personalizado": {
    "intervenciones_recomendadas": [
      {
        "accion": "Definir plan de carrera explícito",
        "plazo": "30 días",
        "responsable": "RRHH + Dirección Técnica",
        "presupuesto": 500,
        "impacto_predicho_reduccion_riesgo": 0.15
      },
      {
        "accion": "Revisión salarial alineada mercado (52K→54.5K)",
        "plazo": "15 días",
        "responsable": "RRHH + Finanzas",
        "presupuesto": 1560,
        "impacto_predicho_reduccion_riesgo": 0.18
      },
      {
        "accion": "Bonus retencion 2024 (5.000€)",
        "plazo": "Inmediato",
        "responsable": "CEO/Finanzas",
        "presupuesto": 5000,
        "impacto_predicho_reduccion_riesgo": 0.20
      },
      {
        "accion": "Flexible working: 2 días remotos/semana",
        "plazo": "Inmediato",
        "responsable": "RRHH",
        "presupuesto": 0,
        "impacto_predicho_reduccion_riesgo": 0.12
      },
      {
        "accion": "Programa mentoring con líder senior",
        "plazo": "60 días",
        "responsable": "Dirección Técnica",
        "presupuesto": 0,
        "impacto_predicho_reduccion_riesgo": 0.10
      }
    ],
    "riesgo_post_intervencion": 0.31,
    "probabilidad_marcha_post_intervencion": 0.18
  },
  "privacidad_rgpd_consideraciones": {
    "base_legal": "Interés legítimo empresarial (art. 6.1.f RGPD)",
    "datos_procesados": [
      "Datos de RR.HH. (antigüedad, salario - sensible art. 9)"
    ],
    "medidas_proteccion": [
      "Anonimización completa en reportes agregados",
      "Acceso restringido a RRHH y dirección",
      "Retención máxima 12 meses post-análisis",
      "Consentimiento implícito via política privacidad (si aplica)"
    ],
    "derechos_empleado": "Derecho a acceso (art. 15) y rectificación (art. 16) si datos inexactos"
  },
  "puntos_vigilancia": {
    "señales_amarillas": [
      "Actualización reciente de perfil LinkedIn (28 dic 2024)",
      "Reducción de participación en reuniones team (auditoría de calendarios)",
      "Aumento solicitudes de flexibilidad (patrón típico 3-6 meses antes marcha)"
    ],
    "proximos_checks": "Revisión en 30 días; seguimiento trimestral"
  }
}
```

---

## Explicabilidad con SHAP

El score final es resultado de importancia de features:

```python
import shap
import xgboost as xgb

# Modelo entrenado con datos históricos
model = xgb.XGBClassifier(...)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Output: cada decisión es interpretable
# Ejemplo: "Falta de crecimiento = +18% riesgo"
```

---

## Auditorías Periódicas de Sesgo (Quarterly Schedule)

**OBLIGATORIA si flight risk scoring se usa en decisiones empleo.**

```
CALENDARIO AUDITORÍA (Trimestral):

Q1 2025 (Enero-Marzo):
├─ Verificación datos accuracy (muestra 50 registros vs. source system)
├─ Bias audit: Adverse impact ratio (4/5 rule) por edad, género, origen
├─ Modelo performance: Precision, recall, F1-score
├─ Human review compliance: ¿100% decisiones tuvieron review?
└─ Documentación hallazgos + correcciones (si necesario)

Q2 2025 (Abril-Junio):
├─ Disparate impact analysis: ¿Modelo predice diferente por grupos?
├─ Fairness metrics: Equal opportunity, demographic parity, predictive parity
├─ Model retraining: Nueva data (Q1–Q2); recalibrar si sesgo detected
├─ Protected category monitoring: Focus en edad (>45), origen, discapacidad
└─ Report Board + DPO

Q3 2025 (Julio-Septiembre):
├─ Validation on new employees (post-Q1 hiring)
├─ Intersectional analysis: Edad + género combinations (double discrimination risk)
├─ Feature importance audit: ¿Qué variables más influencian? ¿Alguna proxy sospechosa?
├─ Rebalance if: Disparate impact encontrado → Retrain con fairness constraints
└─ Escalation if: High discrimination risk detected → Stop use pending review

Q4 2025 (Octubre-Diciembre):
├─ Annual comprehensive audit: Summary de Q1–Q3 findings
├─ Model refresh: Full retraining con mejor data/fairness
├─ Policy updates: Si risk mitigation approach necesita cambios
├─ AEPD report: Si required (es buena práctica compartir)
└─ Compliance certification: "Flight risk model meets GDPR + Ley 15/2022"

TRIGGERS FOR IMMEDIATE ACTION (No wait until quarterly):
├─ Si adverse impact ratio < 0.70 en cualquier categoría → URGENT audit
├─ Si employee complaint sobre "scoring discriminatorio" → STOP uso; formal investigation
├─ Si data breach involving salaries/scores → Art. 33 notification AEPD
├─ Si audit detects proxy discrimination → Immediate model retraining
└─ Si human review compliance < 95% → Process failure; correct before next decision

DOCUMENTACIÓN AUDITORÍA:
├─ Audit report (2–5 páginas; executivve summary)
│  ├─ Methodology (qué tests, qué data)
│  ├─ Findings (resultados numéricos)
│  ├─ Risk assessment (acceptable / borderline / unacceptable)
│  ├─ Recommended actions (if any)
│  └─ Next audit date
├─ Detailed logs (statistician workpaper)
│  ├─ Adverse impact ratios por stratum
│  ├─ Chi-squared / Fisher exact p-values
│  ├─ Disparate impact analysis (logistic regression)
│  └─ Data quality checks
├─ Stored: Segregated folder (attorney work product; privilegio legal)
└─ Shared with: Board, DPO, External auditor; NOT employees (unless complaint)

THRESHOLD FAILURE (When to STOP using model):
├─ Si adverse impact ratio < 0.60 ANY protected category
├─ Si p-value < 0.05 sugiere systematic discrimination
├─ Si human review compliance < 80%
├─ Si employee complaint substantiated
└─ Action: Pause scoring; conduct root cause analysis; retrain or abandon
```

## Benchmarking Sector

Tasas típicas de rotación voluntaria:
- **Tecnología**: 13-18% anual
- **Finanzas**: 9-12% anual
- **Servicios profesionales**: 15-20% anual

---

## Ethical Disclaimer (MANDATORY)

**Este módulo conlleva riesgos significativos bajo RGPD, Ley 15/2022 y jurisprudencia STS.**

El "flight risk scoring" basado en machine learning es una herramienta **informativa** ÚNICAMENTE. Su uso en decisiones adversas (terminar, reducir bonus, denegar ascenso) sin cumplimiento riguroso de:
- DPIA (Art. 35 RGPD)
- Human review (Art. 22 RGPD)
- Transparency (Art. 13-14 RGPD)
- Bias auditing (Ley 15/2022)
- Employee consent (Art. 7 RGPD)

...es **ILEGAL y expone a la empresa a**:
- Multas AEPD: €10M–€20M
- Litigio laboral: Indemnizaciones por discriminación (€50K–€500K+ por empleado)
- Reputacional: "Surveillance capitalist employer" perception
- Criminal: Si datos filtrados, posible Art. 248 CP (fraud/data breach)

**RECOMENDACIÓN**: Si empresa no puede implementar mitigaciones robustas (DPIA, human review 100%, bias audit quarterly, transparency), **ABANDONAR flight risk scoring** a favor de métodos menos invasivos:
- Encuestas engagement voluntarias (opt-in)
- Manager check-ins regulares
- Exit interviews (post-marcha, no predictivo pero menos invasivo)
- Salary benchmarking transparente

Mejor perder predicción temprana que enfrentar litigio multimillonario por discriminación legal.
