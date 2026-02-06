---
name: salary-equity-calc
description: Calcula brecha salarial por género y equity gaps entre categorías usando descomposición Oaxaca-Blinder, análisis de regresión con controles (experiencia, rol, desempeño), output audit-ready con significancia estadística. Cumple RDL 902/2020 (Plan de Igualdad) y EU Pay Transparency Directive.
---

# Salary Equity Calculator

## Rol del Modelo

Actúas como **Analista de Compensación y Equidad de Género** especializado en compliance normativo español y europeo. Tu objetivo es cuantificar brechas salariales con rigor estadístico y generar reportes defendibles judicialmente.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Datos Nómina    │───▶│ Limpieza de      │───▶│ Análisis        │
│ + Plantilla     │    │ datos + Outliers │    │ Descriptivo     │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe         │◀───│ Descomposición   │◀───│ Regresión OLS   │
│ Ejecutivo +     │    │ Oaxaca-Blinder   │    │ + p-values      │
│ Anexos Técnicos │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Diagnóstico de brecha de género (RDL 902/2020)
- Auditoría de equidad salarial pre-litigio
- Cumplimiento EU Pay Transparency Directive
- Diseño de plan de igualdad
- Due Diligence en M&A

---

## Marco Regulatorio

| Norma | Aplicación | Plazo |
|-------|-----------|-------|
| **RDL 902/2020** | Diagnóstico brecha género (empresas >250 empleados) | Bienal |
| **Ley 15/2022** | Actualización: incluye hombres como víctimas; auditoría externa | 2024+ |
| **EU Pay Transparency** | Derecho a conocer salarios; trabajadores privados | 2024-2026 |
| **LGBTIQ+** | Brecha más allá de género (algunas CCAA) | Variable |

---

## Metodología Estadística

### 1. Brecha Salarial Media (Simple)

```
Gap = (Salario_Hombres - Salario_Mujeres) / Salario_Hombres × 100%
```

Ejemplo: Hombres 50K, Mujeres 42K → Gap = 16%

### 2. Descomposición Oaxaca-Blinder

Separa:
- **Componente explicado**: diferencias en características (experiencia, educación, puesto)
- **Componente no explicado**: "ajustado por discriminación" (no causal, pero sospechoso)

```
Gap_Total = Gap_Explicado + Gap_No_Explicado
```

### 3. Regresión Multivariante

```
log(Salario) = β₀ + β₁(Género) + β₂(Antigüedad) + β₃(Nivel) + β₄(Performance) + ε
```

Controla variables confundentes; β₁ = efecto género puro

---

## Inputs

```json
{
  "periodo": "2024-01-01_2024-12-31",
  "empresa": {
    "cif": "A12345678",
    "tamaño": 340,
    "sector": "Servicios Profesionales"
  },
  "dataset_empleados": [
    {
      "id_anonimizado": "EMP_001",
      "genero": "mujer",
      "salario_bruto_anual": 45000,
      "salario_base": 38000,
      "bonus_medio": 7000,
      "antiguedad_años": 6.5,
      "nivel_jerarquico": "Senior Consultant",
      "categoria_ccap": "Cuadro Técnico",
      "departamento": "Consultoría",
      "score_desempeño_1_5": 4.2,
      "formacion_anos": 18,
      "experiencia_relevante_anos": 8
    },
    {
      "id_anonimizado": "EMP_002",
      "genero": "hombre",
      "salario_bruto_anual": 52000,
      "salario_base": 44000,
      "bonus_medio": 8000,
      "antiguedad_años": 5.2,
      "nivel_jerarquico": "Senior Consultant",
      "categoria_ccap": "Cuadro Técnico",
      "departamento": "Consultoría",
      "score_desempeño_1_5": 4.0,
      "formacion_anos": 17,
      "experiencia_relevante_anos": 7
    }
  ],
  "controles_solicitud": {
    "incluir_datos_sensibles": false,
    "nivel_anonimizacion": "completo",
    "test_estadistico": "t-test_welch"
  }
}
```

---

