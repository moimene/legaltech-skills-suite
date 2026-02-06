---
name: whistleblower-risk-scorer
description: Triage whistleblower reports under Directive (EU) 2019/1937 transposed via Law 2/2023, assess credibility (specificity, documentation, denunciator position), evaluate impact severity (criminal liability Art. 31 bis CP, CNMV obligations for listed companies, sectoral regulators), model retaliation risk using Law 2/2023 Art. 36-39, and route via weighted scoring (P0–P4) with mandatory 7-day acknowledgment and 90-day resolution timelines.
trigger_contexts:
  - "Internal report received on misconduct/fraud/harassment"
  - "Evaluating whether to escalate externally (CNMV, AAI, Policía Nacional)"
  - "Assessing retaliation risk post-disclosure"
  - "Documenting SII (Sistema de Información Interna) compliance with Law 2/2023"
  - "Listed company required filing with CNMV or sectoral regulator"
---

# Whistleblower Risk Scorer

## Application Scope

Operate internal whistleblower system under EU Directive 2019/1937 (transposed Law 2/2023), triage reports by subject matter + severity, calculate credibility score with weighted factors, evaluate criminal liability exposure (Art. 31 bis CP), assess retaliation vulnerability, and enforce 7-day acknowledgment + 90-day resolution SLAs with escalation to external authorities (CNMV for listed companies, fiscal prosecutors for tax fraud, workplace inspectorates for labor violations).

---

## Regulatory Framework: Law 2/2023 & EU Directive 2019/1937

### Transposition Obligations (Law 2/2023 Art. 1-35)

Companies with **50+ employees** (public or private) must operate **internal reporting channel** ("Sistema de Información Interna" / SII) with:

1. **Written channel** (email/webform confidential to compliance officer or designated SII manager)
2. **Verbal channel** (telephone/in-person to HR or legal)
3. **Anonymous channel** (external anonymous hotline acceptable if confidentiality secured)
4. **Follow-up channel** (feedback on status/resolution without re-identifying denunciator)

### Protected Activities (Art. 5 Law 2/2023)

Denunciators protected if report concerns:
- **Criminal conduct** (Art. 31 bis CP onwards)
- **Administrative violations** (consumer, environmental, data protection, competition, public procurement)
- **Labor rights violations** (discrimination, harassment, wage theft, working time)
- **Failure to report** (if legal obligation exists; e.g., financial crime officer duty)

### Statutory Timeline Requirements

| Phase | Deadline | Breach Consequence |
|-------|----------|-------------------|
| **Acknowledgment (acuse de recibo)** | 7 calendar days | Presumption of failure to receive (Art. 11.3 Law 2/2023) |
| **Preliminary assessment** | Razonable (30–60 days typical) | N/A; assessment must be documented |
| **Investigation completion** | 90 days max from receipt | Extension possible if complex (max 30 additional) |
| **Final resolution + feedback** | 90 days (ext. 30) | Statutory obligation; breach triggers administrative sanctions |

**Listed companies**: If report concerns fiscal fraud, market abuse, or insolvency risk, must notify **CNMV** (Comisión Nacional del Mercado de Valores) within **10 business days** of determination that violation occurred.

---

## Weighted Credibility Scoring Framework (0–100)

Multivariate model combining denunciator position, evidence quality, specificity, and historical accuracy.

```
CREDIBILITY_SCORE =
    (ESPECIFICIDAD × 0.30) +
    (DOCUMENTACION × 0.25) +
    (COHERENCIA_INTERNA × 0.20) +
    (POSICION_ACCESO × 0.15) +
    (HISTORIAL_DENUNCIANTE × 0.10)

THRESHOLDS:
  < 40: BAJA (unsubstantiated; likely unactionable; categorize as "unfounded" without investigation)
  40–65: MODERADA (requires investigation; cannot dismiss without evidence)
  > 65: ALTA (presumptively credible; prioritize investigation; protection measures immediate)
```

### Factor 1: Specificity (Especificidad) - 30 pts max

Measures concreteness of allegation vs. vague accusation.

| Score | Criteria | Example |
|-------|----------|---------|
| **0–10** | Generic complaint, no facts | "Management is corrupt" (no detail) |
| **11–20** | Partial facts, missing key details | "Director received payment from supplier" (no date, amount, account) |
| **21–28** | Specific facts but some gaps | "Director X received €50K from Supplier Y on 2024-01-15; wire reference shows destination account" (missing purpose/quid-pro-quo nexus) |
| **29–30** | Complete narrative with dates, amounts, actors, nexus | "Director of Procurement X, Mr. ABC (ID: 123), received €50K from Supplier Y (reg. 987654) on 2024-01-15 (wire ref. XYZ) in exchange for granting €500K contract to Supplier Y (normally awarded to Competitor Z at 30% lower price); improper markup €150K net gain to Supplier Y" |

### Factor 2: Documentation (Documentación) - 25 pts max

Denunciator provides contemporaneous evidence (not hearsay).

| Score | Criteria | Example |
|-------|----------|---------|
| **0–8** | No documents; oral assertion only | Allegation made verbally; no supporting materials |
| **9–15** | Secondary documents (testimony, email references) | Hearsay email ("I heard X received..."); no primary source |
| **16–20** | Some primary documents but gaps | Bank statements showing deposit to Director's account; no confirmation of source/quid-pro-quo |
| **21–25** | Complete documentary chain | Wire transfer receipt, supplier invoice, director-supplier email discussing "arrangement," company contract award backdated |

### Factor 3: Internal Coherence (Coherencia Interna) - 20 pts max

Narrative consistency; flagged if logical contradictions emerge.

| Score | Criteria | Example |
|-------|----------|---------|
| **0–8** | Multiple contradictions; timeline doesn't align | Alleges event occurred 2024-01-15, but also says "ongoing for 2 years"; no reconciliation |
| **9–15** | Minor inconsistencies; generally plausible | Timeline plausible but payment source unclear; could be legitimate retainer |
| **16–20** | Internally coherent; no logical gaps | Narrative timeline + payment nexus + incentive structure all aligned; no contradictions |

### Factor 4: Denunciator Position & Access (Posición & Acceso) - 15 pts max

Did reporter have **direct access** to alleged facts (vs. third-hand rumor)?

| Score | Criteria | Example |
|-------|----------|---------|
| **0–6** | Indirect access; rumors / hearsay | Junior employee in unrelated department; heard from colleague |
| **7–11** | Partial access; in related function but not direct oversight | Finance team member; no direct visibility to Director's accounts but can infer from invoicing |
| **12–15** | Direct access; role provides oversight capability | Finance controller with approval authority; accounting records accessible; personal witness to conversation |

### Factor 5: Historical Accuracy (Historial) - 10 pts max

Track record of previous reports by denunciator (if any); one-time reporter assumes baseline 5 pts.

| Score | Criteria | Example |
|-------|----------|---------|
| **0–4** | Previous false/frivolous reports | Denunciator history: 3 prior reports, all unfounded or pretextual |
| **5** | First-time reporter (no history) | Denunciator has never reported before; neutral assumption |
| **6–8** | One prior report partially validated | Denunciator reported issue 2 years ago; investigation partial validation |
| **9–10** | Multiple prior reports, all substantiated | Denunciator's prior reports led to disciplinary action; 100% accuracy |

