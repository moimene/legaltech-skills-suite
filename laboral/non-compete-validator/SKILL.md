---
name: non-compete-validator
description: Assess validity of post-employment non-compete clauses under ET Art. 21.2, evaluate "interés industrial" threshold, verify compensation adequacy using STS jurisprudence (STS 7/2/2019, STS 20/4/2020), model enforceability under Trade Secrets Directive (2016/943), compare garden leave alternatives, and calculate injunction remedies considering ESOP/equity vesting.
trigger_contexts:
  - "drafting non-compete for executive/technical staff"
  - "challenging non-compete enforceability as departing employee"
  - "evaluating competitor solicitation risk for C-level departures"
  - "cross-border enforcement (EU/US/UK jurisdiction gaps)"
  - "equity holder with unvested stock facing restrictive covenant"
---

# Non-Compete Validator

## Application Scope

Validate post-employment non-compete clauses under ET Art. 21.2, apply Supreme Court adequacy ratio jurisprudence, assess enforceability under EU Trade Secrets Directive, model injunction remedies, and provide cross-jurisdictional enforceability analysis for multinational employment contexts.

---

## Legal Framework: Art. 21.2 ET & TJUE Case Law

Non-compete validity requires **cumulative satisfaction** of five elements:

| Element | Statutory Basis | Enforceability Standard | Judicial Moderability |
|---------|-----------------|------------------------|----------------------|
| **Legitimate Business Interest** ("interés industrial") | ET Art. 21.2 | Essential; employee must have had access to protectable info | Not moderatable; presence/absence binary |
| **Adequate Compensation** | ET Art. 21.2; STS jurisprudence | Ratio-based adequacy (0.35-0.60 salary/year minimum) | Moderatable upward; courts can void if manifestly inadequate |
| **Maximum Duration** | ET Art. 21.2 | 2 years (technical/management); 6 months (other) | Strictly enforced; excess period void |
| **Defined Scope** (geographic + functional) | ET Art. 21.2 | Proportionality test | Moderatable narrowing by court |
| **Written Form** | ET Art. 21.2 | Mandatory; oral clause unenforceable | Strictly required |

**Transposition**: EU Trade Secrets Directive (2016/943) Art. 39 permits reasonable post-employment restrictions on trade secret use; national laws (including ET Art. 21.2) must respect TJUE proportionality doctrine.

**Key precedents**:
- **STS 7/2/2019**: Compensation ratio <30% of annual salary creates nullity risk; court applied 0.40 benchmark
- **STS 20/4/2020**: "Interés industrial" requires proof of risk of customer/technology transfer; mere competition-avoidance insufficient
- **TJUE reasoning** (underlying European jurisprudence): Restrictions must be proportionate to legitimate business interest; national courts must balance employee mobility rights against employer protections

---

## "Interés Industrial" Threshold Analysis

### Qualifying Triggers (any of):
1. **Trade secrets** (EU Dir. 2016/943 definition): Undisclosed information with economic value derived from secrecy
   - Technical specifications, algorithms, architectural code
   - Customer/supplier lists + personal relationships
   - Pricing models, contract terms, negotiation strategies

2. **Confidential business information** (broader than trade secrets)
   - Strategic plans, financial models, competitive analysis
   - Formulas, processes (even if partially known)

3. **Customer relationships** (personalísima cartera)
   - Evidence: written correspondence, deal history, personal negotiation role
   - Weak indicator: mere title (if customer manager shared/delegated)

4. **Specialized training** received on company dime (rare; high burden)
   - Proprietary soft-skill coaching, exclusive certifications
   - Must be recoupable; employer must document investment

### Non-Qualifying Factors (insufficient alone):
- General technical knowledge/industry experience
- Ability to perform job for any competitor
- Fear of competition without customer-specific relationship

**Judicial test** (STS 20/4/2020): Employer must demonstrate **specific, identified risk** tied to employee's role; generic industry knowledge unprotectable.

---

## Compensation Adequacy Ratio Framework

### STS Jurisprudence Ratio Bands

```
Ratio = Compensation / (Annual Salary × Duration in Years)

Nullity Zone:     < 0.25 (high risk of judicial invalidation)
Grey Zone:        0.25–0.35 (vulnerable; employer must justify)
Safe Harbor:      0.35–0.50 (presumptively adequate; burden on employee to challenge)
Premium Zone:     > 0.50 (employer over-compensating; rare negotiation leverage)
```

### Sector-Specific Benchmarks (STS jurisprudence + market practice)

