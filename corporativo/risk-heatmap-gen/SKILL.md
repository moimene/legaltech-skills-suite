---
name: risk-heatmap-gen
description: Generar mapa de calor dinámico de riesgos en due diligence (M&A, fund raising) mediante scoring Zero-Shot de cláusulas vs playbook estándar (Clifford Chance, Allen & Overy). Quantificar riesgos con Monte Carlo para contingencies, thresholds de materialidad por tamaño de deal, análisis W&I insurance coverage con outputs exportables para pólizas, templates específicos por industria (tech IP, pharma regulatory, real estate, energy). Detección multidisciplinaria de red flags legales (LSC, laboral, fiscal) con trazabilidad de supuestos, documentación y confianza analítica. Contextos: DD de tech company (IP+labor+tax), identificación de red flags, materialidad relativa, W&I submission packs.
---

# Risk Heatmap Generator - M&A Due Diligence

## Scoring de Riesgos Contractuales & Operacionales

La due diligence en M&A requiere evaluar riesgos contractuales, fiscales, laborales e IP versus benchmarks de mercado. Magic Circle practices cuantifican materialidad relativa (% de deal size) para priorizar hallazgos.

---

## Topología de Procesamiento

```
┌───────────────────┐ ┌─────────────────┐ ┌──────────────────┐
│ DD Docs           │→│ Extraer         │→│ Zero-Shot        │
│ (PDF, DOCX)       │ │ cláusulas por   │ │ classification   │
│ + Deal memo       │ │ categoría       │ │ (áreas clave)    │
└───────────────────┘ └─────────────────┘ └────────┬─────────┘
                                                    │
        ┌───────────────┬────────────┬────────────────┬──────────────┐
        │               │            │                │              │
        ▼               ▼            ▼                ▼              ▼
    Scoring vs    Materialidad   Monte Carlo    W&I Insurance    Templates
    playbook      (% deal size)   (contingency)  (coverage gaps)  (industria)
        │               │            │                │              │
        └───────────────┴────────────┴────────────────┴──────────────┘
                                   ▼
                    Risk Heatmap + Deal-breaker register

---

## Aplicar cuando

- **DD inicial**: evaluar riesgos top 50 antes de entrar en profundidad
- **Tech M&A**: mapear IP, labor, compliance risks (GDPR, AML)
- **Pharma**: regulatory approval contingencies, patent expiry
- **Real estate**: title, zoning, environmental liens
- **Portfolio audit**: gestionar cartera de contratos existentes
- **Insurance negotiation**: identificar gaps de W&I coverage
- **Price adjustments**: cuantificar risky areas como base para purchase price reduction

---

## Categorías de Riesgo por Industria

### Tech Company (IP-heavy)

| Categoría | Áreas | Materialidad Threshold |
|-----------|-------|----------------------|
| **IP** | Patentes (validez, claims), licencias OSS, dominio, marca | >5% deal (RED) |
| **Laboral** | Opciones, non-competes, key person retention | >3% deal |
| **Compliance** | GDPR, DPA, AML, privacy violations | Unlimited (RED) |
| **Contractual** | Key customer contracts (>15% revenue), SLAs | >2% deal |
| **Corporate** | Capitalization, board seats, voting agreements | Structural risk |

### Pharma / Healthcare

| Categoría | Áreas | Materialidad |
|-----------|-------|----------------|
| **Regulatory** | FDA approval status, trials, market authorization | Absolute blocker |
| **IP** | Patent estate, exclusivity periods, generics risk | >10% deal |
| **Laboral** | Key scientists, non-solicits, research continuity | >5% deal |
| **Fiscal** | Transfer pricing, grant contingencies | >3% deal |
| **Compliance** | Anti-kickback statutes, physician payments, SOX | Unlimited |

---

## Red Flags Legales Multidisciplinares

### Corporativo / LSC (Ley de Sociedades de Capital)

**Riesgos Estructurales Críticos:**

| Red Flag | Norma | Threshold | Impacto Típico | Acción DD |
|----------|-------|-----------|---|---|
| **Operaciones no autorizadas en activos esenciales** | Art. 160 LSC | >25% del activo total | Vicio de consentimiento, nulidad, reclamaciones socios minoritarios | Validar JGA signatures, verificar libros actas |
| **Conflictos de interés no declarados** | Art. 162 LSC | Cualquier administrador con interés conflictivo | Responsabilidad civil solidaria, daño al patrimonio social | Analizar transactions con partes vinculadas últimos 3 años |
| **Deber de abstención incumplido** | Art. 190 LSC | Voto de interesado en decisión material | Anulabilidad del acuerdo, indemnización | Revisar JGA actas, votaciones en revaluaciones/adquisiciones |
| **Acuerdos impugnables por lesión interés social** | Art. 204 LSC | Daño patrimonial demostrable | Plazo 1 año para impugnación post-acquisition | Due diligence de acuerdos comerciales, arm's length analysis |
| **Derecho separación por dividendos** | Art. 348bis LSC | Targets sin distribuciones 5+ años | Salida forzada socio, contingencia post-deal | Proyectar dividend policy, asegurar distribuciones post-acquisition |

**Elementos a verificar en DD:**
- Resoluciones JGA últimos 3 años: comprobar quórum, representación, conflictos declarados
- Registro de conflictos de interés: matriz de relacionadas, operations con administradores
- Estatutos: cláusulas de protección de socios minoritarios, pre-emption rights
- Libros actas: certificación notarial de decisiones de órganos, especialmente M&A/financing

---

### Laboral (Estatuto de los Trabajadores, Seguridad Social)

**Riesgos Operacionales Post-Cierre:**

| Red Flag | Norma | Threshold | Impacto Típico | Acción DD |
|----------|-------|-----------|---|---|
| **Sucesión de empresa sin subrogación** | Art. 44 ET | Todos los contratos + obligaciones de acreedor social | Responsabilidad solidaria adquirente 3 años post-deal | Validar cómo se estructura la asunción de contratos laborales |
| **Planes de igualdad no registrados** | RDL 901/2020 | >250 empleados (50+ en algunos sectores) | Multa €10k-100k anual, nulidad de cláusulas discriminatorias | Solicitar registro EEOC, evaluar claims pendientes |
| **Contingencias ERE/ERTE activas** | Art. 51 ET / RDL 9/2022 | Salarios + prestaciones |Litigios post-restructuring, indemnizaciones impugnadas | Revisar resoluciones administrativa, litigios en curso |
| **Non-competes excesivos** | Art. 21.2 ET | Duración >6 meses, radio >provincia | Nulidad automática → potencial claim de empleado post-exit | Auditar todos non-compete agreements, alcance geográfico/temporal |

**Elementos a verificar en DD:**
- Contratos individuales: cláusulas de no-compete, confidencialidad, ESOP vesting
- Certificado de plantilla: convenio colectivo aplicable, conflictividad laboral
- Registros Inspección: accidentes, denuncias, sanciones pendientes
- Planes de continuidad clave: key person insurance, retention agreements, flight risk assessment

---

### Fiscal (LIS, Régimen Fiscal Internacional)

**Riesgos Pre-Cierre y Post-Cierre:**

| Red Flag | Norma | Threshold | Impacto Típico | Acción DD |
|----------|-------|-----------|---|---|
| **Operaciones vinculadas sin documentación arm's length** | Art. 18 LIS | Cualquier transacción intercompañía | Ajuste de precios + recargo del 5-15%, intereses moratorios | Solicitar transfer pricing documentation, comparables de mercado |
| **ESOP mal documentado → contingencia IRPF** | Art. 7 LIS / Art. 119-121 EIR | Variable según renta vs ganancia patrimonial | Retención doble: employer + beneficiario, litigios IRPF | Validar ESOP plan, calcular tax basis, provisión contingencia |
| **IVA intra-grupo sin arm's length** | Art. 16a LIVA | Precios entre almacenes, servicios internos | Reclasificación como suministro gravado, IVA repercutible | Revisar políticas transfer pricing, servicios centralizados |
| **Establecimiento permanente oculto** | TRLIRNR RDL 5/2004 Art. 12 | Actividad económica persistente en otra jurisdicción | Sujección a taxation plena, interest + penalties | Mapear oficinas, agentes independientes, digital footprint fiscal |

**Elementos a verificar en DD:**
- Transfer Pricing documentation: precios intercompañía, métodos comparables
- Registros Hacienda: últimas 4 liquidaciones IVA/IS/IRPF, verificaciones
- Convenios internacionales: double taxation treaties, permanent establishment analysis
- IP & royalties: documentación de gastos deducibles, regalías a matriz/partners

---

### Integración: Matriz de Riesgo Cruzado (Impacto en W&I)

```
┌────────────────────────────────────────────────────────────────┐
│ RED FLAG           │ CATEGORÍA      │ COBERTURA W&I TÍPICA      │
├────────────────────────────────────────────────────────────────┤
│ Art. 160 LSC       │ Corporativo    │ EXCLUIDA (conocida antes) │
│ Art. 162 LSC       │ Corporativo    │ Knowledge qualifier       │
│ Art. 44 ET         │ Laboral        │ EXCLUIDA (obligatoria)    │
│ Non-competes nulos │ Laboral        │ SUBLIMITADA (defend. cost)│
│ Transfer pricing   │ Fiscal         │ EXCLUIDA o separada       │
│ Establec. perm.    │ Fiscal         │ Muy cara (reaseguro)      │
└────────────────────────────────────────────────────────────────┘
```

---

## Metodología de Scoring (Cuantificado)

**Formula**: `Riesgo_Score = (Desviación_Estándar × Peso_Categoría) + Ajuste_Materialidad`

```python
# Threshold absolutos por tamaño deal (Magic Circle practice)
deal_size = 100_000_000  # €100M