## Output: Informe Audit-Ready

```json
{
  "diagnostico_ejecutivo": {
    "periodo": "2024 (año completo)",
    "muestra_total_empleados": 340,
    "distribucion_genero": {
      "mujeres_n": 134,
      "mujeres_pct": 39.4,
      "hombres_n": 206,
      "hombres_pct": 60.6
    }
  },
  "brecha_salarial_media": {
    "salario_bruto_medio_mujeres": 41200,
    "salario_bruto_medio_hombres": 47800,
    "diferencia_absoluta": 6600,
    "brecha_relativa_pct": 13.8,
    "intervalo_confianza_95": "12.1%-15.5%",
    "significancia_estadistica": {
      "test": "t-test Welch",
      "t_statistic": 4.18,
      "p_value": 0.0001,
      "es_significativo": true,
      "interpretacion": "Diferencia estadísticamente significativa (p<0.05)"
    }
  },
  "brecha_por_categoria": [
    {
      "nivel": "Cuadro Directivo",
      "mujeres_salario": 72000,
      "hombres_salario": 78500,
      "brecha_pct": 8.3,
      "p_value": 0.18,
      "significativo": false,
      "muestra_mujeres": 8,
      "muestra_hombres": 22,
      "nota": "Muestra pequeña; no conclusivo"
    },
    {
      "nivel": "Senior Consultant",
      "mujeres_salario": 45500,
      "hombres_salario": 52100,
      "brecha_pct": 12.8,
      "p_value": 0.002,
      "significativo": true,
      "muestra_mujeres": 42,
      "muestra_hombres": 71,
      "nota": "Brecha significativa; investigar causas"
    },
    {
      "nivel": "Junior Consultant",
      "mujeres_salario": 28500,
      "hombres_salario": 28900,
      "brecha_pct": 1.4,
      "p_value": 0.72,
      "significativo": false,
      "muestra_mujeres": 84,
      "muestra_hombres": 113,
      "nota": "Sin brecha significativa"
    }
  ],
  "descomposicion_oaxaca_blinder": {
    "gap_total_pct": 13.8,
    "gap_explicado_pct": 7.2,
    "gap_no_explicado_pct": 6.6,
    "interpretacion": {
      "gap_explicado": "Diferencias en antigüedad, experiencia, desempeño entre hombres y mujeres",
      "gap_no_explicado": "No atribuible a diferencias en características observadas; requiere investigación"
    },
    "desglose_gap_explicado": [
      {
        "factor": "Antigüedad promedio (mujeres 3.8 vs. hombres 5.2 años)",
        "contribucion_gap_pct": 3.5,
        "interpretacion": "Contratación reciente de mujeres reduce experiencia media"
      },
      {
        "factor": "Puntuación desempeño (mujeres 4.0 vs. hombres 4.1)",
        "contribucion_gap_pct": 1.2,
        "interpretacion": "Mínima diferencia"
      },
      {
        "factor": "Distribución por nivel (more women in junior roles)",
        "contribucion_gap_pct": 2.5,
        "interpretacion": "Segregación ocupacional vertical; mujeres concentradas en niveles menores"
      }
    ]
  },
  "regresion_multivariante": {
    "modelo": "OLS log(salario) ~ género + antigüedad + nivel + desempeño + departamento",
    "r_squared": 0.82,
    "observaciones": 340,
    "coeficientes": [
      {
        "variable": "Género (mujer=1)",
        "coeficiente": -0.089,
        "error_tipico": 0.018,
        "t_statistic": -4.94,
        "p_value": 0.0001,
        "efecto_salario": "8.5% menos por ser mujer (controlando otros factores)",
        "intervalo_confianza_95": "-12.3% a -4.8%"
      },
      {
        "variable": "Antigüedad (años)",
        "coeficiente": 0.035,
        "error_tipico": 0.005,
        "t_statistic": 7.2,
        "p_value": 0.0001,
        "efecto_salario": "+3.5% por año adicional",
        "intervalo_confianza_95": "2.5% a 4.5%"
      },
      {
        "variable": "Senior Consultant (vs. Junior)",
        "coeficiente": 0.42,
        "error_tipico": 0.08,
        "t_statistic": 5.25,
        "p_value": 0.0001,
        "efecto_salario": "+52% si es nivel senior",
        "intervalo_confianza_95": "26% a 78%"
      },
      {
        "variable": "Departamento: Operaciones (vs. Consultoría)",
        "coeficiente": -0.12,
        "error_tipico": 0.07,
        "t_statistic": -1.71,
        "p_value": 0.088,
        "efecto_salario": "-11% si en Operaciones",
        "intervalo_confianza_95": "-26% a 4%"
      }
    ],
    "diagnosticos": {
      "normalidad_residuos": "OK (Q-Q plot)",
      "multicolinealidad": "OK (VIF <5)",
      "heterocedasticidad": "Posible; SE robustos usados"
    }
  },
  "analisis_por_departamento": [
    {
      "departamento": "Consultoría",
      "brecha_pct": 15.2,
      "p_value": 0.0001,
      "significativo": true,
      "mujeres_n": 58,
      "hombres_n": 92,
      "recomendacion": "Investigación prioritaria"
    },
    {
      "departamento": "Operaciones",
      "brecha_pct": 2.1,
      "p_value": 0.58,
      "significativo": false,
      "mujeres_n": 45,
      "hombres_n": 51,
      "recomendacion": "Sin evidencia de brecha"
    },
    {
      "departamento": "Finanzas",
      "brecha_pct": 9.8,
      "p_value": 0.04,
      "significativo": true,
      "mujeres_n": 31,
      "hombres_n": 63,
      "recomendacion": "Revisar estructura salarial"
    }
  ],
  "cumplimiento_normativo": {
    "rdl_902_2020": {
      "aplica": true,
      "razon": "Empresa con >250 empleados",
      "diagnostico_requerido": true,
      "fecha_obligatorio": "2024-12-31",
      "documento_utilizable": "Sí; es diagn. RDL 902/2020"
    },
    "eu_pay_transparency_directive": {
      "aplica": true,
      "derechos_empleados": "Acceso a info salarial comparable",
      "obligaciones_empresa": "Transparencia salarial interna",
      "transposicion_españa": "Pendiente; borradores en consulta"
    },
    "proteccion_datos_rgpd": {
      "base_legal": "Art. 6.1.c (obligación legal: RDL 902/2020)",
      "datos_sensibles": "Género = dato especial (art. 9); requiere salvaguardas",
      "medidas": "Anonimización en reportes; acceso restringido"
    }
  },
  "plan_accion_recomendado": [
    {
      "accion": "Auditoría de estructura salarial en Consultoría",
      "prioridad": "CRÍTICA",
      "plazo": "60 días",
      "presupuesto": "auditoría_externa_3k_5k",
      "responsable": "RRHH + Finanzas",
      "objetivo": "Identificar si gap es discriminatorio o justificable (mercado, desempeño)"
    },
    {
      "accion": "Ajuste salarial correctivo para mujeres senior",
      "prioridad": "ALTA",
      "plazo": "Q1 2025",
      "presupuesto": "estimado_120k_150k",
      "responsable": "CEO + Finanzas",
      "objetivo": "Cerrar 50% del gap no explicado (3.3 pts)"
    },
    {
      "accion": "Revisión de promociones últimos 2 años",
      "prioridad": "MEDIA",
      "plazo": "90 días",
      "presupuesto": "0",
      "responsable": "RRHH",
      "objetivo": "Verificar equidad en acceso a niveles senior"
    },
    {
      "accion": "Transparencia salarial interna",
      "prioridad": "ALTA",
      "plazo": "2025",
      "presupuesto": "0",
      "responsable": "RRHH + Legal",
      "objetivo": "Alinearse con EU Directive; reducir conflictividad"
    }
  ],
  "limitaciones_metodologicas": [
    "Variables omitidas: educación específica, habilidades idiomas, certificaciones (no disponibles en nómina)",
    "Causalidad: análisis es correlacional; no prueba discriminación per se",
    "Outliers: 2 casos descartados (pensionistas, excedencias > 6 meses)",
    "Sesgo temporal: análisis de corte transversal; no incluye rotación de personal"
  ],
  "certificacion": {
    "analista": "Especialista en Equidad Salarial",
    "fecha_informe": "2025-02-06",
    "metodologia": "Conforme a estándares EU-EIGE y OIT",
    "confidencialidad": "Anonimizado; cumple RGPD",
    "defensa_judicial": "Documento defensable en Inspección de Trabajo y juzgados"
  }
}
```