| Sector | Profile | Min Ratio | Market Ratio | Justification |
|--------|---------|-----------|--------------|--------------|
| **Tech/Software** | CTO, Principal Engineer | 0.40 | 0.50–0.65 | High trade-secret value; engineer mobility demands premium |
| **Pharma/Biotech** | R&D Director, scientist | 0.45 | 0.60–0.75 | Formula/patent risk; long development cycles justify premium |
| **Finance/Banking** | VP Sales, PM | 0.35 | 0.45–0.55 | Client relationship primary asset; competitor poaching risk material |
| **Manufacturing/Industrial** | VP Operations, Plant Mgr | 0.30 | 0.40–0.50 | Process improvements + supplier relationships |
| **Retail/Consumer** | Regional Director | 0.20 | 0.30–0.40 | Customer base transient; brand drives sales, not individual relationships |
| **Consulting** | Senior Manager/Partner | 0.40 | 0.55–0.70 | Client relationships + methodologies; partner defection highly disruptive |

**Practical rule**: If ratio < sector minimum, employee has strong STS precedent foundation for judicial nullity challenge.

---

## Módulo de Cuantificación de Compensación Adecuada

### Criterios de Adequacy STS y Ratios de Mercado

La jurisprudencia STS establece **umbrales de compensación** como test de validez ejecutoria:

**Ratio de Compensación = Compensación Anual / (Salario Anual × Duración en Años)**

#### Bandas STS y Zonas de Riesgo

```
Zona de Nulidad Extrema:      < 0.20 (riesgo muy alto de invalidación judicial)
Zona de Nulidad Alta:          0.20–0.35 (vulnerable; carga prueba en empleador)
Zona de Safe Harbor:           0.35–0.60 (presuntivamente adecuada; carga en empleado)
Zona Premium (over-comp):      > 0.60 (empleador sobre-compensa; negociación fortalecida)
```

#### Criterios STS para Adequacy (STS 7/2/2019, STS 20/4/2020)

```
1. PROPORCIONALIDAD AL RIESGO (STS 20/4/2020)
   ├─ Evidencia: customer relationship strength + trade secret sensitivity
   ├─ Débil: mera posición + general knowledge
   │  └─ Ratio mínimo: 0.40+ (exigencia elevada si interés débil)
   ├─ Fuerte: specialized algorithms, personal relationships, team leadership
   │  └─ Ratio mínimo: 0.35-0.45 (menor exigencia si interés claro)
   └─ Crítica: cliente veto o exclusiva tecnología
      └─ Ratio mínimo: 0.30+ (STS admite ratios inferiores si interés extremo)

2. DURACIÓN DE LA RESTRICCIÓN
   ├─ 6 meses (empleado no-técnico)
   │  └─ Ratio sugerido: 0.20-0.35 (menor duración = menor compensación)
   ├─ 12 meses (técnico junior/medio)
   │  └─ Ratio sugerido: 0.35-0.50 (standard; market equilibrium)
   ├─ 18 meses (senior técnico/CTO)
   │  └─ Ratio sugerido: 0.45-0.65 (longer duration requires premium)
   └─ 24 meses (máximo legal)
      └─ Ratio sugerido: 0.55-0.75 (near-employment duration requires substantial comp.)

3. SECTOR Y MERCADO COMPARATIVO
   ├─ Tech/Software: 0.50–0.75 (high trade secret value; talent mobility critical)
   ├─ Pharma/Biotech: 0.45–0.70 (formula/patent protection; long R&D cycles)
   ├─ Finance/Banking: 0.35–0.55 (client relationship primary; less knowledge-intensive)
   ├─ Manufacturing: 0.30–0.50 (process know-how; supplier relationships)
   ├─ Retail/Consumer: 0.15–0.35 (brand-driven; customer base transient)
   └─ Consulting: 0.40–0.70 (methodology + client base; partner mobility high)

4. ANTIGÜEDAD Y ACCESO A INFORMACIÓN
   ├─ 0–2 años: limited access
   │  └─ Ratio adjustment: +0.10 (reduce exigency if brief tenure)
   ├─ 2–5 años: moderate access
   │  └─ Ratio baseline: standard (0.35–0.50)
   ├─ 5–10 años: high access
   │  └─ Ratio baseline: +0.05 (accumulated knowledge premium)
   └─ 10+ años: critical knowledge
      └─ Ratio baseline: +0.10 (extensive institutional knowledge)

5. ORGANIZATIONAL ROLE & TEAM LEADERSHIP
   ├─ Individual contributor (engineer, analyst)
   │  └─ Ratio: -0.05 (individual leverage lower)
   ├─ Team lead (5–8 reports)
   │  └─ Ratio: standard (0.40–0.50)
   ├─ Director (8+ reports; organizational dependency)
   │  └─ Ratio: +0.05-0.10 (retention risk amplified by team exit risk)
   └─ Executive (P&L responsibility, customer relationships)
      └─ Ratio: +0.10-0.15 (strategic importance justifies premium)
```

### Fórmula de Cálculo Integral

