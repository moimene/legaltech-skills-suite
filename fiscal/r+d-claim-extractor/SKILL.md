---
name: r+d-claim-extractor
description: Identify eligible R&D expenses for Informe Motivado Vinculante (IMV) process under Art. 35 LIS. Classify activities per Frascati Manual guidelines (Research vs. Technological Innovation), analyze CDTI certification eligibility, extract deductible base from invoices, payroll, and timesheets using DEMPE labor allocation. Calculate tax relief (25-42% I+D rate, 12% IT rate), apply working capital adjustments, test patent box interaction (Art. 23 LIS), and assess bonus deducciones (incremental 10% threshold). Applicable for R&D tax claim optimization, IMV pre-filing analysis, audit defense, and R&D portfolio planning.
---

# R+D Claim Extractor

---

## Application Topology

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Invoices,        │───▶│ Frascati Manual  │───▶│ Research (I) vs  │
│ Payroll,         │    │ Classification   │    │ Tech Innovation  │
│ Timesheets       │    │ per DEMPE        │    │ (IT) Assessment  │
└──────────────────┘    └──────────────────┘    └────────┬─────────┘
                                                        │
                                                        ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Informe Motivado │◀───│ Patent Box &     │◀───│ IMV Analysis:    │
│ Vinculante (IMV) │    │ Bonus Deductions │    │ CDTI certification
│ & Tax Deduction  │    │ (Art. 35.2 LIS)  │    │ & Incremental %   │
│ Report           │    │                  │    │ Testing (10%)     │
└──────────────────┘    └──────────────────┘    └──────────────────┘
```

---

## Trigger Contexts

- Filing Informe Motivado Vinculante (IMV) for R&D tax certainty
- Preparing R&D deduction claim in corporate income tax return (Impuesto Sociedades)
- Optimizing R&D portfolio under patent box regime (Art. 23 LIS nexus approach)
- Responding to inspección challenges on R&D classifications
- Evaluating CDTI certification process (Centro para el Desarrollo Tecnológico)
- Testing bonus deducciones eligibility (incremental 10% spend threshold)

---

## Tax Deduction Categories per Art. 35 LIS

### I+D (Research & Development)

**Definition (Frascati Manual)**: Planned original activity to obtain new scientific or technological knowledge. Must demonstrate technological uncertainty and systematic approach.

| Deduction Rate | Criterion |
|---|---|
| **25%** | Base eligible expenditure (general rate) |
| **42%** | Incremental bonus if R&D spend increases >10% vs. 2-year average |
| **+17%** | Additional bonus for exclusive research personnel (doctores, investigadores) |
| **8% additional** | Subcontracting to universities or public research centers |

**Key**: Research component must satisfy OECD/BEPS guidelines. No mere routine engineering. Evidence: technical reports, lab notebooks, patent applications.

### Innovación Tecnológica (IT - Technological Innovation)

**Definition (Art. 35 LIS)**: Obtaining new or substantially improved products or processes. Uncertainty exists but lower than I+D; must be beyond standard engineering/implementation.

| Deduction Rate | Criterion |
|---|---|
| **12%** | Base eligible expenditure (general rate) |
| **N/A** | No incremental bonus available for IT-only activities |

**Frascati Test**: If activity fails Frascati I+D criteria (e.g., no genuine R&D, purely market-driven), classifies as IT. If fails IT test (routine engineering), non-deductible.

---

### Comparability Matrix: Frascati I+D vs. IT vs. Non-Eligible

| Criterion | I+D (Research) | IT (Innovation) | Non-Eligible |
|---|---|---|---|
| **Novelty** | Original; not in market | New/improved; market exists | None; standard practice |
| **Uncertainty** | High (technical risk unresolved) | Medium (application uncertain) | None; known solution |
| **Systematicity** | Documented, planned | Planned project | Reactive, ad-hoc |
| **Transferability** | Generates reproducible knowledge | Proprietary process/product | Internal-only routine |
| **Deduction** | 25-42% + bonuses | 12% fixed | 0% |

---

## Eligible Expense Categories (Art. 35 LIS with DEMPE Labor Methodology)

| Category | Examples | Eligibility Rules | DEMPE Test |
|---|---|---|---|
| **Personnel - I+D** | PhDs, researchers, engineers (R&D focus) | 100% of salary × allocation % | Development, Enhancement, Maintenance functions |
| **Personnel - IT** | Developers, technicians (innovation focus) | 100% of salary × allocation % | Exploitation, minor Protection functions |
| **Materials & Supplies** | Prototype components, test samples, consumables | 100% if consumed in R&D project | Must be project-specific, traceable |
| **Subcontracting (Universities)** | Research contracts, pilot studies | 100% (no cap, LIS Art. 35) | Enhancement via academic collaboration |
| **Equipment Depreciation** | Lab instruments, specialized machinery | Proportional to R&D use (time allocation) | Must be R&D-specific; full depreciation for dedicated equipment |
| **Patent & IP** | Patent filing, prosecution, defense fees | IT only; NOT I+D under LIS | Protection function (Art. 23 patent box interaction) |
| **Certifications** | ISO certifications, CE marking, quality assurance | IT only; NOT I+D under LIS | Market-driven certification, not research |
| **Outsourced R&D** | Consulting firms, contract research | 100% for eligible services | Must verify subcontractor is truly performing R&D |

**DEMPE Labor Allocation**: For personnel, allocate salary based on documented time allocation (timesheets, project budgets) across Development, Enhancement, Maintenance, Protection, Exploitation functions.

---

## Input Data

```json
{
  "ejercicio_fiscal": 2024,
  "imv_solicitado": true,
  "proyectos": [
    {
      "nombre": "Desarrollo motor IA ML v2",
      "clasificacion_propuesta": "I+D",
      "descripcion_tecnica": "Algoritmo ML para predicción de comportamiento usuario; incertidumbre técnica en convergencia modelo",
      "fecha_inicio": "2024-01-01",
      "fecha_fin": "2024-12-31",
      "frascati_criteria": {
        "novedad": "Originality in algorithm design (published research incorporated)",
        "incertidumbre_tecnica": "Model optimization path unknown; multiple convergence scenarios tested",
        "sistematicidad": "Documented lab-notebook approach; monthly technical reviews",
        "transferibilidad": "Knowledge base for future projects; reproducible methodology"
      }
    }
  ],
  "fuentes_datos": [
    {"tipo": "facturas_proveedor", "path": "/facturas_2024/", "formato": "PDF/XML"},
    {"tipo": "nominas_rrhh", "path": "/rrhh/nominas_2024.csv", "formato": "CSV"},
    {"tipo": "timesheet_proyecto", "path": "/proyectos/dedicacion_2024.csv", "formato": "CSV"},
    {"tipo": "informes_tecnicos", "path": "/tech_reports/2024/", "formato": "PDF"}
  ],
  "cdti_certification": {
    "solicitado": false,
    "recomendacion": "Solicitar CDTI certification para mayor seguridad jurídica; plazo 6-9 meses"
  },
  "bonus_deduction_testing": {
    "r_d_spend_2023": 420000,
    "r_d_spend_2022": 380000,
    "media_2ano_base": 400000,
    "r_d_spend_2024_propuesto": 450000,
    "incremento_porcentaje": 12.5,
    "cumple_10_pct_threshold": true,
    "bonus_deduction_aplicable": true
  }
}
```

---

## Output & Deduction Calculation

```json
{
  "ejercicio_fiscal": 2024,
  "resumen_ejecutivo_deduccion": {
    "base_i_d_eligible": 450000,
    "base_it_eligible": 120000,
    "deduccion_calculada": {
      "i_d_base_25pct": 112500,
      "i_d_bonus_incremental_17pct": 76500,
      "i_d_personal_investigador_25pct": 38250,
      "it_12pct": 14400,
      "total_deduccion_anual": 241650
    },
    "cuota_integra_estimada_2024": 500000,
    "limite_deduccion_15pct_cil": 75000,
    "deduccion_aplicable_2024": 75000,
    "exceso_pendiente_carryforward": 166650
  },
  "proyectos_detallados": [
    {
      "nombre": "Desarrollo motor IA ML v2",
      "clasificacion_final": "I+D",
      "confianza_clasificacion": 0.94,
      "frascati_scoring": "4/4 Frascati criteria met",
      "justificacion_brevis": "Original ML architecture; technical uncertainty in model convergence; systematic documentation; reproducible methodology for future projects",
      "gastos_elegibles_desglosados": {
        "personal": {
          "importe_total": 320000,
          "detalles": [
            {"empleado": "Juan García (PhD)", "rol": "Researcher", "dedicacion": "80%", "coste": 64000, "bonus_investigador": true},
            {"empleado": "María López (Dev)", "rol": "Developer", "dedicacion": "60%", "coste": 36000, "bonus_investigador": false},
            {"empleado": "Carlos Ruiz (QA)", "rol": "QA", "dedicacion": "40%", "coste": 22000, "bonus_investigador": false}
          ]
        },
        "materiales": {"importe": 45000, "items": ["Cloud computing (AWS)", "Data labeling", "Testing tools"]},
        "subcontratacion_universidad": {"importe": 85000, "beneficiario": "UPM", "bonus_8pct": 6800},
        "amortizacion_equipos": {"importe": 12000, "equipo": "GPU cluster", "dedicacion_r_d": "80%"}
      },
      "total_gastos_brutos": 462000,
      "ajustes": [
        {"tipo": "QA partial dedication", "reduccion": 8000},
        {"tipo": "Cloud computing non-R&D portion", "reduccion": 4000}
      ],
      "base_elegible_i_d": 450000,
      "deduccion_proyecto_i_d": 229650
    },
    {
      "nombre": "Mejora Plataforma UI/UX",
      "clasificacion_propuesta": "IT",
      "frascati_scoring": "2/4 (not genuine R&D)",
      "base_elegible_it": 39000,
      "deduccion_proyecto_it": 4680
    }
  ],
  "soporte_documentacion": {
    "informe_tecnico_i_d": {
      "status": "REQUERIDO para I+D",
      "contenido_minimo": ["Descripción proyecto", "Incertidumbre técnica", "Metodología", "Resultados/deliverables"],
      "responsable": "R&D Director + Technical Lead"
    },
    "registros_cumplimiento": {
      "timesheets": "Monthly project allocation (GDPR-compliant)",
      "lab_notebooks": "Technical documentation (GitHub repos)",
      "facturas": "Vendor invoices with R&D project reference"
    },
    "certificaciones_valor": [
      {
        "certificacion": "CDTI Certification (Centro para el Desarrollo Tecnológico e Industrial)",
        "beneficio": "Greater legal certainty; 6-month processing",
        "coste": "EUR 500-1000 (administrative fee)",
        "recomendacion": "SOLICITAR para evitar disputas en inspección"
      }
    ],
    "informe_motivado_vinculante_imv": {
      "status": "RECOMENDADO",
      "razon": "IMV provides 3-year legal certainty on R&D classification",
      "proceso": "Pre-file with Tax Authority; binding ruling",
      "plazo": "3-6 months for resolution",
      "riesgo_si_no_imv": "High audit risk; inspección can re-classify projects"
    }
  },
  "patent_box_interaction": {
    "articulo": "Art. 23 LIS (Patent Box - Nexus Approach)",
    "interaccion": "R&D base eligible for standard deduction (Art. 35) AND patent box qualifying income (if patents filed)",
    "cuidado": "Do NOT double-dip: R&D deduction reduces CIL; patent box applies to qualifying income separately",
    "ejemplo": "If EUR 450k I+D → EUR 112.5k deduction → EUR 337.5k taxable. If patents generate licensing income → Apply patent box nexus (80% adjusted income) to licensing revenue."
  },
  "bonus_deducciones_incrementales": {
    "art_35_2_lis": "Incremental bonus deduction for R&D spend growth",
    "criterio": "If R&D spending increases >10% vs. 2-year average",
    "calculo": {
      "r_d_2022": 380000,
      "r_d_2023": 420000,
      "media_2_anos": 400000,
      "r_d_2024_propuesto": 450000,
      "incremento": 50000,
      "incremento_porcentaje": 12.5,
      "cumple_umbral_10_pct": true,
      "bonus_aplicable": true,
      "tasa_bonus": "17% incremental (adicional a 25% base)"
    },
    "quantificacion": {
      "base_elegible_incremental": 50000,
      "bonus_17_pct": 8500,
      "nota": "Bonus applies ONLY to incremental R&D spend, not base"
    }
  },
  "alertas_compliance": [
    {"alerta": "Technical documentation incomplete - file IMV before tax deadline", "prioridad": "ALTA"},
    {"alerta": "CDTI Certification recommended for legal certainty (3-year safe harbor)", "prioridad": "MEDIA"}
  ]
}
```

---

## Example: Fintech ML Credit Scoring R&D

**Facts**: Fintech develops ML model for credit risk (I+D). 2 PhDs (EUR 160k), AWS EUR 30k, data labeling EUR 45k, GPU depreciation EUR 12k. ISO 27001 test (EUR 8k) NOT eligible.

**Frascati Test**: 4/4 → I+D classification. Total base: EUR 247k. Deduction: (EUR 247k × 25%) + (EUR 160k × 17%) = EUR 88,950. Tax relief: ~EUR 22,237 @ 25% rate.

---

## Frascati Manual Classification Test (Decision Tree)

```
1. Is activity aimed at developing NEW scientific/technical knowledge?
   → NO: Go to Non-Eligible
   → YES: Go to 2