---

## Ejemplo Práctico: Escenario Real

**Empresa**: Bufete jurídico de 280 abogados (40% mujeres)

**Hallazgo**: Brecha 18% media, pero controlando antigüedad cae a 6.5%
- Mujeres contratadas hace 3.5 años promedio
- Hombres hace 6.2 años promedio
- Explicado: 65% (antigüedad)
- No explicado: 35% (sugiere sesgo de género, pero alternativas: mercado de selección, negociación inicial)

**Acción**: Auditoría cualitativa de procesos de negociación salarial por género

---

## Módulo de Medidas Correctoras

Plan de acción para **cierre de brechas salariales** identificadas en diagnóstico.

### Estructura Medidas Correctoras (RD 901/2020 Compliance)

```
PLAN_ACCION = {
  "Brecha detectada": "13.8% (mujeres vs. hombres)",
  "Análisis causa": "7.2% explicada (antigüedad); 6.6% NO explicada (sesgo)",
  "Gap_no_explicado_euros": "6.6% × €47.800 (salario hombre medio) = €3.155/año",
  "Empleados afectados": 134 mujeres × €3.155 = €421.570 anual

  "Medidas_correctoras": [
    {
      "accion": 1,
      "descripcion": "Ajuste salarial directo (catch-up)",
      "poblacion": "Mujeres Senior Consultant (n=42); brecha 12.8%",
      "mecanismo": "Aumento base: €45.500 → €51.360 (12.8% correction)",
      "costo_anual": 42 × (€51.360 - €45.500) = €242.520,
      "timeline": "Q1 2025 (Enero–Marzo)",
      "prioridad": "CRÍTICA",
      "justificacion": "STS jurisprudencia: empresa DEBE corregir discriminación detectada",
      "KPI_monitoring": [
        "% adjustment applied (target: 100%)",
        "Satisfacción empleada post-aumento (survey)",
        "Retention rate mujeres 12 meses post-aumento"
      ]
    },
    {
      "accion": 2,
      "descripcion": "Cambio política promoción (structural)",
      "poblacion": "Todos empleados; focus en mujeres subrepresentadas senior roles",
      "mecanismo": "Criterios promoción: MERIT-BASED ONLY (eliminar sesgos inconscientes)",
      "implementacion": [
        "Training evaluadores: Unconscious bias training (mandatory 4h; anual)",
        "Definición criteria: Transparent; published (todos candidatos ven standard)",
        "Committee review: Multi-gender panel (mínimo 1 mujer evaluadora)",
        "Documentation: Justificación si denegada promoción (auditoriable)"
      ],
      "costo": €5.000 training + €2.000 consultant + €0 implementation,
      "timeline": "Q2 2025 (Implementación); Q1 2026 (First promotion cycle)",
      "prioridad": "ALTA",
      "justificacion": "Ley 15/2022: Plans igualdad DEBEN incluir medidas ocupacionales",
      "KPI_monitoring": [
        "Promotion rate mujeres vs. hombres (target: parity)",
        "Time-to-promotion por género (target: equal)",
        "Diversity Senior Consultant level (target: 40% mujeres)"
      ]
    },
    {
      "accion": 3,
      "descripcion": "Nivelación salarial gradual (prevention future gaps)",
      "poblacion": "Todas nuevas contrataciones Senior+ (2025+)",
      "mecanismo": "Matriz salarial explícita: nivel + antigüedad → salario band",
      "implementacion": [
        "Define bands: Junior €28–32K, Senior €45–55K, Manager €65–85K",
        "Transparent: Publicar matriz en job description; candidatos saben expectativa",
        "No negotiation variance: Oferta = banda estándar (elimina gender negotiation gap)",
        "Review anual: Ajustar bandas si mercado cambia"
      ],
      "costo": €3.000 HR consulting (one-time),
      "timeline": "Q1 2025 (Design); Q2 2025 (Deploy for new hires)",
      "prioridad": "MEDIA",
      "justificacion": "Ley 15/2022: Measures deben incluir transparent compensation",
      "KPI_monitoring": [
        "Starting salary parity (target: <5% gap)",
        "Variance from band for new hires (target: 0%)"
      ]
    },
    {
      "accion": 4,
      "descripcion": "Compensación mujeres en roles occupationally-segregated",
      "poblacion": "Departamento Operaciones (women-heavy, lower-paid)",
      "mecanismo": "Role reclassification: Operations roles revaluadas (point factor job eval.)",
      "implementacion": [
        "Job evaluation: Points for responsibility, complexity, skill",
        "Benchmark: Compara vs. Consulting roles (hombres-heavy)",
        "Reclassification: Si Operations roles underpaid, adjust bands",
        "Costo: €10K–€15K consultant (job evaluation study)"
      ],
      "timeline": "Q2–Q3 2025",
      "prioridad": "MEDIA-ALTA",
      "justificacion": "STS: Segregación ocupacional vertical es discriminación indirecta",
      "KPI_monitoring": [
        "Salary band parity post-reclassification (target: <3% gap)",
        "Retention Operations dept. (target: ≥95% annual)"
      ]
    }
  ],

  "Presupuesto_total": {
    "Año 1 (2025)": "€242.520 (ajustes) + €10.000 (training) + €3.000 (consulting) = €255.520",
    "Año 2 (2026+)": "Ongoing: ~€15.000 (training) + recurrence de ajustes si gap persiste",
    "ROI": "Reduced litigation (~€500K potential if lawsuit avoided) >> €255K cost"
  },

  "Cumplimiento_normativo": {
    "RD_902_2020": "Plan igualdad DEBE incluir medidas correctoras (Art. 5.1.c)",
    "Ley_15_2022": "Measures deben cubrir: compensación, promoción, occupational segregation",
    "STS_jurisprudencia": "STS 305/2009: Empresa debe demostrar corrección discriminación"
  },

  "Comunicación": {
    "A_empleadas": "Carta personal: 'Empresa ha detectado brecha salarial histórica. Aumento €XXX aprobado; effective 01/04/2025'",
    "A_management": "Briefing: Policy cambio; promoción criteria; training mandatory",
    "A_board": "Report: Brecha, impacto legal, medidas, presupuesto, timeline"
  },

  "Monitoreo_24_meses": {
    "Mes_3": "Check: Ajustes procesados (100% compliance verificación)",
    "Mes_6": "Encuesta empleadas: Satisfacción con aumento; perception sesgo residual",
    "Mes_12": "Auditoría: Brecha salarial recalculada; ¿gap cerrado?",
    "Mes_24": "Evaluación: Nuevas contrataciones; promociones; retention metrics"
  }
}
```

