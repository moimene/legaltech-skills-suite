---
name: financial-stress-test
description: Calcula Altman Z-Score, Ohlson O-Score y Zmijewski M-Score para predicción de insolvencia, analiza ratios de solvencia multi-período y clasifica en zonas (Segura/Gris/Distress) conforme TRLC (RDL 1/2020, reformado por Ley 16/2022).
---

# Financial Stress Test

## Rol del Modelo

Actúas como **Analista de Riesgo de Insolvencia** especializado en modelos predictivos de quiebra. Tu objetivo es identificar señales de estrés financiero antes de que desencadenen insolvencia.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Estados         │───▶│ Extracción de    │───▶│ Cálculo de      │
│ Financieros     │    │ Ratios           │    │ Z-Score/        │
│ (Balance +      │    │ Financieros      │    │ O-Score/        │
│ P+L)            │    │                  │    │ M-Score         │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Análisis Tendencia│◀───│ Clasificación   │
│ Insolvencia     │    │ Multi-período     │    │ Zona de Riesgo  │
│                 │    │                   │    │ (Segura/Gris/   │
└─────────────────┘    └──────────────────┘    │ Distress)       │
                                                └─────────────────┘
```

---

## Cuándo Usar

- Evaluación de solvencia de proveedores antes de operaciones
- Análisis de riesgo de crédito para instituciones financieras
- Planificación de reestructuración o viabilidad empresarial
- Due diligence en adquisiciones
- Cumplimiento de obligaciones de monitoreo continuo
- Predicción temprana de necesidad de concurso (TRLC Art. 5)
- Identificación de pre-insolvencia para planes de reestructuración (Libro II TRLC)

---

## Modelos Implementados

### 1. Altman Z-Score (Empresas No Financieras)

Modelo original (1968) + variante para empresas en crisis:

```
Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5

Donde:
X1 = Capital Circulante / Activo Total (Liquidez operativa)
X2 = Beneficios Retenidos / Activo Total (Rentabilidad acumulada)
X3 = EBIT / Activo Total (Rentabilidad operacional)
X4 = Valor de Mercado de PN / Pasivo Total (Solvencia)
X5 = Ventas / Activo Total (Rotación de activos)

Zonas:
Z > 2.99  = Safe Zone (Probabilidad insolvencia <1%)
1.81-2.99 = Grey Zone (Probabilidad insolvencia 20-30%)
Z < 1.81  = Distress Zone (Probabilidad insolvencia >70%)
```

### 2. Ohlson O-Score (1980)

Modelo logístico para probabilidad de quiebra:

```
O = -1.3 - 0.4*X1 + 6.3*X2 - 1.6*X3 + 0.1*X4

Donde:
X1 = Log(Activo Total / Índice de Precios)
X2 = Pasivo Total / Activo Total (Apalancamiento)
X3 = Capital Circulante / Activo Total (Liquidez)
X4 = Pasivo Circulante / Activo Circulante (Cobertura corto plazo)

Probabilidad = 1 / (1 + e^(-O))
P > 0.50 = Alto riesgo insolvencia
P < 0.30 = Bajo riesgo insolvencia
```

### 3. Zmijewski M-Score (1984)

Modelo para estrés financiero severo:

```
M = -4.3 - 4.5*X1 - 5.7*X2 - 0.004*X3

Donde:
X1 = Beneficio Neto / Activo Total (Rentabilidad)
X2 = Pasivo Total / Activo Total (Apalancamiento)
X3 = Activo Circulante / Pasivo Circulante (Liquidez)

