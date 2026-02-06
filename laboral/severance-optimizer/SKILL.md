---
name: severance-optimizer
description: Calculate severance cost under ET Art. 52/54/56, analyze collective (ERE/ERTE RD 1483/2012) vs. individual terminations, apply CBA improvements, compute salary base (Art. 26 ET), evaluate FOGASA coverage, and model judicial challenge scenarios with probability-weighted outcomes for dismissal risk management.
trigger_contexts:
  - "planning individual termination with cost certainty"
  - "evaluating restructuring scenarios (ERE vs. ERTE)"
  - "comparing post-2012 reform vs. pre-2012 transitional contracts"
  - "negotiating severance with judicial risk assessment"
  - "assessing FOGASA guarantees and unemployment implications"
---

# Severance Optimizer

## Application Scope

Calculate lawful severance payments (ET Art. 52-56), apply collective bargaining improvements, factor transitional salary regimes, model judicial challenge probability, and optimize termination strategy balancing cost certainty against litigation risk.

---

## Dismissal Typology & Legal Basis

| Type | Statutory Indemnity | CBA Range | Key Statute | Judicial Risk |
|------|---------------------|-----------|------------|---------------|
| **Objective/Economical** | 20 days/year (capped 12 months) | 22-28 days | ET Art. 52 | 35-45% |
| **Disciplinary (sound)** | None | Bonus negotiable | ET Art. 54.2 | <5% |
| **Procedure-deficient** | 33 days/year (capped 24 months) | 35-45 days | ET Art. 56.1.a | 65-80% |
| **ERE collective** | 20 days/year (negotiated) | RD 1483/2012 | ET Art. 51 | 20-35% |
| **ERTE (temporary suspension)** | None initially; severance if converted | Variable | RD 1483/2012 | 25-40% |
| **Mutual agreement** | Negotiated (tax-optimized) | No ceiling | ET Art. 49.1.a | <2% |

**Key reference**: RD 1483/2012 governs ERE/ERTE procedures; Art. 33 ET + FOGASA regime caps employer payment obligation.

---

## Salário Base Calculation (Art. 26 ET & TJUE jurisprudence)

The regulador daily rate includes:
1. **Fixed salary** (salario base)
2. **Salary in kind** (vivienda, vehículo, etc.) at official valuation
3. **3-year average bonus** (excludes extraordinary gratifications absent contractual entitlement)

Components **excluded** from regulador:
- Extraordinary bonuses (irregular, discretionary)
- Reimbursements (mileage, meals)
- Benefits with third-party value

```
Salario_regulador_diario = (Anual_fijo + Especie_anual + Media_bonus_36m) / 365
```

For contracts pre-2012 reform: apply **45 días/año régimen anterior** if acquisition date prior to RDL 3/2012 and employee expressly retained former regime.

---

## CBA Enhancement Mapping

Major Spanish bargaining agreements improve statutory minimums:

| Sector | Objective | Improcedent | Source | Floor Coverage |
|--------|-----------|-------------|--------|----------------|
| **Banking** | 25 days | 45 days | Conf. Banca 2020 | 98% major banks |
| **Insurance** | 23 days | 40 days | Aseguración 2019 | Large groups |
| **IT/Tech** | 22 days | 38 days | Sector tech 2022 | Varies |
| **Pharma** | 24 days | 42 days | Industria 2021 | Large pharma |
| **Retail** | 20 days (legal) | 33 days (legal) | Limited CBA coverage | Sector fragmented |

---

## Scenario Modeling: Senior Director Example

**Profile**: Director (15 years tenure since 2009; pre-reform contract preserved; salary €65K fixed + €15K bonus avg.)