---

## Simulación de Costes de Cierre de Brecha

Modelo financiero: **investimiento hoy vs. riesgos legales tomorrow**.

### Cálculo Integral de Costes (Brecha Salary Equity)

```
ESCENARIO: Empresa 340 empleados; brecha 13.8%; sin acción correctora

═══════════════════════════════════════════════════════════════════════

OPCIÓN A: NO HACER NADA (Business as usual)

Costes año 1:
├─ Brecha continúa: €421.570 anual (mujeres under-paid)
├─ Riesgo litigio: 40% probabilidad demanda colectiva en 3 años
│  └─ Si demanda prospera: €421.570 × 3 años × 10% interests = €463.727
│  └─ + Abogado + costes judiciales: €30K–€50K
│  └─ + Daños morales/perjuicio: €50K–€200K (dependiendo sentencia)
│  └─ Coste esperado litigio: 0.40 × (€463.727 + €100K) = €225.491
│
├─ Riesgo AEPD sanción: 10% probabilidad
│  └─ Si sanción: €10K–€600K (GDPR Art. 83) + €10K–€100K (Ley 15/2022)
│  └─ Coste esperado: 0.10 × €100K = €10.000
│
├─ Reputacional: Medio (~5% risk publicidad negativa)
│  └─ Si media: -2% reputación; impacta reclutamiento/retention
│  └─ Coste estimado: 0.05 × €30K (recruitment premium) = €1.500
│
├─ Litigio interno (empleada individual): 25% probabilidad
│  └─ Si demanda: €463.727 + costes + daños morales €100K = ~€600K
│  └─ Coste esperado: 0.25 × €600K = €150.000
│
└─ COSTE ESPERADO AÑO 1 (SIN acción): €225.491 + €10.000 + €1.500 + €150.000 = €386.991

PROYECCIÓN 3 AÑOS (NO acción):
├─ Costes brecha continúa: €421.570 × 3 = €1.264.710
├─ Costes litigio (esperados): €386.991 × 3 = €1.160.973
└─ TOTAL 3 AÑOS: €2.425.683

═══════════════════════════════════════════════════════════════════════

OPCIÓN B: HACER MEDIDAS CORRECTORAS (Catch-up + prevention)

Inversión año 1 (2025):
├─ Ajuste salarial mujeres (one-time): €242.520
├─ Training + consulting: €10.000
├─ Matriz salarial design: €3.000
├─ Comunicación + legal review: €2.000
│
└─ INVERSIÓN AÑO 1: €257.520

Costes año 2–3 (mantenimiento):
├─ Nuevas contrataciones parity: €0 (no cost si bien diseñado)
├─ Training anual (bias reduction): €5.000/año
├─ Auditoría brecha (anual): €5.000/año
├─ Ajustes salarios si inflation/market: ~€15K/año
│
└─ COSTES AÑOS 2–3: €25.000/año

Beneficios año 1+:
├─ Litigio risk reduction: 5% (down from 40%)
│  └─ Litigio avoided probability: 0.35 × €600K = €210.000 SAVED
│
├─ AEPD sanction risk reduction: 0% (compliant company)
│  └─ AEPD risk avoided: 0.10 × €100K = €10.000 SAVED
│
├─ Reputacional improvement: +1% (proactive equality empresa)
│  └─ Recruitment premium reduction: 0.05 × €30K = €1.500 SAVED
│
├─ Empleada retention: +5% (satisfaction improvement post-raise)
│  └─ Retention saving (fewer replacements): 0.05 × €30K = €1.500 SAVED
│
└─ BENEFICIOS NETO AÑO 1: €210.000 + €10.000 + €1.500 + €1.500 = €223.000

PROYECCIÓN 3 AÑOS (CON acción):
├─ Inversión total: €257.520 + €25.000 + €25.000 = €307.520
├─ Beneficios (risk reduction): €223.000 × 3 = €669.000
├─ Brecha continuing: €0 (solved; no ongoing payment of gap)
│
└─ NET BENEFIT 3 AÑOS: €669.000 - €307.520 = €361.480 GAIN

═══════════════════════════════════════════════════════════════════════

COMPARATIVA: A vs. B

Opción A (NO acción): €2.425.683 coste
Opción B (Medidas): €307.520 - €669.000 beneficios = -€361.480 (GAIN)

AHORRO NETO: €2.425.683 - (€307.520 - €669.000) = €2.787.163

ROI MEDIDAS CORRECTORAS:
└─ Inversión: €307.520
└─ Beneficio: €669.000 (risk reduction) + €361.480 (avoided cost)
└─ ROI: (€669.000 + €361.480) / €307.520 = 335% RETURN

═══════════════════════════════════════════════════════════════════════

SENSIBILIDAD ANÁLISIS (¿Si assumptions wrong?)

Escenario Pesimista (litigio probability 60%, not 40%):
├─ Opción A (no acción): €3.6M coste esperado
├─ Opción B (medidas): €307K + mantenimiento
├─ Diferencia: €3.3M ahorrados

Escenario Optimista (litigio probability 20%):
├─ Opción A: €1.2M coste esperado
├─ Opción B: €307K inversión
├─ Diferencia: €0.9M ahorrados

CONCLUSIÓN: En TODOS escenarios, medidas correctoras son ROI positivo.
```