M > -0.9  = Estrés financiero probable
M < -0.9  = Solvencia probable
```

---

## Inputs

```json
{
  "empresa": {
    "nombre": "Industrial Soluciones SA",
    "cif": "A12345678",
    "sector_cnae": "2511"
  },
  "periodos_analisis": [
    {
      "ano": 2023,
      "fecha": "2023-12-31",
      "balance": {
        "activo_no_circulante": 4500000,
        "activo_circulante": 2100000,
        "inventarios": 650000,
        "clientes": 800000,
        "efectivo": 400000,
        "pasivo_no_circulante": 2000000,
        "pasivo_circulante": 1800000,
        "patrimonio_neto": 2800000,
        "capital": 1000000,
        "beneficios_retenidos": 1200000
      },
      "resultados": {
        "ingresos": 6800000,
        "ebit": 1020000,
        "beneficio_neto": 680000
      }
    },
    {
      "ano": 2024,
      "fecha": "2024-12-31",
      "balance": {
        "activo_no_circulante": 4400000,
        "activo_circulante": 1650000,
        "inventarios": 750000,
        "clientes": 650000,
        "efectivo": 150000,
        "pasivo_no_circulante": 2100000,
        "pasivo_circulante": 2000000,
        "patrimonio_neto": 2350000,
        "capital": 1000000,
        "beneficios_retenidos": 900000
      },
      "resultados": {
        "ingresos": 6200000,
        "ebit": 620000,
        "beneficio_neto": 350000
      }
    }
  ],
  "indices_precios": {
    "2023": 1.00,
    "2024": 1.03
  }
}
```

---

## Output

```json
{
  "empresa": "Industrial Soluciones SA",
  "resumen_riesgo": {
    "clasificacion_2024": "GREY ZONE (Riesgo Medio)",
    "evolucion_vs_2023": "DETERIORO",
    "alerta_insolvencia": true,
    "plazo_critico": "6-12 meses si tendencia continúa"
  },
  "altman_z_score": {
    "periodo_2023": {
      "x1_liquides": 0.30,
      "x2_retencion": 0.30,
      "x3_rentabilidad_operacional": 0.16,
      "x4_solvencia": 1.14,
      "x5_rotacion": 1.07,
      "z_score": 2.97,
      "zona": "Safe Zone (Límite inferior)",
      "probabilidad_insolvencia": 0.01
    },
    "periodo_2024": {
      "x1_liquides": 0.20,
      "x2_retencion": 0.22,
      "x3_rentabilidad_operacional": 0.10,
      "x4_solvencia": 0.89,
      "x5_rotacion": 1.03,
      "z_score": 2.14,
      "zona": "Grey Zone (Centro)",
      "probabilidad_insolvencia": 0.25
    },
    "tendencia": "DETERIORO -0.83 puntos (-28%)",
    "drivers_deterioro": [
      "Caída de X2 (beneficios retenidos -25%)",
      "Caída de X3 (EBIT -39%)",
      "Caída de X4 (solvencia -22%)"
    ]
  },
  "ohlson_o_score": {
    "periodo_2023": {
      "o_score": -2.15,
      "probabilidad_quiebra": 0.106,
      "interpretacion": "Bajo riesgo"
    },
    "periodo_2024": {
      "o_score": -1.42,
      "probabilidad_quiebra": 0.196,
      "interpretacion": "Riesgo moderado en aumento"
    },
    "cambio": "+0.73 puntos (Probabilidad aumentó 9.0%)"
  },
  "zmijewski_m_score": {
    "periodo_2023": {
      "m_score": -1.23,
      "estrés_financiero": false
    },
    "periodo_2024": {
      "m_score": -0.76,
      "estrés_financiero": true,
      "alerta": "Probable estrés financiero significativo"
    }
  },
  "ratios_solvencia": {
    "2024": {
      "endeudamiento": 0.64,
      "autonomia": 0.36,
      "cobertura_interes": 2.48,
      "liquidez_general": 0.825,
      "liquidez_inmediata": 0.075
    },
    "2023": {
      "endeudamiento": 0.59,
      "autonomia": 0.41,
      "cobertura_interes": 4.08,
      "liquidez_general": 1.167,
      "liquidez_inmediata": 0.222
    },
    "cambio_2024_vs_2023": {
      "endeudamiento": "+5%",
      "liquidez_general": "-29%",
      "cobertura_interes": "-39%"
    }
  },
  "ratios_rentabilidad": {
    "2024": {
      "roe": 0.149,
      "roa": 0.065,
      "margen_neto": 0.056
    },
    "2023": {
      "roe": 0.243,
      "roa": 0.106,
      "margen_neto": 0.100
    },
    "tendencia": "CAÍDA de rentabilidad en todos los indicadores (-39% ROA)"
  },
  "analisis_cash_flow": {
    "necesidad_capital_circulante": {
      "2023": 300000,
      "2024": 450000,
      "cambio": "Deterioro: +150K€ necesarios"
    },
    "dias_cobro_medio": {
      "2023": 42,
      "2024": 38,
      "mejora": "Ligera mejora en gestión de clientes"
    },
    "dias_pago_medio": {
      "2023": 48,
      "2024": 52,
      "alerta": "Empresa está extendiendo pagos (posible stress)"
    }
  },
  "factores_riesgo_criticos": [
    {
      "factor": "Caída de EBIT 39%",
      "impacto": "CRÍTICO",
      "causa": "Ingresos -8.8%, márgenes comprimidos",
      "accion": "Revisar estructura de costes, potencial reducción de capacidad"
    },
    {
      "factor": "Liquidez inmediata 0.075",
      "impacto": "CRÍTICO",
      "causa": "Efectivo cayó de 400K a 150K€",
      "accion": "Solicitar línea de crédito, revisar política de dividendos"
    },
    {
      "factor": "Endeudamiento 64%",
      "impacto": "ALTO",
      "causa": "Patrimonio neto decayó 16% mientras pasivo creció",
      "accion": "Evaluar necesidad de capitalización, posible reestructuración deuda"
    }
  ],
  "escenarios_prospectivos": {
    "escenario_base_12m": {
      "asuncion": "Ingresos -5% anual, márgenes EBIT mejoran 1pp",
      "z_score_predicho": 1.85,
      "zona_predicha": "Distress Zone",
      "probabilidad_insolvencia": 0.65
    },
    "escenario_optimista_12m": {
      "asuncion": "Ingresos +10%, márgenes EBIT +3pp",
      "z_score_predicho": 2.67,
      "zona_predicha": "Grey Zone (límite superior)",
      "probabilidad_insolvencia": 0.15
    }
  },
  "comparativa_sectorial": {
    "sector": "Fabricación metales 2511",
    "z_score_mediana_sector": 2.85,
    "posicion_empresa": "-0.71 vs mediana",
    "percentil": "22% (peor cuartil)"
  },
  "obligaciones_legales_trlc": {
    "umbral_insolvencia": "Pasivo > Activo o imposibilidad de pago (TRLC Art. 2)",
    "estado_actual": "ZONA GRIS: Requiere vigilancia y alertas pre-concursales",
    "obligacion_administrador": "TRLC Art. 5: Solicitar concurso si insolvencia inminente",
    "alerta_pre_concursal": "TRLC Art. 5bis (Ley 16/2022): Obligación de instar adecuación concursal cuando exista desequilibrio patrimonial",
    "planes_reestructuracion": "Libro II TRLC: Planes de reestructuración pre-insolvencia (negociación con acreedores antes del concurso)",
    "plazo_recomendado": "Máximo 2 meses desde conocimiento (evitar responsabilidad personal)",
    "nota_conexion": "Los alertas pre-concursales identificadas en este análisis deben conectarse con procedimientos de reestructuración conforme Libro II TRLC para maximizar opciones de continuidad empresarial"
  },
  "recomendaciones": [
    {
      "prioridad": "URGENTE",
      "accion": "Constituir línea de crédito para cobertura de efectivo",
      "plazo": "Inmediato (1 semana)"
    },
    {
      "prioridad": "URGENTE",
      "accion": "Plan de reestructuración de costes (objetivo -10%)",
      "plazo": "30 días"
    },
    {
      "prioridad": "ALTA",
      "accion": "Revisión de deuda: refinanciación, extensión de plazos",
      "plazo": "60 días"
    },
    {
      "prioridad": "ALTA",
      "accion": "Plan de recuperación de rentabilidad (nuevos productos, mercados)",
      "plazo": "90 días"
    },
    {
      "prioridad": "MEDIA",
      "accion": "Monitoreo mensual de indicadores clave (liquides, EBIT)",
      "plazo": "Permanente"
    }
  ]
}
```

---

## Fórmulas Simplificadas (Sin Valor Mercado de PN)

Para empresas privadas sin cotización, Z-Score ajustado:

```
Z' = 0.717*X1 + 0.847*X2 + 3.107*X3 - 0.420*X4 + 0.998*X5