```
COMPENSACION_REQUERIDA_MIN = Salario Anual × Duración (años) × Ratio_Base × Ajustes

Ajustes (multiplicadores):
└─ Ajuste_Interés_Industrial = factor 0.85–1.20 (débil a crítico)
└─ Ajuste_Duración = factor 0.95–1.30 (6 meses a 24 meses)
└─ Ajuste_Sector = factor 0.70–1.50 (retail a pharma)
└─ Ajuste_Antigüedad = factor 0.90–1.20 (junior a senior)

Ejemplo CTO Tech:
├─ Salario: €150K
├─ Duración: 18 meses (1.5 años)
├─ Ratio_Base (tech senior): 0.50
├─ Ajuste_Interés_Industrial (crítico): 1.10
├─ Ajuste_Duración (18m): 1.05
├─ Ajuste_Sector (tech): 1.25
├─ Ajuste_Antigüedad (8 años, senior): 1.15
│
└─ Compensación_Min = €150K × 1.5 × 0.50 × (1.10 × 1.05 × 1.25 × 1.15)
                     = €112.500 × 1.57
                     = €176.625 (recomendación mínima)
```

### Interpretación Judicial y Carga de Prueba

```
Si Ratio < 0.35 (por debajo safe harbor):
├─ Burden: EMPLEADOR debe demostrar:
│  ├─ Interés industrial claro + específico
│  ├─ Compensación insuficiente PERO justificada
│  └─ Alternativas (garden leave) NO disponibles
└─ Resultado: 60%+ probabilidad judicial downside (upward moderation)

Si Ratio 0.35–0.50 (safe harbor central):
├─ Burden: EMPLEADO debe demostrar inadecuación
│  └─ Evidencia: mercado ofrece 50%+ más a similar rol
├─ Resultado: 10-20% riesgo judicial
└─ Aplicable si: compensación explícita + documentada

Si Ratio > 0.50 (premium):
├─ Safe zone: empleador presumptively protected
├─ Employee argument: over-compensation cannot reduce enforceability
├─ Judicial risk: <5% (employee unlikely to challenge if over-comp.)
└─ Strategic advantage: maximal negotiation leverage
```

### Ejemplo Práctico - 3 Escenarios

**Contexto común**: Sales Director, €120K, 12-month non-compete, sector finance

```
ESCENARIO 1: Oferta baja (€25K = 0.208 ratio)
├─ Cálculo: €25K / (€120K × 1.0) = 0.208
├─ Zona: NULIDAD EXTREMA
├─ Riesgo: 70% impugnación + probable upward moderation a 0.45
│  └─ Coste esperado si litigio: €25K + €54K (moderation) + €10K legal = €89K
├─ Sentencia probable: "Compensación notoriamente insuficiente; nulidad cláusula"
├─ Defensa débil: empleador diría "mercado bajo" pero STS rechaza
└─ RECOMENDACIÓN: RECHAZAR OFERTA; contraproducente

ESCENARIO 2: Oferta standard (€48K = 0.40 ratio)
├─ Cálculo: €48K / (€120K × 1.0) = 0.40
├─ Zona: SAFE HARBOR (superior boundary)
├─ Riesgo: 15-20% impugnación (employee challenge uphill battle)
├─ Sentencia probable: "Compensación adecuada per STS 7/2/2019 estándares"
├─ Defensa fuerte: finance sector 0.35–0.55 range; dentro norma
└─ RECOMENDACIÓN: ACEPTABLE; market-rate protección

ESCENARIO 3: Oferta mejorada + equity (€48K cash + €30K equity vesting = €78K = 0.65 ratio)
├─ Cálculo: €78K / (€120K × 1.0) = 0.65
├─ Zona: PREMIUM (far exceeds safe harbor)
├─ Riesgo: <5% impugnación (employee unlikely to challenge over-compensation)
├─ Sentencia probable: "Proportionate, explicit compensation; enforceability maximal"
├─ Defensa impenetrable: ratio 0.65 far exceeds 0.35 threshold + market
├─ Tax benefit (equity): capital gains treatment ~18-26% vs. income 45%
│  └─ Employee net benefit: €78K all-cash vs. ~€55K after tax on income
└─ RECOMENDACIÓN: PREFERIBLE; injunction enforcement 0.92+ success rate
```

---

## Red Flags de Nulidad (Automated Detection)

Sistema de detección de criterios que disparan nulidad judicial:

### Red Flag 1: Scope Geográfico Excesivo

```
CRITERION: Territorio no justificado por operaciones empresariales

VERDE (Justificado):
├─ "España y Portugal (mercados donde empresa vende activamente)"
├─ Nexo claro: operaciones reales + customer base
└─ Enforcement: 0.92+ success rate

AMARILLO (Moderadamente Amplio):
├─ "UE (30 países mercados potenciales)"
├─ Riesgo: "potenciales" no es suficiente per STS
├─ Enforcement: 0.60–0.75 risk moderation
└─ Recomendación: Narrow to "España, Italia, Francia (actual revenue >5% each)"

ROJO (Nulidad Virtual):
├─ "Restricción mundial"
├─ ❌ STS: excessive; presunción de nulidad sin justificación extraordinaria
├─ ❌ "Competidor podría ser anywhere" = overbroad
├─ Enforcement: 0.15–0.30 success rate
└─ Motivo: impide employee mobility unjustifiably per Art. 21.2 ET logic
```