2. Is there GENUINE UNCERTAINTY about technical approach/outcome?
   → NO: Go to Non-Eligible or IT
   → YES: Go to 3

3. Is activity SYSTEMATICALLY DOCUMENTED & PLANNED?
   → NO: Go to Non-Eligible
   → YES: Go to 4

4. Does activity generate REPRODUCIBLE/TRANSFERABLE KNOWLEDGE?
   → NO: Go to IT
   → YES: → I+D CLASSIFICATION (25-42% deduction)

Non-Eligible → 0% deduction
IT → 12% deduction
I+D → 25-42% deduction (with bonuses)
```

---

---

## Requisitos Formales: Informes Motivados Vinculantes (IMV)

### Procedimiento de Obtención IMV desde MINECO

El Informe Motivado Vinculante (IMV) es una resolución previa que vincula a AEAT sobre clasificación R+D/IT:

```
PROCEDIMIENTO IMV:
══════════════════

PASO 1: PRE-PROJECT (RECOMENDADO)
├─ Timing: 6-9 meses ANTES de deducción
├─ Requisitos:
│  ├─ Descripción técnica proyecto (2-5 páginas)
│  ├─ Timeline ejecución esperado
│  ├─ Presupuesto estimado
│  ├─ Equipo técnico asignado (CVs PhDs/researchers)
│  └─ Justificación Frascati (novedad + incertidumbre)
├─ Responsable: MINECO (Ministerio de Ciencia e Innovación)
├─ Plazo resolución: 3-6 meses
└─ Efecto: VINCULANTE para AEAT (salvo cambios sustanciales)