red_threshold = deal_size * 0.05      # >€5M = RED
yellow_threshold = deal_size * 0.02   # €2-5M = YELLOW
green_threshold = deal_size * 0.005   # <€500k = GREEN

# Ejemplo: tax contingency €2.5M
contingencia = 2_500_000
materialidad = contingencia / deal_size = 2.5%  # YELLOW
```

### Matriz de Riesgo: Ejemplos de Playbook

| Cláusula | Estándar Market | Threshold YELLOW | Threshold RED | Referencia |
|----------|-----------------|------------------|---------------|-----------|
| **Limitation of Liability** | 100% purchase price | <50% | Sin límite |  |
| **Warranty Period** | 18-24 meses | <12 | <6 meses | CC Art. 1966 |
| **Basket (tipping)** | 0.5% EV | <0.25% | <0.1% | |
| **Cap Indemnification** | 15-20% precio | <10% | <5% | |
| **Tax Indemnity** | Igual que warranty cap | -30% cap | Separate unlimited | IRPF 19% |
| **IP Reps** | 18+ meses | <12 | <6 | Patent validity risk |

---

## Ejemplo Concreto: Tech Company DD (€40M Acquisition)

**Target**: SoftCorp Spain (AI/SaaS, 120 empleados, 40 clientes)
**Deal size**: €40M
**Red threshold**: >€2M (5%), **Yellow threshold**: €800k-2M (2-5%)

### Output: Risk Heatmap JSON

```json
{
  "target": "SoftCorp Spain",
  "deal_size_eur": 40000000,
  "fecha_analisis": "2024-02-06",
  "documentos_analizados": 156,
  "resumen_ejecutivo": {
    "red_count": 3,
    "yellow_count": 12,
    "green_count": 89,
    "pending_info": 5,
    "weighted_risk_score": 6.2
  },
  "deal_breakers": [
    {
      "id": "IP-001",
      "categoria": "IP",
      "titulo": "Depuración de titularidad de IP core",
      "severidad": "RED",
      "descripcion": "Patente de algoritmo ML (EP3847395) registrada a co-founder original, no cedida a SoftCorp. Co-founder exited 2021, sin novación registrada en OEPM.",
      "contingencia_estimada": {
        "low": 500000,
        "mid": 2000000,
        "high": 8000000,
        "probabilidad": 0.45
      },
      "materialidad": 5.0,
      "recomendacion": "Obtener cesión registrada ante OEPM o negociar precio reducción €2M escrow",
      "documentos": ["registro_oepm.pdf", "estatutos_2021.pdf", "cesion_inconclusa.docx"]
    },
    {
      "id": "LABOR-001",
      "categoria": "Laboral",
      "titulo": "Acciones de empleados sin plan formal",
      "severidad": "RED",
      "descripcion": "100 empleados tienen opciones (ESOP) sin documento formalmente aprobado por JA. Cliff 4 años pero sin certificado de validez. Potencial reclamación de empleados al exit.",
      "contingencia_estimada": {
        "low": 300000,
        "mid": 1500000,
        "high": 5000000,
        "probabilidad": 0.30
      },
      "materialidad": 3.75,
      "recomendacion": "Ejecutar resolución de JA urgente, ESOP plan documentation antes de closing",
      "referencias_legales": "Ley 20/1990 ESOP, Ley 19/1988 Planes accionariales"
    }
  ],
  "heatmap_resumen": {
    "IP": {
      "red": 2,
      "yellow": 1,
      "green": 8,
      "score_ponderado": 7.8
    },
    "Laboral": {
      "red": 1,
      "yellow": 4,
      "green": 12,
      "score_ponderado": 5.2
    },
    "Fiscal": {
      "red": 0,
      "yellow": 3,
      "green": 15,
      "score_ponderado": 3.1
    },
    "Compliance": {
      "red": 0,
      "yellow": 2,
      "green": 18,
      "score_ponderado": 2.4
    },
    "Contractual": {
      "red": 0,
      "yellow": 2,
      "green": 22,
      "score_ponderado": 2.8
    }
  },
  "analisis_monte_carlo": {
    "metodologia": "10,000 simulaciones de contingencias acumuladas",
    "distribuciones": {
      "IP_contingency": {"mean": 2000000, "std": 1800000},
      "Labor_contingency": {"mean": 1500000, "std": 1200000},
      "Tax_contingency": {"mean": 450000, "std": 350000}
    },
    "resultados": {
      "p10_percentile": 1200000,
      "p50_percentile": 4100000,
      "p90_percentile": 8500000,
      "distribucion_grafico": "bell_curve_desc.png"
    },
    "recomendacion": "Escrow €4.1M (50th percentile) o €2.8M (30th percentile) con IBNR cap"
  },
  "wi_insurance_analysis": {
    "coverage_recomendado": 10000000,
    "deducible": 400000,
    "retention": 500000,
    "gaps": [
      {
        "area": "IP title defects",
        "gap": "Típicamente excluidas si co-founder aún identifiable",
        "impacto": "€2-8M expuesto"
      },
      {
        "area": "Undisclosed litigation",
        "gap": "Knowledge qualifier - employee claims no covered",
        "impacto": "€1-2M expuesto (labor risks)"
      },
      {
        "area": "Tax contingencies",
        "gap": "Generalmente cap separado 18 meses",
        "impacto": "IBNR risk €500k-1M"
      }
    ],
    "prime_anual": 120000,
    "retention_total": 900000,
    "recomendacion": "W&I policy €8M + transactional insurance para IP cedente"
  }
}
```

---

## Output para Pólizas W&I (Warranties & Indemnities Insurance)

### Template de Datos Exportables para Brokers

La integración del análisis de riesgos con pólizas W&I requiere standardización de datos. El siguiente template es exportable en formato JSON y compatible con brokers de seguros especializados (AON, Marsh, BRP).

```json
{
  "wi_submission_pack": {
    "deal_metadata": {
      "target_name": "SoftCorp Spain",
      "buyer_name": "TechGlobal Holdings",
      "deal_size_eur": 40000000,
      "closing_date": "2024-06-30",
      "deal_type": "asset_sale",
      "sector": "software_saas",
      "jurisdiction": "ES"
    },
    "insurance_requirements": {
      "coverage_amount_requested_eur": 8000000,
      "deductible_eur": 400000,
      "retention_eur": 500000,
      "policy_period_months": 24,
      "survival_period_months": 18
    },
    "risk_exposures_quantified": [
      {
        "exposure_id": "IP-001",
        "risk_category": "IP title defects",
        "exposure_description": "Patent EP3847395 registered to departed co-founder, not fully assigned",
        "estimated_exposure_eur": {
          "low": 500000,
          "mid": 2000000,
          "high": 8000000,
          "probability": 0.45
        },
        "buyer_knowledge_qualifier": "unknown",
        "seller_disclosure_status": "not_disclosed",
        "coverage_likelihood": "excluded_if_co_founder_identifiable",
        "supporting_documentation": ["registro_oepm.pdf", "cesion_inconclusa.docx"],
        "w&i_note": "Typically excluded under standard IP reps if assignor traceable"
      },
      {
        "exposure_id": "LABOR-001",
        "risk_category": "Undisclosed labor claims",
        "exposure_description": "ESOP without formal shareholder approval; cliff 4 years",
        "estimated_exposure_eur": {
          "low": 300000,
          "mid": 1500000,
          "high": 5000000,
          "probability": 0.30
        },
        "buyer_knowledge_qualifier": "disclosed_in_da",
        "seller_disclosure_status": "disclosed_schedule",
        "coverage_likelihood": "sublimited_defend_cost_only",
        "supporting_documentation": ["esop_plan.docx", "shareholder_records.pdf"],
        "w&i_note": "Labor claims typically covered only for defense costs; capped separately"
      },
      {
        "exposure_id": "TAX-001",
        "risk_category": "Transfer pricing documentation",
        "exposure_description": "Intercompany royalties (IP licensing to parent) undocumented",
        "estimated_exposure_eur": {
          "low": 100000,
          "mid": 450000,
          "high": 1200000,
          "probability": 0.25
        },
        "buyer_knowledge_qualifier": "suspected",
        "seller_disclosure_status": "not_disclosed",
        "coverage_likelihood": "excluded_tax_specific_policy",
        "supporting_documentation": ["tax_returns_3yr.pdf"],
        "w&i_note": "Tax transfer pricing audits typically need separate tax indemnity (18-24 month cap)"
      }
    ],
    "monte_carlo_integration": {
      "total_contingency_p50": 4100000,
      "total_insurable_exposure_calculated": 7600000,
      "rationale": "Sum of mid-range exposures minus seller's disclosed items",
      "recommendation": "Seek W&I coverage of €8M to cover p50 + 95% confidence buffer"
    }
  }
}
```

### Campos Requeridos por Aseguradoras

Los brokers internacionales (AON, Marsh, Howden) solicitan en fase de underwriting:

| Campo | Descripción | Obligatorio | Ejemplo |
|-------|-------------|------------|---------|
| **risk_category** | Clasificación estándar (IP, Labor, Tax, Compliance, Contractual) | Sí | "IP title defects" |
| **estimated_exposure_eur** | Rango low/mid/high con probabilidad | Sí | {"low": 500k, "mid": 2M, "high": 8M, "probability": 0.45} |
| **buyer_knowledge_qualifier** | "unknown", "disclosed_in_da", "suspected", "known" | Sí | "unknown" |
| **seller_disclosure_status** | "disclosed_schedule", "not_disclosed", "partially_disclosed" | Sí | "not_disclosed" |
| **supporting_documentation** | Lista de docs proporcionados a broker | Sí | ["registro_oepm.pdf", ...] |
| **coverage_likelihood** | "covered", "excluded", "sublimited", "separate_cap" | Recomendado | "excluded_if_co_founder_identifiable" |
| **w&i_note** | Justificación de cobertura/exclusión basada en market practice | Recomendado | "Typically excluded under standard IP reps..." |

---

### Matriz de Exclusiones Estándar (Market Practice)

```
CATEGORÍA          │ TÍPICAMENTE CUBIERTO        │ EXCLUIDO/SUBLIMITADO
───────────────────┼────────────────────────────┼──────────────────────
IP REPS            │ Ownership, validity        │ Co-founder IP if assignor traceable
LABORAL            │ Undisclosed litigios       │ Labor claims (only defend costs)
                   │ Benefit plan legality      │ Known claims in SPA