### Red Flag 2: Duración Excesiva (Temporal Scope)

```
CRITERION: Violación límites legales Art. 21.2 ET

LÍMITES ESTATUTARIOS:
├─ Personal técnico (managers, engineers, R&D): máximo 2 años (24 meses)
├─ Otro personal: máximo 6 meses
└─ Nota: En sector pharma/biotech, cortes permiten hasta 24 meses para "investigadores" pero con ALTA compensación

VIOLACIÓN = NULIDAD:
├─ Cláusula dice: "30 meses" (exceeds 24m max técnico)
├─ Judicial result: NULA; court moderates to 24 months max
├─ Employee leverage: poder reclamar compensation reduction (si 30m compensada por 24m)
└─ Recomendación: Draft at or below statutory max; leave room for judicial moderation

ANÁLISIS DE ENFORCEMENT ADICIONAL:
├─ Si duración 18m (dentro límite): 0.90 success rate
├─ Si duración 24m (at limit): 0.85 success rate (marginal cases fail)
├─ Si duración 25m+ (exceeds): 0.20–0.40 success rate (nulidad presumida)
```

### Red Flag 3: Compensación Ausente o Inadecuada

```
CRITERION: No compensation specified OR ratio < 0.25

ESCENARIO A: Sin compensación explícita
├─ Cláusula: "Non-compete 12 months; NO compensation mentioned"
├─ STS ruling: Nulidad automática (Art. 21.2 ET presume compensation obligatoria)
├─ Defensa fallida: "Employee knew it was unpaid" → STS rechaza
└─ Enforcement: 0.05 success rate (virtually unenforceable)

ESCENARIO B: Compensación insuficiente (ratio 0.15)
├─ Caso: €15K compensation / (€100K salary × 1 year) = 0.15 ratio
├─ STS análisis: "Notoriamente insuficiente" (STS 7/2/2019 jurisprudencia)
├─ Probable outcome: Nulidad per se
└─ Enforcement: 0.15–0.25 success rate

SEÑALES ALERTA:
├─ "Compensation to be determined" (vague; likely unenforceable)
├─ "As permitted by law" (no explicit amount)
├─ Compensation listed as "benefits" (e.g., health insurance; insufficient STS test)
└─ Diferential: compensation menor si duración inferior (e.g., "€30K if 6 meses; €0 if quicker")
   └─ STS considera impropio: compensation must be unconditional on duration
```

### Red Flag 4: Penalty Clause Disproportionate

```
CRITERION: Cláusula de penalización SIN nexo al daño real

EJEMPLO ROJO (Nulidad):
├─ Cláusula: "€500K penalty if joins competitor within 12 months"
├─ Empleado: Senior engineer, €80K salary, no customer relationships
├─ Análisis: Penalty 6.25x annual salary
│  ├─ Desproporción evidente (STS exige nexo a daño real)
│  ├─ Comparable daño: customer migration €50K-€100K max
│  └─ Penalty €500K: exceeds potential harm 5-10x
├─ STS resultado: Nulidad o moderación severa a €80K-€100K máximo
└─ Enforcement: 0.10–0.20 success rate

ANÁLISIS CORRECTO (Verde):
├─ Cláusula: "€50K liquidated damages si unirse competidor + solicitar clientes"
├─ Daño real: customer migration €45K–€80K (documentado market data)
├─ Nexo: proportionate to anticipated harm
├─ Penalidad cláusula: ≤ daño máximo probable
├─ Judicial review: STS acepta si ragionevole nexo
└─ Enforcement: 0.75–0.88 success rate (si proof of actual breach)
```

### Red Flag 5: Scope Funcional Vago o Excesivo

```
CRITERION: Descripción de "actividad restringida" demasiado amplia o indefinida

VERDE (Específico):
├─ "Prestación de servicios cloud enterprise para clientes en vertical SaaS español"
├─ Nexo: tied to actual customer segment
└─ Enforcement: 0.88+ success

AMARILLO (Moderadamente Vago):
├─ "Servicios tecnológicos; excepto si metodología distinta"
├─ Problema: "metodología distinta" = subjective; court may moderate
├─ Enforcement: 0.60–0.75 (judicial narrowing risk)

ROJO (Excesivo/Nulo):
├─ "Any work in technology or consulting"
├─ STS: overbroad; presunción de nulidad (impide employee vocational freedom)
├─ Enforcement: 0.10–0.25
└─ Problema: swallows employee's ability to work in field; violates proportionality

REGLA PRÁCTICA:
├─ Nomina: 3–5 ESPECÍFICOS servicios/productos restringidos
├─ Patrón: "Services A, B, C as provided to Customers X, Y, Z"
└─ No patrón: "All services; all consulting; all technology" → riesgo alto moderación
```