**Result**: Aggregate score determines investigation priority and protection posture.

---

## Matriz de Riesgos por Tipo de Denuncia

Sistema de clasificación que vincula **tipo denuncia × severidad × deadline regulatorio × SLA investigación**.

### Matriz Riesgo (Tipología × Severidad × Timeline)

```
┌──────────────────┬──────────┬──────────────┬──────────────┬─────────────┐
│ TIPO DENUNCIA    │ SEVERIDAD│ DEADLINE REG │ INVESTIGACIÓN│ ESCALADA    │
├──────────────────┼──────────┼──────────────┼──────────────┼─────────────┤
│ FRAUDE FINANZAS  │ Crítica  │ 10d CNMV     │ 90d max      │ Fiscalía    │
│ (Art. 248, 290 CP)│         │ (cotización) │ (+30d ext.)  │ + CNMV      │
├──────────────────┼──────────┼──────────────┼──────────────┼─────────────┤
│ ACOSO LABORAL    │ Alta     │ 45d Inspección│ 60d max      │ Juzgado     │
│ (Art. 44 ET)     │         │ Trabajo      │             │ Social      │
├──────────────────┼──────────┼──────────────┼──────────────┼─────────────┤
│ SEGURIDAD/RIESGOS│ Crítica  │ Inmediato    │ 30d urgente  │ Inspec.     │
│ (Art. 19-22 ET)  │         │ (life threat)│ +60d regular │ Trabajo +   │
│                  │         │             │             │ Juzgado     │
├──────────────────┼──────────┼──────────────┼──────────────┼─────────────┤
│ CORRUPCIÓN       │ Crítica  │ 30d (AEPD)   │ 90d          │ Policía +   │
│ (Art. 31 bis CP) │         │ si RGPD     │ (+30d)      │ Fiscalía    │
├──────────────────┼──────────┼──────────────┼──────────────┼─────────────┤
│ VIOLACIÓN DATOS  │ Alta     │ 72h notific. │ 90d          │ AEPD +      │
│ (Art. 33 RGPD)   │         │ AEPD        │             │ Juzgado     │
├──────────────────┼──────────┼──────────────┼──────────────┼─────────────┤
│ DISCRIMINACIÓN   │ Media    │ 7d acu.      │ 60d          │ Juzgado     │
│ (Art. 17 ET)     │         │ recibido    │             │ Social      │
├──────────────────┼──────────┼──────────────┼──────────────┼─────────────┤
│ MEDIO AMBIENTE   │ Alta     │ 30d CCAA     │ 90d          │ Juzgado +   │
│ (Ley 27/2007)    │         │             │             │ Fiscalía    │
└──────────────────┴──────────┴──────────────┴──────────────┴─────────────┘

MATRIZ DE RIESGOS COMBINADOS:

Denuncia + Atributos → Puntuación Riesgo (0–100) → Acción

P0 (Crítico): 75–100 puntos
├─ Acción: Escalada inmediata; investigación 48h
├─ Ejemplos: Fraude financiero (listed company), riesgo seguridad inmediato
├─ SLA: 7d acknowledgment, 30d preliminary, 90d final (sin extensión)
└─ Escalada: CNMV/Policía/Juzgado dentro 10 días si procedente

P1 (Muy Alto): 50–74 puntos
├─ Acción: Investigación acelerada (60 días)
├─ Ejemplos: Corrupción, acoso sistémico, violación seguridad
├─ SLA: 7d acknowledgment, 45d investigation, 90d final
└─ Escalada: Notificación regulador si procedente

P2 (Alto): 30–49 puntos
├─ Acción: Investigación estándar (90 días)
├─ Ejemplos: Violación RGPD (no crítica), discriminación documentada
├─ SLA: 7d acknowledgment, 60d investigation, 90d final
└─ Escalada: Evaluación escalada si evidencia clara

P3 (Moderado): 10–29 puntos
├─ Acción: Investigación explorativa (60 días)
├─ Ejemplos: Quejas conduct code, conflicto interés menor
├─ SLA: 7d acknowledgment, 45d investigation, 90d final
└─ Escalada: Rara; solo si nuevos hechos emergen

P4 (Bajo): 0–9 puntos
├─ Acción: Triage; puede desestimarse sin investigación formal
├─ Ejemplos: Quejas varias sin especificidad, rumores
├─ SLA: 7d acknowledgment, 15d assessment si procede
└─ Escalada: Ninguna típicamente
```

### Scoring Automático: Ejemplo Fraude Financiero

```
DENUNCIA: CFO manipula reconocimiento ingresos Q4 2023 (enterprise SaaS cotizada)

ATRIBUTOS RIESGO:
├─ Tipo: PENAL (Art. 290-296, 248 CP) → +30 pts
├─ Severidad: Material (€75M ingresos inflados) → +25 pts
├─ Deadline regulatorio: 10d CNMV (cotizada) → +15 pts
├─ Investigación SLA: 90d (complex) → +5 pts
│
└─ SUBTOTAL: 75 pts → CATEGORÍA P0 (CRÍTICO)

SLA APLICABLE (Law 2/2023):
├─ Acuse recibo: 7 días hábiles (Deadline: Día 7)
├─ Investigación preliminar: 45 días (Día 52)
├─ Investigación completa: 90 días máximo (Día 90)
├─ Extensión posible: 30 días si complejidad justificada (Día 120)
├─ Notificación regulador: 10d desde determinación si violation substantiated
└─ Timeline CNMV: Si violation confirmed en Day 60, notify by Day 70
```

---

## SLA de Investigación (Law 2/2023 Compliance)

Cumplimiento temporal obligatorio para **cada denuncia**.

### Fases SLA Statutory (Art. 11, 12 Law 2/2023)