───────────────────┼────────────────────────────┼──────────────────────
TAX                │ Transfer pricing (separate)│ Routine audits, soft law changes
                   │ Deferred tax assets        │ IRPF contingencies (separate cap)
                   │ Loss of tax benefits       │ Establish. permanente (reaseguro)
───────────────────┼────────────────────────────┼──────────────────────
COMPLIANCE         │ Regulatory violations      │ Known violations in disclosure schedule
                   │ Unlicensed activities      │ Change in law (soft law exclusion)
───────────────────┼────────────────────────────┼──────────────────────
CONTRACTUAL        │ Key customer concentration │ Known contract terminations
                   │ Unregistered IP licenses   │ IPO-related contractual changes
```

---

### Integración: De Monte Carlo a Póliza W&I

**Paso 1: Cuantificación Aggregate**
```
P10 percentile:  €1.2M  (muy optimista)
P50 percentile:  €4.1M  (base case)
P90 percentile:  €8.5M  (conservador)

IBNR (Incurred But Not Reported): +€500k-1M
```

**Paso 2: Mapeo a Cobertura de Aseguradora**
```
Exposure P50                     €4.1M
+ IBNR Buffer (20%)              €0.8M
+ Sublimit Labor riesgos         €1.5M
+ Separate Tax cap               €1.2M
─────────────────────────────────────
TOTAL INSURABLE EXPOSURE         €7.6M