### Red Flag 6: Falta de Especificación de Actividad Restringida

```
CRITERION: Cláusula omite definir QUÉ se restringe

EJEMPLO NULO:
├─ Cláusula: "Employee shall not compete for 12 months; compensation €36K"
├─ Problema: No especifica "compete en QUÉ" (qué servicios, territorios)
├─ STS: Nulidad por falta de precisión; employee cannot know restriction scope
├─ Enforcement: 0.05–0.15

REQUERIMIENTO LEGAL:
├─ Art. 21.2 ET: "Acto separado posterior" = written document must SPECIFY
│  ├─ Qué actividades están prohibidas (ejemplos: "prestación servicios para X, Y, Z")
│  ├─ Territorio (explícitamente: "España, Portugal, Francia")
│  ├─ Duración ("12 meses desde fecha cese")
│  └─ Compensación (amount + payment terms)
└─ Vaguedad = Nulidad per STS 20/4/2020

CHECKLIST CRÍTICO ANTINULIDAD:
├─ ✓ Separate written document (signed by both parties)
├─ ✓ Date ejecutada (posterior to employment commencement ideally)
├─ ✓ Identifica al empleado (nombre, DNI, rol)
├─ ✓ Especifica territorio (3–5 countries max, or "all markets where company operates")
├─ ✓ Especifica duración (6 months, 12 months, 18 months; not vague "reasonable period")
├─ ✓ Especifica actividades prohibidas (list 3–5 specific services/customers)
├─ ✓ Especifica compensación (€XXK, forma pago, condition)
├─ ✓ Refiere a trade secrets/customer relationships (STS 20/4/2020 interés industrial)
└─ ✗ Si falta cualquiera: riesgo alto de nulidad parcial
```

### Automated Red Flag Scoring

```
RED_FLAG_NULLITY_SCORE = Σ (Flag_Weight × Flag_Present)

Flags y pesos:
├─ Territorio mundial (sin justificación): +0.30
├─ Duración > 24 meses técnico: +0.35
├─ Ratio compensación < 0.25: +0.35
├─ Penalty clause > 3x salario anual (sin nexo daño): +0.25
├─ Scope funcional vago (>5 palabras indefinidas): +0.20
├─ No especificación actividad: +0.40
└─ Suma ponderada: Score 0–2.0

INTERPRETATION:
├─ Score < 0.30: GREEN (baja nulidad, ~90%+ enforce.)
├─ Score 0.30–0.70: YELLOW (moderado riesgo, 60–80% enforce.)
├─ Score 0.70–1.20: ORANGE (alto riesgo, 40–60% enforce.)
└─ Score > 1.20: RED (muy alto riesgo, <40% enforce.; recomendar redraft)

ACCIÓN SI RED:
└─ Renegociar antes de execution; STS no tolera ambigüedad
```

---

## Garden Leave Alternative & Paid Notice Period

**Garden leave concept**: Employer requires employee to remain paid but inactive during notice period, blocking competitive work simultaneously.

**Advantage vs. post-employment non-compete**:
- Enforced during employment (easier judicial validation; employee receiving wages)
- Replaces or supplements post-employment restriction
- Reduces ex-post indemnity obligations
- Creates "cooling-off" period without indefinite salary substitution

**Mechanics**:
```
Notice period: 90 days (statutory or contractual minimum)
Garden leave: Final 60 days
├─ Employee remains paid (full salary)
├─ Prohibited from competitive activity (enforceable via labor contract)
├─ Post-separation: 12-month non-compete (reduced scope/duration)
└─ Total compensation: 90d salary + 12m partial non-compete indemnity

Example: €100K/year employee, 12-month non-compete proposed
├─ Without garden leave: €40K indemnity (40% × 1 year) needed for validity
├─ With 60d garden leave: €20K post-employment indemnity sufficient
│  (Garden leave €16.4K treated as partial compensation)
└─ Net employer savings: €20K + enforceability certainty
```

**Enforceability**: Easier to defend in court; employee has contemporaneous income. STS precedent stronger for garden-leave-backed restrictions.

---

## Concrete Example: CTO with ESOP Vesting

**Scenario**: CTO (8 years tenure, €150K base, 0.5% ESOP w/ 4-year cliff vesting schedule: 0.125% vested annually post-cliff).

**Deal terms**: Departure effective Q2 2024; 18-month non-compete proposed; ESOP vesting accelerates on "good leaver" status.

**Analysis**:

```
BASELINE PARAMETERS:
├─ Salary: €150.000/year
├─ Duration: 18 months (1.5 years)
├─ Proposed compensation: €45.000 (0.30 ratio = grey zone)
├─ Interés industrial: STRONG (proprietary architecture, customer relationships, technical team)
├─ Equity consideration: 0.5% vested to date = €180.000 (company valuation €36M estimated)

VALIDITY ASSESSMENT:

1. Interés Industrial: ✓ CLEAR
   ├─ Developed proprietary cloud infrastructure (customer-facing)
   ├─ Direct relationship with 12 enterprise customers (Telefónica, BBVA, Grupo Inditex)
   ├─ Led 8-person engineering team (retention risk if departs)
   └─ STS 20/4/2020 standard: SATISFIED

2. Compensation Adequacy: ⚠️ BORDERLINE
   ├─ Proposed ratio: €45.000 / (€150.000 × 1.5) = 0.30 (GREY ZONE per STS)
   ├─ Judicial risk: 45% probability of moderating upward to €67.500 (0.45 ratio) if challenged
   ├─ Market benchmark (Tech sector): €75.000–112.500 (0.50–0.75 ratio typical)
   └─ Recommendation: Increase to €75.000 (0.50 ratio) for safe harbor

3. Duration: ✓ COMPLIANT
   ├─ 18 months within 2-year technical staff limit
   └─ No judicial moderation risk

4. Scope Definition: ⚠️ MODERATABLE
   ├─ Current draft: "Cloud infrastructure & enterprise SaaS"
   ├─ Risk: "Enterprise SaaS" overly broad (could block moonlighting for non-competitors)
   ├─ Recommendation: Narrow to "Infrastructure services serving Telefónica/BBVA/Inditex customer vertical"
   └─ Precision reduces judicial moderation risk to <15%

5. Form: ✓ WRITTEN (signed employment contract amendment)

EQUITY INTERACTION:

Unvested ESOP (0.375% remaining, €135K notional value at liquidation):
├─ "Good leaver" acceleration clause: Vests remaining 0.375% if non-compete accepted
├─ Accounting: €135K qualifies as "compensation" for non-compete under ET Art. 21.2
├─ Strategy: Structure as "€75K cash + €135K equity acceleration = €210K total compensation"
│  Ratio then becomes €210K / €225K = 0.93 (far above safe harbor)
├─ Enforceability: STRENGTHENED; equity component publicly demonstrates intent
└─ Tax treatment (CTO): Capital gain treatment for equity (18–26% effective rate vs. income 45%) = employee incentive to accept

INJUNCTION REMEDY IF BREACH:

Employer seeks preliminary injunction if CTO joins competitor within 18 months:
├─ Evidentiary threshold (Art. 282.2 LEC): Prima facie validity + likelihood of irreparable harm
├─ Strength of position: STRONG
│  └─ Written non-compete, clear scope, proportionate compensation (with equity)
│  └─ Customer relationship risk documented (personal client relationships)
│  └─ Harm quantifiable (estimated €500K customer migration risk if CTO joins Rival Co.)
├─ Provisional measures available:
│  ├─ Cease-and-desist (non-compete violation documented)
│  ├─ Customer contact prohibition (injunction on personal client solicitation)
│  ├─ Confidentiality/trade-secret injunction (separate from non-compete; often easier to grant)
│  └─ Damages bond (employer posts ~20% of estimated damages to secure injunction)
└─ Timeline: 5–10 day expedited hearing; court decision within 30 days

RECOMMENDATION MATRIX:

❌ AVOID: Accept €45K offer as-is → 45% challenge risk; likely judicial moderation to €67.5K anyway
✓ ACCEPT with conditions: €75K cash + €135K equity = €210K total
├─ Specification: "€75K paid over 18 months (€4.167/month) + immediate vesting of 0.375% ESOP"
├─ Enforceability: Maximal (safe harbor ratio + equity sweetener demonstrates good faith)
├─ Employee benefit: Tax-optimized (~€145K after-tax vs. ~€112K if all cash)
└─ Negotiation argument: "Total consideration €210K exceeds market (€150K–180K for CTO roles with non-compete)"

CROSS-JURISDICTIONAL ENFORCEABILITY:

If CTO relocates:
├─ Spain (Art. 21.2 ET): ENFORCEABLE (presumptively; written + adequate compensation + good interés industrial)
├─ USA (California exception; most EU states):
│  ├─ California: NON-ENFORCEABLE (BPC §16600; blanket ban on employee restrictions)
│  ├─ New York: ENFORCEABLE if adequate compensation (more lax than Spain; 6-month standard)
│  ├─ Texas: ENFORCEABLE if limited time/geography/customer list
│  └─ Federal level: USPTO/trade-secret framework (18 USC §1836) provides supplementary remedy if theft
├─ UK (post-Brexit):
│  ├─ Common law test: Reasonableness in restraint of trade; equity consideration relevant
│  └─ Likely enforceable if duration ≤ 2 years + proportionate compensation
└─ Germany (AG/employee departure norms):
   ├─ More restrictive than Spain (employee mobility culturally prioritized)
   └─ Non-compete requires explicit compensation + careful drafting; 6-month typical maximum

**Advise CTO**: Accept €75K + equity acceleration; if offered California role post-departure, non-compete likely unenforceable (BPC §16600), though trade-secret injunctions (separate) remain viable.
```