**Calculation**:
```
Antigüedad: 15 años
Salario regulador: (65.000 + 0 + 15.000) / 365 = €219.18/día
Régimen anterior aplicable: Sí (pre-2012 contract preserved)

ESCENARIO 1 - Despido Objetivo + Causa Documentada
├─ Indemnización base: 45 días/año (régimen anterior) × 15 × €219.18 = €147.996
├─ Tope legal (Art. 52.1): 12 × salario mensual = €80.000
├─ Indemnización legal: €80.000
├─ Mejora convenio (banca 25d): 25 × 15 × €219.18 = €82.635 (vs. 20d legal = €65.754)
│  → Mejora adicional: €16.881
├─ Coste total procedente: €96.881
├─ FOGASA guarantee: Art. 33 ET → cubre hasta €26.000 si insolvencia
└─ Riesgo impugnación (documentación débil): 40% × €161.470 coste improcedencia = €64.588 valor esperado

ESCENARIO 2 - Judicial Finding of Improcedence (Art. 56.1.a)
├─ Indemnización 33 días/año: 33 × 15 × €219.18 = €108.384
├─ Tope: 24 × mensual = €130.000
├─ Total adeudado: €108.384 + +salarios no pagados período judicial
├─ Intereses legales (5% anual) sobre cantidad vencida
└─ Abogado empresa (condena):€8.000-15.000

ESCENARIO 3 - Mutuo Acuerdo (Transacción)
├─ Mercado para director 15 años: €95.000-125.000
├─ Impuestos diferidos si estructurado correctamente: puede mejorar situación vs. improcedencia
├─ Empleado pierde derecho desempleo (pese a Law 27/2022 parcial restoration)
└─ Documentar expresamente: exoneración responsabilidades reciprocas
```

**Recommendation matrix by risk tolerance**:
- **Conservative (low litigation budget)**: Scenario 3 (mutual agreement €110K) → certainty + minimal process
- **Moderately aggressive (solid documentation)**: Scenario 1 (objective + CBA improvement) → expected value €96.8K with 40% challenge risk
- **Aggressive (strong economic evidence)**: Scenario 1 with pre-dismissal consultoria audit → reduce challenge probability to 25%

---

## Collective Dismissal (ERE) vs. Temporary Suspension (ERTE)

### ERE Procedure (RD 1483/2012)

**Triggers**: Threshold of 10+ employees dismissed within 90 days OR 10% of workforce in companies <100.

**Mandatory process**:
1. Prior consultation period: **30 days minimum** (unions/worker representatives)
2. Administrative authorization request to labor authority
3. Severance payment: 20 days/year (improved by CBA) + vacation accrued
4. Unemployment eligibility preserved (empleado no ha renunciado)

**Advantage**: Statutory certainty, reduced individual challenge rate (20-30% vs. 35-45%), possible ERTE-to-ERE conversions preserve job protections partially.

### ERTE Procedure (RD 1483/2012 Art. 47)

**Nature**: Temporary suspension (suspension de contrato) for max 12 months initially; renewable 6 months.

**Key features**:
- No indemnization; employee receives unemployment benefits (cuota parte employer-financed)
- Employer maintains rehiring obligation
- If converted to ERE: statutory indemnity applies retroactively
- Social security contributions suspended (employer savings ~30%)

**Cost advantage vs. immediate ERE**: Save 30% contributions + delay indemnity outlay 12 months = positive NPV if recovery probability >30%.

---

## Interacción con FOGASA

**Marco normativo (Art. 33 ET)**: Fondo de Garantía Salarial protege créditos laborales en caso de insolvencia empresarial.

**Cobertura FOGASA**:
- Indemnización por despido: €26.536 máximo por empleado (2024; indexado anualmente)
- Salarios acumulados + vacaciones devengadas: hasta 30 días × salario diario
- **Límite por concepto**: cada crédito goza protección independiente hasta topes legales

**Aplicación Art. 33 ET - Procedimiento de reclamación**:
1. Solicitar **certificado de insolvencia** ante SPEE (Servicio Público Estatal de Empleo)
2. Si SPEE certifica insolvencia (litigio favorable al trabajador o liquidación concursal abierta)
3. Presentar denuncia ante FOGASA con documentación: sentencia, acta despido, liquidación pendiente
4. FOGASA responde en **hasta 30 días hábiles** desde recepción completa de solicitud
5. **Subrogación automática**: FOGASA asume derechos del trabajador contra la empresa concursada

**Derechos de subrogación**:
- FOGASA sustituye legalmente al trabajador en su crédito
- Participa en concurso como acreedor privilegiado (Art. 184 LC)
- Cobro prioritario respecto a acreedores ordinarios
- Timeline: inscripción en concurso dentro 5 días de pago a trabajador

