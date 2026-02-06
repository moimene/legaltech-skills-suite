---
name: cap-table-simulator
description: Simular tablas de capitalización complejas en startups españolas incluyendo protecciones anti-dilución (full ratchet, broad-based weighted average), drag-along/tag-along, convertibles (SAFE [atípico en Derecho español], notas con cap y descuento), ESOP con régimen fiscal diferido (Ley 28/2022 Art. 43), vesting schedules e impacto fiscal. Cascadas de liquidación (waterfall) con seniority y participación. Advertencia: SAFE requiere adaptación contractual/fiscal; stock options acogen exención IRPF 50.000€/año diferida. Contextos: análisis de term sheet, impacto de Series B con SAFE conversion, ESOP expansion, planificación de exit, certificación startup ENISA.
---

# Cap Table Simulator

## Simulación de Instrumentos de Equity

Modelar estructuras de capital de startups requiere considerar múltiples clases de instrumentos, protecciones de inversores y derechos de liquidación. En España, el ecosistema startup (Ley 28/2022) permite estructuras flexibles con consideraciones fiscales específicas (Art. 43 incentivos por opciones).

---

## Topología de Procesamiento

```
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Cap Table    │→│ Parser &     │→│ Validación   │
│ (CSV/JSON)   │ │ normalización│ │ (Ley 28/22) │
└──────────────┘ └──────────────┘ └──────┬───────┘
                                         │
        ┌────────────────┬───────────────┼────────────────┬─────────────────┐
        │                │               │                │                 │
        ▼                ▼               ▼                ▼                 ▼
  Anti-dilution    Waterfall          Vesting        ESOP expansion    Tax analysis
  (full ratchet    (liquidation       simulation     (Ley 28/22 Art.43) (retention)
   vs weighted)     preference)
        │                │               │                │                 │
        └────────────────┴───────────────┼────────────────┴─────────────────┘
                                        ▼
                        Informe consolidado + escenarios
```

---

## Aplicar cuando

- **Term sheet negociación**: evaluar impacto de full ratchet vs weighted average anti-dilution
- **Series B planning**: convertir SAFE a equity considerando cap, descuento y spark (down round protection)
- **ESOP setup**: simular vesting schedule (4-year cliff, monthly acceleration) con impacto fiscal
- **Exit analysis**: calcular retornos de cada shareholder con seniority de preferred vs common
- **Down round strategy**: evaluar protecciones anti-dilución en nuevas rondas (Ley 28/2022 incentivos)

---

## Instrumentos Soportados

| Instrumento | Parámetros Clave | Notas Fiscales |
|-------------|------------------|-----------------|
| **Common Stock** | Shares, vesting cliff/schedule | Tax-neutral under Ley 28/2022 if ESOP |
| **Preferred Stock** | Liquidation pref, participation, seniority | Tratamiento diferenciado según participación |
| **SAFE** | Cap, descuento, MFN, pro-rata | No convertida automáticamente (evento de conversión) |
| **Convertible Note** | Principal, tasa, vencimiento, cap, descuento | Conversión en próxima ronda o valuación trigger |
| **Stock Options (ESOP)** | Strike, vesting (4yr/1yr cliff), expiration | **Art. 43 Ley 28/2022**: deducción fiscal hasta 1M€/año |
| **Phantom Shares / SARs** | Strike, cash settlement | Liquidación en efectivo, impact waterfall |
| **Drag-along / Tag-along** | Threshold (>50%, >75%), derechos | Validez según LSC + LMERCA para startup |

---

## Advertencia Legal: SAFE en Derecho Español

**Instrumento atípico**: Los SAFE (Simple Agreements for Future Equity) no tienen equivalente tipificado en la Ley de Sociedades Anónimas (LSC) ni en el Código de Comercio. Su tratamiento legal en España presenta incertidumbre jurídica.

### Problemas de Calificación Legal

A falta de tipificación legislativa, las Autoridades Tributarias (AT) pueden reinterpretar un SAFE como:

- **Préstamo participativo** (Art. 20 RDL 7/1996, de 7 de junio): si incluye participación en resultados
- **Cuenta en participación** (Arts. 239-243 CCom): si se estructura como aportación sin asociación formal
- **Contrato atípico** mixto: combinación de rasgos de préstamo, opción y equity

**Riesgo**: La AT puede recharacterizar sustancialmente el instrumento en auditoría o litigio fiscal, alterando:
- Tratamiento de la conversión (evento taxable o no)
- Base imponible para ganancias patrimoniales
- Deducibilidad de gastos (intereses vs. dividendos)