Recomendación de límite W&I:     €8.0M (10% buffer)
Deductible recomendado:          €400k (estándar 1% deal)
Retention total:                 €900k (deductible + buyer reserve)
```

**Paso 3: Estimación de Prima**
```
Tasa de mercado (SaaS, €40M):    3% del límite
Prima estimada €8M × 3%:         €240k
Con reaseguro (established co):  €120k-180k
```

---

### Caso Práctico: SoftCorp W&I Submission Pack

**Resumen ejecutivo para broker:**

```
Target: SoftCorp Spain
Deal size: €40M | Closing: June 2024

TOP 3 EXPOSURES PARA W&I:
───────────────────────────────────────────
1. IP TITLE (EP3847395 ownership)
   Exposure: €2M (mid) | Probability: 45%
   Status: Unknown to buyer, not disclosed
   Coverage: EXCLUDED (co-founder identifiable)
   → Negotiate separate IP indemnity or price reduction

2. LABOR (ESOP undisclosed)
   Exposure: €1.5M (mid) | Probability: 30%
   Status: Disclosed schedule
   Coverage: SUBLIMITED (defend costs only)
   → Structure as escrow holdback vs insurance

3. TAX (Transfer pricing)
   Exposure: €450k (mid) | Probability: 25%
   Status: Not disclosed, undocumented
   Coverage: Separate tax indemnity (18-month cap)
   → Obtain TP documentation or negotiate tax indemnity