**Ejemplo práctico - Director 15 años, despido objetivo €96.881**:
```
Escenario: Empresa declara insolvencia 3 meses tras despido

1. Trabajador acumula crédito: €96.881
2. Solicita certificado insolvencia (SPEE): confirmado
3. Denuncia FOGASA: presenta sentencia + finiquito pendiente
4. FOGASA cubre: €26.536 (tope legal)
5. Brecha no cubierta: €96.881 - €26.536 = €70.345
   ├─ Trabajador queda acreedor ordinario (bajo priority)
   └─ Recuperación: ~2-8% en concurso según patrimonio activo

Implicación: Empresa puede negociar mejor si riesgo insolvencia > 30%
├─ Aumentar indemnización a €26.536+ sin coste marginal
└─ FOGASA absorbe parte; empresa cubre diferencial
```

**Consideraciones estratégicas**:
- Si riesgo insolvencia > 25%, negociar acuerdo antes de declaración concursal
- FOGASA **no cubre** despidos por incapacidad temporal sostenida (Incapacidad Permanente → prestación SS, no indemnidad)
- Notificación denunciante: empresario debe informar sobre derecho a FOGASA en acta despido

---

## Simulación de Costes Totales de Despido

Modelo integral: **indemnización + finiquito + cotizaciones pendientes + riesgo judicial + costes procesales + daño reputacional**

### Estructura de Cálculo Integral

```
COSTE_TOTAL_DESPIDO = Indemnización + Finiquito + SS_Pendiente + Procesales + Riesgo_Judicial + Reputacional

Donde:

1. INDEMNIZACIÓN (dependiente tipología)
   ├─ Base legal: 20d/año (objetivo), 33d/año (improcedente), 45d/año (pre-2012)
   ├─ Mejora convenio colectivo: +5-15 días típico
   ├─ Topes: 12 meses (objetivo), 24 meses (improcedente)
   └─ Fórmula: [días × antigüedad × salario_regulador_diario] capped

2. FINIQUITO (obligatorio; incluye)
   ├─ Vacaciones devengadas (no disfrutadas) = días_acumulados × salario_diario
   ├─ Bonus/gratificaciones acumuladas (si devengo)
   ├─ Pagas extraordinarias prorrateadas (si no cobradas mensualmente)
   ├─ Comisiones pendientes (si variable contractual)
   └─ Seguridad Social: retenciones IRPF (indemnización parcialmente exenta hasta €180K) + cotización SS

3. COTIZACIÓN SEGURIDAD SOCIAL PENDIENTE
   ├─ Período de preaviso (si 30 días mínimo)
   ├─ Período litigio (meses desde despido hasta sentencia o acuerdo)
   ├─ Cuota empresa: ~30% de base reguladora mensual
   │  └─ Cálculo típico: [salario mensual + bonificaciones] × tasa sector × meses
   └─ Ejemplo director 15 años, 6 meses litigio:
       └─ SS pendiente = €6.575 × 30% × 6 = ~€11.835

4. RIESGO JUDICIAL (probabilidad-ponderado)
   ├─ Si despido objetivo con docs débil: 40% × coste improcedencia
   │  └─ Coste improcedencia = [33d × 15 años × €219.18] + intereses 5% + abogado €10K
   │  └─ EV = 0.40 × €161.470 = €64.588
   ├─ Si despido objetivo con docs sólido: 15-25% riesgo
   └─ Si mutuo acuerdo: <2% riesgo residual

5. COSTES PROCESALES
   ├─ Conciliación SMAC (obligatoria previa): €60-300
   ├─ Jurisdicción Social (si litigio)
   │  ├─ Tasas juzgado: ~0.5-2% cantidad reclamada (mín €300)
   │  ├─ Abogado empresa: €5K-15K según complejidad
   │  ├─ Perito laboral (si necesario): €2K-5K
   │  └─ Timeline: 6-18 meses típico
   ├─ Máximo coste**: ambas partes incurren; condenado paga gastos (Art. 141.2 LPRJS)
   └─ Ejemplo: €15K abogado + €1K tasas + €3K perito = €19K adicionales

6. DAÑO REPUTACIONAL (intangible; estimado)
   ├─ Sector conoce despidos improcedentes → riesgos retención
   ├─ Sindicatos pueden publicar litigio → presión social
   ├─ Impacto empleado: "despido injusto" etiqueta → difícil recolocación
   └─ Estimación conservadora: 10-20% indemnización base como factor intangible
       └─ Ejemplo: despido €96.881 → daño reput. ~€10K como provision contable

```

### Ejemplo Integrado - Director 15 años, Despido Objetivo Economía