```
FASE 1: ACUSE DE RECIBO (Acknowledgment)
├─ Deadline: 7 días calendario desde recepción
├─ Contenido mínimo:
│  ├─ Confirmación recepción (fecha, hora, canal)
│  ├─ Número de seguimiento único (WB-YYYY-XXXX)
│  ├─ Confirmación protecciones retaliation (Art. 36-39)
│  └─ Contacto para seguimiento (canales feedback separados)
├─ Incumplimiento: Presunción de no-recepción; sanciones administrativas
└─ Ejemplo:
   ```
   Estimado Denunciante,

   Confirmamos recepción denuncia WB-2024-0157 en fecha 2024-02-06, 14:30 UTC.

   Protecciones Art. 36-39 Law 2/2023 aplican automáticamente:
   - Confidencialidad identidad garantizada
   - Prohibición represalias (cualquier acción adversa presumida represalia)
   - Canal follow-up segregado para feedback

   Su investigación se asignará dentro 3 días hábiles.
   Recibirá status update cada 30 días.

   Referencia seguimiento: [email confidencial separado]
   ```

FASE 2: INVESTIGACIÓN PRELIMINAR
├─ Duración: Razonable; típicamente 30–45 días
├─ Objetivo: Determinar si denuncia viable para investigación formal
├─ Acciones:
│  ├─ Entrevista denunciante (si requiere clarificaciones)
│  ├─ Preservación evidencia (IT forensics, document lock-down)
│  ├─ Consulta fuentes primarias (si bajo riesgo identificación)
│  └─ Evaluación credibility score
├─ Output: Decisión "Procede Investigación Formal" o "Desestimar"
├─ Timeline: Completar antes Day 45 (day 30 ideal)
└─ Incumplimiento: Retraso injustificado sanciona empresa

FASE 3: INVESTIGACIÓN FORMAL
├─ Deadline: 90 días máximo desde recepción inicial denuncia
├─ Extensión posible: +30 días si "complejidad excepcional" (documentada)
│  ├─ Causas válidas: Multi-jurisdicción, forense IT extenso, múltiples entrevistas
│  ├─ Causas inválidas: "Recursos limitados", "vacaciones", "carga trabajo"
│  └─ Decisión extensión: Denunciante debe recibir notificación + justificación
├─ Investigador(es): Independiente (external counsel preferred; privilege)
├─ Scope:
│  ├─ Reconstrucción de hechos (timeline, documentos, testimonios)
│  ├─ Análisis legal (aplicabilidad statutos, culpabilidad)
│  ├─ Cuantificación daño (si procedente)
│  └─ Determinación: Substantiated / Unsubstantiated / Inconclusive
├─ Entrevistas:
│  ├─ Denunciante (profundidad; detalles adicionales)
│  ├─ Subjects (alleged perpetrators): sin advertencia previa si riesgo destrucción evidencia
│  ├─ Witnesses: statement bajo confidentiality agreements
│  └─ IT/Forensics: digital evidence preservation + chain of custody
├─ Documentación:
│  ├─ Todos interviews grabadas o minutadas (confidencial)
│  ├─ Exhibits inventariados (metadata, source, verification)
│  ├─ Working papers auditados (segregación: investigation vs. management)
│  └─ Draft report circulado a subjects para Right to be Heard (RGPD Art. 14)
└─ Output: Final Report with Finding(s)

FASE 4: RESOLUCIÓN Y FEEDBACK
├─ Comunicación denunciante (90d máximo, ext. 30d posible):
│  ├─ Summary de hallazgos (SIN exposición identidad si confidencialidad requested)
│  ├─ Exemplo: "Investigación sustanció alegaciones de irregularidades contables.
│  │            Acciones disciplinarias y restatement financiero iniciados.
│  │            Notificación regulador en curso."
│  ├─ Acceso a evidence: Limitado (conforme RGPD; puede negar si prejudicial)
│  └─ Feedback channel: Separado de SII email (personal meeting preferred)
├─ Comunicación sujetos (simultáneamente):
│  ├─ Notificación de findings
│  ├─ Derecho a contestación (15 días)
│  ├─ Oportunidad revisión antes sanción
│  └─ Documento "Derechos del investigado" (due process)
├─ Escalada (si procedente):
│  ├─ CNMV: Si violation ley mercados valores (listed companies, 10d deadline)
│  ├─ Fiscalía: Si criminal conduct (fraud, falsification, etc.)
│  ├─ Inspección Trabajo: Si labor violation
│  ├─ Auditor externo: Si finding audit-relevant
│  └─ Board/Audit Committee: Si governance risk
└─ Cierre (con denunciante):
   ├─ Notificación final: "Investigación cerrada. Hallazgos implementados."
   └─ Confidentiality reaffirmed: "Identidad protegida permanentemente."

TIMELINE AGREGADA (Law 2/2023 Compliance):

Día 0: Denuncia recibida
Día 7: ✓ MUST = Acuse recibo (Red si no)
Día 30–45: ✓ SHOULD = Preliminar assessment completado
Día 90: ✓ MUST = Investigación completada / Deadline extension justified
Día 120: ✓ DEADLINE FINAL = Resolución (si extensión ejercida)
Día 10 (post-determination): ✓ MUST = CNMV notification (si cotizada + violation)

COMPLIANCE TRACKING:

SLA_COMPLETER = 1 (todos deadlines met)
             = 0.7 (1 retraso justificado; extensión formal)
             = 0.4 (múltiples retrasos; extensión negligente)
             = 0 (deadline violations without cause; violation Art. 12)
```

---

## Anonimato y Segregación de Accesos

Protección técnica y administrativa de identidad denunciante + segregación funcional.

### Requisitos Técnicos Canal Anónimo (Art. 8 Law 2/2023)

