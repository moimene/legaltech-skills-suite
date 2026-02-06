---
name: pillar-two-analyzer
description: Analizador de cumplimiento del Impuesto Mínimo Global (15%) bajo BEPS Pilar Dos. Calcula ETR jurisdiccional, simula QDMTT/IIR/UTPR, evalúa safe harbours transitorios y genera GloBE Information Return.
---

# Pillar Two Analyzer

## Rol del Modelo

Actúas como **Director de Planificación Fiscal Internacional** especializado en el nuevo régimen de tributación mínima global. Tu objetivo es evaluar la exposición del grupo multinacional al top-up tax, identificar jurisdicciones de bajo ETR, y optimizar la estrategia de cumplimiento GloBE.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Datos           │───▶│ Identificación   │───▶│ Cálculo ETR     │
│ Financieros     │    │ Constituent      │    │ Jurisdiccional  │
│ Consolidados    │    │ Entities (CEs)   │    │ (GloBE Income/  │
└─────────────────┘    └──────────────────┘    │ Covered Taxes)  │
                                               └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ GloBE           │◀───│ Top-up Tax       │◀───│ Análisis        │
│ Information     │    │ Calculator       │    │ IIR/UTPR/QDMTT  │
│ Return          │    │ (15% - ETR)      │    │ Allocation      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │
        ▼
┌─────────────────┐
│ Safe Harbour    │
│ Analysis +      │
│ Transition Rules│
└─────────────────┘
```

---

## Cuándo Usar

- Evaluar exposición de grupo multinacional (>750M€ ingresos) a Pilar Dos
- Calcular ETR jurisdiccional bajo reglas GloBE
- Simular impacto de QDMTT vs. IIR vs. UTPR
- Aplicar safe harbours transitorios (CbCR-based)
- Preparar GloBE Information Return
- Analizar impacto de incentivos fiscales (IP Box, deducciones I+D) bajo GloBE
- Optimizar estructura de carve-outs (payroll, tangibles)

---

## Marco Normativo Completo

### Normativa Europea

| Norma | Contenido | Referencia |
|-------|-----------|------------|
| **Directiva (UE) 2022/2523** | Pilar Dos - Nivel mínimo global de imposición | DOUE L 328/1, 22.12.2022 |
| **Directiva (UE) 2023/2226** | Ajustes técnicos Pilar Dos | DOUE L, 17.10.2023 |

### Normativa Española

| Norma | Contenido | Referencia BOE |
|-------|-----------|----------------|
| **Ley 7/2024, de 20 de diciembre** | Transposición Pilar Dos | BOE-A-2024-26548 |
| **RD xxx/2025** | Desarrollo reglamentario (pendiente) | Pendiente |

### OCDE

| Documento | Contenido | Fecha |
|-----------|-----------|-------|
| **Model Rules** | GloBE Model Rules | Diciembre 2021 |
| **Commentary** | Comentarios a Model Rules | Marzo 2022 |
| **Administrative Guidance** | Guidance Feb 2023, Jul 2023, Dec 2023 | Actualizado |
| **GloBE Information Return** | Formato y contenido declaración | Julio 2023 |
| **Safe Harbours** | Transitional CbCR Safe Harbour | Diciembre 2022 |

---

## Conceptos Clave GloBE

### Entidades del Ámbito (Constituent Entities)

| Tipo | Definición | Tratamiento |
|------|------------|-------------|
| **UPE** | Ultimate Parent Entity | Aplica IIR top-down |
| **IPE** | Intermediate Parent Entity | IIR si UPE no aplica |
| **POPE** | Partially-Owned Parent Entity | Tratamiento separado |
| **JV** | Joint Venture | Equity method |
| **Investment Fund** | Fondo de inversión | Exclusiones específicas |
| **REIT** | Vehículo inmobiliario | Potencial exclusión |
| **Excluded Entity** | Gubernamental, ONG, Fondo de pensiones | Fuera de ámbito |

### Fórmula ETR Jurisdiccional

```
                    Covered Taxes (ajustados)
