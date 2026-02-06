---
name: pe-exposure-scanner
description: Detect hidden permanent establishment (PE) risk under OECD Model Tax Convention (2017) and BEPS Action 7 (digital PE). Analyze agent contracts, employee travel calendars, and subsidiary activities to identify dependent agent PE, fixed place PE, service PE, and digital function PE exposure. Generate defensible PE risk assessments aligned with CDI thresholds (bilateral tax treaties), Article 5 OECD exemptions, and post-Brexit UK rules. Applicable for international expansion planning, inter-company service arrangements, distributed digital operations, and audit response.
---

# PE Exposure Scanner

---

## Application Topology

```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Agent Contracts │───▶│ Authority to     │───▶│ Dependent Agent  │
│ & Terms         │    │ Bind Analysis    │    │ PE Detection     │
│ (Art. 5(5))     │    │ (Art. 5(5) OECD) │    │ (BEPS-safe)      │
└─────────────────┘    └──────────────────┘    └────────┬─────────┘
                                                        │
┌─────────────────┐    ┌──────────────────┐             │
│ Employee Travel │───▶│ Day-Counting     │─────────────┤
│ Calendars       │    │ per CDI Thresholds           │
│                 │    │ (183d, 12m, etc)│             │
└─────────────────┘    └──────────────────┘             │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ PE Risk Report  │◀───│ Evaluate vs CDI  │◀───│ Fixed Place &    │
│ & Mitigation    │    │ + Art. 5(4) OECD │    │ Service PE Tests │
│ (BEPS A7)       │    │ Exceptions       │    │ (Digital BEPS-1) │
└─────────────────┘    └──────────────────┘    └──────────────────┘
```

---

## Trigger Contexts

- Establishing operations in new jurisdictions (expansion planning)
- Reviewing international sales structures with distributed agent networks
- Testing distributed digital operations under BEPS Action 7 (digital PE)
- Evaluating service delivery arrangements across multiple EU countries
- Audit response to revenue authority queries on PE status
- Post-Brexit UK operations (new PE rules post-TCA)

---

## PE Categories & OECD/BEPS Triggers

| PE Type | OECD Article | Threshold | BEPS Implication |
|---------|--------------|-----------|------------------|
| **Fixed Place PE** | Art. 5(1) | Place of business at disposal; permanence | Action 7 applies |
| **Construction PE** | Art. 5(3)(a) | >12 months (or CDI-specific) | Base erosion risk |
| **Dependent Agent PE** | Art. 5(5) | Authority to bind; habituality | High risk; MLI covered |
| **Service PE** | Art. 5(3)(b) | >183 days in 12 months | Action 7 (digital services) |
| **Digital PE (BEPS A7)** | Modified Art. 5 | Pillar One Amount A/B implications | Mandatory filing (soft law in transition) |
| **Preparatory/Auxiliary Exception** | Art. 5(4) | Limited to prep/prep-only activities | Safe harbor (if met) |
| **Spanish PE Definition** | TRLIRNR (RDL 5/2004) | Aligned with OECD Model; Art. 5 application | PE effects under Spanish corporate tax |

---

## Input Data Structures

### Agent Contract Analysis

```json
{
  "contrato_id": "comision_agente_francia_2024",
  "jurisdiccion": "Francia",
  "contratante": "Parent Company (UK)",
  "agente_dependiente": "Commercial Agent (FR)",
  "analisis_requerido": [
    "autoridad_para_vincular",
    "negociacion_contrato",
    "exclusividad",
    "plazo_duracion",
    "independencia_economica"
  ],
  "clausulas_criticas": {
    "art_5_5_ocde": "Poder negociar y cerrar en nombre del principal",
    "art_5_4_ocde": "¿Limitado a actividades preparatorias?",
    "independencia": "¿Agente realmente independiente?"
  }
}
```

### Employee Travel Calendar (Day-Counting per CDI)

```csv
empleado,pais_destino,fecha_inicio,fecha_fin,duracion_dias,proposito,categorizado
Juan García,Francia,2024-01-15,2024-01-20,6,Client meeting,Service PE test
Juan García,Francia,2024-02-10,2024-02-15,6,Contract negotiation,Service PE test
María López,Francia,2024-03-01,2024-03-31,31,Project implementation,Service PE test
María López,Francia,2024-06-10,2024-06-25,16,Implementation follow-up,Service PE test
```