### Tratamiento Fiscal

La administración tributaria evalúa la "sustancia económica" del SAFE:

1. **Conversión automática a equity**: puede tributar como ganancia patrimonial en momento de conversión (no diferida)
2. **Intereses implícitos o descuentos**: pueden ser reclasificados como renta de capital
3. **Falta de claridad en mechanics**: SAFE sin especificación de conversión o trigger → riesgo de nulidad o reinterpretación

### Recomendación de Adaptación

Para operar en España con SAFE o instrumentos similares:

- **Formalización notarial**: constituir la obligación mediante escritura pública (art. 1227 CC) para mayor certeza legal
- **Pacto de conversión explícito**: detallar trigger, precio de conversión (cap, descuento), seniority conforme a LSC (arts. 295-317)
- **Dictamen fiscal**: obtener opinión de asesor fiscal sobre calificación y consecuencias IRPF/Patrimonio
- **Adaptación a LSC**: si es factible, estructurar como aumento de capital con exclusión de preferential subscription (art. 308 LSC) en lugar de SAFE puro

### Caso de Riesgo

Startup recibe €500k SAFE sin conversión mechanics explícita ni escritura notarial. En Serie B, inversores intentan convertir a común. AT audita y reinterpreta SAFE como préstamo participativo. Resultado:
- Startup debe tributar diferencias de valor en conversión
- Conflicto sobre seniority en insolvencia
- Posible requerimiento de regularización cadastral (Impuesto sobre el Patrimonio)

---

## Análisis Anti-Dilution

```python
# Full Ratchet: Nueva valuation < anterior
# Fundadores dilución severa en down round
full_ratchet_new_price = serie_b_ppp / (serie_a_shares / serie_a_capital)

# Broad-Based Weighted Average: Mitiga impacto down round
weighted_new_price = (serie_a_capital + serie_b_capital) /
                     (serie_a_shares + serie_b_shares)
```

**Escenario**: Ronda A a €10/share (1M€), Ronda B a €5/share (2M€) down round
- Full Ratchet: €5 (severe dilution)
- Weighted Avg: €6.67 (balanced protection)

---

## Parámetros de Liquidation Preference

```python
PreferredStock(
    multiple=1.0,              # 1x, 2x no-participation
    participation=False,       # True = participates after pref return
    participation_cap=3.0,     # Si participa, cap at 3x investment
    seniority=1,              # Orden en waterfall (1=first to receive)
    anti_dilution="weighted"  # "full_ratchet" or "weighted_average"
)
```

---

## Régimen Fiscal Stock Options (Ley 28/2022)

El artículo 43 de la Ley 28/2022, de 21 de diciembre, de fomento del ecosistema de startups, establece un régimen fiscal preferente para planes de opciones sobre acciones (ESOP) en empresas certificadas como startup emergente.

### Incentivos IRPF (Art. 43 Ley 28/2022)

**Exención en origen y diferimiento tributario**:

| Parámetro | Detalle |
|-----------|---------|
| **Límite anual exención** | €50.000/año (incrementado desde €12.000 del régimen anterior) |
| **Momento de tributación** | **Diferido**: No tributa al ejercicio de opciones, sino a la transmisión de acciones |
| **Tipo impositivo aplicable** | Ganancias patrimoniales: 19-26% según Ley 12/2023 (Art. 17.2 LIRPF) |
| **Requisitos empresa** | • Certificación como startup emergente (ENISA) • Período mínimo de tenencia según plan |
| **Requisitos plan** | • Aprobación por Junta General de Accionistas (JGA) • Inclusión en plan escrito • Límite de participación (no superar determinada % del capital) |

**Mecánica fiscal**:
1. **Ejercicio de opciones**: empleado ejercita opción a strike price (ej. €3/share). NO hay tributación en este momento si cumple requisitos.
2. **Tenencia**: acciones se mantienen en cartera del empleado.
3. **Transmisión/exit**: al vender las acciones (exit, M&A, secundaria), tributa como ganancia patrimonial = (precio venta - strike price) × número acciones. La diferencia entre FMV al ejercicio y strike se exonera (hasta €50k/año).