**Escenario: Empresa solida, documentación moderada**

```
SUPUESTOS:
- Salario: €65K fijo + €15K bonus = €80K anual
- Antigüedad: 15 años (pre-2012 régimen preservado)
- Régimen: 45d/año (vs. 20d actual); mejora CBA banca 25d
- Documentación económica: moderada (3-4 meses pérdidas, pero no trimestral completo)
- Riesgo impugnación estimado: 40%

DESGLOSE COSTE INTEGRAL:

1. INDEMNIZACIÓN BASE
   ├─ Régimen anterior 45d/año aplicable: 45 × 15 × €219.18 = €147.996
   ├─ Tope legal (12 × 6.575): €78.900
   ├─ Indemnización legal neta: €78.900
   ├─ Mejora CBA (banca): 25d × 15 × €219.18 = €82.635
   │  (vs. 20d legal €65.754, diferencial +€16.881)
   └─ Total indemnización procedente: €78.900 + €16.881 = €95.781

2. FINIQUITO
   ├─ Vacaciones devengadas (24 días restantes): 24 × €219.18 = €5.260
   ├─ Bonus prorrateado 2 meses: (€15K/12) × 2 = €2.500
   ├─ Paga extra prorrateada: (€80K/14) = €5.714
   ├─ Retencion IRPF indemnización: €0 (dentro de €180K exención)
   ├─ SS aportación empleado (~8.35%): €95.781 × 8.35% = €7.998
   └─ Finiquito neto: €5.260 + €2.500 + €5.714 + €7.998 = €21.472

3. SEGURIDAD SOCIAL PENDIENTE (Empresa)
   ├─ Período preaviso 30 días: €6.575 × 30% = €1.973
   ├─ Período estimado litigio 6 meses: €6.575 × 30% × 6 = €11.835
   └─ SS total adeudada: €13.808

4. RIESGO JUDICIAL (Probabilidad-ponderado)
   ├─ Escenario A (60% prob.): Despido procedente
   │  └─ Coste: indemnización base €95.781
   ├─ Escenario B (40% prob.): Sentencia improcedencia
   │  ├─ Indemnización 33d: 33 × 15 × €219.18 = €108.384
   │  ├─ Tope 24 meses: €130.000
   │  ├─ Salarios período litigio 6m: €40.000
   │  ├─ Intereses 5% anual sobre vencidos: ~€2.000
   │  ├─ Abogado empresa (condena): €12.000
   │  └─ Coste improcedencia: €162.384
   │
   └─ Valor esperado: (0.60 × €95.781) + (0.40 × €162.384) = €57.468 + €64.953 = €122.421

5. COSTES PROCESALES ESPERADOS
   ├─ Conciliación SMAC: €200 (típico)
   ├─ Tasas juzgado social (si 50% prob litigio): 0.50 × 1.5% × €162.384 = €1.218
   ├─ Abogado empresa (esperado): 0.40 × €12.000 = €4.800 (ya incluido arriba)
   ├─ Perito laboral (si necesario; 30% prob): 0.30 × €3.500 = €1.050
   └─ Costes procesales esperados: €200 + €1.218 + €1.050 = €2.468

6. DAÑO REPUTACIONAL
   ├─ Factor sector: medio (banca = riesgo reputacional moderado)
   ├─ Estimación: 12% sobre indemnización base
   ├─ Cantidad: €95.781 × 12% = €11.494
   └─ Provision contable conservadora: €11.494

───────────────────────────────────────────
COSTE TOTAL INTEGRAL:

├─ Indemnización: €95.781
├─ Finiquito: €21.472
├─ SS pendiente: €13.808
├─ Riesgo judicial (EV): €122.421 (sustitye indem. + costes)
├─ Costes procesales adicionales (EV): €2.468
├─ Daño reputacional: €11.494
├─ COSTE_TOTAL (escenario procedente): €95.781 + €21.472 + €13.808 + €2.468 = €133.529
├─ COSTE_TOTAL (escenario improcedencia): €133.529 + (€162.384 - €95.781) = €200.132
└─ VALOR_ESPERADO_INTEGRAL: €122.421 + €21.472 + €13.808 + €2.468 + €11.494 = €171.663

COMPARATIVA ESTRATEGIAS:

Opción A: Despido Objetivo Documentado
├─ Coste base esperado: €122.421
├─ + gastos adicionales: €37.742 (finiquito + SS + procesales + reput.)
├─ = Coste total esperado: €160.163
└─ Riesgo residual: 40% impugnación

Opción B: Mutuo Acuerdo Transaccional
├─ Oferta mercado: €115.000
├─ Costes procesales: €500 (simple formalización)
├─ = Coste total: €115.500
├─ Riesgo residual: <2% (ambas partes acuerdan exoneración)
└─ AHORRO vs. Opción A: €44.663

Opción C: ERTE + Posterior ERE (si recuperación probable)
├─ Suspensión 6 meses: €0 indemnidad; SS empleado recibe 70% prestación desempleo
├─ Si después ERE 20d: 20 × 15 × €219.18 = €65.754
├─ = Coste total diferido: €65.754
├─ Riesgo: si empresa no recupera → litigio improcedencia igual
└─ AHORRO si recuperación: €94.409 vs. Opción A

RECOMENDACIÓN (Risk tolerance bajo):
└─ Opción B (Mutuo Acuerdo €115.000) minimiza riesgo y coste total
   ├─ Premium €-7.421 vs. Opción A (falso coste)
   ├─ Certidumbre legal + cierre rápido
   └─ Finiquito consentido = sin litigio futuro

RECOMENDACIÓN (Risk tolerance moderado):
└─ Opción A (Despido Objetivo) si documentación sólida
   ├─ Documentar: 4 trimestres resultados negativos
   ├─ Acta consulta sindical formalizada
   ├─ Comunicación clara causa económica (10d previos)
   └─ EV €160.163; reducible a €130K si docs +'s
```