**Day-Counting Rules per CDI**: Consecutive or aggregate days within 12-month rolling period; treaty-specific rules apply.

---

## Output & Risk Assessment

```json
{
  "jurisdiccion_riesgo": "Francia",
  "periodo_testeo": "2024 (rolling 12-month)",
  "resumen_ejecutivo": {
    "nivel_riesgo": "ALTO",
    "score_pe_overall": 0.78,
    "tipos_pe_identificados": ["Dependent Agent PE", "Service PE (proximity)"],
    "recomendacion_inmediata": "Contract amendment required (URGENT)"
  },
  "hallazgos_detallados": [
    {
      "tipo_pe": "DEPENDENT_AGENT_PE",
      "art_ocde": "Art. 5(5)",
      "nivel_riesgo": "ALTO",
      "elementos_riesgo": {
        "autoridad_vincular": {
          "evidencia_contrato": "Cláusula 4.2: 'El agente podrá negociar y cerrar contratos en nombre del principal'",
          "cumplimiento_5_5": "FAIL - Autoridad para vincular está presente",
          "defensa_art_5_4": "NO APLICA - Not a preparatory/auxiliary-only exception case"
        },
        "habitualidad": {
          "meses_activos": "12/12 (permanente)",
          "negociaciones_cerradas": "Múltiples (evidenciable)"
        }
      },
      "jurisprudencia_clave": "OECD Guidelines 2017, Art. 5(5) Commentary; Pillar 1 Amount A implications under BEPS",
      "mitigacion": [
        "Enmienda contractual: Limitar a 'solicitud de oferta' sin autoridad de cierre",
        "Segregación de funciones: Solo matriz UK puede cerrar contratos",
        "Documentación: Evidencia de rechazo explícito de autoridad"
      ]
    },
    {
      "tipo_pe": "SERVICE_PE",
      "art_ocde": "Art. 5(3)(b)",
      "nivel_riesgo": "MEDIO-ALTO (approaching threshold)",
      "dia_counting_metodologia": {
        "regimen_cdi": "España-Francia CDI 1999, P1",
        "umbral": "183 days in 12-month rolling period",
        "dias_acumulado": 156,
        "margen": "27 días antes umbral",
        "proyeccion": "If pace continues → exceeds 183d in Q4 2024"
      },
      "analisis_por_empleado": [
        {
          "empleado": "Juan García",
          "rol": "Sales Representative",
          "dias_francia": 45,
          "periodos": "6 months activity in 12-month window",
          "proposito": "Client meetings & contract negotiation",
          "estatus_pe": "Transitory - no PE risk currently"
        },
        {
          "empleado": "María López",
          "rol": "Service Implementation Lead",
          "dias_francia": 111,
          "periodos": "5 months sustained activity",
          "proposito": "Project implementation & support",
          "estatus_pe": "HIGH RISK - 72 days from threshold"
        }
      ]
    },
    {
      "tipo_pe": "BEPS_ACTION_7_DIGITAL_PE",
      "art_ocde": "Modified Art. 5 under BEPS Action 7",
      "nivel_riesgo": "LOW-MEDIUM",
      "trigger": "Pillar One Amount A/Amount B mandatory filing",
      "monitoreo": "If Parent UK sells digital services to FR clients, Pillar 1 thresholds apply"
    }
  ],
  "cdi_analisis": {
    "convenio": "Spain-France Tax Treaty 1999, Protocol 1",
    "art_5_3a_construction": "12 months (or CDI override)",
    "art_5_3b_services": "183 days in 12-month period",
    "art_5_5_dependent_agent": "Standard OECD model (no material deviation)",
    "art_5_4_exception_test": {
      "preparatory_auxiliary": "Art. 5(4) safe harbor",
      "current_status": "FAILED - Services exceed preparatory scope"
    }
  },
  "beps_pillar_one_status": "Soft law in transition - Pillar One Amount A/B thresholds not yet binding for most jurisdictions; monitor implementation timelines per OECD Inclusive Framework",
  "post_brexit_uk": "Spain-UK TCA (post-Brexit) - identical 12m/183d thresholds",
  "mli_coverage": "MLI applies (both signatories) - peer review standard articles enforced",
  "mitigacion_accionable": [
    {
      "prioridad": "URGENTE (1-30 días)",
      "accion": "Enmendar contrato agencia - eliminar autoridad vinculante",
      "responsable": "Legal + Tax",
      "riesgo": "Reassessment FR authority under Art. 5(5) OECD"
    },
    {
      "prioridad": "ALTA (30-60 días)",
      "accion": "Implementar tracking 183d rolling (alert at 140d)",
      "responsable": "Tax Compliance",
      "mechanism": "Automated calendar alerts for employee travel"
    },
    {
      "prioridad": "MEDIA (60-90 días)",
      "accion": "Evaluar local employment o restructuring para María López",
      "responsable": "Operations + Tax",
      "beneficio": "Eliminaria Service PE bajo Art. 5(3)(b)"
    }
  ]
}
```