**Ejemplo práctico**:
- Opción: 1.000 acciones @ strike €3/share (aprobado en plan ESOP JGA)
- Ejercicio (año 2025): empleado paga €3.000 (1.000 × €3). SIN tributación.
- Exit 2028 @ €20/share: vende por €20.000. Ganancia patrimonial = (€20 - €3) × 1.000 = €17.000. Tributa 19% = €3.230.
  - Parte exonerada (diferencial en origen): (€10 FMV al ejercicio - €3 strike) × 1.000 = €7.000, exenta si ≤ €50k/año acumulado.

### Interacción con Ley de Sociedades Anónimas (LSC)

**Art. 308 LSC (Derecho de Suscripción Preferente)**:
- Toda emisión de nuevas acciones genera derecho de suscripción preferente a accionistas existentes (proporcional a participación).
- Para ESOP: la JGA **debe excluir expresamente** este derecho (art. 308.2 LSC) para que empleados puedan suscribir opciones sin competencia de shareholders.
- **Resolución JGA necesaria**: "Se excluye el derecho de suscripción preferente conforme a art. 308.2 LSC para la emisión de opciones del plan ESOP 2024-2028".

**Art. 304 LSC (Asignación Gratuita de Acciones)**:
- Si el plan contempla asignación gratuita (bonus shares sin contraprestación), requiere igualmente autorización JGA y fijación de procedimiento.
- Raro en startups españolas (típicamente strike > 0).

**Art. 295-297 LSC (Aumento de Capital)**:
- Cuando opciones se ejercitan y se convierten en acciones, se ejecuta aumento de capital (desembolso de strike).
- Requiere:
  - Existencia de acuerdo previo (art. 297: delegación a administración si aprobado previamente en JGA)
  - Boletín Oficial del Registro Mercantil (BORM) si capital social > umbral
  - Inscripción en Registro Mercantil

### Impacto de Ley 12/2023 (Reforma del Régimen de Ganancias Patrimoniales)

La Ley 12/2023, de 24 de febrero, modificó el régimen de tributación de ganancias patrimoniales:

| Plazo tenencia | Tarifa (2024-2025) | Notas |
|---|---|---|
| ≤ 1 año | 26% | Corto plazo |
| 1-3 años | 23% | Plazo medio |
| > 3 años | 19% | Plazo largo (típico en exit/M&A startups) |

**Aplicación a stock options**: el diferimiento de tributación bajo Art. 43 Ley 28/2022 es complementario. La reducción por plazo se calcula sobre la ganancia patrimonial total al exit, siempre que se cumpla requisito de tenencia mínima (generalmente 3 años para reducción a 19%).

### Ejemplo Completo: ESOP de 500k Opciones

**Contexto empresa**:
- TechStartup Spain, certificada startup emergente (ENISA)
- Capital social pre-ESOP: 1.000.000 acciones ordinarias
- Valuación pre-ESOP: €10M post-money

**Plan ESOP Aprobado JGA 1 Feb 2024**:
- 500.000 opciones (5% dilución al llegar a full dilution)
- Strike price: €2.00/share (FMV al plan announcement: €10/share)
- Vesting: 4-year with 1-year cliff
- Expiration: 10 años
- Tenencia mínima: 3 años post-ejercicio

**Resolución JGA template**:
```
"Aprobar plan de opciones sobre acciones denominado ESOP 2024-2028,
con máximo 500.000 opciones, strike €2.00/share, vesting 4yr/1yr cliff.
EXCLUIR derecho de suscripción preferente conforme Art. 308.2 LSC
para emisiones derivadas del presente plan. DELEGAR en Consejo
Administración ejecución y términos (art. 297 LSC)."
```

**Timeline de Eventos Fiscales**:

| Fecha | Evento | Impacto Fiscal |
|-------|--------|---|
| 1 Feb 2024 | JGA aprueba ESOP | Sin impacto (acto administrativo) |
| 1 Mar 2024 | Empleado A recibe 10.000 opciones | Sin impacto (opción sin valor fiscal) |
| 1 Mar 2025 | 2.500 opciones vestan (cliff completado) | Sin impacto (aún no ejercidas) |
| 15 Ago 2025 | Empleado A ejerce 5.000 opciones @ €2 (aumento capital) | **SIN TRIBUTACIÓN** (Art. 43 Ley 28/22): diferencial €10/sh - €2/sh = €8/sh × 5.000 = €40k exonerado (< €50k límite) |
| 31 Dic 2027 | Empleado A vende 5.000 acciones @ €25 (post-Series-B) | **Ganancia patrimonial**: (€25 - €2) × 5.000 = €115.000. Tributa 19% (plazo > 3 años) = €21.850. Parte exonerada en origen (€8/sh) no vuelve a tributar. |