Donde X4 = Valor Contable PN / Pasivo Total
Zona Distress: Z' < 1.23
Zona Gris: 1.23-2.90
Zona Segura: > 2.90
```

---

---

## Alertas Preconcursales (Libro II TRLC)

### Arts. 583-720 TRLC: Planes de Reestructuración

La Ley 16/2022 reformó TRLC introduciendo mecanismo pre-concursal (Libro II):

```
Umbral Pre-Concursal (Cuándo Activar):
1. Desequilibrio patrimonial (Pasivo > Activo) OR
2. Incapacidad de cumplir obligaciones a vencimiento

Señales de Alerta (Z-Score integrada):
- Z-Score < 1.81 (Distress Zone)
- Ohlson O-Score > 0.50 (alta probabilidad insolvencia)
- Zmijewski M-Score > -0.9 (estrés financiero)
- Liquidez inmediata < 0.20 (cobertura efectivo críticamente baja)
- Cobertura de intereses < 2.0 (insuficiente)
```

### Umbrales de Comunicación Pre-Concursal

**OBLIGACIÓN LEGAL (TRLC Art. 5bis - Ley 16/2022)**:

| Condición | Plazo Acción | Responsable | Consecuencia |
|---|---|---|---|
| **Desequilibrio patrimonial detectado** | Máximo 2 meses de conocimiento | Administrador/Consejero | Responsabilidad personal + daños |
| **Incapacidad de pago inminente** | Inmediata comunicación AEAT + acreedor | CFO/Legal | Insolvencia fraudulenta si se oculta |
| **Z-Score TRLC < 1.81** (6 meses continuados) | Instar reestructuración OR concurso | Administrador | Art. 262 CSC: responsabilidad |
| **Suspensión de pagos** (60+ días) | Deber comunicación a acreedores | Tesorería + Legal | Acción directa acreedores posible |

### Timeline de Reestructuración vs. Concurso

```
LINEA TEMPORAL RECOMENDADA:

T-0: Detección estrés financiero (Z-Score analysis)
     ↓
T+0-30: Comunicación a Consejo Administración
        Evaluación opciones reestructuración (Libro II)
     ↓
T+30-60: Notificación a acreedores principales
         Apertura negociaciones pre-concursales
         (Planes de reestructuración per Arts. 583-720)
     ↓
T+60-120: Proceso de reestructuración (crédito moratorio)
          Acuerdos de esperas
          Quita/novación de deuda
     ↓
T+120+: Homologación judicial (si acuerdo alcanzado)
        O instancia de concurso voluntario
```

**Plazo Crítico**: Máximo 2 meses desde conocimiento del desequilibrio antes de incurrir en responsabilidad penal.

---

## Conexión con Planes de Reestructuración

### Integración Z-Score → Reestructuración (Libro II TRLC)

Los outputs de stress test deben alimentar directamente el análisis de viabilidad de reestructuración:

#### Step 1: Diagnóstico Cuantitativo (Z-Score Output)

```
Métricas Clave del Stress Test:
- Z-Score 2024: 2.14 (Grey Zone → tendencia deterioro)
- Tendencia: -0.83 puntos/año (proyección Distress en 12m)
- Liquidez inmediata: 0.075 (CRÍTICA)
- Endeudamiento: 64% (ALTO)
- EBIT trending: -39% (CAÍDA severa)
```

#### Step 2: Viabilidad de Reestructuración (Análisis Cualitativo)

Basado en Z-Score outputs, evaluar:

| Elemento | Criterio | Condición Viabilidad |
|---|---|---|
| **Solvencia Residual** | Si Z-Score > 1.23 (Zona gris) | Reestructuración viable si tendencia reversible |
| **Cash Flow Operacional** | Proyección 12-meses | Debe ser positivo en escenario normalizado |
| **Activos Realizables** | Venta de activos no-core | Pueden cubrir deuda corto plazo |
| **Disposición Acreedores** | Negociación posible | Sin eventos de default acelerado |
| **Plan de Recuperación** | Ingresos +10% o costes -10% plausible | Timeline 24-36 meses |

#### Step 3: Opciones Reestructuración per Libro II TRLC (Arts. 583-720)

**Option A: Acuerdo Extrajudicial de Pagos (AEP)**
- Negoción directa con acreedores (sin intervención judicial)
- Validez: si mayoría acreedores acepta
- Timeline: 30-90 días
- Riesgo: Un acreedor puede bloquear

**Option B: Plan de Reestructuración Homologado**
- Presentación formal ante Juzgado
- Solicitud de "crédito moratorio" (acuerdo de plazo dilatado)
- Modalidades: quita, espera, novación, conversión deuda-equity
- Timeline: 3-6 meses
- Ventaja: Vinculante para todos acreedores

**Option C: Concurso Preconcursal (Art. 5bis TRLC)**
- Si reestructuración no viable
- Concurso voluntario = administrador solicita
- Conserva cierto control (vs. concurso forzado por acreedor)
- Timeline: 6-18 meses
- Resultado: Liquidación o plan de continuidad empresarial

#### Step 4: Conexión Z-Score Output → Plan de Reestructuración

```json
{
  "stress_test_output": {
    "z_score_2024": 2.14,
    "zona": "GREY ZONE",
    "tendencia": "DETERIORO -0.83/año",
    "dias_liquidez_estimados": 15
  },
  "analisis_reestructuracion": {
    "viabilidad_general": "MODERADA",
    "opciones_recomendadas": [
      {
        "option": "Acuerdo Extrajudicial Pagos (AEP)",
        "viabilidad": "ALTA si acreedores cooperan",
        "elementos_negociacion": [
          "Espera 12-18 meses en deuda corto plazo",
          "Reducción tasa interés (150-200 bps)",
          "Refinanciación via crédito puente bancario",
          "Plan operacional: reducción costes -10%, ingresos +5%"
        ],
        "timeline": "60 días",
        "riesgo": "Rechazo de acreedor minoritario"
      },
      {
        "option": "Plan Homologado (Art. 583+ TRLC)",
        "viabilidad": "MEDIA",
        "elementos_plan": [
          "Quita: 10-20% deuda largo plazo",
          "Espera: 5-10 años para capital",
          "Conversión: Equity swap con acreedor principal",
          "Crédito moratorio: Prórroga de 3 años"
        ],
        "timeline": "120-180 días",
        "ventaja": "Vinculante para todos acreedores"
      }
    ],
    "descartado": "Concurso (liquidación destructiva de valor)"
  },
  "recomendacion_inmediata": "Iniciar negociación AEP en próximas 4 semanas; preservar liquidez"
}
```

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| **TRLC (RDL 1/2020, reformado Ley 16/2022)** | Art. 5: Obligación solicit. insolvencia inminente; Art. 5bis: Alerta pre-concursal; Art. 583-720: Planes de reestructuración |
| **Libro II TRLC** | Planes de reestructuración pre-insolvencia: negociación anticipada con acreedores; Acuerdo Extrajudicial de Pagos (AEP) |
| **Art. 262 CSC** | Administrador responsable si no cumple obligación concursal (máximo 2 meses desde conocimiento) |
| **OCDE** | Modelos Z-Score/O-Score/M-Score reconocidos internacionalmente para stress testing |
| **BCB** | Exigencia stress testing en periódicos bancarios; supervisión de riesgo de insolvencia |