PASO 2: POST-PROJECT (MENOS RECOMENDADO)
├─ Timing: Dentro 180 días POST-conclusión proyecto
├─ Requisitos ADICIONALES:
│  ├─ Resultados técnicos alcanzados
│  ├─ Documentación completa (lab notebooks, código, reports)
│  ├─ Gastos certificados (invoices, payroll, timesheets)
│  └─ Análisis Frascati POST-FACTO
├─ Responsable: MINECO + CDTI review
├─ Plazo resolución: 4-8 meses (más extenso que pre-project)
└─ Riesgo: AEAT puede impugnar si project outputs inconsistent

PRE vs POST ANÁLISIS:
PRE-PROJECT:
✓ Binding pre-emptive (mayor seguridad)
✓ Permite ajustes antes ejecución
✓ Timeline favorable (resolución pre-deducción)
✗ Requiere propuesta inicial sólida

POST-PROJECT:
✗ Menor certeza (AEAT puede reabrir)
✗ Deducción temporal hasta resolución
✓ Basado en hechos reales (mejor documentación)
```

### Efecto Vinculante IMV en AEAT

Una vez MINECO emite IMV, AEAT está **vinculada** a la clasificación:

```
VINCULATORIEDAD IMV:
────────────────────
Efecto Formal:
- AEAT no puede re-clasificar proyecto en auditoría
- Cobertura legal para Art. 35 LIS deducción
- 3-4 años de "safe harbor" típicamente