**Cálculo final para empleado A**:
- Coste total: 5.000 opciones × €2 = €10.000 ejercidas
- Venta: 5.000 acciones × €25 = €125.000
- Ganancia: €125.000 - €10.000 = €115.000
- **Impuesto IRPF (ganancias patrimoniales)**: €115.000 × 19% = €21.850
- **Rentabilidad neta**: €125.000 - €10.000 (coste) - €21.850 (impuestos) = €93.150 (~12.5x sobre inversión inicial en opciones)

---

## Ejemplo Concreto: Series B Round + SAFE Conversion + ESOP

**Empresa**: TechStartup Spain (2+ años operación, startup bajo Ley 28/2022)

### Cap Table Pre-Series B
```csv
holder,instrumento,shares,price_per_share,tipo,vesting_status
Fundador A,Common,2000000,0.001,Common,100%
Fundador B,Common,2000000,0.001,Common,100%
Co-founder C,Options,500000,0.001,ESOP,2yr vested (50%)
Seed Investor A,Preferred Seed,250000,2.00,Pref 1x non-part,100%
ESOP Pool (non-allocated),Options,1000000,3.00,ESOP,0%
```

### Events Simulables

| Evento | Cálculo | Impacto |
|--------|---------|--------|
| **SAFE Conversion** | SAFEs de €500k + €300k (caps €10M, descto 20%) → Pref Series B | 1.2M nuevas acciones Pref B |
| **Series B Cierre** | €5M @ €15/share ppp (post-money €20M) | 333k nuevas Pref B shares |
| **Anti-dilution** | Seed A activar weighted average (down round scenario) | New ppp ~€12-14 |
| **ESOP Vesting** | Aceleración 4-year cliff (1yr acantilado); Co-founder C accelerate 50% | 250k nuevas acciones disponibles |
| **Drag-along** | >75% preference stack can force sale → waterfall | Ordinal pago |

---

## Input: Cap Table CSV

```csv
holder,instrumento,shares,precio_base,seniority,liq_pref_multiple,participation,vesting_cliff_meses,vesting_total_meses
Fundador A,Common,2000000,0.001,99,0,false,0,0
Fundador B,Common,2000000,0.001,99,0,false,0,0
Co-founder C,ESOP,500000,0.001,99,0,false,12,48
Seed Investor A,Preferred Seed,250000,2.00,1,1.0,false,0,0
ESOP Pool,ESOP,1000000,3.00,99,0,false,0,0
SAFE Investor X,SAFE,500000,10000000,2,0,false,0,0
SAFE Investor Y,SAFE,300000,10000000,2,0.20,false,0,0
```

---

## Output: Simulación Completa (Series B → Exit)