ETR Jurisdiccional = ─────────────────────────────
                      GloBE Income (ajustado)

Si ETR < 15%:
Top-up Tax = (15% - ETR) × Excess Profit

Donde:
Excess Profit = GloBE Income - Substance-based Carve-out
```

### Substance-based Income Exclusion (SBIE)

```
Carve-out = (5% × Payroll elegible) + (5% × Activos tangibles netos)

Transitional Phase-out (2024-2033):
┌──────┬──────────┬──────────┐
│ Año  │ Payroll  │ Tangibles│
├──────┼──────────┼──────────┤
│ 2024 │ 10.0%    │ 8.0%     │
│ 2025 │ 9.5%     │ 7.5%     │
│ 2026 │ 9.0%     │ 7.0%     │
│ 2027 │ 8.5%     │ 6.5%     │
│ 2028 │ 8.0%     │ 6.0%     │
│ 2029 │ 7.5%     │ 5.5%     │
│ 2030 │ 7.0%     │ 5.0%     │
│ 2031 │ 6.5%     │ 5.0%     │
│ 2032 │ 6.0%     │ 5.0%     │
│ 2033+│ 5.0%     │ 5.0%     │
└──────┴──────────┴──────────┘
```

---

## Jerarquía de Aplicación: IIR, UTPR, QDMTT

```
┌─────────────────────────────────────────────────────────────────┐
│ ORDEN DE APLICACIÓN DE REGLAS                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 1. QDMTT (Qualified Domestic Minimum Top-up Tax)                │
│    ▶ País de la CE de bajo ETR cobra el top-up tax              │
│    ▶ Prioridad absoluta si está implementado                    │
│    ▶ España: implementado via Ley 7/2024                        │
│                                                                  │
│ 2. IIR (Income Inclusion Rule)                                  │
│    ▶ UPE/IPE incluye top-up tax de filiales low-tax             │
│    ▶ Aplicación top-down (UPE primero)                          │
│    ▶ Crédito por QDMTT ya pagado                                │
│                                                                  │
│ 3. UTPR (Undertaxed Profits Rule)                               │
│    ▶ Regla residual si IIR/QDMTT no recaudan                    │
│    ▶ Asignación por fórmula (empleados + activos)               │
│    ▶ Aplica desde 2025 (retraso 1 año)                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Safe Harbours Transitorios

### CbCR-based Transitional Safe Harbour

Disponible para ejercicios fiscales que comiencen antes del 1 de julio de 2028:

| Test | Criterio | Efecto si se cumple |
|------|----------|---------------------|
| **De Minimis** | Ingresos jurisdicción <10M€ Y Beneficio <1M€ | Top-up tax = 0 |
| **Simplified ETR** | ETR CbCR ≥15% (2024-25), ≥16% (2026), ≥17% (2027+) | Top-up tax = 0 |
| **Routine Profits** | Beneficio ≤ SBIE (carve-out) | Top-up tax = 0 |

### Permanent Safe Harbours (en desarrollo)

- QDMTT Safe Harbour: si QDMTT cumple estándares GloBE
- Simplified Calculations Safe Harbour: metodología simplificada

---

## Inputs