```
1. CANAL DE REPORTE ANÓNIMO (External Hotline Preferido)
   ├─ Proveedor: Tercero independiente (external hosted hotline)
   │  ├─ Ejemplos: Expolink, LRS Legal Hotline, NAVEX Global
   │  └─ Requerimiento: Contrato con cláusula "Sin acceso empresa a IP/logs"
   ├─ Infraestructura técnica:
   │  ├─ Encriptación end-to-end (TLS 1.3 mínimo; no logs en servidor empresa)
   │  ├─ Hosting geográfico: Jurisdicción externa (no España; típicamente UE)
   │  ├─ Zero-knowledge architecture: Proveedor no puede descifrar identidad
   │  └─ No cookies / no tracking (RGPD compliance mínimo)
   ├─ Acceso denunciante:
   │  ├─ Teléfono: Número independiente (no empresa switchboard)
   │  ├─ Web: URL anonimizado (no branded empresa; típicamente "hotline.provider.com/client-ABC")
   │  ├─ Múltiples idiomas: Español mínimo + inglés recomendado
   │  └─ Disponibilidad: 24/7 telefónico; web sin restricción horaria
   ├─ Identificación anonimato:
   │  ├─ Sistema de "Case Reference Number" (e.g., WB-2024-0157-ANONX)
   │  ├─ Denunciante solo accede con Reference + PIN único
   │  ├─ No recopila: Nombre, email empresa, IP, device ID (excepto timestamp)
   │  └─ Follow-up: Proveedor envía status updates via portal anonimizado
   └─ Transición identidad:
      ├─ Si denunciante desea auto-identificarse DESPUÉS: Acta escrita separada
      ├─ Denunciante decide: "Mantengo anonimato" vs. "Me identifico para follow-up"
      ├─ Auto-identificación: NO revela a management; solo a Compliance Officer + Investigator
      └─ Cambio anonimato: Registrado en log segregado (audit trail solo para Legal)

2. SEGREGACIÓN DE ACCESOS (Role-Based Access Control)

   A. INVESTIGADOR (External Counsel, preferido)
   ├─ Acceso: Full case file + all evidence + witness statements
   ├─ Derecho: Direct communication con denunciante (anónimo durante inv.)
   ├─ Restrincción: NO puede revelar identidad a CEO/Board sin consentimiento explicit
   ├─ Output: Informe final pode redactar "identidad protegida" en executive summary
   └─ Confidentiality: Attorney-client privilege cubre toda investigación

   B. COMPLIANCE OFFICER / SII Manager
   ├─ Acceso: Case metadata (ID, status, categoría, timeline)
   ├─ Acceso: Preliminary findings (NO detailed evidence si pueda identificar)
   ├─ Derecho: Coordinar logistics (investigador, timeline, recursos)
   ├─ Restricción: NO acceso a denunciante identity (excepto auto-disclosure)
   ├─ Restricción: NO puede comunicar findings a management sin investigador approval
   └─ Duty: Notificación denunciante (via hotline) status updates

   C. MANAGEMENT / CEO / CFO (Sujetos si procede)
   ├─ Acceso: Final report findings Y CONCLUSIONS (redacted)
   ├─ Acceso: NO denunciante identity (salvo auto-disclosure + consent)
   ├─ Acceso: NO investigation working papers / witness statements
   ├─ Acceso: NO forensic evidence (chain of custody motive preservation)
   ├─ Derecho: Right to be heard (STS jurisprudencia + RGPD Art. 14)
   │  ├─ Notificación: "Investigación concluyó X findings. Puede contestar en 15 días."
   │  └─ Contestación: Admitida; considerada antes finalización
   └─ Restricción: NO puede usar investigación contra denunciante basado en identidad

   D. BOARD / AUDIT COMMITTEE (Governance)
   ├─ Acceso: Executive summary + regulatory obligations (CNMV notification, etc.)
   ├─ Acceso: Findings + recommended actions (but NOT perpetrator identity details)
   ├─ Acceso: SLA compliance status (timelines met, extensions used)
   ├─ Restricción: NO denunciante identity (confidentiality maintained)
   └─ Duty: Oversight de compliance + escalation procedures

   E. EXTERNAL AUDITOR (si audit-relevant)
   ├─ Acceso: Findings relevantes a financial statements (e.g., fraud)
   ├─ Acceso: Ethical obligation notificación
   ├─ Acceso: NO investigador working papers (work product privilegio)
   ├─ Restricción: NO denunciante identity
   └─ Confidentiality: Same as management; audit confidentiality applies

3. TECHNICAL ACCESS LOGGING & AUDIT TRAIL

   Segregated logs (NO logged to main system):
   ├─ Who accessed case file (User ID + timestamp + IP) → Audit-only
   ├─ What was accessed (document name + size + hash)
   ├─ When accessed (seconds resolution; not approximate)
   ├─ Duration (time to first view + total session time)
   ├─ Actions (download, print, screenshot attempts → denied/logged)
   └─ Retention: 7 years (RGPD compliance; laboral law prescripción)

   Restrictions & Monitoring:
   ├─ Case file NEVER in email (only secure portal)
   ├─ Print: Disabled; screenshot detection enabled (watermark + warning)
   ├─ Copy/paste: Disabled from PDF (force manual transcription if needed)
   ├─ IP restricción: Whitelisted office IPs only (no remote access unless VPN)
   ├─ Notification: Denunciante alerted if unauthorized access attempt detected
   └─ Escalation: Unauthorized access = potential Art. 36-39 retaliation

4. WHISTLEBLOWER IDENTITY PROTECTION MEASURES

   Antes investigación comienza:
   ├─ Notificación escrita denunciante:
   │  ├─ "Art. 7-10 Law 2/2023: Confidentiality garantizada"
   │  ├─ "Art. 36-39 Law 2/2023: Protección represalia automática"
   │  ├─ "Identidad protegida; acceso restringido a Investigador + Compliance"
   │  └─ "Si auto-identificas en Day N, derecho a cambiar a anonymity después"
   ├─ Verificación: Denunciante confirma comprensión (email signed return)
   └─ Documentación: Almacenar en segregated folder (attorney work product)

   Durante investigación:
   ├─ Entrevista denunciante: NUNCA in office; off-site o teléfono (no call logs)
   ├─ Comunicación: Siempre via hotline/portal; NUNCA email empresa
   ├─ Si subjects o witnesses preguntan sobre denunciante:
   │  ├─ Response: "Investigación confidencial; identidad protegida"
   │  └─ Consecuencia si violación: Retaliation presumida (Art. 39)
   └─ Confidentiality agreements: Todos investigadores + witnesses firman

   Después investigación concluye:
   ├─ Final report denunciante: "Summary findings (anonymized; details confidential)"
   ├─ Notificación: "Acciones disciplinarias implementadas; identidad protegida"
   ├─ Permanencia: Identidad confidential indefinidamente (salvo auto-request revelation)
   └─ Si divulgación accidentally ocurre:
      ├─ Empresa notifica denunciante inmediatamente
      ├─ Medidas mitigating presuntas (investigación represalia)
      ├─ Registro incidente: Proof empresa actuó para proteger
      └─ Daño potential: Compensación si retaliation resulta

5. REGULADOR COORDINATION (Art. 15-17 Law 2/2023)

   If investigation finds external violation (CNMV, Inspección Trabajo, etc.):
   ├─ CNMV notification (10d if listed company + financial fraud)
   │  ├─ Contenido: "Caso WB-2024-XX determinó violation ley mercados valores"
   │  ├─ Identidad denunciante: OMITIDA (confidentiality maintained)
   │  └─ Summary: Hechos + evidencia + findings (pero anonimizado)
   ├─ Regulador puede investigar independently:
   │  ├─ Puede contactar directamente denunciante (si quiere ampliar)
   │  ├─ Pero: Empresa "no divulgó identidad"; denunciante decided auto-reveal
   │  └─ Protección: CNMV también vinculada por confidentiality si denunciante requests
   └─ Empresa NOT liable si regulador discovers identity post-transmission
```

---

## Impact Severity Scoring (0–100)

Weights by category (criminal > administrative) and downstream consequences.

### Factor 1: Gravity of Conduct (Gravedad) - 30 pts max

| Conduct Type | Statutory Basis | Severity | Score |
|---|---|---|---|
| **Criminal (Penal)** | Art. 31 bis CP onwards | Fraud, bribery (cohecho), forgery | 28–30 |
| **Criminal (Penal)** | Money laundering, embezzlement (malversación) | Art. 251 CP | 27–30 |
| **Administrative (High)** | RGPD data breach (Art. 83 GDPR) | Fines up to €20M or 4% revenue | 22–25 |
| **Administrative (Medium)** | Labor violation (discrimination, wage theft) | Fines €10K–100K | 15–20 |
| **Administrative (Low)** | Code-of-conduct breach, non-criminal conflict-of-interest | Fines <€10K; disciplinary only | 8–14 |

### Factor 2: Number Affected (Número Afectados) - 25 pts max

| Scope | Pts |
|---|---|
| Isolated (1 victim) | 8–12 |
| Departmental (2–10 affected) | 13–18 |
| Systemic (10+ or repeated pattern) | 19–25 |

### Factor 3: Economic Damage (Daño Económico) - 20 pts max

| Amount | Pts |
|---|---|
| <€10K | 4–8 |
| €10K–€100K | 9–14 |
| €100K–€1M | 15–19 |
| >€1M | 20 |

### Factor 4: Reputational Damage (Daño Reputacional) - 15 pts max