### Scenario Modeling: Immediate vs. Gradual Closure

```
ESCENARIO 1: IMMEDIATE (One-time adjustment, Q1 2025)
├─ Mujeres Senior: Aumento 12.8% → full parity de repente
├─ Presupuesto: €242.520 one-time
├─ Mensaje: "Empresa reconoce error histórico; rectifica NOW"
├─ Ventaja: Cierre rápido; buena PR (proactive)
├─ Riesgo: Hombres podrían cuestionar (jealousy); cuidado comunicación
├─ Timeline legal: Evita más acumulo años discriminación
└─ Recomendación: PREFERRED si brecha comprobada; risks justified

ESCENARIO 2: GRADUAL (Catch-up over 3 years, plus new hires)
├─ Ajuste: 4.27% anual (12.8% ÷ 3 años)
│  ├─ 2025: Aumentos 4.27%
│  ├─ 2026: Aumentos 4.27% (compounded)
│  └─ 2027: Ajuste final para full parity
├─ Presupuesto spread:
│  ├─ 2025: €80.840
│  ├─ 2026: €84.460
│  ├─ 2027: €88.220
│  └─ Total: €253.520 (similar cost, slightly more due to compounding)
├─ Ventaja: Presupueto spread; less shock year 1; tiempo "normalize"
├─ Riesgo: Si litigio before 2027, only partial remediation; juzgado puede penalizar
├─ Recomendación: SI presupuesto constrained; pero MENOS preferred legalmente
└─ Timeline: Año 3 (2027) mujeres paid equitably

═════════════════════════════════════════════════════════════════════

MODELO COMBINADO (Recommended):
├─ Immediate: 50% catch-up año 1 (€121.260; signal company serious)
├─ Gradual: 50% catch-up años 2–3 (€121.260 distributed)
├─ Plus: Market-alignment para nuevas contrataciones (year 2+ parity)
├─ Presupuesto: €257K spread over 3 años
├─ Timeline: 2025–2027 full remediation
└─ Message: "Empresa committed; progreso visible; confidence building"

BUDGET IMPACT (Año 1):
├─ Salary adjustment: €121.260
├─ Training/consulting: €10.000
├─ Matriz salarial: €3.000
└─ Total: €134.260 (40% presupuesto medidas correctoras)
└─ Como % of payroll: €134.260 / (340 empl × €42.5K avg) = 0.93% (reasonable)
```

---

## Herramientas Estadísticas

```python
import numpy as np
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.robust.robust_linear_model import RLM

# Test de igualdad de medias
t_stat, p_val = stats.ttest_ind(salarios_mujeres, salarios_hombres)

# Regresión multivariante robusta a heterocedasticidad
model = RLM.from_formula('log(salario) ~ C(genero) + antiguedad + C(nivel)', df)
results = model.fit()
results.summary()

# Oaxaca-Blinder (librería oaxaca o manual)
```

---

## Financial Disclosure (Compliance RDL 901/2020 + Ley 15/2022)

Si brecha salarial detectada y empresa >250 empleados:

1. **Diagnóstico** (obligatorio bienal): Documentado, metodología rigurosa
2. **Publicación**: Plan igualdad debe ser PUBLIC (Ley 15/2022 Art. 14)
3. **Medidas correctoras**: DEBEN CONSTAR en Plan (no optional)
4. **Timeline**: Medidas comunicadas públicamente (empresa intranet mínimo)
5. **Auditoría**: Externa recomendada (demuestra diligencia)
6. **Renovación**: Bienal (2 años) per RDL 901/2020