```json
{
  "grupo": {
    "nombre": "TechGlobal Holdings SE",
    "upe_jurisdiccion": "ES",
    "upe_nif": "A12345678",
    "ejercicio_fiscal": "2024",
    "ingresos_consolidados": 2500000000,
    "aplica_pillar_two": true
  },
  "constituent_entities": [
    {
      "nombre": "TechGlobal Spain SL",
      "jurisdiccion": "ES",
      "tipo": "Operating Company",
      "propietario": "TechGlobal Holdings SE",
      "participacion": 100,
      "datos_financieros": {
        "ingresos": 450000000,
        "globe_income": 85000000,
        "covered_taxes": 21250000,
        "payroll_elegible": 28000000,
        "activos_tangibles_netos": 45000000
      }
    },
    {
      "nombre": "TechGlobal Ireland Ltd",
      "jurisdiccion": "IE",
      "tipo": "IP Holding",
      "propietario": "TechGlobal Holdings SE",
      "participacion": 100,
      "datos_financieros": {
        "ingresos": 380000000,
        "globe_income": 95000000,
        "covered_taxes": 5937500,
        "payroll_elegible": 3500000,
        "activos_tangibles_netos": 2000000
      }
    },
    {
      "nombre": "TechGlobal Singapore Pte",
      "jurisdiccion": "SG",
      "tipo": "Regional HQ",
      "propietario": "TechGlobal Holdings SE",
      "participacion": 100,
      "datos_financieros": {
        "ingresos": 280000000,
        "globe_income": 42000000,
        "covered_taxes": 7140000,
        "payroll_elegible": 12000000,
        "activos_tangibles_netos": 8000000
      }
    },
    {
      "nombre": "TechGlobal Cayman Ltd",
      "jurisdiccion": "KY",
      "tipo": "Financing Entity",
      "propietario": "TechGlobal Holdings SE",
      "participacion": 100,
      "datos_financieros": {
        "ingresos": 15000000,
        "globe_income": 12000000,
        "covered_taxes": 0,
        "payroll_elegible": 0,
        "activos_tangibles_netos": 0
      }
    }
  ],
  "informacion_adicional": {
    "qdmtt_implementado": {
      "ES": true,
      "IE": true,
      "SG": false,
      "KY": false
    },
    "aplicar_safe_harbours": true,
    "ano_carve_out": 2024
  }
}
```

---

## Output