Limitaciones:
- Si empresa posteriormente reporta gastos DIFERENTES vs. IMV
- Si DEMPE allocation substantially changes
- Si cambios normativos POSTERIORES (muy raro)
→ AEAT puede reopener (pero con alto threshold de prueba)

Implicación Practica:
- IMV pre-project = máxima protección
- Documentación post-project debe COINCIDIR con IMV proposal
- Variaciones menores (±15%) aceptables; mayores requieren addendum
```

### Timeline Requirements (Pre vs Post)

| Fase | Timing Crítico | Plazo Máximo | Documentación |
|---|---|---|---|
| **Planificación** | T-0 (inicio proyecto) | - | Propuesta técnica + budget |
| **IMV Solicitud (Pre)** | T-6/9 meses ANTES deducción | - | Proyecto description + Frascati analysis |
| **Resolución IMV (Pre)** | T-3/6 meses | Antes T+deducción | Official IMV certificate |
| **Ejecución Proyecto** | T-0 a T+24 meses | Per proyecto spec | Technical docs + timesheets + invoices |
| **IMV Solicitud (Post)** | T+180 días MAX post-conclusión | Plazo hard (6 meses) | Resultados finales + gastos totales |
| **Resolución IMV (Post)** | T+4/8 meses | Depende MINECO queue | Final IMV vinculante |
| **Deducción Fiscal** | Año T+0 (si pre-project) O T+1 (si post) | 10 días desde AEAT request | IMV certification + timesheets |

**CRITICAL**: Si deducción se toma sin IMV (o post-auditoría), riesgo de:
- Penalización 15% (Art. 18.13 LIS equivalent para R+D)
- Reversal de deducción
- Intereses compensatorios

---

## Compatibilidades y Deducciones Mínimas

### Art. 35.2 LIS: Deducción Mínima

Art. 35.2 LIS establece una deducción MÍNIMA sobre base elegible:

```
DEDUCCIÓN MÍNIMA ESTRUCTURA:

Base Elegible R+D (EUR 450k):
├─ Deducción obligatoria MÍNIMA: 25% (EUR 112.5k)
├─ Bonus incremental (si > 10% growth): +17% (EUR 76.5k)
├─ Bonus personal investigador: +25% (EUR 38.25k PhD)
└─ Total MÁXIMO: EUR 227k (sin caps)

PERO: Límite Deducción Aplicable vs. Cuota Íntegra:

Cuota Íntegra 2024 (CIL): EUR 500k
Art. 39 LIS: Deducción máxima = 25% cuota íntegra = EUR 125k

Resultado:
┌─────────────────────────┐
│ Deducción Calculada: EUR 227k │
│ Límite Legal (Art. 39): EUR 125k │
│ Deducción APLICADA 2024: EUR 125k │
│ EXCESO CARRY-FORWARD: EUR 102k │
└─────────────────────────┘

Plazo carry-forward: Hasta 15 años (Art. 39 LIS)
```

### Compatibilidad con Bonificaciones SS (Investigadores)

RDL 4/2024 introdujo bonificación de Seguridad Social para personal investigador:

```
COMPATIBILIDAD SS + DEDUCCIÓN R+D:
──────────────────────────────────

Beneficiario: Personal investigador con doctorado (PhD, engineers)
Concepto SS: Reducción cotización social empresa (25% en algunos sectores)
Deducción R+D: 25% base elegible + 17% bonus incremental

EJEMPLO INTEGRADO:
─────────────────
Salario PhD investigador: EUR 60,000/año
├─ Cotización SS (normal): 30% = EUR 18,000
├─ Bonificación SS (RDL 4/2024): -25% × EUR 18,000 = EUR 4,500 ahorro
└─ Neto SS cost: EUR 13,500 (vs EUR 18,000)

R+D Deducción sobre mismo salario:
├─ Base elegible (100% if dedicated): EUR 60,000
├─ Deducción 25% + 17% bonus: EUR 25,200
├─ Tax relief @ 25% IS rate: EUR 6,300