---

## Concrete Example: Tech Company with Distributed EU Team (BEPS A7 & Service PE Testing)

**Scenario**: German software company provides cloud services and implementation support across EU. Employees from HQ travel to client locations (France, Spain, Benelux). PE test: (1) Service PE under Art. 5(3)(b)? (2) Digital PE under BEPS Action 7?

**Day-Counting Methodology per CDI**:
- **Art. 5(3)(b) Service PE threshold**: 183 consecutive or aggregate days in 12-month period
- **Rolling window**: Any 12-month period (not calendar year)
- **Day countable**: Partial days typically count as full day per treaty

**Facts**:
- **Carlos (Implementation)**: 120 days France 2024 → 63-day margin to threshold
- **Petra (Multi-skilled)**: 90 days Spain + 45 days France (135 total) → BUT must test by country separately
- **Klaus (Sales)**: 60 days scattered EU → Below all thresholds

**Analysis per OECD Art. 5**:
1. **Carlos in France**: 120d < 183d → NO Service PE (safe)
2. **Petra**: 90d Spain alone + 45d France separately → Neither exceeds 183d by country → NO PE under treaty literal reading
3. **Digital overlay**: Cloud hosting from Germany server + remote implementation → BEPS Action 7 assessment required (Pillar One Amount A compliance)

**Mitigation Actions**:
- Rotate Carlos out at day 150 (33-day safety buffer)
- Document subcontracting vs. employee travel allocation
- Separate billing for digital services vs. on-site services (Pillar One)

---

## CDI Database with Treaty-Specific Service PE Thresholds

| Treaty | Construction PE | Service PE | Dependent Agent PE | Art. 5(4) Exception | Special Notes |
|--------|---|---|---|---|---|
| ES-FR | 12 months | 183 days/12mo | Art. 5(5) OECD | Preparatory/auxiliary safe | Cour de Cassation case law; P1 applies |
| ES-UK (TCA post-Brexit) | 12 months | 183 days/12mo | Art. 5(5) OECD | Preparatory/auxiliary safe | UK BEPS-aligned; no EU VAT |
| ES-DE | 12 months | 183 days/12mo | Art. 5(5) OECD | Preparatory/auxiliary safe | Bundesfinanzhof jurisprudence relevant |
| ES-US | 12 months | N/A (no service PE) | Art. 5(5) US variant | Preparatory safe | US treaty unique (no 183-day service PE) |
| **Digital Layer** | N/A | Modified by Pillar 1 | N/A | BEPS A7 safe harbor test | Pillar One Amount A/B thresholds override |

---

## Parametrización por CDI (Convenio de Doble Imposición)

### Red de Convenios España (97+ Tratados)

España ha suscrito 97+ tratados bilaterales de doble imposición (CDI). Cada uno puede tener variaciones en PE definition:

```
RED DE CDI ESPAÑA - JURISDICCIONES CLAVE:

UE (27 Estados):
- France, Germany, Italy, Netherlands, Poland, etc.
- Thresholds típicamente: PE art. 5(1) OECD + 183d service PE
- Variación: Art. 5(4) exception scope puede diferir (jurisprudencia local)

Mercados Emergentes:
- Mexico: 12 months construction PE; 183 days service PE
- Brazil: Modified definitions (service PE @ 90 days for specific sectors)
- India: Art. 12 dependent agent PE - broader interpretation
- China: Similar OECD model; enforcement issues common

US & EFTA:
- US: Unique (no 183-day service PE in US treaty model)
- Switzerland: Standard 12/183 + preparatory exception
- Norway: Aligned OECD

Key Jurisdictions Divergence:
```

### Diferencias PE Definition por CDI

Pese a que mayoría están alineados con OECD Model 2017, existen divergencias:

| CDI | Art. 5(1) Definición | Service PE Threshold | Dependent Agent PE | Especificidad |
|---|---|---|---|---|
| **ES-FR** | Fijo en disponibilidad | 183d cumulative | Art. 5(5) OECD | Jurisprudencia Cour Cassation amplia |
| **ES-UK** | Fijo (post-TCA) | 183d (12-month rolling) | Art. 5(5) + MLI | MLI Art. 12 dependent agent |
| **ES-MX** | Fijo, instalaciones | 183d en 12 meses | Art. 5(5) modificado | Actividades preparatorias definidas restringidamente |
| **ES-BR** | Fijo permanente | 183d PERO con excepciones sector-específicas | Art. 5(5) interpretación expansiva | Riesgo ajuste alto por interpretación local |
| **ES-IN** | Fijo | 183d BUT interpretación restrictiva (consecutive?) | Art. 12 agent PE MUY amplio (jurisprudencia India) | Alto riesgo dependent agent PE |
| **ES-US** | Fixed place (sin 183d service PE) | Service PE NO EXISTE en treaty | Art. 5(5) US variant (narrow) | Actividades preparatorias safe |

### Análisis OECD Model vs. UN Model

España suscribe mayormente OECD Model, pero algunos países usan UN Model con PE definition expandida:

```
OECD MODEL (Usado por: EU, US, developed markets):
- Art. 5(1): Fixed place available for business
- Art. 5(3)(b): Service PE @ 183 days
- Art. 5(5): Dependent agent (standard)
- Art. 5(4): Preparatory/auxiliary SAFE HARBOR

UN MODEL (Usado por: Algunos emergentes, G77):
- Art. 5: Expanded definition (PE @ construction sites even < 12m)
- Service PE: Some countries @ 90 days (not 183)
- Agent PE: Broader definition (comissionaire NOT safe)
- Preparatory exception: Narrower or NO exception

IMPLICACIÓN ESPAÑA: Si contraparte es UN Model jurisdiction:
→ PE risk MAYOR (tester contra interpretación expansiva)
→ APA pre-emptivo recomendado
```

### Mapeo Automático CDI en Skill

Sistema parametrizable por:
1. País de la contraparte (input usuario)
2. Tipo de operación (sales, services, PE risk)
3. Búsqueda automática de CDI applicable
4. Extracción de Art. 5 thresholds específicos
5. Comparativa vs. OECD Model standard

---

## Actividades Digitales y Riesgo Agencia

### Digital PE: Pillar One Amount A y BEPS Action 7

BEPS Action 7 introdujo modificaciones al PE definition para operaciones digitales. Pillar One (Amount A/B) está en transición:

```
PILLAR ONE AMOUNT A: Nexus Digital
─────────────────────────────────────
Trigger: Multinational enterprise with:
- Annual revenue > EUR 20 billion (global threshold)
- AND digital/automated services sold into jurisdiction

PE Risk: Nueva categoría "sustained interaction" sin PE físico:
- Customer relationship management (CRM systems)
- Cloud infrastructure con customer data
- Digital marketplace facilitation
- Distance selling (direct to consumer)

Threshold: If > EUR 1M annual revenue to customers in jurisdiction
→ Amount A taxation applies (jurisdiction profit reallocation)
→ Independent of traditional PE definition
```

**Implicación para España**: Si empresa española es subsidiary de multinacional digital:
→ Riesgo de Amount A assessment (no importa si hay PE tradicional)
→ Filing obligations emerge (soft law transitioning to binding)