```json
{
  "operacion": "TechStartup_Series_B_2024",
  "fase": "Series B + ESOP Acceleration",
  "cap_table_pre_series_b": {
    "total_shares": 7250000,
    "holders": [
      {
        "nombre": "Fundador A",
        "shares": 2000000,
        "porcentaje": 27.59%,
        "instrumento": "Common"
      },
      {
        "nombre": "SAFE Investor X",
        "shares": 0,
        "outstanding": "SAFEs: €500k",
        "conversion_trigger": "Series B cierre"
      }
    ],
    "vesting_status": {
      "Co-founder C": "50% vested (250k), 250k pending"
    }
  },
  "simulacion_serie_b": {
    "inversion": 5000000,
    "ppp_post_money": 15.00,
    "post_money_valuation": 20000000,
    "nuevas_shares": 333333,
    "dilution_effect": {
      "fundadores_antes": 54.79%,
      "fundadores_despues": 38.18%,
      "dilution_absolute": -16.61
    }
  },
  "conversion_safe": {
    "SAFE_Investor_X": {
      "monto": 500000,
      "cap": 10000000,
      "descuento": 0.20,
      "ppp_efectivo": 12.00,
      "shares_convertidas": 41667,
      "nota": "Cap favorece conversion, recibe más shares"
    },
    "SAFE_Investor_Y": {
      "monto": 300000,
      "ppp_efectivo": 12.00,
      "shares_convertidas": 25000,
      "participation_rights": true
    }
  },
  "esop_acceleration": {
    "evento": "Series B → aceleración parcial",
    "co_founder_c": {
      "vesting_antes": 250000,
      "acelerado": 250000,
      "total_disponible": 500000,
      "cliff_preservation": true
    },
    "nuevas_asignaciones": {
      "pool_size": 750000,
      "strike_price": 12.00,
      "vesting": "4yr/1yr cliff (Ley 28/2022 compliant)"
    }
  },
  "waterfall_exit_30m": {
    "total_proceeds": 30000000,
    "distribucion": [
      {
        "rango": 1,
        "holder": "Preferred Series B",
        "shares": 333333,
        "liq_pref": 1.0,
        "monto": 5000000,
        "multiple": 1.0,
        "nota": "1x non-participating"
      },
      {
        "rango": 2,
        "holder": "SAFE conversion (X+Y)",
        "shares": 66667,
        "liq_pref": 1.0,
        "monto": 1000000,
        "multiple": 1.3
      },
      {
        "rango": 3,
        "holder": "Preferred Seed",
        "shares": 250000,
        "liq_pref": 1.0,
        "monto": 500000,
        "multiple": 10.0
      },
      {
        "rango": 4,
        "holder": "Common pro-rata",
        "pool": 5000000,
        "desglose": {
          "Fundador A": 1487603,
          "Fundador B": 1487603,
          "Co-founder C (vested)": 371901,
          "ESOP pool": 371901,
          "otros": 280992
        }
      }
    ],
    "resumen_final": [
      {
        "holder": "Fundador A",
        "total": 1487603,
        "porcentaje": 4.96%,
        "multiple": 1489.6
      },
      {
        "holder": "Seed Investor A",
        "total": 1500000,
        "multiple": 30.0,
        "return_profile": "Excellent"
      },
      {
        "holder": "Series B Investors",
        "total": 5000000,
        "multiple": 1.0,
        "nota": "Capital recovery, no upside in 1x non-part"
      }
    ]
  },
  "analisis_fiscal": {
    "reino_unido": "N/A",
    "espana_ley_28_2022": {
      "esop_stock_options": {
        "articulo": "Art. 43 Ley 28/2022",
        "beneficiarios": "Empleados empresa startup emergente (certificación ENISA)",
        "mecanismo": "Tributación diferida: no tributa al ejercicio, sino al exit/transmisión",
        "exencion_irpf_anual": {
          "cantidad": 50000,
          "unidad": "EUR",
          "descripcion": "Exención en origen del diferencial entre FMV y strike price (incrementado desde €12.000 régimen anterior)",
          "acumulable": true,
          "nota": "Si empleado recibe opciones por €100k diferenciales en un año, solo exentos €50k"
        },
        "momento_tributacion": "Venta/transmisión de acciones post-ejercicio",
        "tipo_impositivo": "19-26% ganancias patrimoniales según plazo (Ley 12/2023)",
        "requisitos": [
          "Empresa certificada startup emergente",
          "Plan de opciones aprobado por JGA (resolución escrita)",
          "Exclusión de derecho de suscripción preferente (Art. 308.2 LSC)",
          "Tenencia mínima (típicamente 3 años) para aplicar tarifa reducida"
        ],
        "ejemplo_empleado": {
          "opciones": 5000,
          "strike_price": 2.00,
          "fmv_ejercicio": 10.00,
          "diferencial_exonerado": "€8/share × 5.000 = €40.000 (< €50k límite)",
          "precio_exit": 25.00,
          "ganancia_total": 115000,
          "impuesto_19_pct": 21850,
          "rentabilidad_neta": 93150
        }
      },
      "common_stock_founders": {
        "impacto": "Ganancias patrimoniales al exit",
        "tasa_aplicable": "19-26% según plazo tenencia (Art. 17.2 LIRPF - Ley 12/2023)",
        "aplazamiento": "Posible bajo art.42 LIRPF si reinversión inmediata en nueva startup"
      },
      "safe_considerations": {
        "riesgo": "SAFE atípico en Derecho español - reclasificación potencial como préstamo o cuenta participación",
        "recomendacion": "Formalización notarial + dictamen fiscal + adaptación LSC explícita"
      }
    }
  }
}
```

---

## Gráficos de Visualización

1. **Ownership pie chart**: Pre vs Post-Series B (barras apiladas)
2. **Waterfall chart**: Exit proceeds by shareholder (cascada descendente)
3. **Dilution tracker**: Ownership % por ronda (línea temporal)
4. **Vesting schedule**: ESOP acceleration timeline (Gantt chart)
