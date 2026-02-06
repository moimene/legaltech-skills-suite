---
name: gdpr-consent-tracker
description: Audit consent validity across web forms, mobile apps, and databases against GDPR Art. 7 and EDPB Guidelines 05/2020. Evaluate consent requirements, identify legitimate interest alternatives (LIA), analyze cookie compliance, verify children's consent (14+ in Spain), and generate remediation roadmap.
---

# GDPR Consent Tracker

Validate that personal data processing relies on lawful legal bases by analyzing consent mechanisms, identifying gaps against GDPR Art. 7 and EDPB guidance, assessing legitimate interest balancing tests, and ensuring compliance with LOPDGDD requirements for minors (Spain: 14 years).

## Trigger Contexts

- Periodic GDPR audit following data breach or complaint
- Pre-inspection preparation for AEPD (Spanish Data Protection Authority)
- Due diligence on acquisition: consent mechanism audit across all touchpoints
- Legacy system migration: validate historical consent records
- Cookie banner implementation review (ePrivacy Directive + LSSI compliance)
- Age-gated services: verify children's consent thresholds per jurisdiction

---

## Consent Validity Framework

### GDPR Art. 7: Six Core Requirements

| Requirement | Legal Basis | Verification |
|-------------|------------|--------------|
| **Free** | Art. 7.4 | NOT conditional on unrelated service provision; no coercion |
| **Specific** | Art. 7.2 | Distinct consent per processing purpose (not blanket) |
| **Informed** | Art. 6(1)(a) + Art. 13-14 | Pre-consent disclosure: identity, purpose, recipients, retention |
| **Unambiguous** | Art. 7.4 | Affirmative action required (no pre-ticked, silence insufficient) |
| **Recordable** | Art. 7.1 | Timestamp + proof of obtaining consent (form data logged) |
| **Revocable** | Art. 7.3 | Withdrawal mechanism as easy as granting consent |

### EDPB Guidelines 05/2020: Consent Standards

**Three Critical Principles:**

1. **Informed Consent (EDPB point 2.2)**
   - Information provided BEFORE obtaining consent (not buried in privacy policy)
   - Granular purposes explained in plain language
   - No "dark patterns" (excessive scrolling, confusing language)

2. **Freely Given (EDPB point 3.3)**
   - No essential functionality locked behind consent (except performance/security cookies)
   - No pre-ticked boxes or inactivity-as-consent
   - Refusal must not disadvantage user (no different pricing/quality)

3. **Specific (EDPB point 2.5)**
   - One consent request per processing purpose minimum
   - Cannot bundle unrelated processing ("marketing + analytics + third-party sharing" = 3 checkboxes minimum)

---

## Legitimate Interest Alternative (LIA)

**When Consent Insufficient:** Use Legitimate Interest Assessment (Art. 6(1)(f))

| Processing Type | Legal Base | LIA Required | Example |
|-----------------|-----------|--------------|---------|
| Marketing emails | **Consent** (Art. 6.1.a) | No; consent is easier | Email marketing, re-targeting |
| Fraud detection | **Legitimate Interest** | YES | Real-time transaction monitoring |
| Analytics (aggregated) | **Legitimate Interest** | YES (often) | Website improvement, anonymized stats |
| Direct marketing (B2B) | **Legitimate Interest** | Maybe | Business prospect outreach |
| Purpose limitation change | **Consent OR LIA** | Test LIA first | Repurpose historical data |

### Three-Step LIA Test (Art. 6(1)(f))

1. **Purpose Test:** Is legitimate interest compelling? (examples: fraud prevention, business operations, legal compliance)
2. **Necessity Test:** Is data collection proportionate to purpose? (minimize sensitive data)
3. **Balancing Test:** Do data subject rights outweigh legitimate interest?

**Example LIA Analysis:**
```json
{
  "processing": "Real-time fraud detection on credit card transactions",
  "proposed_legal_base": "Legitimate Interest (Art. 6.1.f)",
  "step_1_purpose": {
    "interest": "Prevent financial fraud and protect cardholder assets",
    "compelling": true,
    "evidence": "Industry standard; regulatory expectation (PSD2)"
  },
  "step_2_necessity": {
    "data_minimized": true,
    "only_essential": ["transaction_amount", "merchant_category", "cardholder_location"],
    "excluded": ["purchase_history", "salary_data", "credit_score"]
  },
  "step_3_balancing": {
    "data_subject_rights": "HIGH (financial privacy is sensitive)",
    "legitimate_interest": "HIGH (fraud causes direct harm)",
    "conclusion": "Legitimate interest OUTWEIGHS (fraud prevention is necessary); LIA PASSES"
  },
  "mitigation": [
    "Provide privacy notice explaining fraud monitoring",
    "Implement data minimization (only transaction flags, no history)",
    "Retention: 90 days max (fraud chargeback period)",
    "Allow opt-out for users (lower fraud protection tier)"
  ]
}
```

---

## Children's Consent Requirements (14+ in Spain)

### GDPR Art. 8 + LOPDGDD Art. 7

| Jurisdiction | Parental Consent Threshold | Parental Notification Required |
|---------------|---------------------------|------------------------------|
| EU (Default) | 16 years old | YES (Art. 8.1) |
| Spain (LOPDGDD) | 14 years old | NO consent, but notification |
| Germany (TMG) | 16 years old | YES |
| France (CNIL) | 15 years old | YES |