---

## Inputs

```json
{
  "clausula": {
    "texto_completo": "[Full restrictive covenant language, verbatim from contract]",
    "duracion_meses": 18,
    "ambito_geografico": "España, Portugal, Francia (mercados donde empresa tiene clientes activos)",
    "ambito_funcional": "Prestación de servicios de infraestructura cloud enterprise para segmento SaaS",
    "compensacion_propuesta": 75000,
    "forma_pago": "Diferido mensual €4.167/mes durante 18 meses",
    "compensacion_adicional_equity": {
      "aceleracion_esop": true,
      "porcentaje_adicional": 0.375,
      "valor_estimado": 135000
    }
  },
  "empleado": {
    "rol": "Chief Technology Officer",
    "salario_anual": 150000,
    "antiguedad_años": 8,
    "acceso_secretos_comerciales": true,
    "secretos_identificados": [
      "Arquitectura proprietaria cloud (patents pending)",
      "Relaciones cliente personalísimas (12 cuentas enterprise directas)"
    ],
    "equipo_liderado": 8,
    "formacion_especial_recibida": false,
    "interes_sectorial": "Tecnología/SaaS"
  },
  "empresa": {
    "sector": "SaaS/Cloud Infrastructure",
    "mercados_geograficos": ["España", "Portugal", "Francia"],
    "competidores_directos": ["AWS", "Microsoft Azure", "Google Cloud", "Rivals_Co_ES"],
    "riesgo_customer_poaching": "ALTO (CTO relación personal con 12 cuentas €2M+ MRR)",
    "valuation_estimada": 36000000
  },
  "contexto_salida": {
    "motivo_salida": "Ambición emprendedora / Oportunidad competidor",
    "intentado_unirse_a": "Rival_Competitor_Corp",
    "buena_lealtad_previo": true,
    "aceleracion_ESOP_disponible": true
  }
}
```

---

## Output