---

---

## Social Security & Unemployment Implications

**Dismissal classification impact on employee benefits**:

| Dismissal Type | Unemployment Eligibility | Contribution Record | Duration Benefit |
|---|---|---|---|
| Objective (ET 52) | Sí, 100% | Preserved | 4.5 años típico |
| Disciplinary procedent (ET 54) | Sí, 100% | Preserved | 4.5 años típico |
| Improcedent (ET 56) | Sí, 100% (+ 20% bonus employer contrib.) | Preserved | 4.5 años |
| Mutual agreement | Sí, pero 50% employer contrib. por ley 27/2022 | Preserved | Reducido |

**Employer considerations**:
- Improcedent dismissal triggers 5% bonus-contribution to unemployment fund (Art. 268 LGSS)
- ERTE preserves contribution record for employee; delays cash outlay for severance
- Structured mutual agreement can optimize tax position for both parties (IRPF deductible fringe for employee if classified "indemnización por despido")

---

## Negotiation Scenarios: Probability-Weighted Outcomes

Given dispute risk, model negotiation space:

```
Objective case with 40% impugnation risk:

Expected value to employer = (60% × €96.881) + (40% × €161.470 improcedent coste)
                           = €58.128 + €64.588 = €122.716

Settlement offer range (reduces risk to ~5%):
├─ Low (signaling confidence): €105.000 → Savings €17.716 vs. EV
├─ Market (sector benchmark): €115.000 → Savings €7.716 vs. EV, but >95% acceptance
└─ High (maximize closure): €130.000 → Cost €7.284 above EV, but guarantees exit

Optimal offer: €115.000 (market-rate) = minimizes residual risk + avoids over-payment
```

---

## Inputs

```json
{
  "empleado": {
    "fecha_alta": "2009-03-15",
    "fecha_terminacion_propuesta": "2024-06-30",
    "categoria": "Director General",
    "salario_base_anual": 65000,
    "salario_especie_anual": 0,
    "bonus_promedio_36_meses": 15000,
    "convenio_colectivo": "Conf. Banca 2020",
    "contrato_pre2012_preservado": true,
    "motivo_extincion": "economico_documentado"
  },
  "empresa": {
    "solvencia": "solvente",
    "sector": "banca",
    "empleados_totales": 450,
    "otras_extincciones_90dias": 0
  },
  "documentacion": {
    "causa_economica_comprobable": true,
    "meses_perdidas": 8,
    "comunicacion_trabajador": "escrita_clara",
    "integridad_procedimiento": "rigurosa"
  }
}
```

---

## Output