VENTAJA COMBINADA POR AÑO:
= EUR 4,500 (SS reduction) + EUR 6,300 (IS deduction) = EUR 10,800
= ~18% of researcher salary (sin doble-conteo)

COMPATIBILIDAD: ✓ SÍ (SS bonif + R+D deducción son independientes)
NO HAY DOUBLE-DIP: Salario no se reduce para cálculo deducción
```

### Patent Box (Art. 23 LIS): Interacción

Art. 23 LIS introduce Patent Box (nexus approach) que interactúa con deducción R+D:

```
PATENT BOX MECHANICS:
─────────────────────

Componente 1: Ingreso Qualifying (Patent Box)
├─ Ingresos por licencias de patentes/intangibles desarrollados internamente
├─ Tasa preferente: 12.5% vs. 25% ordinaria
├─ Condición: Patent deve existir (aplicación + concesión)
└─ Nexus approach: 80% ingresos adjust (20% cost add-back)

Componente 2: Gastos R+D (Art. 35)
├─ Deducción directa de gastos R+D (25-42%)
├─ Reduce CIL (cuota íntegra) directamente
└─ Base diferente vs. Patent Box income

COMPATIBILIDAD ESTRUCTURA:
─────────────────────────

Ejemplo: Desarrollo patente software
├─ R+D Expense 2024: EUR 300,000
│  └─ Deducción 25% = EUR 75,000 (reduce CIL)
│
├─ Patent Filed 2024, Concedida 2025
│  └─ Licensing revenue 2025 onwards: EUR 200,000/año
│
├─ Patent Box 2025+:
│  ├─ Gross patent income: EUR 200,000
│  ├─ Nexus adjustment (80%): EUR 160,000
│  └─ Patent box rate: 12.5% on EUR 160,000
│
└─ NO DOUBLE-DIP:
   - EUR 300,000 R+D expense → deduction (reduces CIL)
   - EUR 160,000 patent-adjusted income → Patent Box (separate, lower rate)
   ✓ CUMULATIVE BENEFIT (no restriction)

CUIDADO:
- Si deducción R+D taken, gastos NO can be capitalized to patent asset
- Patent box aplica only to INCOME, not to cost basis
```

### Límites Deducción Art. 39 LIS (25-50% de Cuota)

Art. 39 LIS establece límites generales deducción fiscal:

```
LÍMITE DEDUCCIÓN FISCAL ART. 39 LIS:
────────────────────────────────────

Regla General:
Deducción máxima = 25% Cuota Íntegra (CIL)

EXCEPCIONES con límite 50%:
├─ Pérdidas de ejercicios anteriores (carry-forward)
├─ Donaciones + otros créditos + deducciones públicas
└─ Combinación puede llevar a límite 50% CIL

APLICACIÓN R+D:
┌────────────────────────────────────┐
│ CIL 2024: EUR 500,000              │
│ 25% limit = EUR 125,000 ordinaria  │
│ 50% limit = EUR 250,000 excepcional│
├────────────────────────────────────┤
│ R+D Deducción Calculada: EUR 227k  │
│ Limit aplicable: EUR 125k (25%)    │
│ Deducción aplicable 2024: EUR 125k │
│ Exceso C/F: EUR 102k (15 años)     │
└────────────────────────────────────┘

TIMING CARRY-FORWARD:
─ Si EUR 102k exceso → puedo usar EUR 102k en 2025 (25% limit 2025 CIL)
─ Plazo máximo carry-forward: 15 años
─ Orden aplicación: C/F previos ANTES deducciones nuevas (FIFO)
```

---

## Key Documentation for IMV & CDTI

- **Technical Reports**: Monthly documentation of R&D activities, technical uncertainty, results (required pre/post IMV)
- **Timesheets**: Project allocation per employee per task (DEMPE function traceability); must align with IMV proposal
- **Invoices**: Project-coded for R&D expense traceability; certified amounts per IMV
- **CDTI Application**: Optional but recommended (EUR 500-1000; 3-year safe harbor if approved by Centro para el Desarrollo Tecnológico e Industrial)
- **IMV Filing**: Pre-file 6-9 months BEFORE deduction (recommended); post-file within 180 days max post-project completion (less favorable)