TOTAL INSURABLE EXPOSURE: €7.6M
COVERAGE RECOMENDADO: €8M (póliza principal) + €1-2M (tax indemnity)
DEDUCTIBLE: €400k | RETENTION: €900k
PRIMA ESTIMADA: €120-180k (tasa 3% con reaseguro)
```

---

## Trazabilidad de Supuestos (Audit Trail & Disclaimers)

La evaluación de riesgos se basa en análisis documental y modelos probabilísticos. Para evitar falsa seguridad y garantizar transparencia, cada scoring debe incluir trazabilidad completa de fuentes, supuestos y confianza analítica.

### Formato de Trazabilidad Requerida (Audit Trail)

```json
{
  "risk_finding": {
    "id": "IP-001",
    "titulo": "Patent EP3847395 titularidad unclear",
    "riesgo_score": 7.8,
    "audit_trail": {
      "extraido_por": "juan.torres@legaltech.es",
      "fecha_extraccion": "2024-02-06",
      "fuentes_documentales": [
        {
          "documento": "Registro OEPM EP3847395",
          "tipo": "public_registry",
          "fecha_consulta": "2024-02-05",
          "titular_registrado": "Carlos García Álvarez (persona física)",
          "estatus": "active",
          "claims": "Method for real-time ML optimization"
        },
        {
          "documento": "Estatutos Sociales SoftCorp (reforma 2021)",
          "tipo": "corporate_bylaws",
          "fecha_consulta": "2024-02-06",
          "mención_ip": "IP assets held in holding subsidiary per Article 5.3",
          "actualización": "2021-04-15"
        },
        {
          "documento": "Acta JGA 2021-06-20 (salida co-founder)",
          "tipo": "board_minutes",
          "fecha_consulta": "2024-02-06",
          "observacion": "No mention of patent assignment; co-founder dissolution clause silent on IP"
        },
        {
          "documento": "Acuerdo Cesión Incompleto (draft, sin firmar)",
          "tipo": "transaction_doc",
          "fecha_consulta": "2024-02-06",
          "estatus": "draft_unsigned",
          "comentario": "Cesión de derechos morales y patrimoniales pero sin registro OEPM"
        }
      ],
      "supuestos_clave": [
        "Se asume que registro OEPM es de autoridad única (cierto en ES)",
        "Se asume que cesión sin registro no surte efectos de publicidad (Art. 17 LP 11/1988)",
        "Se asume que co-founder, aunque exited, retiene rights si no hay cesión registrada",
        "Se asume que buyer no tiene knowledge de issue (no disclosed en SPA)"
      ],
      "lagunas_data": [
        "Falta: Licencia de explotación actual con co-founder",
        "Falta: Correspondencia entre SoftCorp y co-founder 2021-2024 sobre IP status",
        "Falta: Informe de counsel externo validando titularidad pre-cierre",
        "Falta: Suscripción de non-assertion letter por co-founder"
      ],
      "nivel_confianza": {
        "score": 0.65,
        "justificacion": "Medium confidence: registry data clear, but assignment chain incomplete. Missing direct correspondence with co-founder post-2021."
      },
      "sensitivity_analysis": {
        "si_cesion_registrada": "Confidence → 0.95 (RED downgrade a YELLOW)",
        "si_non_assertion_letter": "Confidence → 0.85, Exposure → €0-500k",
        "si_co_founder_insolvente": "Exposure → €8M (co-founder rights worthless)"
      }
    }
  }
}
```

### Elementos Obligatorios en Cada Riesgo

| Elemento | Propósito | Ejemplo |
|----------|-----------|---------|
| **extraido_por** | Responsabilidad analítica | juan.torres@legaltech.es |
| **fecha_extraccion** | Temporalidad (docs pueden cambiar) | 2024-02-06 |
| **fuentes_documentales** | Trazabilidad al origen | OEPM registry, Board minutes, etc. |
| **supuestos_clave** | Explicitación de premise no testeada | "Asume co-founder no cedió IP" |
| **lagunas_data** | Transparencia de incompletitud | "Falta non-assertion letter" |
| **nivel_confianza** | Métrica cuantitativa 0-1 | 0.65 = medium confidence |
| **sensitivity_analysis** | Scenarios para cambiar la scoring | If cesión registrada → downgrade risk |

---

### Disclaimer Template (Obligatorio en Reportes)

**Insértese en sección "Legal Disclaimers" de todo reporte:**

```
═══════════════════════════════════════════════════════════════════════