```json
{
  "empleado": {
    "nombre": "[Anonimizado]",
    "antiguedad_años": 15,
    "antiguedad_regimen": "pre-2012 (45 días/año aplicable)",
    "salario_regulador_diario": 219.18,
    "salario_regulador_mensual": 6575
  },
  "escenarios": [
    {
      "tipo": "DESPIDO_OBJETIVO_ECONOMICO_PROCEDENTE",
      "probabilidad_judicial_viabilidad": 0.60,
      "indemnizacion_legal": {
        "base_dias": 20,
        "antigüedad_años": 15,
        "calculo": "20 × 15 × €219.18 = €65.754",
        "tope_legal": "12 × €6.575 = €78.900",
        "importe_neto": 65754,
        "aplicable_mejora_cba": true,
        "mejora_dias": 5,
        "mejora_importe": 16881,
        "indemnizacion_total_mejora": 82635
      },
      "costes_adicionales": {
        "preaviso_minimo_dias": 30,
        "vacaciones_devengadas": 6250,
        "seguridad_social_retenciones": 4105,
        "finiquito_total": 92990
      },
      "riesgos_judiciales": {
        "probabilidad_impugnacion": 0.40,
        "motivo_riesgo": "Documentación causa económica debería incluir reportes trimestres",
        "coste_si_improcedente": 161470,
        "gastos_legales_estimados": 10000,
        "valor_esperado_caso": 122716
      },
      "coste_esperado": 122716,
      "recomendacion": "Procedimiento objetivo viable si se documentan pérdidas mensuales 3+ meses consecutivos + acta consulta sindical"
    },
    {
      "tipo": "DESPIDO_IMPROCEDENTE_PACTADO",
      "negociacion_escenario": "ACUERDO_TRANSACCIONAL",
      "indemnizacion_dias": 33,
      "indemnizacion_importe": 108384,
      "tope_aplicable": false,
      "coste_negociacion_tipica": {
        "minimo": 105000,
        "mercado": 115000,
        "maximo": 130000
      },
      "ventajas": [
        "Certidumbre legal vs. litigio",
        "Finiquito consentido",
        "Preservación relación futura si recontratación posible"
      ],
      "desventajas": [
        "Reconocimiento implícito de vicio procedural",
        "Coste €3-8K superior a escenario objetivo documentado"
      ],
      "riesgo_residual": 0.02,
      "valor_esperado": 115800
    },
    {
      "tipo": "ERE_COLECTIVO",
      "aplicable": false,
      "razon": "Umbral 10 empleados no alcanzado en 90 días",
      "alternativa_si_multiples_extincciones": "Considerar ERE si 9+ empleados adicionales previstos en próximos 60 días"
    },
    {
      "tipo": "ERTE_CONVERSION",
      "recomendacion": "No aplicable a director con causa económica clara; ERTE señalizaría debilidad causal",
      "aplicable_solo_si": "Recuperación probable en 6-12 meses"
    }
  ],
  "recomendacion_optima": {
    "escenario": "DESPIDO_OBJETIVO_ECONOMICO_PROCEDENTE",
    "coste_esperado": 122716,
    "alternativa_certidumbre": "Acuerdo transaccional €115.000 (trade-off €7.716 premium vs. eliminación riesgo judicial)",
    "precondiciones": [
      "Documentar pérdidas mensuales consecutivas 3+ meses",
      "Acta formal consulta representantes trabajadores (30 días)",
      "Solicitud autorización laboral (si 10+ empl., tributario de ERE)",
      "Comunicación clara causa económica al empleado 10 días antes"
    ],
    "timeline": "Notificación → 30d pre-comunicación → Acta despido → Finiquito 7d"
  },
  "fogasa": {
    "cobertura_aplicable": true,
    "limite_cobertura": 26536,
    "proteccion_en_insolvencia": "FOGASA responde hasta €26.536 si empresa insolvente; resto a cargo trabajador",
    "procedimiento_reclamacion": "Solicitar certificado solvencia SPEE; si negativo, reclamación ante FOGASA en 30 días"
  },
  "seguridad_social": {
    "impacto_desempleo_empleado": "Derecho 100% a prestación desempleo; duracion ~4.5 años por antigüedad 15 años",
    "contribucion_extra_empleador": "5% bonus RETE si judicial posterior falla procedimiento (Art. 268 LGSS)",
    "retencion_irpf_indemnizacion": "Exempt up to €180.000 if severance-classified; retain €92.990 within exemption"
  }
}
```
