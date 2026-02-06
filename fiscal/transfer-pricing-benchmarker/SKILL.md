---
name: transfer-pricing-benchmarker
description: Validate intercompany transactions against arm's length pricing using OECD Guidelines 2022 (Chapters I-III) and RD 634/2015 documentation standards. Analyze comparables via public databases (Compustat, Orbis Light), compute interquartile ranges with DEMPE assessment, comparability adjustments (Berry ratio, working capital), and generate defensible benchmarking reports. Applicable when testing transfer pricing in administrative audits, preparing documentation, or responding to inspection requirements.
---

# Transfer Pricing Benchmarker

---

## Application Topology

```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Intercompany    │───▶│ DEMPE Function   │───▶│ Identify         │
│ Transaction     │    │ Analysis         │    │ Comparables      │
│ & Economics     │    │ (Art. 5 OECD)    │    │ (Orbis/Compustat)│
└─────────────────┘    └──────────────────┘    └────────┬─────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Benchmarking    │◀───│ Comparability    │◀───│ Multi-year       │
│ Report (RD      │    │ Adjustments      │    │ Testing & Berry  │
│ 634/2015)       │    │ (Working Capital,│    │ Ratio Analysis   │
│                 │    │ Berry, Size)     │    │                  │
└─────────────────┘    └──────────────────┘    └──────────────────┘
```

---

## Trigger Contexts

- Defending transfer pricing in administrative audits (Inspección de Hacienda)
- Preparing mandatory documentation under RD 634/2015
- Testing intragroup services, royalties, or tangible property transactions
- Evaluating penalty exposure (Art. 18.13 LIS) for non-compliant pricing
- Multi-jurisdictional groups requiring OECD Guidelines 2022 compliance

---

## Valuation Methods (OECD Guidelines 2022)

| Method | Code | Application |
|--------|------|-------------|
| Comparable Uncontrolled Price | CUP | Commodity transactions, intercompany management services |
| Cost Plus | Cost+ | Intragroup services (DEMPE: D+E+M+P+E functions) |
| Resale Minus | Resale- | Distribution, low-value-added functions |
| Transactional Net Margin Method | TNMM | Complex operations, limited comparables |
| Profit Split | PS | Highly integrated transactions, joint value creation |

**DEMPE Framework**: Identify Development, Enhancement, Maintenance, Protection, Exploitation functions per OECD Art. 5 guidance.

---

## Inputs & Configuration

### Core Parameters

```json
{
  "transaccion": {
    "tipo": "Intragroup Management Services",
    "entidad_local": "Filial ES",
    "entidad_vinculada": "Matriz UK",
    "importe_anual": 2500000,
    "metodo": "TNMM - Cost Plus",
    "margen_testado": 0.08,
    "funciones_dempe": {
      "development": false,
      "enhancement": true,
      "maintenance": true,
      "protection": false,
      "exploitation": true
    }
  },
  "filtros_comparables": {
    "sectores_naics": ["541611", "541612"],
    "geografias": ["Europa Occidental"],
    "tamaño_ingresos_min_eur": 10000000,
    "anos_testeo": [2021, 2022, 2023],
    "enfoque_multi_ano": "weighted_average"
  },
  "ajustes_comparabilidad": {
    "ajuste_capital_circulante": true,
    "ajuste_berry_ratio": true,
    "ajuste_tamaño": false
  }
}
```

---

## Output & Defensibility Assessment