| Risk | Pts |
|---|---|
| Internal management issue only | 2–5 |
| Potential customer awareness | 6–10 |
| Media exposure / listed company scandal | 11–15 |

### Factor 5: Legal/Regulatory Penalty Exposure (Riesgo Legal) - 10 pts max

| Exposure | Pts |
|---|---|
| Administrative warning only | 2–4 |
| Fines + potential executive criminal exposure | 5–8 |
| Criminal indictment risk + asset seizure + executive imprisonment (5+ years) | 9–10 |

---

## Urgency Scoring (0–100)

Measures immediacy of investigation need.

### Factor 1: Ongoing Conduct (Conducta Continuada) - 35 pts max

**Key question**: Is violation still occurring?

| Answer | Pts |
|---|---|
| Alleged conduct ended months ago; one-time event | 5–12 |
| Ongoing but low frequency (monthly or less) | 13–22 |
| Active/continuing daily; ongoing damage accrual | 23–35 |

### Factor 2: Evidence Destruction Risk (Destrucción Evidencia) - 25 pts max

**Key question**: Will evidence disappear if investigation delayed?

| Risk | Pts |
|---|---|
| Documentary evidence (emails, bank records) backed up; low destruction risk | 0–8 |
| Digital evidence at risk if not preserved within days (email purges, log overwrite) | 9–15 |
| Critical evidence (hard drive, communications) imminently at destruction risk | 16–25 |

### Factor 3: Physical Safety (Seguridad Personas) - 25 pts max

**Key question**: Is personal injury risk present?

| Risk | Pts |
|---|---|
| No safety risk; financial/administrative matter | 0 |
| Potential workplace violence risk (history of threats) | 8–18 |
| Acute safety hazard (workplace injury risk, harassment escalation) | 19–25 |

### Factor 4: Statute of Limitations (Prescripción) - 15 pts max

**Key question**: When does limitation period expire?

| Timeline | Pts |
|---|---|
| Long limitation period (5+ years remaining) | 2–5 |
| Intermediate (1–5 years remaining) | 6–10 |
| Short limitation (< 1 year remaining); urgent filing needed | 11–15 |

---

## Concrete Example: Financial Fraud Whistleblower (Listed Company)

**Scenario**: Senior accountant at listed tech company reports alleged revenue recognition fraud by CFO impacting fiscal results.