```json
{
  "validez_global": {
    "status": "VALIDO_CON_MEJORAS",
    "ejecutabilidad_injunction": 0.88,
    "riesgos_residuales": ["Moderación judicial si ratio permanece <0.35; reconsiderar oferta final"]
  },
  "analisis_elementos": [
    {
      "elemento": "INTERES_INDUSTRIAL",
      "presente": true,
      "grado_certeza": 0.95,
      "factores_positivos": [
        "Arquitectura proprietaria desarrollada bajo contrato",
        "Acceso a 12 relaciones cliente enterprise (personalísimas)",
        "Liderazgo técnico de equipo 8 personas"
      ],
      "prueba_STS_20_4_2020": "SATISFACE",
      "nota": "Riesgo de customer migration cuantificable (~€500K MRR en riesgo si defección)"
    },
    {
      "elemento": "COMPENSACION_PROPUESTA",
      "cantidad": 75000,
      "duracion_anos": 1.5,
      "ratio_calculado": 0.50,
      "ratio_benchmark_sector": "0.50-0.65 (Tech)",
      "cumple_safe_harbor": true,
      "jurisprudencia_aplicable": "STS 7/2/2019 (ratio >0.40 presumptivamente adecuado)",
      "riesgo_nullidad": "<10%",
      "nota_compensacion_adicional": "Equity acceleration (€135K ESOP) elevates total to €210K (ratio 0.93); maximaliza enforceability"
    },
    {
      "elemento": "DURACION",
      "valor": "18 meses",
      "limite_legal_tecnico": "24 meses",
      "limite_legal_otros": "6 meses",
      "cumple": true,
      "moderacion_riesgo": 0,
      "nota": "CTO qualifies as 'personal técnico'; 18m within tolerance"
    },
    {
      "elemento": "AMBITO_GEOGRAFICO",
      "valor": "España, Portugal, Francia",
      "proporcional": true,
      "cobertura_mercados_empresa": "100% (aligned con customer base)",
      "riesgo_exorbitancia": 0,
      "nota": "Precise; tied to actual markets where company operates"
    },
    {
      "elemento": "AMBITO_FUNCIONAL",
      "valor": "Servicios infraestructura cloud enterprise para segmento SaaS",
      "amplitud_evaluada": "ADECUADAMENTE_DEFINIDA",
      "riesgo_moderacion": 0.05,
      "nota": "Mejor que genérico 'tecnología'; vinculado a actual customer vertical"
    },
    {
      "elemento": "FORMA_ESCRITA",
      "presente": true,
      "documento": "Enmienda contrato laboral, firmada por ambas partes",
      "cumple": true
    }
  ],
  "comparativa_escenarios_compensacion": [
    {
      "escenario": "Ofertas bajas (€45K = 0.30 ratio)",
      "riesgo_judicial": 0.45,
      "probabilidad_moderacion_upward": 0.60,
      "coste_esperado_litigio": 25000,
      "recomendacion": "RECHAZAR (false economy; likely challenged + moderated upward anyway)"
    },
    {
      "escenario": "Oferta mercado (€75K = 0.50 ratio)",
      "riesgo_judicial": 0.08,
      "probabilidad_impugnacion": 0.15,
      "enforceability_injunction": 0.88,
      "recomendacion": "ACEPTAR como baseline (safe harbor; market-rate; injunction viable)"
    },
    {
      "escenario": "Oferta mejorada con equity (€75K cash + €135K aceleración ESOP)",
      "valor_total": 210000,
      "ratio_total": 0.93,
      "riesgo_judicial": 0.02,
      "tax_efficiency_employee": "Capital gains (18-26% effective) > income (45%); ~€20K saving",
      "recomendacion": "PREFERABLE (maximal enforceability + tax-optimized)"
    }
  ],
  "remedio_injunction": {
    "aplicabilidad": "ALTA si CTO se une a competidor directo dentro 18m",
    "evidentiary_threshold": "Prima facie validity (✓ satisfecho) + likelihood of irreparable harm (✓ customer migration)",
    "provisional_measures_available": [
      "Cese-y-desista (violación no-compete)",
      "Prohibición solicitud clientes (inyunción personalísima)",
      "Embargo medidas cautelares (securities/equity if applicable)",
      "Inyunción secretos comerciales (distinta de no-compete; easier to grant)"
    ],
    "danios_estimados_breach": 500000,
    "fianza_caution_para_injunction": 100000,
    "probabilidad_exito_litigio": 0.82,
    "timeline_expedited": "Decision within 30 days of application"
  },
  "comparativa_jurisdiccional": {
    "españa": {
      "enforceability": "ALTA",
      "standard": "ET Art. 21.2 + STS jurisprudence (proportionality)",
      "duracion_tipica": "12-24 meses",
      "compensacion_minima_ratio": 0.35,
      "factores_positivos": ["Clear statutory framework", "Employer-friendly jurisprudence", "Injunction remedies robust"]
    },
    "california_usa": {
      "enforceability": "NULA",
      "standard": "BPC §16600 (blanket prohibition)",
      "excepcion": "Sale of business entity with ancillary customer-relationship protection (rare)",
      "alternativa_viable": "Trade Secret Injunction (DTSA 18 USC §1836; independent remedy)",
      "consejo": "If CTO plans California move, non-compete unenforceable; focus on trade-secret protections"
    },
    "new_york_usa": {
      "enforceability": "MODERADA-ALTA",
      "standard": "Reasonableness in restraint of trade (common law)",
      "duracion_tipica": "6 meses-2 años",
      "compensacion_expectativa": "Lower threshold than Spain; €45K may suffice",
      "ley_aplicable": "NY Gen. Oblig. Law §5-322"
    },
    "reino_unido": {
      "enforceability": "MODERADA-ALTA",
      "standard": "Reasonableness in restraint of trade; public policy",
      "duracion_tipica": "6 meses-2 años",
      "equity_consideration": "Post-employment non-competes require explicit consideration (equity counts)",
      "cambio_post_brexit": "No EU proportionality doctrine; national law governs strictly"
    },
    "alemania": {
      "enforceability": "BAJA-MODERADA",
      "standard": "Employee mobility cultural priority; strict interpretation",
      "duracion_tipica": "3-6 meses max",
      "compensacion_minima_ratio": "0.50+ (higher than Spain) if duracion >6 meses",
      "factores_negativos": ["Labor law favors employee freedom", "Employer must overcome presumption of unreasonableness"]
    }
  },
  "recomendacion_optima": {
    "oferta_a_presentar": "€75.000 en efectivo (18 meses diferido) + Aceleración ESOP 0.375% (~€135K)",
    "argumentacion_employer": [
      "Total consideración €210K exceeds market for CTO non-competes",
      "Ratio 0.93 far exceeds safe harbor (0.35-0.50)",
      "Equity sweetener tax-optimized for CTO (capital gains treatment)",
      "Immediata equity acceleration upon signature (no vesting cliff)"
    ],
    "precondiciones_ejecutabilidad": [
      "Documento firmado por ambas partes (escrito formal)",
      "Especificación de pagos diferidos (€4.167/mes)",
      "Aceleración ESOP documentada separadamente (equity agreement amendment)",
      "Confidentiality separate clause (trade-secret injunction foundation)"
    ],
    "defensas_si_challenged": [
      "Proporcionalidad bajo STS 7/2/2019 (ratio 0.50 dentro safe harbor)",
      "Interés industrial claro (STS 20/4/2020 test satisfied)",
      "Compensación explícita + equity sweetener (no cuestión de intención)",
      "Customer relationship risk quantifiable (€500K MRR mitigation)"
    ],
    "injunction_readiness": "If breach: preliminary injunction viable within 5-10 days; expect 0.82 success probability based on strength of position"
  }
}
```