### Spanish Requirement (LOPDGDD Art. 7): Age 14+

**Key Difference:** Spain allows minors 14+ to give own consent **without** parental authorization, but:
- Parent/guardian notification must occur BEFORE processing
- Child must verify age through (parents' email confirmation recommended)
- Service must warn parents of potential risks (social media, tracking)

### Implementation Checklist

```
If target audience includes users <14:
☐ Age verification gate before consent (email verification required)
☐ If <14: Obtain parental consent in writing (email sufficient in Spain)
☐ If 14-15 (Spain): Notification to parent/guardian; child's direct consent valid
☐ If 16+: Direct child consent valid (Art. 8 GDPR)
☐ Consent form must highlight: data sharing, profiling, behavioral targeting
☐ Offer simple parental controls (data access, deletion requests)
```

---

## Evidencias de Consentimiento por Finalidad

### Requisitos de Granularidad (EDPB Guidelines 05/2020)

Cada finalidad de procesamiento requiere consentimiento independiente y verificable:

| Finalidad | Base Legal | Granularidad | Evidencia Requerida |
|----|----|----|----|
| **Marketing directo** | Consentimiento (Art. 6.1.a) | Checkbox único | Timestamp + versión texto consentimiento + estado checkbox |
| **Análisis/Analytics** | Consent OR Legitimate Interest | Checkbox único | IP, device fingerprint, consentimiento timestamp |
| **Profiling comportamental** | Consentimiento (Art. 6.1.a) | Checkbox único + explicación | Consentimiento explícito para decisiones automatizadas (Art. 22) |
| **Compartir con terceros** | Consentimiento (Art. 6.1.a) | Checkbox por destinatario | Nombre del tercero, propósito, política privacidad enlazada |
| **Transferencias internacionales** | Consentimiento (Art. 6.1.a) | Checkbox único con avisos | País destino, mecanismo (SCCs/BCRs), nivel protección |

### Formato de Evidencia de Consentimiento

**Datos que DEBEN registrarse para cada consentimiento:**

```json
{
  "consentimiento": {
    "id_unico": "consent_abc123xyz",
    "usuario_id": "user_456",
    "fecha_hora_otorgado": "2024-02-06T14:32:15Z",
    "timestamp_unix": 1707223935,
    "ip_address_anonimizada": "192.168.1.XXX",
    "dispositivo": {
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
      "tipo_dispositivo": "desktop",
      "navegador": "Chrome 122.0"
    },
    "finalidad": {
      "id": "MARKETING",
      "descripcion": "Envío de emails promocionales y ofertas personalizadas",
      "retension_meses": 24
    },
    "version_politica": {
      "numero_version": "3.2",
      "hash_documento": "sha256:a1b2c3d4e5f6",
      "enlace_politica": "https://ejemplo.com/privacy-v3.2.pdf"
    },
    "checkboxes_estado": {
      "marketing_email": true,
      "marketing_sms": false,
      "profilado": true,
      "compartir_terceros": false
    },
    "mecanismo_otorgamiento": {
      "tipo": "explicit_click",
      "elemento_html": "button#consent-marketing-submit",
      "interaccion_usuario": "click"
    },
    "revocacion": {
      "revocado": false,
      "fecha_revocacion": null,
      "mecanismo_revocacion": "enlace_email_pie_pagina"
    },
    "cumplimiento_edpb": {
      "informado": true,
      "libremente_otorgado": true,
      "especifico": true,
      "inequivoco": true,
      "registrable": true,
      "revocable": true
    }
  }
}
```

### Integración CMP (Consent Management Platform)

**Plataformas recomendadas para España/UE:**

- **Cookiebot** - Auditoría automática de cookies + consentimiento granular
- **OneTrust** - Enterprise-grade CMP con validaciones EDPB
- **TrustArc** - Gestión integral consentimiento + LIA assessment
- **iubenda** - Enfocada en GDPR-CCPA; cumple LSSI España

**Requerimientos de integración:**

```markdown
☐ CMP almacena cada consentimiento con timestamp exacto
☐ Versión de política privacidad hashada y almacenada
☐ Estado individual de cada checkbox (no consolidado)
☐ IP anonimizada (último octeto/3 últimos dígitos bloqueados)
☐ Mecanismo de revocación integrado en CMP
☐ Exportación de registros para auditoría AEPD
☐ Webhook para sincronización con backend de bases de datos
☐ Testing de accesibilidad (WCAG 2.1 AA)
```

---

## Gestor de Revocaciones en 1 Clic

### Requisito Art. 7(3) RGPD

**Obligación:** "La revocación del consentimiento debe ser tan fácil como su otorgamiento"

Esto significa:
- Si el usuario tarda 3 clics para consentir → máximo 3 clics para revocar
- Si es un botón para consentir → debe ser UN botón para revocar
- NO puede requerir login, contraseña, o múltiples pasos de verificación

### Implementación de Revocación en 1 Clic

**Arquitectura técnica:**

```
Email del usuario → [Enlace de revocación único] → Revocación procesada → Confirmación
↓
GET /revoke?token=xyz789 (token con firma HMAC, válido 30 días)
↓
Backend verifica token → Identifica usuario → Revoca consentimiento(s)
↓
Actualiza registro: revoked=true, timestamp, método revocación
↓
Envía confirmación email
```

**Checklist de implementación:**

```markdown
☐ **Mecanismo de revocación accesible**
  - Enlace en pie de página de TODOS los emails
  - Centrado, legible, contraste de color (WCAG AA)
  - Texto: "Cancelar suscripción / Revocar consentimiento"
  - URL: ejemplo.com/revoke?token=[JWT]

☐ **Token de revocación**
  - Firmado HMAC-SHA256 (no reversible, no predecible)
  - Incluye: user_id, timestamp, propósito (marketing/analytics/etc)
  - Válido durante 30 días (balanza: usabilidad vs. seguridad)
  - No requiere login previo del usuario

☐ **Procesamiento de revocación**
  - Verifica token HMAC
  - Identifica finalidad(es) afectadas por revocación
  - Marca consentimiento como revocado: revoked_datetime = NOW()
  - Registra método: "email_link" / "website_form" / "api_call"

☐ **Efectos en cascada inmediatos**
  - MARKETING → Parar envío de emails dentro de 24h
  - ANALYTICS → Parar recopilación de datos nuevos
  - PROFILING → Parar procesamiento de datos existentes (mantener para auditoría)
  - COMPARTIR_TERCEROS → Parar compartición a Google/Meta inmediatamente

☐ **Confirmación y auditoría**
  - Enviar email confirmando revocación (proof of receipt)
  - Registrar en log inmutable: usuario, finalidad, fecha, IP (anonimizada)
  - Mantener registro durante mín. 3 años (para defensa en auditoría)

☐ **Testing de conformidad**
  - Revocación funciona desde dispositivo diferente (sin login)
  - Procesa dentro de 1h (no 24h o más)
  - Email de confirmación enviado en tiempo real
  - Marketing emails paran dentro de 24h de revocación
```

### Patrones Oscuros (Dark Patterns) - Prohibido (EDPB 3/2022)

**NO PERMITIDO:**

```markdown
❌ "Rechazar Todo" oculto tras 3+ clics; "Aceptar Todo" visible inmediatamente
❌ Desconexión automática si usuario rechaza (toma el rechazo como consentimiento)
❌ Consentimiento por inactividad ("Si no actúa en 10s, aceptamos por Ud.")
❌ Countdown timer ("Rechazará en 5...4...3..." presión temporal)
❌ Remordimiento táctica ("Seguro que no quiere recibir ofertas especiales?")
❌ Interfaz de negativa menos visible que interfaz de aceptación
❌ Requerir datos personales para revocar (ej: "ingrese email para cancelar suscripción")
❌ Requerir explicación de por qué revocar ("¿Por qué quiere cancelar?" → obligatorio llenar)
❌ Límite de revocaciones ("Solo puede cancelar 1 vez al año")
```

**OBLIGATORIO:**

```markdown
✅ "Aceptar Todo" y "Rechazar Todo" botones de igual tamaño y contraste
✅ Ubicación simétrica (mismo nivel visual)
✅ Igual número de clics para aceptar y rechazar
✅ Revocación sin login; sin verificación adicional
✅ Confirmación inmediata (dentro de 1h) de revocación
✅ Interfaz clara sin presión temporal
```

### Revocación por Propósito (Cascada)

**Ejemplo: Usuario revoca "Marketing":**

```json
{
  "revocation_event": {
    "user_id": "user_456",
    "finalidad_revocada": "MARKETING",
    "timestamp_revocacion": "2024-02-06T15:45:22Z",
    "metodo": "email_link",
    "efectos_inmediatos": {
      "email_marketing": {
        "estado_anterior": "ACTIVE",
        "estado_nuevo": "REVOKED",
        "accion": "Parar envío de emails promocionales",
        "plazo_cumplimiento": "24 horas"
      },
      "push_notifications": {
        "estado_anterior": "ACTIVE",
        "estado_nuevo": "REVOKED",
        "accion": "Parar notificaciones de ofertas"
      },
      "sms_marketing": {
        "estado_anterior": "INACTIVE (nunca fue consentido)",
        "estado_nuevo": "REVOKED (preemptivo)"
      }
    },
    "efectos_NO_cascada": {
      "order_processing": "NO AFECTADO (base legal: contrato)",
      "fraud_detection": "NO AFECTADO (base legal: interés legítimo)",
      "analytics": "NO AFECTADO (consentimiento separado)"
    },
    "datos_historicos": {
      "accion": "Mantener para auditoría 3 años",
      "procesamiento_nuevo": "Parado inmediatamente"
    },
    "confirmacion_usuario": {
      "email_enviado": true,
      "contenido": "Tu revocación de marketing ha sido procesada. Dejaremos de enviarte emails promocionales en 24 horas.",
      "link_reactivar": "https://ejemplo.com/reconsent?token=xyz" // válido 30 días
    }
  }
}
```

### Auditoría de Revocaciones (AEPD)

**Datos que AEPD espera encontrar en auditoría:**

```markdown
AEPD Interrogatorio:
"Demostrar que User_ABC revocó consentimiento para marketing el 2024-01-15"

Respuesta requerida:
☐ Log inmutable con timestamp exacto de revocación
☐ Método de revocación (email link / website form / phone call con grabación / API)
☐ Token/evidencia de autenticación del usuario
☐ Confirmación enviada al usuario
☐ Evidencia de que marketing paró (log de últimos emails: previos a 2024-01-15)
☐ Registro de datos históricos mantenidos (con justificación de retención)
```

---

## Cookie Compliance (ePrivacy Directive 2002/58/EC + LSSI Spain)

### Cookie Categories Under EDPB Guidelines

| Cookie Type | Legal Base | User Action Required | Lifetime |
|------------|-----------|----------------------|----------|
| **Strictly Necessary** | Legitimate Interest (Art. 6.1.f) | NO consent; May pre-load | Session |
| **Performance** | Consent (Art. 6.1.a) or LIA | YES (pre-ticked banned) | 12 months |
| **Functional** | Consent (Art. 6.1.a) | YES | 12 months |
| **Marketing** | Consent (Art. 6.1.a) | YES (explicit opt-in) | 24 months |
| **Third-party** (e.g., Google Ads) | Consent (Art. 6.1.a) | YES (explicit opt-in) | 24 months |

### LSSI Spain Specific Rules

- **ePrivacy Registry (Registro de Cookies):** Register domain cookies with AEPD registry (transparency requirement)
- **Prior Informed Consent:** Unlike GDPR, LSSI mandates consent **before** cookie placement (not retrospective)
- **Exemption:** Only authentication cookies + load balancing exempt

---

## Concrete Example: E-Commerce Platform Consent Audit

**Platform:** ShopEurope (German e-commerce SaaS serving EU)
**Market:** All EU + UK
**Data Subjects:** 2.5M active users (estimated 15% under 18)

### Scenario Analysis: 5 Consent Purposes

#### Purpose 1: Core Service Delivery (Order Processing)
```json
{
  "id": "P1-ORDER",
  "purpose": "Process customer order, payment, shipping",
  "legal_base": "CONTRACT (Art. 6.1.b) - NOT Consent",
  "data_categories": ["Name", "Address", "Payment method", "Order history"],
  "consent_required": false,
  "reason": "Service cannot be delivered without data",
  "verification": "No checkbox needed; implied by purchase action",
  "status": "COMPLIANT"
}
```

#### Purpose 2: Marketing Emails (Newsletter)
```json
{
  "id": "P2-MARKETING",
  "purpose": "Send promotional emails about new products, sales, recommendations",
  "legal_base": "CONSENT (Art. 6.1.a) - Pre-consent required",
  "data_categories": ["Email address", "Purchase history (for segmentation)", "Browsing behavior"],
  "consent_required": true,
  "edpb_05_2020_check": {
    "informed": "PASS - Privacy notice provided BEFORE checkout; clear description of marketing emails",
    "freely_given": "FAIL - Checkbox pre-ticked by default; must be unchecked by default",
    "specific": "PASS - Separate checkbox from analytics and third-party sharing",
    "unambiguous": "PASS - Clear affirmative language required ('Receive marketing emails')"
  },
  "findings": [
    {
      "issue": "GDPR-M1",
      "severity": "CRITICA",
      "problem": "Marketing checkbox pre-ticked",
      "requirement": "Art. 7.4 + EDPB 05/2020 point 3.3",
      "remediation": "Uncheck by default; require active opt-in"
    }
  ],
  "retention": "Until opt-out; max 2 years without engagement",
  "opt_out_mechanism": "PASS - One-click unsubscribe in footer of all emails (Art. 7.3 compliant)"
}
```

#### Purpose 3: Analytics (Behavioral Tracking)
```json
{
  "id": "P3-ANALYTICS",
  "purpose": "Analyze user behavior, page performance, conversion funnels for site improvement",
  "legal_base": "CONSENT (Art. 6.1.a) OR Legitimate Interest (Art. 6.1.f)",
  "analysis": {
    "approach_1_consent": {
      "required": true,
      "tool": "Google Analytics 4 w/ IP anonymization",
      "edpb_status": "COMPLIANT if unchecked by default",
      "effort": "Low; already implemented"
    },
    "approach_2_legitimate_interest": {
      "viable": true,
      "rationale": "Website improvement is legitimate interest (EDPB 05/2020 examples)",
      "mitigation_required": [
        "Publish LIA balance test (transparency)",
        "Anonymize data (remove user ID linking)",
        "Offer opt-out mechanism",
        "Retention: 13 months max (data minimization)"
      ],
      "recommendation": "LIA approach reduces implementation burden; acceptable if data minimized"
    }
  },
  "data_categories": ["Pages visited", "Time on site", "Referrer source", "Device type", "IP address (anonymized)"],
  "status": "PARTIALLY_COMPLIANT - Switch to LIA or uncheck checkbox by default",
  "deadline": "14 days"
}
```

#### Purpose 4: Third-Party Sharing (Advertising Networks)
```json
{
  "id": "P4-THIRD_PARTY",
  "purpose": "Share user data with Google, Meta for behavioral targeting and retargeting ads",
  "legal_base": "CONSENT (Art. 6.1.a) - Explicit opt-in REQUIRED",
  "data_categories": ["Cookie ID", "Purchase history", "Browsing behavior", "Email address (if shared)"],
  "recipients": ["Google Ads", "Meta Pixel", "Criteo"],
  "edpb_requirements": {
    "informed": "FAIL - Current text generic ('Third-party advertising partners')",
    "issue": "User unaware of Google/Meta data usage; no mention of profiling",
    "required_transparency": "Name each third party; explain how they use data; link to their privacy policies"
  },
  "findings": [
    {
      "issue": "GDPR-3P1",
      "severity": "ALTA",
      "problem": "Inadequate third-party transparency",
      "requirement": "Art. 13.1(e) - Recipients must be identified or category specified",
      "current": "Generic text 'advertising partners'",
      "remediation": "List Google, Meta, Criteo by name; explain each partner's use case"
    }
  ],
  "children_risk": "ALTA (if minors <16: requires parental consent per Art. 8; profiling is high-risk)",
  "status": "NON_COMPLIANT",
  "deadline": "7 days (CRITICAL)"
}
```

#### Purpose 5: Profiling & Personalization
```json
{
  "id": "P5-PROFILING",
  "purpose": "Create user profiles (purchase patterns, interests, demographics) for personalized product recommendations",
  "legal_base": "CONSENT (Art. 6.1.a) + Special handling for children (Art. 8 GDPR, Art. 7 LOPDGDD)",
  "data_categories": ["Purchase history", "Browsing history", "Inferred demographics", "Behavioral segments"],
  "risks": {
    "gdpr": "Profiling + decisioning triggering Art. 22 rights (automated decision-making)",
    "children": "Behavioral targeting of minors may violate Art. 5.1(a) (lawfulness for children)"
  },
  "edpb_guidance": "EDPB 05/2020 point 4: Consent for profiling must be EXPLICIT; granular consent required",
  "findings": [
    {
      "issue": "GDPR-PROF1",
      "severity": "ALTA",
      "problem": "Profiling consent not explicitly mentioned",
      "requirement": "EDPB 05/2020 point 4 - explicit consent required",
      "remediation": "Add separate checkbox: 'I consent to personalized product recommendations based on my purchase and browsing history'"
    },
    {
      "issue": "GDPR-PROF2",
      "severity": "CRITICA",
      "problem": "Minors <16 profiled without parental consent",
      "requirement": "Art. 8 GDPR + LOPDGDD Art. 7 (Spain: 14+)",
      "remediation": "Obtain parental consent for users <14 (Spain); <16 (EU default); block profiling until consent obtained"
    }
  ],
  "children_requirement": "If minors <16: explicit parental consent required BEFORE profiling (Art. 8)",
  "status": "NON_COMPLIANT",
  "deadline": "14 days"
}
```

### Audit Results Summary

```json
{
  "auditoria": {
    "fecha": "2024-02-06",
    "plataforma": "ShopEurope",
    "formularios_analizados": 3,
    "cookies_analizadas": 18,
    "propositos_procesamiento": 5,
    "usuarios_evaluados": 2500000
  },
  "compliance_score": {
    "overall": "62/100",
    "por_categoria": {
      "consent_validity": "45/100 (critical issues)",
      "cookie_compliance": "70/100 (minor issues)",
      "children_consent": "30/100 (major gaps)",
      "third_party_transparency": "55/100 (significant gaps)"
    }
  },
  "hallazgos": [
    {
      "id": "CRIT-M1",
      "severidad": "CRITICA",
      "elemento": "Marketing consent checkbox",
      "problema": "Pre-ticked by default",
      "requisito_incumplido": "Art. 7.4 + EDPB Guidelines 05/2020 point 3.3",
      "evidencia": "Form inspection: input type='checkbox' checked='checked' for marketing_consent",
      "impacto_legal": "Invalidates all marketing consent; potential AEPD sanction",
      "remediacion": "1. Change HTML: remove checked='checked' attribute; 2. Deploy within 7 days; 3. Re-collect valid consents",
      "prioridad": 1,
      "deadline": "2024-02-13",
      "responsable": "Frontend Engineering"
    },
    {
      "id": "CRIT-T1",
      "severidad": "CRITICA",
      "elemento": "Third-party data sharing disclosure",
      "problema": "Generic reference to 'advertising partners' without naming Google, Meta, Criteo",
      "requisito_incumplido": "Art. 13.1(e) + Art. 6.1(a) GDPR; EDPB 05/2020 informed requirement",
      "evidencia": "Privacy policy section 3.2: 'We share your data with selected third-party advertising partners'",
      "impacto_legal": "Consent not informed; recipient consent invalid; processing non-compliant",
      "remediacion": "1. Update consent text: 'Google Ads, Meta Pixel, Criteo'; 2. Link to recipient privacy policies; 3. Re-obtain consent",
      "prioridad": 1,
      "deadline": "2024-02-13",
      "responsable": "Legal + Product"
    },
    {
      "id": "CRIT-C1",
      "severidad": "CRITICA",
      "elemento": "Children's consent mechanism (est. 375K users <16)",
      "problema": "No age verification; profiling applied to all minors without parental consent",
      "requisito_incumplido": "Art. 8 GDPR (EU: 16+, Spain LOPDGDD: 14+)",
      "impacto_legal": "Unlawful processing of 375K children; exposure to €20M+ sanction or 4% revenue",
      "remediacion": [
        "1. Implement age gate (email verification required)",
        "2. For Spain users 14-15: parental notification (email); child consent valid",
        "3. For all users <14: parental written consent required (email + verification)",
        "4. Block profiling/targeting until consent obtained",
        "5. Audit historical data; delete profiles of non-consenting minors"
      ],
      "prioridad": 1,
      "deadline": "2024-02-27 (URGENT)",
      "responsable": "Product + Backend + Legal"
    },
    {
      "id": "HIGH-A1",
      "severidad": "ALTA",
      "elemento": "Analytics checkbox",
      "problema": "Pre-ticked; OR consent not required if LIA adopted",
      "requisito_incumplido": "Art. 7.4 (if consent) OR Art. 6.1(f) (if LIA)",
      "opciones": [
        "Option A: Uncheck by default (quick fix)",
        "Option B: Switch to Legitimate Interest + publish LIA assessment (better experience)"
      ],
      "prioridad": 2,
      "deadline": "2024-02-20",
      "responsable": "Product"
    },
    {
      "id": "HIGH-P1",
      "severidad": "ALTA",
      "elemento": "Profiling consent checkbox",
      "problema": "Not explicitly mentioned; bundled with marketing",
      "requisito_incumplido": "EDPB 05/2020 point 4 + Art. 6.1(a) specificity requirement",
      "remediacion": "Separate checkbox: 'Personalized product recommendations' with clear explanation",
      "prioridad": 2,
      "deadline": "2024-02-20",
      "responsable": "Product + Legal"
    }
  ],
  "matriz_consentimientos": {
    "propositos": [
      {
        "id": "P1-ORDER",
        "proposito": "Order processing & fulfillment",
        "base_legal": "CONTRACT (Art. 6.1.b)",
        "consentimiento_requerido": false,
        "status": "COMPLIANT",
        "retencion": "During relationship + 3 years (tax)"
      },
      {
        "id": "P2-MARKETING",
        "proposito": "Marketing emails & promotions",
        "base_legal": "CONSENT (Art. 6.1.a)",
        "consentimiento_requerido": true,
        "consentimiento_valido": false,
        "problemas": ["Pre-ticked checkbox"],
        "status": "NON_COMPLIANT",
        "deadline_remediacion": "2024-02-13",
        "retencion": "2 years from last engagement"
      },
      {
        "id": "P3-ANALYTICS",
        "proposito": "Website analytics & improvement",
        "base_legal": "CONSENT (Art. 6.1.a) OR LEGITIMATE_INTEREST (Art. 6.1.f)",
        "consentimiento_requerido_si_consent": true,
        "status": "PARTIALLY_COMPLIANT (pre-ticked if consent route)",
        "alternativa": "Switch to LIA (recommended)",
        "deadline_remediacion": "2024-02-20",
        "retencion": "13 months (anonymized)"
      },
      {
        "id": "P4-THIRD_PARTY",
        "proposito": "Third-party behavioral advertising",
        "base_legal": "CONSENT (Art. 6.1.a)",
        "consentimiento_requerido": true,
        "consentimiento_valido": false,
        "problemas": ["Recipient not specifically identified", "No explanation of profiling"],
        "status": "NON_COMPLIANT",
        "deadline_remediacion": "2024-02-13",
        "retencion": "24 months (third-party data)"
      },
      {
        "id": "P5-PROFILING",
        "proposito": "Personalized product recommendations",
        "base_legal": "CONSENT (Art. 6.1.a)",
        "consentimiento_requerido": true,
        "consentimiento_valido": false,
        "problemas": ["Not explicitly consented (bundled with marketing)", "Minor protection gap"],
        "status": "NON_COMPLIANT",
        "deadline_remediacion": "2024-02-20",
        "retencion": "As long as customer relationship"
      }
    ]
  },
  "cookie_audit": {
    "cookies_analizadas": 18,
    "halazgos": [
      {
        "cookie": "_ga (Google Analytics)",
        "tipo": "Performance",
        "legal_base": "CONSENT OR LIA",
        "actual": "Pre-ticked",
        "problema": "Pre-ticked consent invalid under EDPB 05/2020",
        "remediacion": "Option A: Uncheck by default | Option B: Switch to LIA (data minimization required)"
      },
      {
        "cookie": "fbp (Meta Pixel)",
        "tipo": "Marketing",
        "legal_base": "CONSENT (explicit)",
        "actual": "Pre-ticked",
        "problema": "Non-essential; must be unchecked by default",
        "remediacion": "Uncheck by default; implement opt-in mechanism"
      },
      {
        "cookie": "session_id",
        "tipo": "Strictly Necessary",
        "legal_base": "Legitimate Interest (Art. 6.1.f)",
        "actual": "No consent required; pre-loads on page",
        "status": "COMPLIANT",
        "retention": "Session (deleted on browser close)"
      }
    ]
  },
  "children_consent_gap": {
    "target_minors": 375000,
    "estimated_under_14": 112500,
    "estimated_14_15": 262500,
    "current_protection": "NONE",
    "required_process": {
      "users_under_14": "Parental written consent (email + verification code) REQUIRED before processing",
      "users_14_15_spain": "Age verification ONLY; parental notification (email) required; child's own consent valid (LOPDGDD Art. 7)",
      "users_14_15_other_eu": "Parental consent required (GDPR Art. 8 default)",
      "profiling_risk": "CRITICAL: Behavioral targeting of minors may violate Art. 5.1(a) even with consent"
    },
    "remediation_steps": [
      "1. Deploy age verification gate (email-based)",
      "2. Create parent consent flow (email + verification code)",
      "3. Notify existing parents of <14 users (retrospective compliance)",
      "4. Delete/anonymize profiles of non-consenting minors",
      "5. Block profiling/targeting features for minors <14 until parental consent"
    ],
    "timeline": "4-6 weeks for implementation",
    "legal_exposure": "20M€ or 4% global revenue if AEPD enforcement action"
  },
  "aepd_references": {
    "doctrine_aplicable": [
      {
        "tema": "Cajas de consentimiento pre-marcadas",
        "base_legal": "Art. 7.4 RGPD + EDPB Guidelines 05/2020 punto 3.3",
        "principio": "El consentimiento obtenido mediante cajas pre-marcadas es inválido; requiere opt-in activo",
        "aplicacion": "Checkbox debe estar DESCHECKED por defecto; usuario debe hacer clic activo para dar consentimiento",
        "sanciones_potenciales": "Hasta €20M o 4% ingresos globales (violación sustancial)"
      },
      {
        "tema": "Simetría en mecanismos de aceptación/rechazo",
        "base_legal": "Art. 7.3 RGPD",
        "principio": "Revocación debe ser tan fácil como otorgamiento",
        "aplicacion": "Si usuario tarda 1 clic en aceptar cookies → máximo 1 clic para rechazar",
        "sanciones_potenciales": "Hasta €20M o 4% ingresos globales"
      },
      {
        "tema": "Consentimiento de menores de edad",
        "base_legal": "Art. 8 RGPD + LOPDGDD Art. 7 (España: 14+)",
        "principio": "España: Menores <14 requieren consentimiento parental; 14-15 requieren notificación parental (consentimiento del menor válido)",
        "aplicacion": "Implementar age gate; solicitar consentimiento parental para <14; notificar a padres para 14-15",
        "sanciones_potenciales": "Hasta €20M o 4% ingresos (procesamiento de menores sin consentimiento)"
      }
    ],
    "doctrina_edpb_vigente": {
      "guidelines_05_2020": "Consent under GDPR - Fundamental principles and rules for implementation",
      "url": "https://edpb.ec.europa.eu/our-work-tools/our-documents_en",
      "puntos_criticos": [
        "Punto 2.2: Consentimiento informado (información clara ANTES de solicitar consentimiento)",
        "Punto 3.3: Consentimiento libremente otorgado (sin cajas pre-marcadas, sin dependencia de servicio no-relacionado)",
        "Punto 4: Consentimiento específico (granular por finalidad, no consentimiento general/blanket)"
      ]
    },
    "doctrina_edpb_vigente_dark_patterns": {
      "guidelines_03_2022": "Guidelines on Dark Patterns in User Interfaces",
      "url": "https://edpb.ec.europa.eu/our-work-tools/our-documents_en",
      "practicas_prohibidas": [
        "Countdown timers presionando al usuario a aceptar",
        "Remordimiento tactics ('¿Seguro que no quiere...?')",
        "Desconexión automática por inactividad",
        "Interfaz de rechazo menos visible/funcional que aceptación"
      ]
    },
    "aepd_contact": "consultas.generales@aepd.es",
    "notification_requirement": "Violaciones de consentimiento deben reportarse a AEPD dentro de 72 horas si afectan >100 usuarios (obligación de breach notification Art. 33 RGPD)"
  },
  "plan_remediacion": [
    {
      "prioridad": 1,
      "hallazgo": "CRIT-M1 (Marketing pre-ticked)",
      "accion": "Remove pre-ticked attribute from marketing checkbox",
      "responsable": "Frontend Engineer + QA",
      "deadline": "2024-02-13",
      "esfuerzo": "Bajo (2 hours)",
      "pruebas": "Verify unchecked by default on desktop/mobile; re-test consent flow"
    },
    {
      "prioridad": 1,
      "hallazgo": "CRIT-T1 (Third-party transparency)",
      "accion": "Update consent text to name Google/Meta/Criteo; link privacy policies",
      "responsable": "Legal + Product",
      "deadline": "2024-02-13",
      "esfuerzo": "Bajo (4 hours)",
      "post_remediacion": "Re-obtain explicit consent from all users (banner campaign)"
    },
    {
      "prioridad": 1,
      "hallazgo": "CRIT-C1 (Children consent gap)",
      "accion": "Implement age verification gate; create parental consent flow; block profiling until consent",
      "responsable": "Product + Backend + Legal",
      "deadline": "2024-02-27",
      "esfuerzo": "Alto (200 hours)",
      "sprints": "Sprint 1 (Feb): Age gate + email verification (40h); Sprint 2 (Feb-Mar): Parental consent flow (80h); Sprint 3 (Mar): Profiling restrictions + audit (80h)",
      "testing": "QA test parent/child flows across 5 languages; AEPD notification pre-launch"
    },
    {
      "prioridad": 2,
      "hallazgo": "HIGH-A1 (Analytics checkbox)",
      "accion": "Either uncheck by default OR switch to Legitimate Interest assessment",
      "responsable": "Product + Data Team",
      "deadline": "2024-02-20",
      "esfuerzo": "Bajo-Medio (20 hours)",
      "opciones": "Recommend Option B (LIA) for better UX; publish balance test"
    },
    {
      "prioridad": 2,
      "hallazgo": "HIGH-P1 (Profiling consent)",
      "accion": "Separate checkbox for profiling; clarify use case (personalized recommendations)",
      "responsable": "Product + Legal",
      "deadline": "2024-02-20",
      "esfuerzo": "Bajo (8 hours)"
    }
  ],
  "riesgo_sancion": {
    "base_legal": "GDPR Art. 83 (Infringement penalties)",
    "potencial_sanciones": {
      "consentimiento_invalido": "20M€ or 4% annual global revenue (whichever is higher)",
      "transparencia_insuficiente": "10M€ or 2% annual global revenue",
      "procesamiento_menores": "20M€ or 4% annual global revenue (higher penalty tier)"
    },
    "atenuantes": [
      "Proactive disclosure to AEPD (notification within 72h of discovery)",
      "Documented compliance efforts (audit trail of remediation)",
      "First-time violation (no history)",
      "Limited scope (few users affected)"
    ],
    "agravantes": [
      "Intent to deceive (pre-ticked boxes = deliberate dark pattern)",
      "Large-scale processing (2.5M users affected)",
      "Processing of minors (sensitive category)",
      "Repeated violations (multiple consent breaches across purposes)"
    ],
    "nivel_riesgo_actual": "ALTO-CRITICO",
    "estimated_sanction": "€5M-15M (given scale + children + intent)",
    "exposure_timeline": "3-6 months if complaint filed; AEPD can impose precautionary measures immediately"
  },
  "regulatory_references": {
    "gdpr_articles": [
      "Art. 6 (lawfulness of processing)",
      "Art. 7 (conditions for consent)",
      "Art. 8 (children's consent)",
      "Art. 13-14 (transparency requirements)",
      "Art. 83 (penalties)"
    ],
    "edpb_guidelines": "Guidelines 05/2020 on consent - https://edpb.ec.europa.eu/our-work-tools/our-documents_en",
    "lopdgdd_articles": [
      "Art. 6 (Spanish consent equivalence)",
      "Art. 7 (Spain: parental consent for <14, notification for 14-15)"
    ],
    "lssi_spain": "Ley 34/1988 (ePrivacy + cookies in Spain)",
    "aepd_register": "Spanish Cookie Registry (Registro de Cookies AEPD)"
  }
}
```

---

## Checklist: Consent Validity Audit

```markdown
### Core Consent Requirements (Art. 7)
☐ Consent checkbox UNCHECKED by default (not pre-ticked)
☐ Separate checkbox per processing purpose (not bundled)
☐ Clear, jargon-free text explaining what data + purpose
☐ Privacy notice provided BEFORE consent request
☐ Affirmative action required (checking box, not silence/inaction)
☐ Timestamp logged when consent granted
☐ Version of consent text stored (for later dispute)
☐ Revocation mechanism as easy as acceptance (one-click unsubscribe)

### EDPB 05/2020 Informed Consent (Point 2.2)
☐ Identity of controller clearly stated
☐ Purpose of processing explained in plain language
☐ Categories of data disclosed
☐ Recipients identified by name or category
☐ Retention period specified
☐ Rights (ARCO: access, rectification, objection, deletion) explained
☐ Complaint mechanism (DPA contact) provided
☐ No dark patterns (excessive scrolling, confusing language)

### Legitimate Interest Alternative (Art. 6.1.f)
☐ LIA balance test published (Purpose + Necessity + Balancing)
☐ Data minimization applied (only essential fields)
☐ Opt-out mechanism provided (to honor objection)
☐ Legitimate interest compelling (not arbitrary)
☐ Data subject rights not systematically outweighed

### Children's Consent (Art. 8 GDPR + LOPDGDD Spain)
☐ Age verification gate implemented (email-based)
☐ Parental consent obtained for Spain <14, EU <16 (if applicable)
☐ Parental notification sent for Spain 14-15 (child owns consent)
☐ Profiling/targeting restricted for minors without consent
☐ Profiles of non-consenting minors deleted/anonymized
☐ Age-appropriate language and warnings in consent form

### Cookie Compliance (ePrivacy Directive + LSSI)
☐ Strictly necessary cookies load without consent
☐ Non-essential cookies blocked until user acceptance
☐ "Reject All" button visible, same prominence as "Accept All"
☐ Rejection mechanism as simple as acceptance (one-click)
☐ Cookie names, purposes, and retention listed
☐ Third-party cookie recipients disclosed (Google, Meta, Criteo, etc.)
☐ Spanish Cookie Registry notification completed (if applicable)

### Revocation & Rights (Art. 7.3, Art. 21)
☐ Withdrawal link in every communication (unsubscribe footer in emails)
☐ Unsubscribe visible without login (no account access required)
☐ Revocation processed within 30 days
☐ Delete of personal data upon withdrawal (within 45 days)
☐ Objection mechanism available (Art. 21 direct marketing opt-out)
☐ Receipt confirmation of withdrawal sent to user

### Data Subject Rights (Art. 15-22)
☐ Rights explanation (ARCO: Access, Rectification, Cancellation, Opposition)
☐ DPA contact information provided (AEPD for Spain)
☐ Complaint mechanism visible (link to AEPD, ICO, etc.)
☐ Explanation of automated decision-making (Art. 22)
☐ Request process simple and free (no fees for access/deletion)
```

---

## References

- **GDPR Art. 6-8, 13-14:** https://gdpr-info.eu
- **EDPB Guidelines 05/2020:** https://edpb.ec.europa.eu/our-work-tools/documents/public-consultations-art-64_en
- **LOPDGDD Art. 6-7 (Spain):** https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673
- **LSSI Law 34/1988 (Spain, ePrivacy):** https://www.boe.es/buscar/act.php?id=BOE-A-1988-26156
- **AEPD Decision PS/00479/2020 (Google consent):** https://www.aepd.es
- **ePrivacy Directive 2002/58/EC:** https://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:32002L0058:en:HTML