AVISO LEGAL - ANÁLISIS DE RIESGOS

Este análisis de riesgos se basa exclusivamente en los documentos
proporcionados por el cliente y análisis de due diligence conducido por
[Firma legal / Equipo de análisis] entre [fechas del análisis].

LIMITACIONES EXPLÍCITAS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. NO SUSTITUYE ASESORÍA JURÍDICA: Este análisis es soporte cuantitativo
   para decisión de compra. No reemplaza dictamen de counsel especializado
   en corporativo, laboral, fiscal e IP.

2. INCOMPLETITUD DOCUMENTAL: Análisis sujeto a documentación incompleta.
   Nuevos documentos, litigios ocultos o cambios legislativos pueden
   alterar significativamente las conclusiones.

3. SUPUESTOS DE MERCADO: Scoring basado en prácticas de Magic Circle
   (CC, A&O). Aplicabilidad varía por jurisdicción, tamaño deal,
   capacidad negociadora.

4. NO AUDITADO: Los números de contingen cias son estimaciones
   probabilísticas (Monte Carlo), no valores auditados.

5. CAMBIOS LEGISLATIVOS: Análisis fiscal y laboral sujeto a cambios
   de ley. RDL, resoluciones Inspección, jurisprudencia post-análisis
   no están incluidas.