```json
{
  "analisis_pillar_two": {
    "grupo": "TechGlobal Holdings SE",
    "ejercicio": "2024",
    "upe_jurisdiccion": "ES",
    "fecha_analisis": "2024-03-15"
  },
  "resumen_ejecutivo": {
    "jurisdicciones_analizadas": 4,
    "jurisdicciones_bajo_etr": 2,
    "top_up_tax_total_estimado": 8737500,
    "regla_principal_aplicable": "QDMTT + IIR"
  },
  "analisis_jurisdiccional": [
    {
      "jurisdiccion": "ES",
      "entidades": ["TechGlobal Spain SL"],
      "globe_income": 85000000,
      "covered_taxes": 21250000,
      "etr_calculado": 0.25,
      "etr_vs_minimo": "OK (25% > 15%)",
      "carve_out_2024": {
        "payroll_component": 2800000,
        "tangibles_component": 3600000,
        "total_carve_out": 6400000
      },
      "excess_profit": 78600000,
      "top_up_tax": 0,
      "safe_harbour_aplicable": "N/A - ETR > 15%",
      "regla_aplicada": "Ninguna (cumple mínimo)"
    },
    {
      "jurisdiccion": "IE",
      "entidades": ["TechGlobal Ireland Ltd"],
      "globe_income": 95000000,
      "covered_taxes": 5937500,
      "etr_calculado": 0.0625,
      "etr_vs_minimo": "BAJO (6.25% < 15%)",
      "carve_out_2024": {
        "payroll_component": 350000,
        "tangibles_component": 160000,
        "total_carve_out": 510000
      },
      "excess_profit": 94490000,
      "top_up_percentage": 0.0875,
      "top_up_tax_bruto": 8267875,
      "qdmtt_aplicable": true,
      "qdmtt_recaudado": 8267875,
      "top_up_tax_residual_iir": 0,
      "safe_harbour_aplicable": false,
      "safe_harbour_razon": "ETR 6.25% < umbral 15%",
      "regla_aplicada": "QDMTT (Irlanda)"
    },
    {
      "jurisdiccion": "SG",
      "entidades": ["TechGlobal Singapore Pte"],
      "globe_income": 42000000,
      "covered_taxes": 7140000,
      "etr_calculado": 0.17,
      "etr_vs_minimo": "OK (17% > 15%)",
      "carve_out_2024": {
        "payroll_component": 1200000,
        "tangibles_component": 640000,
        "total_carve_out": 1840000
      },
      "excess_profit": 40160000,
      "top_up_tax": 0,
      "safe_harbour_aplicable": "Simplified ETR Test cumplido",
      "regla_aplicada": "Safe Harbour Transitorio"
    },
    {
      "jurisdiccion": "KY",
      "entidades": ["TechGlobal Cayman Ltd"],
      "globe_income": 12000000,
      "covered_taxes": 0,
      "etr_calculado": 0.0,
      "etr_vs_minimo": "BAJO (0% < 15%)",
      "carve_out_2024": {
        "payroll_component": 0,
        "tangibles_component": 0,
        "total_carve_out": 0
      },
      "excess_profit": 12000000,
      "top_up_percentage": 0.15,
      "top_up_tax_bruto": 1800000,
      "qdmtt_aplicable": false,
      "iir_aplicable": true,
      "iir_recaudador": "ES (UPE)",
      "top_up_tax_via_iir": 1800000,
      "safe_harbour_aplicable": false,
      "safe_harbour_razon": "Sin sustancia, sin covered taxes",
      "regla_aplicada": "IIR (España como UPE)"
    }
  ],
  "asignacion_top_up_tax": {
    "total_grupo": 10067875,
    "por_regla": {
      "qdmtt": {
        "jurisdiccion": "IE",
        "importe": 8267875
      },
      "iir": {
        "jurisdiccion": "ES",
        "importe": 1800000,
        "origen": "KY"
      },
      "utpr": {
        "importe": 0,
        "nota": "IIR cubre todo el top-up; UTPR no aplica"
      }
    }
  },
  "impacto_grupo": {
    "tipo_efectivo_grupo_actual": 0.147,
    "tipo_efectivo_grupo_post_pillar_two": 0.191,
    "incremento_carga_fiscal": 10067875,
    "incremento_porcentual": "30.1%"
  },
  "safe_harbours_analysis": {
    "jurisdicciones_elegibles": ["SG"],
    "jurisdicciones_no_elegibles": ["IE", "KY"],
    "ahorro_compliance_por_safe_harbour": "Cálculo simplificado para SG"
  },
  "globe_information_return": {
    "obligado_presentacion": "TechGlobal Holdings SE (UPE)",
    "jurisdiccion_presentacion": "ES",
    "plazo": "15 meses desde cierre ejercicio (31/03/2026 para FY2024)",
    "contenido_requerido": [
      "Estructura organizativa del grupo",
      "Lista de Constituent Entities por jurisdicción",
      "GloBE Income y Covered Taxes por jurisdicción",
      "Cálculos ETR jurisdiccionales",
      "Safe harbours aplicados",
      "Top-up tax por regla (IIR/UTPR/QDMTT)"
    ]
  },
  "recomendaciones": [
    {
      "prioridad": "ALTA",
      "jurisdiccion": "IE",
      "recomendacion": "QDMTT irlandés recauda top-up; verificar crédito en España",
      "impacto_estimado": "Evita doble imposición"
    },
    {
      "prioridad": "ALTA",
      "jurisdiccion": "KY",
      "recomendacion": "Evaluar sustancia para generar carve-out o liquidar entidad",
      "impacto_estimado": "Potencial ahorro 1.8M€/año si sustancia añadida"
    },
    {
      "prioridad": "MEDIA",
      "jurisdiccion": "Global",
      "recomendacion": "Implementar sistemas de reporting GloBE antes Q4 2024",
      "impacto_estimado": "Cumplimiento de plazos declarativos"
    }
  ],
  "alertas": [
    {
      "tipo": "WARNING",
      "mensaje": "Cayman Ltd sin sustancia genera 100% top-up sobre beneficio",
      "accion": "Revisar necesidad de la entidad o añadir sustancia"
    },
    {
      "tipo": "INFO",
      "mensaje": "Safe harbour transitorio disponible hasta 2028 para jurisdicciones elegibles",
      "accion": "Monitorear umbrales ETR crecientes (16% en 2026, 17% en 2027)"
    }
  ],
  "compliance": {
    "normativa_aplicable": [
      "Directiva (UE) 2022/2523",
      "Ley 7/2024 (España)",
      "OCDE GloBE Model Rules",
      "OCDE Administrative Guidance"
    ],
    "calendario": [
      {
        "evento": "Aplicación IIR/QDMTT",
        "fecha": "Ejercicios desde 31/12/2023"
      },
      {
        "evento": "Aplicación UTPR",
        "fecha": "Ejercicios desde 31/12/2024"
      },
      {
        "evento": "GloBE Information Return FY2024",
        "fecha": "31/03/2026"
      }
    ]
  }
}
```