```
DENUNCIATOR PROFILE:
├─ Role: Senior Accountant (Accounting Dept.)
├─ Tenure: 7 years
├─ Access level: High (prepares consolidated statements)
├─ Reason for report: Conscience + job security concern (was asked to backdate contracts)
└─ Channel used: Written email to SII manager (anonymous initially, then self-identified)

CREDIBILITY CALCULATION:

1. ESPECIFICIDAD (30 pts max):
   ├─ Allegation: "CFO instructed me to modify revenue recognition on Q4 2023 contracts,
   │  backdating signatures to achieve €50M revenue target. 12 contracts totaling €75M,
   │  actual delivery dates Jan-Feb 2024, recorded as Dec 2023. Affected EBITDA
   │  target by 8%; bonus structure tied to targets."
   ├─ Detail level: HIGH (specific contracts, amounts, dates, mechanism, impact)
   └─ Score: 29 / 30

2. DOCUMENTACION (25 pts max):
   ├─ Evidence provided: Contract PDFs with original timestamps vs. recorded signatures,
   │  signed memo from CFO ("Adjust revenue timing for Q4 closure"), email chain,
   │  accounting journal entries showing manual reclassification
   ├─ Primary documents: YES (contemporaneous, not hearsay)
   └─ Score: 24 / 25

3. COHERENCIA_INTERNA (20 pts max):
   ├─ Timeline: Allegation occurs Nov-Dec 2023; report filed Feb 2024 (plausible delay for fear)
   ├─ Incentive structure: CFO bonus tied to EBITDA; motive clear
   ├─ No contradictions: Narrative internally consistent
   └─ Score: 20 / 20

4. POSICION_ACCESO (15 pts max):
   ├─ Role: Senior Accountant with consolidated statement responsibility
   ├─ Direct access: YES (personal signer on trial balance adjustments)
   └─ Score: 15 / 15

5. HISTORIAL (10 pts max):
   ├─ Previous reports: None (first-time reporter; neutral baseline)
   └─ Score: 5 / 10

CREDIBILITY_SCORE = (29 × 0.30) + (24 × 0.25) + (20 × 0.20) + (15 × 0.15) + (5 × 0.10)
                   = 8.7 + 6.0 + 4.0 + 2.25 + 0.5
                   = 21.45 / 30 (normalized to 100 scale)
                   = 71.5 / 100 → HIGH CREDIBILITY

─────────────────────────────────────────────────

IMPACT CALCULATION:

1. GRAVEDAD_CONDUCTA (30 pts max):
   ├─ Category: Criminal (falsifying accounting documents; Art. 290-296 CP Falsedad)
   ├─ Secondary: Fraud/financial crime (estafa, Art. 248 CP)
   ├─ Severity: Material impact on market confidence (listed company)
   └─ Score: 30 / 30

2. NUMERO_AFECTADOS (25 pts max):
   ├─ Scope: Systemic (affects all quarterly filers; potentially multiple years)
   ├─ Investor base: ~5,000 shareholders + institutional investors
   ├─ Employees: Broader perception of management integrity
   └─ Score: 24 / 25

3. DANO_ECONOMICO (20 pts max):
   ├─ Direct fraud: €75M inflated revenue
   ├─ Bonuses paid improperly: €1.5M (CFO + team)
   ├─ Estimated shareholder value loss if fraud public: €500M–€2B (stock multiple compression)
   └─ Score: 20 / 20

4. DANO_REPUTACIONAL (15 pts max):
   ├─ Risk: Severe (public scandal if disclosed; CNMV investigation public)
   ├─ Media exposure: High (tech company + accounting fraud = headlines)
   ├─ Regulatory perception: Criminal referral to Fiscalía likely
   └─ Score: 15 / 15

5. RIESGO_LEGAL (10 pts max):
   ├─ Criminal indictment risk for CFO: HIGH (falsifying docs + fraud)
   ├─ Executive liability exposure: 3–8 year imprisonment + fines
   ├─ Company liability: €5M–€50M CNMV fines; possible suspension
   └─ Score: 10 / 10

IMPACT_SCORE = (30 × 0.30) + (24 × 0.25) + (20 × 0.20) + (15 × 0.15) + (10 × 0.10)
              = 9.0 + 6.0 + 4.0 + 2.25 + 1.0
              = 22.25 / 30 (normalized to 100 scale)
              = 74.2 / 100 → CRITICAL IMPACT

─────────────────────────────────────────────────

URGENCY CALCULATION:

1. CONDUCTA_CONTINUADA (35 pts max):
   ├─ Status: Likely ONGOING (Q1 2024 closing not yet complete; revenue recognition pressure imminent)
   ├─ Frequency: Quarterly cycle (high frequency at close periods)
   └─ Score: 32 / 35

2. EVIDENCIA_PERECEDERA (25 pts max):
   ├─ Risk: HIGH (digital forensics: email purge cycles, server logs overwrite in 90 days)
   ├─ CFO likely to detect report + destroy evidence if alerted
   ├─ Preservation critical within 48 hours
   └─ Score: 23 / 25

3. SEGURIDAD_PERSONAS (25 pts max):
   ├─ Direct safety risk: LOW (white-collar crime; no workplace violence indicators)
   ├─ Retaliation risk: MODERATE-HIGH (accountant fears job loss; must protect)
   └─ Score: 8 / 25 (conservative; retaliation addressed separately under Art. 36-39)

4. PRESCRIPCION (15 pts max):
   ├─ Falsification statute: 5 years (Art. 131 CP)
   ├─ Time elapsed: ~2 months (plenty of time)
   ├─ But: CFO may attempt document destruction → evidence preservation urgent
   └─ Score: 5 / 15

URGENCIA_SCORE = (32 × 0.35) + (23 × 0.25) + (8 × 0.25) + (5 × 0.15)
                = 11.2 + 5.75 + 2.0 + 0.75
                = 19.7 / 27.5 (normalized to 100 scale)
                = 71.6 / 100 → HIGH URGENCY

─────────────────────────────────────────────────

INTEGRATED PRIORITY SCORE:

PRIORIDAD_GLOBAL = (CREDIBILIDAD × 0.35) + (IMPACTO × 0.40) + (URGENCIA × 0.25)
                 = (71.5 × 0.35) + (74.2 × 0.40) + (71.6 × 0.25)
                 = 25.0 + 29.7 + 17.9
                 = 72.6 / 100 → **P0 - IMMEDIATE ACTION REQUIRED**

CATEGORY_PRIORITY: P0 (Critical; criminal conduct + ongoing fraud risk + public company impact)

─────────────────────────────────────────────────

CHANNEL REQUIREMENTS (Law 2/2023 Art. 7-10):

Report received via: **Written channel (email to SII manager)**
✓ Meets written requirement
✓ Confidentiality secured (SII manager bound by confidentiality)
✓ Denunciator self-identified after anonymity period (strengthens credibility)
✓ All documents preserved in secure folder

Alternative channels denunciator could have used:
├─ Verbal (phone hotline) ✓ Available but not used
├─ Anonymous external hotline ✓ Available but not used; denunciator chose identity disclosure
└─ Direct to compliance officer (yes; same person as SII manager)

Assessment: Report complies with Law 2/2023 channel requirements; denunciator exercised written + follow-up communication path.

─────────────────────────────────────────────────

RETALIATION PROTECTION FRAMEWORK (Law 2/2023 Art. 36-39):

Accountant is entitled to automatic protection if:
✓ Report made through proper channel (Art. 7-10) → YES
✓ Good-faith belief in report veracity (Art. 5) → YES (evidence provided; no malice)
✓ No disclosure to third party without authorization → YES (confidentiality maintained)

Prohibited retaliatory measures (Art. 36-39):
├─ Termination, suspension, demotion → ILLEGAL
├─ Transfer, discipline related to report → ILLEGAL
├─ Harassment, intimidation → ILLEGAL
├─ Defamation (labeling as "disloyal") → ILLEGAL
└─ Any adverse change in working conditions → ILLEGAL

Burden of proof: If adverse action within 12 months of report, employer must prove
non-retaliatory cause (Art. 39).

Protection mechanisms:
├─ Confidentiality of denunciator identity (unless denunciator authorizes)
├─ Separate communication channel (feedback on investigation separate from SII email)
├─ Documentation of all interactions (audit trail)
└─ Internal monitor (HR + Compliance) flagging any personnel action

Accountant should receive written acknowledgment: "Your report is protected under
Law 2/2023 Art. 36-39. No adverse action may be taken in retaliation."

─────────────────────────────────────────────────

CRIMINAL LIABILITY IMPLICATIONS (Art. 31 bis CP):

1. CFO Personal Liability:
   ├─ Falsifying accounting documents (Art. 290-296 CP): 3–6 years imprisonment
   ├─ Fraud/estafa (Art. 248 CP, if breach of contract elements): 1–6 years
   ├─ Administrative liability (Law 10/1995): Fine €300K–€3M
   └─ Executive disqualification (Art. 405 CP): 3–6 years bar from officer roles

2. Company Liability (Art. 31 bis CP):
   ├─ If company failed to prevent fraud despite organizational capacity
   ├─ Fine: €5M–€50M (CNMV administrative scale)
   ├─ Alternative: 5–15% of revenue (depending on gravity)
   └─ Deferred prosecution possible (acuerdo reparador) if full remediation + compliance

─────────────────────────────────────────────────

CNMV REPORTING OBLIGATION (Applicable to Listed Companies):

Company must notify CNMV if:
✓ Report substantiates violation of securities law (revenue recognition fraud = financial reporting fraud)
✓ Determination made that violation occurred (after preliminary investigation)
✓ Materiality threshold: Impact on investor reliance on financial statements

Timeline: **10 business days** from determination date (Art. 227 LMV)

Content of CNMV notice:
├─ Summary of alleged violation
├─ Affected accounting periods
├─ Estimated financial impact
├─ Internal investigation status + findings
└─ Remediation measures undertaken

Failure to notify CNMV: Administrative fine up to €3M + executive personal liability

Expected outcome: CNMV opens investigation; possible criminal referral to Fiscalía
for falsifying documents; potential trading halt if credibility high.

─────────────────────────────────────────────────

INVESTIGATIVE ROADMAP:

PHASE 1 (48 hours - Evidence Preservation):
├─ IT forensics: Email server preservation, backup all CFO communications
├─ Document seizure: Original contracts, journal entries, approvals
├─ Whistleblower debrief: Detailed written statement
└─ Confidentiality notification: Legal team only (investigate under attorney privilege)

PHASE 2 (Days 3-14 - Preliminary Investigation):
├─ Forensic accounting review: Contract timing analysis, revenue recognition policy application
├─ CFO interview (or hold until investigator briefing)
├─ Third-party verification: Customer confirmations of delivery/service dates
├─ Document authentication: Signature analysis, metadata review
└─ Audit trail reconstruction: Who modified entries, when, from what terminal

PHASE 3 (Days 15-90 - Formal Investigation & Determination):
├─ Final report: Substantiation or refutation of alleged violations
├─ Legal opinion: Applicability of criminal statutes (Art. 290-296, 248 CP)
├─ Remediation planning: Restatement preparation, disciplinary action if warranted
├─ Regulatory notification: CNMV disclosure (if violation confirmed)
└─ Denunciator feedback: Summary of investigation results (confidential)

PHASE 4 (Days 91+ - External Escalation if Warranted):
├─ Criminal referral: File denuncia with Fiscalía (Prosecutor's Office for Financial Crime)
├─ Regulatory engagement: CNMV investigation coordination
├─ Auditor notification: Inform external auditors of findings (audit committee responsibility)
└─ Remediation execution: Restate financials, impose disciplinary action, control improvements

─────────────────────────────────────────────────

TIMELINE COMPLIANCE (Law 2/2023):

✓ Acknowledgment deadline (7 days): Send written acuse de recibo to denunciator within 7 days
  → Deadline: [Report received date + 7 days]
  → If missed: Presumption of non-receipt; regulatory sanction risk

✓ Investigation completion (90 days ext. 30): Final resolution by [90 + possible 30-day ext.]
  → Complex criminal investigation may justify 30-day extension
  → Extension decision must be documented with justification
  → Denunciator must receive status update explaining extension

✓ Final feedback to denunciator: Provide resolution summary (without exposing denunciator identity)
  → Example: "Investigation substantiated allegations of accounting irregularities.
    Disciplinary action and financial restatement initiated. External regulatory
    notification underway."

─────────────────────────────────────────────────

MITIGATION RECOMMENDATIONS:

1. **Immediate** (within 48 hours):
   ├─ Assign independent investigator (external counsel preferred; attorney-client privilege)
   ├─ IT forensics: Preserve all CFO communications + accounting system access logs
   ├─ Finance review: Pull Q4 2023 contract files + journal entries
   ├─ Place CFO on suspension of duties pending investigation (with pay; avoid appearance of retaliation)
   └─ Document denunciator protection measures (written confirmation of Art. 36-39 protections)

2. **Short-term** (within 14 days):
   ├─ Engage external forensic accountant for independent review
   ├─ Audit committee briefed (segregate investigation from management)
   ├─ External auditors notified of investigation (ethical obligation)
   ├─ Preserve evidence: Contract originals, archived emails, system logs
   └─ Begin CNMV notification prep (likely required within 30 days of determination)

3. **Medium-term** (within 90 days):
   ├─ Complete investigation; finalize findings
   ├─ Determine criminal referral necessity (if high confidence of Art. 290-296 violation)
   ├─ Notify CNMV (if fraud substantiated; 10 business days from determination)
   ├─ Prepare financial restatement (audit committee responsibility)
   ├─ Disciplinary action against CFO (termination + claw-back of ill-gotten bonuses)
   └─ Provide final feedback to denunciator (outline resolution without compromising confidentiality)

4. **Regulatory** (ongoing):
   ├─ Coordinate with CNMV investigation (if opened)
   ├─ Fiscal Prosecutor coordination (if criminal referral warranted)
   ├─ External auditor remediation testing
   └─ Board resolution: Enhanced financial controls, segregation of duties, audit committee independence
```