```json
{
  "transaccion": "Intragroup Management Services",
  "metodo_aplicado": "TNMM - Cost Plus (OECD 2022, Ch. II.2.4)",
  "defensibilidad": {
    "margen_testado": 0.080,
    "rango_arm_length": {
      "minimo": 0.032,
      "q1": 0.051,
      "mediana": 0.067,
      "q3": 0.095,
      "maximo": 0.142
    },
    "posicion": "WITHIN INTERQUARTILE (Q1-Q3)",
    "estatus": "DEFENSIBLE - RD 634/2015 compliant",
    "confianza": 0.94
  },
  "comparables_identificados": [
    {
      "empresa": "Consulting Services GmbH",
      "pais": "Alemania",
      "naics": "541611",
      "margen_cost_plus": 0.063,
      "anos": "2021-2023",
      "ajustes_aplicados": ["working_capital", "size"],
      "razon_ajuste": "Diferencias en días circulantes (cobro 45 vs 38 días)",
      "impacto_ajuste": "+0.8%"
    },
    {
      "empresa": "Advisory Partners SARL",
      "pais": "Francia",
      "naics": "541612",
      "margen_cost_plus": 0.078,
      "anos": "2022-2023",
      "ajustes_aplicados": [],
      "razon_sin_ajustes": "Perfil de comparabilidad similar"
    },
    {
      "empresa": "Management Consulting Ltd",
      "pais": "Países Bajos",
      "naics": "541611",
      "margen_cost_plus": 0.069,
      "anos": "2021-2023",
      "ajustes_aplicados": ["berry_ratio"],
      "razon_ajuste": "Verificación de similitud funcional mediante Berry Ratio",
      "impacto_ajuste": "+0.3%"
    }
  ],
  "analisis_comparabilidad": {
    "funciones_entidad_local": ["Management oversight", "Administrative coordination"],
    "activos_utilizados": ["IT infrastructure", "Office equipment"],
    "riesgos_asumidos": ["Operational risk (limited)", "Market timing risk (none)"],
    "dempe_scoring": "E+M+P (Enhancement, Maintenance, Protection) - Low complexity"
  },
  "ajustes_metodologicos": [
    {
      "tipo": "Working Capital Adjustment",
      "criterio": "OECD Guidelines 2022, Art. 5.4.2",
      "calculo": "DSO_local (45) - DSO_comparable_promedio (41)",
      "impacto_porcentual": "±0.5%"
    },
    {
      "tipo": "Multi-year Testing",
      "enfoque": "Weighted average (2021: 0.20, 2022: 0.40, 2023: 0.40)",
      "volatilidad_anual": "Max deviation 2.1% from average",
      "resultado": "Stable y defensible"
    },
    {
      "tipo": "Berry Ratio Verification",
      "formula": "Operating Profit / COGS",
      "rango_comparable": "[0.15, 0.28]",
      "ratio_testado": "0.18",
      "estatus": "DENTRO rango"
    }
  ],
  "compliance_rd_634_2015": {
    "documentacion_requerida": "Presente",
    "estructura_informe": "OECD 2022 Chapter II compliant",
    "auditable": true,
    "riesgo_inspeccion": "BAJO"
  },
  "exposicion_sancion": {
    "articulo": "Art. 18.13 LIS (Ley 27/2014)",
    "penalizacion_potencial": "Mínima (pricing within defensible range)",
    "interes_compensatorio": "Calculable a partir Banco de España rate"
  },
  "alertas": []
}
```

---

## Example: Five-Comparable Intragroup Management Services Benchmarking

**Facts**: Parent company (UK) provides management, strategic planning, and administrative services to Spanish subsidiary. Annual fee: EUR 2.5M. Testing margin: 8% Cost Plus.

**Comparable Selection Process**:
1. Sector filter: NAICS 541611/541612 (Management consulting)
2. Geography: Western Europe (high comparability)
3. Size: EUR 10M+ revenues
4. Year coverage: Weighted average 2021-2023

**Comparables Range**:
- Q1: 5.1%, Median: 6.7%, Q3: 9.5%
- Tested margin (8.0%) within interquartile range

**Adjustments Made**:
- Working capital adjustment (+0.5%) for 4-day difference in collection periods
- Size adjustment for revenue >EUR 50M (-0.3%)
- Berry ratio verification (tested 0.18 vs range 0.15-0.28): within range

**Defensibility**: Robust under OECD 2022 Guidelines; compliant with RD 634/2015 documentation standards.

---

## Data Sources Without Premium Access

If Orbis or Compustat unavailable:
- Public filing databases (Registro Mercantil ES, Companies House UK)
- Sector benchmarks (INE, Eurostat, SABI Public)
- Published studies (Big 4 TP reports, IBFD)

```python
benchmarker = TransferPricingBenchmarker(
    data_source="public",
    country_local="ES",
    cdi_aplicable="España-Reino Unido"
)
```

---

## Reporte Master File / Local File Automatizado

### Estructura de Plantilla RD 634/2015 Arts. 13-16

El reporte generado alineado exactamente a requisitos RD 634/2015:

```
MASTER FILE (Aplicable a Grupo Multi-jurisdicción)
├── 1. ORGANIGRAMA GRUPO & ESTRUCTURA CONTROL
│   ├── Mapa de participaciones (ownership chain)
│   ├── Entidades por jurisdicción
│   ├── Relaciones de control (100%, minoritarios)
│   └── Cambios estructurales período analizado
│
├── 2. DESCRIPCIÓN NEGOCIO GRUPO
│   ├── Líneas de negocio principales
│   ├── Sectores CNAE/SIC codes
│   ├── Cadena de valor (manufacturing, distribution, services)
│   ├── Ciclos económicos y estacionalidad
│   └── Cambios estratégicos (M&A, divestments)
│
├── 3. INTANGIBLES & DEMPE ANALYSIS
│   ├── Inventario completo de intangibles
│   │   ├── Patents, trademarks, copyrights
│   │   ├── Know-how, processes, customer lists
│   │   └── Management strategies
│   ├── Ownership & Legal Title (por intangible)
│   ├── Contribuciones per Función DEMPE
│   │   ├── Development (création/création)
│   │   ├── Enhancement (mejoras)
│   │   ├── Maintenance (mantenimiento)
│   │   ├── Protection (protección legal)
│   │   └── Exploitation (explotación comercial)
│   └── Transfer pricing of intangible contributions
│
├── 4. ACTIVIDADES FINANCIERAS
│   ├── Política de tesorería centralizada
│   ├── Estructuras de financiación
│   ├── Tasas de interés intra-grupo (benchmarked)
│   ├── Garantías y avales
│   └── Covenants de deuda
│
├── 5. POSICIÓN FISCAL & FINANCIERA
│   ├── Credit rating / Solvency assessment
│   ├── Principales ratios financieros (multi-año)
│   ├── Ciclos de rentabilidad histórica
│   ├── Política de dividendos / repatriación
│   └── Carga fiscal efectiva por jurisdicción
│
└── 6. ACUERDOS PRECIOS ANTICIPADOS (APAs)
    ├── APAs bilaterales vigentes
    ├── APAs en negociación
    ├── Resoluciones APA por entidad
    └── Impacto en operaciones documentadas

LOCAL FILE (Específico per Operación > 250k€)
├── 1. OPERACIÓN VINCULADA: DESCRIPCIÓN
│   ├── Naturaleza exacta (servicios, royalties, ventas)
│   ├── Entidades involucradas (CIF, denominación)
│   ├── Período de análisis
│   ├── Moneda & importe anual
│   └── Términos contracuales (pricing mechanism)
│
├── 2. ANÁLISIS FUNCIONAL EXHAUSTIVO
│   ├── Funciones de cada entidad (detalladas)
│   ├── Activos utilizados (tangibles e intangibles)
│   ├── Riesgos asumidos (comercial, financiero, operacional)
│   └── Prueba de comparabilidad
│
├── 3. SELECCIÓN MÉTODO TP
│   ├── Método elegido (CUP, Cost+, Resale-, TNMM, PS)
│   ├── Justificación economica per OECD Guidelines Cap. II
│   ├── Análisis de alternativas metódológicas
│   └── Limitaciones & datos disponibles
│
├── 4. BENCHMARKING & COMPARABLES
│   ├── Búsqueda sistemática (bases: Orbis, Compustat, SABI)
│   ├── Selección de comparables (12+ preferible)
│   ├── Ajustes de comparabilidad (working capital, size, etc.)
│   ├── Rango intercuartil (Q1, mediana, Q3)
│   ├── Posición del testado (dentro o fuera rango)
│   └── Análisis multi-año (estabilidad)
│
├── 5. DOCUMENTACIÓN CONTRATO
│   ├── Acuerdo formal (copia firmada)
│   ├── Términos de pricing explícitos
│   ├── Evidencia de negociación arm's length
│   ├── Cambios contractuales (enmiendas)
│   └── Ratificación de partes
│
└── 6. ANÁLISIS RIESGO & DEFENSA
    ├── Riesgos identificados (ajuste potential)
    ├── Argumentos defensivos
    ├── Comparables robustez
    └── Mitigación recomendada
```

### Template de Campos Automáticos (RD 634/2015)

El reporte genera automáticamente:

| Campo | Fuente | Validación |
|---|---|---|
| **Identificación Grupo** | Input organizacional | CIF verificación vs. Registros Mercantiles |
| **Descripción Negocio** | Narrativa + CNAE | CNAE codes España/EU contra real activity |
| **Intangibles List** | Portafolio IP + DEMPE allocation | Documentación ownership per escrituras |
| **Actividades Financieras** | Políticas de tesorería + financiación docs | Benchmarking tasas de interés vs. EURIBOR+ |
| **Posición Fiscal** | Estados financieros + análisis ratios | Comparativa histórica 3 años mínimo |
| **APAs Vigentes** | Base datos administración fiscal | Verificación contra AEAT BOE público |

---

## Regulatory Compliance Checklist

| Authority | Requirement | Standard |
|-----------|-----------|----------|
| **OECD** | Transfer Pricing Guidelines 2022, Chapters I-III | Methodology, DEMPE analysis |
| **Spain (LIS)** | Art. 18 - Linked party operations | Arm's length principle |
| **Spain (RD 634/2015)** | Contemporaneous documentation; Master File + Local File (Arts. 13-16) | Exact structure per Arts. 13-16; 10-day production requirement |
| **Spain (Art. 18.13 LIS)** | Penalty regime | 15% adjustment if non-compliant pricing |
| **BEPS Action 13** | CBC Reporting | Triggered if group revenues > EUR 750M |