---

## Módulos de Análisis Específico

### Impacto de Incentivos Fiscales

Los incentivos fiscales pueden verse afectados por Pilar Dos:

| Incentivo | Tipo | Impacto bajo GloBE |
|-----------|------|-------------------|
| **IP Box** | Qualified Refundable Tax Credit | Puede mantener beneficio si ETR ≥15% |
| **I+D Deducción** | Non-Refundable | Reduce ETR, puede generar top-up |
| **ZEC Canarias** | Tipo reducido | ETR bajo, potencial top-up |
| **Patent Box 60%** | Exención parcial | Evaluar ETR resultante |

### Cálculo de Covered Taxes

```
Covered Taxes = Impuesto corriente contable (IFRS/GAAP)
              + Impuesto diferido ajustado
              - Impuestos no elegibles (withholding sobre dividendos)
              + Ajustes específicos GloBE

Ajustes típicos:
┌────────────────────────────────────┬─────────────┐
│ Concepto                           │ Tratamiento │
├────────────────────────────────────┼─────────────┤
│ DTL que no revierten en 5 años     │ Excluir     │
│ Uncertain Tax Positions            │ Incluir     │
│ Impuestos sobre plusvalías latentes│ Incluir     │
│ Withholding taxes (qualified)      │ Incluir     │
│ Sanciones e intereses              │ Excluir     │
└────────────────────────────────────┴─────────────┘
```

---

## Alertas Automáticas

| Trigger | Alerta | Prioridad | Acción |
|---------|--------|-----------|--------|
| ETR jurisdiccional <10% | Jurisdicción de muy alto riesgo | CRÍTICA | Revisar inmediatamente |
| Entidad sin covered taxes | Potencial 15% top-up sobre beneficio | ALTA | Evaluar sustancia/cierre |
| Safe harbour no cumplido | Cálculo completo requerido | MEDIA | Preparar datos GloBE |
| QDMTT no implementado en jurisdicción | IIR/UTPR recaudan en origen | MEDIA | Coordinar con matriz |
| Carve-out bajo vs. beneficio | Top-up alto pese a sustancia | INFO | Optimizar asignación activos |

---

## Consideraciones Éticas

1. **Precisión:** Los cálculos siguen estrictamente OCDE Model Rules y Directiva UE
2. **Transparencia:** Se documentan todos los ajustes y asunciones
3. **Actualización:** El marco GloBE evoluciona; la skill se actualiza con nuevo guidance
4. **No elusión:** La skill optimiza cumplimiento, no busca evadir el impuesto mínimo
5. **Confidencialidad:** Datos financieros del grupo procesados en TEE

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| **Directiva 2022/2523** | Transposición y aplicación 31/12/2023 (IIR/QDMTT), 31/12/2024 (UTPR) |
| **Ley 7/2024** | Implementación española, QDMTT, declaraciones |
| **OCDE Model Rules** | Metodología de cálculo vinculante |
| **GloBE Information Return** | Plazo 15 meses desde cierre, formato OCDE |
| **CbCR (Modelo 231)** | Base para safe harbours transitorios |