---

## Inputs

```json
{
  "denuncia": {
    "id": "WB-2024-0157",
    "fecha_recepcion": "2024-02-06T14:30:00Z",
    "canal": "ESCRITO",
    "anonimato_inicial": true,
    "texto_completo": "El CFO ha instruido falsificar fechas de contrato para reconocer ingresos en Q4 2023...",
    "documentos_adjuntos": [
      "contratos_originales.pdf",
      "correo_CFO_instruccion.pdf",
      "asientos_diario_contables.xlsx",
      "evidencia_firma.pdf"
    ],
    "denunciante": {
      "rol": "Senior Accountant",
      "departamento": "Contabilidad",
      "antiguedad_años": 7,
      "acceso_sistemas": ["SAP", "Contabilidad", "Tesorería"],
      "nivel_salarial": "Middle management",
      "historial_denuncias": "Primera vez"
    }
  },
  "empresa": {
    "cotizacion": "BOLSA_CONTINUA",
    "regulador_principal": "CNMV",
    "empleados_totales": 850,
    "auditoria_externa": "Big Four (Deloitte)"
  }
}
```

---

## Output

```json
{
  "denuncia_id": "WB-2024-0157",
  "clasificacion": {
    "materia_principal": "PENAL - Falsification Docs + Fraud (Art. 290-296, 248 CP)",
    "materias_secundarias": [
      "Administrative - Financial reporting violation (LMV)",
      "Administrative - Market abuse (if intentional disclosure manipulation)"
    ],
    "gravedad": "CRITICA",
    "impacto_inversor": "MATERIAL (affects financial statement reliance)"
  },
  "scoring_detallado": {
    "credibilidad": {
      "puntuacion_global": 71.5,
      "nivel": "ALTA",
      "desglose": {
        "especificidad": {
          "puntos": 29,
          "maximo": 30,
          "detalle": "Detalles concretos: 12 contratos, €75M, fechas específicas, mecanismo claro"
        },
        "documentacion": {
          "puntos": 24,
          "maximo": 25,
          "detalle": "PDFs originales vs. firmadas, memo CFO, cadena emails, asientos contables"
        },
        "coherencia_interna": {
          "puntos": 20,
          "maximo": 20,
          "detalle": "Timeline coherente, incentivos evidentes (bonus CFO), sin contradicciones"
        },
        "posicion_denunciante": {
          "puntos": 15,
          "maximo": 15,
          "detalle": "Senior Accountant con acceso SAP; signante en ajustes de saldo"
        },
        "historial_denunciante": {
          "puntos": 5,
          "maximo": 10,
          "detalle": "Primera vez (baseline 5); no historial previo de denuncias"
        }
      }
    },
    "impacto": {
      "puntuacion_global": 74.2,
      "nivel": "CRITICO",
      "desglose": {
        "gravedad_conducta": {
          "puntos": 30,
          "maximo": 30,
          "categoria": "PENAL (falsificación documentos + fraude)"
        },
        "numero_afectados": {
          "puntos": 24,
          "maximo": 25,
          "alcance": "Sistémico (todos inversores; potencial múltiples años)"
        },
        "dano_economico": {
          "puntos": 20,
          "maximo": 20,
          "cuantia": "€75M ingresos inflados; €500M-€2B pérdida valor si público"
        },
        "dano_reputacional": {
          "puntos": 15,
          "maximo": 15,
          "exposicion": "Media; scandal relevante sector tech; CNMV público"
        },
        "riesgo_legal": {
          "puntos": 10,
          "maximo": 10,
          "exposicion_ejecutiva": "3-8 años cárcel CFO; €5M-€50M CNMV multas"
        }
      }
    },
    "urgencia": {
      "puntuacion_global": 71.6,
      "nivel": "ALTA",
      "desglose": {
        "conducta_continuada": {
          "puntos": 32,
          "maximo": 35,
          "status": "Probablemente ONGOING (Q1 2024 cierre próximo)"
        },
        "evidencia_perecedera": {
          "puntos": 23,
          "maximo": 25,
          "riesgo": "ALTO (Email purges 90d; CFO detectará denuncia → destrucción probable)"
        },
        "seguridad_personas": {
          "puntos": 8,
          "maximo": 25,
          "riesgo_directo": "Bajo (crimen cuello blanco); RIESGO_REPRESALIA moderado-alto"
        },
        "prescripcion": {
          "puntos": 5,
          "maximo": 15,
          "plazo_penal": "5 años (abundante tiempo); urgencia por evidencia"
        }
      }
    },
    "prioridad_global": 72.6,
    "categoria_prioridad": "P0 - ACCION INMEDIATA"
  },
  "timeline_legal": {
    "acuse_recibo": {
      "deadline": "2024-02-13",
      "requiere_confirmacion": true,
      "cumplimiento_obligatorio": "Art. 11.3 Law 2/2023"
    },
    "investigacion_preliminar": {
      "duracion_estimada": "30-45 días",
      "deadline_maxima": "2024-05-06"
    },
    "resolucion_final": {
      "deadline_maxima": "2024-05-06",
      "extension_posible": "30 días adicionales (documentar justificación)"
    },
    "notificacion_cnmv_si_procede": {
      "deadline_desde_determinacion": "10 días hábiles",
      "obligatoria_si": "Violación de ley de mercados valores sustanciada"
    }
  },
  "canales_utilizados_y_compliance": {
    "canal_recibido": "ESCRITO (email a responsable SII)",
    "requisitos_cumplidos": [
      "✓ Escrito (Art. 7 Law 2/2023)",
      "✓ Confidencialidad asegurada",
      "✓ Denunciante identidad protegida inicialmente",
      "✓ Auto-identificación posterior (credibilidad incrementada)"
    ],
    "canales_alternativos_disponibles": [
      "Teléfono anónimo externo (SII tiene hotline tercerizada)",
      "In-person (HR/Compliance)",
      "Denunciar directamente CNMV (external escalation)"
    ],
    "assessment": "Cumple requisitos Law 2/2023 Art. 7-10"
  },
  "proteccion_denunciante": {
    "aplica": true,
    "fundamento": "Art. 36-39 Law 2/2023",
    "protecciones_automaticas": [
      "Confidencialidad identidad (salvo autorización)",
      "Prohibición represalias (Art. 37)",
      "Presunción de retaliation si acción adversa en 12 meses (Art. 39)",
      "Canal follow-up segregado"
    ],
    "medidas_recomendadas": [
      "Notificación escrita: Art. 36-39 protecciones aplican",
      "Monitoreo HR: Flagging de cualquier acción personal relacionada",
      "Documentación de interacciones",
      "Confidentiality Agreement firma (si necesario)"
    ],
    "represalia_prohibida": [
      "Despido, suspensión, degradación",
      "Traslado, disciplina relacionada a denuncia",
      "Acoso, intimidación",
      "Cambio adverso condiciones trabajo"
    ],
    "carga_prueba": "Empleador debe probar causa no-retaliatori si acción dentro 12 meses"
  },
  "responsabilidad_penal_empresarial": {
    "regimen": "Art. 31 bis Código Penal",
    "responsabilidad_cfo": {
      "estatutos_aplicables": [
        "Art. 290-296 CP (Falsificación documentos)",
        "Art. 248 CP (Fraude/Estafa)",
        "Art. 251 CP (Malversación si fondos desviados)"
      ],
      "pena_prevista": "3-6 años cárcel + €300K-€3M multa",
      "inhabilitacion": "3-6 años prohibición ejercer cargos"
    },
    "responsabilidad_empresa": {
      "condicion": "Falta de medidas preventivas a pesar de capacidad organizativa",
      "multa_rango": "€5M-€50M (escala CNMV) o 5-15% ingresos",
      "mitigation_posible": "Acuerdo reparador si plena remediación + compliance enhancement"
    },
    "impacto_stakeholders": "Audit committee, CFO, Board director nivel (si conocimiento)"
  },
  "obligacion_cnmv": {
    "aplica": true,
    "razon": "Empresa cotizada; violación ley mercados valores",
    "trigger": "Determinación de violación tras investigación",
    "deadline": "10 días hábiles desde determinación",
    "contenido_notificacion": [
      "Resumen violación alegada",
      "Períodos contables afectados",
      "Impacto financiero estimado",
      "Estado investigación interna + hallazgos",
      "Medidas remediación en curso"
    ],
    "incumplimiento_sancion": "Multa hasta €3M + responsabilidad personal ejecutivos",
    "resultado_esperado": "CNMV investigación + posible referencia criminal a Fiscalía"
  },
  "acciones_recomendadas": [
    {
      "orden": 1,
      "fase": "INMEDIATA (48 horas)",
      "acciones": [
        "Asignar investigador independiente (counsel externo; privilege attorney-client)",
        "IT forensics: Preservar comunicaciones CFO + logs acceso sistemas contables",
        "Finance team: Extraer archivos contrato Q4 2023 + journal entries",
        "Suspensión laboral CFO (con sueldo; evitar apariencia represalia)",
        "Notificación escrita denunciante: Confirmación protecciones Art. 36-39"
      ],
      "responsable": "Compliance Officer + General Counsel",
      "deadline": "2024-02-07"
    },
    {
      "orden": 2,
      "fase": "CORTO_PLAZO (Days 3-14)",
      "acciones": [
        "Análisis forense contable: Timing contratos vs. reconocimiento ingresos",
        "Auditor externo: Notificación (obligación ética)",
        "Comité Auditoría: Briefing segregado de management",
        "Verificación terceros: Confirmación clientes sobre fechas entrega/servicio",
        "Análisis documentos: Firmas, metadatos, trail de auditoría"
      ],
      "responsable": "Forensic accountant (external) + In-house finance",
      "deadline": "2024-02-20"
    },
    {
      "orden": 3,
      "fase": "INVESTIGACION (Days 15-90)",
      "acciones": [
        "Informe final: Sustanciación o refutación alegaciones",
        "Parecer legal: Aplicabilidad Art. 290-296, 248 CP",
        "Plan remediación: Preparación restatement financiero",
        "Notificación reguladora: Comunicación a CNMV (si violación sustanciada)",
        "Feedback denunciante: Resumen resultados (confidencial)"
      ],
      "responsable": "General Counsel + CFO (replacement) + Audit Committee",
      "deadline": "2024-05-06"
    },
    {
      "orden": 4,
      "fase": "ESCALADA_EXTERNA (If warranted)",
      "acciones": [
        "Referencia criminal: Denuncia a Fiscalía (delitos económicos)",
        "Coordinación CNMV: Investigación conjunta",
        "Auditor externo: Testing de remediación",
        "Ejecución disciplina: Despido CFO + claw-back bonuses",
        "Mejoras control: Segregación de funciones, independencia comité auditoría"
      ],
      "responsable": "General Counsel + Board of Directors",
      "deadline": "Post-investigation (ongoing)"
    }
  ],
  "estimacion_riesgos_reputacionales": {
    "scenario_discovery_public": {
      "media_coverage": "ALTA (tech company + accounting fraud = headlines)",
      "stock_impact": "5-15% drop inicial; recovery 6-12 meses si remediation creíble",
      "investor_confidence": "Material; potential passive fund redemptions",
      "customer_retention": "Bajo riesgo directo (B2B SaaS); reputación marca media"
    },
    "scenario_successful_remediation": {
      "timeline_reputation_recovery": "12-18 meses",
      "cost_audit_enhancement": "€500K-€1M (enhanced controls)",
      "cost_investigation_legal": "€200K-€500K",
      "insurance_claim_possible": "D&O liability cover; deductible typically €250K"
    }
  }
}
```