### Dependent Agent PE: Art. 12.1 TRLIRNR

TRLIRNR (Real Decreto Legislativo 5/2004) Art. 12.1 define PE en España:

```
Art. 12.1 TRLIRNR: PE Definition Española
───────────────────────────────────────────
"Hay PE cuando:
1. Establecimiento fijo de negocio (disponibilidad permanente)
2. Agente dependiente con poder de vinculación
3. Actividades de construcción/instalación > 12 meses
4. Servicios > 183 días en 12 meses"

Key Point: TRLIRNR alineado OECD Model, BUT:
- Interpretación AEAT tiende a ser expansiva (riesgo alto)
- Jurisprudencia española (Audiencia Nacional) ha ampliado noción "disponibilidad"
- Agente dependiente: autoridad implícita (no solo explícita) puede trigger PE
```

### Arreglos Commissionaire vs. Dependent Agent

Tipo de contrato agent determina PE classification:

```
COMMISSIONAIRE ARRANGEMENT (Art. 5(5) Safe Harbor - si se cumple):
├─ Requisitos:
│  ├─ Agent actúa en nombre PROPIO (no en nombre del principal)
│  ├─ Agent soporta riesgos operacionales
│  ├─ Agent tiene independencia económica (puede rechazar órdenes)
│  └─ Términos contractuales explícitamente así establecidos
├─ Implicación PE: NO hay PE (safe)
└─ Riesgo: Sustancia vs. Forma (AEAT puede recar actericar como dependent agent)

DEPENDENT AGENT PE (Art. 5(5) Risk):
├─ Indicadores:
│  ├─ Contrato establece autoridad de vinculación explícita
│  ├─ Habitualidad: Agent negocia/cierra contratos regularmente
│  ├─ Principal supervisa/controla operaciones
│  ├─ Agente carece independencia economica (single principal)
│  └─ Términos muy favorable al principal
├─ Implicación PE: RIESGO ALTO PE
└─ Ejemplo: "Sales rep" con poder firma pero sin independencia = PE
```

**Mitigation**: Documentar explícitamente commissionaire terms:
- Agent actúa en nombre propio (facturas emitidas por agent)
- Agent soporta riesgos (inventory risk, credit risk)
- Independencia demostrable (puede operar para otros principals)
- Términos contractuales no-exclusive, with termination flexibility

### Server PE: Ubicación Física de Servidores

Ubicación física de servidores/data centers puede trigger fixed place PE:

```
SERVER PE ANALYSIS:
────────────────────
Elemento | Criterio PE | Riesgo |
---|---|---|
Servidor en servidor compartido | Si está "a disposición" del usuario > 12m consecutivos | BAJO (shared facility = no exclusive availability) |
Data center dedicado | Si servidor está bajo control parent company | ALTO (fixed place PE si > 12m) |
Cloud elasticity | Si servidor puede ser escalado/desprovisionado on-demand | BAJO (no "permanence" traditional) |
Location Spain | Servidor EN ESPAÑA = pe risk territorial | MEDIO-ALTO (AEAT scrutiny alto) |

Mitigation para Cloud Digital:
- Usar multi-jurisdictional data replication (no single fixed location)
- Cloud provider (AWS/Azure) retains control (user access only)
- Terms of Service explícitamente "revocable access"
- Documentar que cloud architecture es scalable (no fixed)
```

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| **OECD Model 2017** | Art. 5 PE definition; Art. 5(4) preparatory exception |
| **Spain TRLIRNR (RDL 5/2004)** | Art. 12: PE definition español; aligned OECD BUT expansive interpretation risk |
| **Bilateral CDI Network** | 97+ tratados España; cada uno con posibles variaciones Art. 5 |
| **BEPS Action 7** | Digital PE guidance; Pillar One Amount A/B (in transition) |
| **MLI (Multilateral Instrument)** | Spain signatory; Article 12 dependent agent PE modifications |
| **BEPS Action 7 (Digital PE)** | Monitoring Pillar One Amount A implementation timelines |
| **Post-Brexit UK (TCA 2021)** | Spain-UK trading agreement: PE thresholds unchanged vs. pre-Brexit |