6. CONFIDENCIALIDAD: Este análisis es confidencial y para uso exclusivo
   de [Buyer name]. No puede ser divulgado a terceros sin consentimiento.

DISCLAIMER DE RESPONSABILIDAD:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Firma / Equipo] no asume responsabilidad por:
- Errores u omisiones en documentación proporcionada
- Cambios legislativos, regulatorios o jurisprudenciales post-análisis
- Incumplimiento de obligaciones de disclosure por seller
- Decisions de deal basadas exclusivamente en este análisis
- Daño derivado de confianza en scores sin validación por counsel

═══════════════════════════════════════════════════════════════════════
```

---

### Version Control & Iteración de DD

Dado que DD es iterativa (inicial, due diligence profundo, post-LOI), registrar versiones:

```json
{
  "version_history": [
    {
      "version": "1.0",
      "fecha": "2024-02-06",
      "fase": "Initial DD",
      "documentos_incluidos": 156,
      "red_count": 3,
      "weighted_risk_score": 6.2,
      "cambios_vs_anterior": "Initial version"
    },
    {
      "version": "1.1",
      "fecha": "2024-02-20",
      "fase": "Post-LOI intensive",
      "documentos_incluidos": 312,
      "red_count": 2,
      "weighted_risk_score": 5.8,
      "cambios_vs_anterior": "Added IP non-assertion letter (confidence IP-001 → 0.85). ESOP plan approved in JGA (LABOR-001 downgrade to YELLOW). No new material risks identified."
    },
    {
      "version": "2.0",
      "fecha": "2024-03-15",
      "fase": "Final DD pre-closing",
      "documentos_incluidos": 450,
      "red_count": 1,
      "weighted_risk_score": 3.2,
      "cambios_vs_anterior": "Transfer pricing documentation received and analyzed (no adjustment needed). IP-001 resolved via escrow holdback of €1.5M. Only TAX-001 unresolved (separate tax indemnity negotiated)."
    }
  ]
}
```

---

## Visualización Interactiva

```html
<!--Heatmap HTML con hover-details-->
    IP       Labor    Fiscal  Compliance  Contractual
Riesgo: 🟥🟨  🟥🟨🟡  🟢🟢🟢   🟢🟢🟡      🟢🟢🟡

[Hover IP-RED] → "EP3847395 ownership unclear, 5% deal risk"
[Click] → expand IP-001, ver documentos, toggle escrow/insurance scenarios
```

---

## Templates de Industria

Cada industria tiene categorías y thresholds propios:

- **Tech**: IP (patents, code ownership), compliance (GDPR, AML), labor (key person, ESOP)
- **Pharma**: regulatory (FDA, EMA), patent expiry, clinical trials continuity
- **Real Estate**: title, environmental liens, zoning, lease expiries
- **Energy**: environmental remediation, permits, supplier contracts (fuel, capacity)
- **Financial Services**: regulatory approvals, complaints register, compliance infrastructure
