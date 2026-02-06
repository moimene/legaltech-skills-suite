---
name: batna-calculator
description: Cuantifica el BATNA (Best Alternative to Negotiated Agreement) mediante teoría de juegos, valor esperado descontado y análisis de sensibilidad. Aplicable en: decisión bilateral litigio vs. acuerdo pre-demanda, evaluación de ofertas de composición en mediación/arbitraje, negociaciones multipartes (ejecución, terceros financiadores), planificación de recursos con impacto de financiación externa. Integra Nash Equilibrium, simulación Monte Carlo, y referencias a Ley 5/2012 mediación + Ley 60/2003 arbitraje españolas.
---

# BATNA Calculator

## Descripción General

Decidir si pactar o litigar es la decisión más relevante en cualquier disputa. Tradicionalmente se resuelve por intuición; esta skill la automatiza con rigor matemático.

**Problemas que resuelve**:
1. **Decisión bilateral**: ¿Aceptamos la oferta de 45.000€ o litigamos por 100.000€?
2. **Multipartes**: En mediación con 3 partes, ¿cuál es mi BATNA si desaparece la Parte C?
3. **Financiación externa**: Si un tercero financia mi litigio (30% del premio), ¿cambia el BATNA?
4. **Sensibilidad**: ¿Qué cambio en probabilidad de éxito hace que prefiera el acuerdo?

**Fundamento**: Cálculo de Valor Esperado descontado (EV) de litigio vs. alternativa (acuerdo, arbitraje, etc.). Si oferta > EV(litigio), aceptar racionalmente.

**Limitaciones**: Asume racionalidad económica; no captura factores no monetarios (reputación, precedente, relación comercial continuada).

---

## Topología de Aplicación

```
┌──────────────────────────────────────────┐
│ Inputs:                                  │
│ - Cantidad reclamada / Defensa           │
│ - Probabilidades por escenario           │
│ - Costes (honorarios, periciales, tasas)│
│ - Duración estimada + Tasa descuento     │
│ - Oferta(s) de acuerdo                   │
│ - [Opcional] Financiador externo         │
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│ Árbol de Decisión Probabilístico         │
│ - Nodo decisión: LITIGAR vs ACORDAR      │
│ - Nodos azar: Victoria/Parcial/Derrota   │
│ - Nodos resultado: Valor neto            │
└────────────┬─────────────────────────────┘
             │
      ┌──────┴──────┐
      ▼             ▼
  ┌────────┐   ┌──────────┐
  │EV Lit. │   │EV Acuerdo│  (descuento temporal + financiación)
  └────┬───┘   └────┬─────┘
       │            │
       └─────┬──────┘
             ▼
    ┌─────────────────┐
    │Comparación y    │
    │Sensibilidad     │  Nash Equilibrium (si es bilateral)
    │(simulación MC)  │
    └────────┬────────┘
             ▼
    ┌─────────────────────────┐
    │ Output: Recomendación   │
    │ BATNA + Tácticas        │
    └─────────────────────────┘
```

---

## Cuándo Usar (Triggers Específicos)

### Pre-demanda / Oferta Inicial
- Contraparte ofrece acuerdo antes de litigar
- Necesitamos BATNA para negociar con datos
- ¿Conviene litigar o pactar? Usar skill para fundamentar decisión

### En Mediación (Ley 5/2012)
- Mediador presenta propuesta de composición a ambas partes
- Calcular EV con nueva información de la otra parte
- Identificar rango de negociación (mi BATNA - su BATNA)

### En Arbitraje (Ley 60/2003)
- Pre-arbitraje: evaluar alternativa vs. sentencia arbitral esperada
- Re-evaluación periódica (cambios en prueba, nuevos datos)

### Multi-partes (Ejecución, Terceros)
- Tercero interesado en el litigio: ¿Le sumo como acreedor?
- Ejecución de sentencia + costas: recalcular EV con nuevos costes/plazos

### Financiación Externa de Litigios
- Fondo de inversión ofrece financiar litigio por 30% del premio
- Impacto en BATNA: EV(litigio) × 0.7 - costes remanentes

---

## Conceptos Clave

### BATNA (Best Alternative to Negotiated Agreement)

Es el valor presente neto esperado del litigio (descontado). Si una oferta de acuerdo supera el BATNA, racionalmente aceptarla. Si la oferta < BATNA, rechazar.

**Nota importante**: BATNA no es "ganar todo". Es el valor promedio ponderado por probabilidades, descontado al presente.

### Valor Esperado (EV) del Litigio

```
EV_bruto = (P_victoria_total × Cantidad)
         + (P_victoria_parcial × Cantidad_parcial)
         + (P_derrota × 0)

EV_neto = EV_bruto - Costes_juicio - P_derrota × Costes_contraparte

EV_presente = EV_neto / (1 + r)^n
              donde r = tasa descuento, n = años
```

### Nash Equilibrium en Negociación Bilateral

Si la oferta de ambas partes genera un área de "solución posible" (zona donde mejora a ambas vs. litigios):
- Equilibrio cooperativo: repartir ganancias de acuerdo proporcionalmente
- Equilibrio no cooperativo: resultado esperado si no hay acuerdo (nuestro BATNA)

---

## Inputs

| Parámetro | Tipo | Descripción | Ejemplo | Nota |
|-----------|------|-------------|---------|------|
| `cantidad_reclamada` | float | Cantidad que reclamamos en demanda | 100,000€ | Principal + intereses + costas |
| `prob_victoria_total` | float | Probabilidad de estimación total | 0.40 | Usar Judicial Profiler para este juez |
| `prob_victoria_parcial` | float | Probabilidad de estimación parcial | 0.30 | P_total + P_parcial + P_derrota = 1.0 |
| `cantidad_parcial` | float | Cantidad si estimación parcial | 60,000€ | Defecto: 60% cantidad reclamada |
| `costes_juicio` | float | Honorarios + tasas + periciales | 15,000€ | Incluir posibles costes de apelación |
| `costes_condena` | float | Costes si perdemos (condena en costas) | 12,000€ | Estimación baja: 0.5-1.0 × nuestros costes |
| `duracion_anos` | float | Tiempo estimado hasta sentencia | 2.5 | Según histórico judicial (Judicial Profiler) |
| `tasa_descuento` | float | Coste del dinero anual (% decimal) | 0.05 | Usar CECA (BCE) + prima riesgo contraparte |
| `oferta_acuerdo` | float (optional) | Oferta que evaluamos | 45,000€ | Si omitir, calcular solo BATNA |
| `porc_tercero_financiador` | float (optional) | % del premio que cede a financiador | 0.30 | Si hay litigation funding, 20-40% típico |
| `num_partes_multipartes` | integer (optional) | Si hay >2 partes, número | 3 | Para análisis coalicional |

---

## Output

```json
{
  "metadata": {
    "caso": "Reclamación de 100.000€ por incumplimiento de contrato",
    "fecha_analisis": "2025-02-06",
    "juez_asignado": "Juzgado Mercantil 3 de Madrid",
    "nota": "Probabilidades basadas en perfil de Judicial Profiler"
  },
  "analisis_valor_esperado": {
    "escenario_litigio": {
      "ev_bruto": 42500,
      "formula": "(0.40 × 100000) + (0.30 × 60000) + (0.30 × 0) = 40000 + 18000 + 0",
      "ev_neto": 27500,
      "detalles_costes": {
        "costes_nuestros": 15000,
        "costes_condena_si_perdemos": 3600,
        "total_rest": 18500
      },
      "ev_valor_presente": 24650,
      "duracion_anos": 2.5,
      "tasa_descuento": 0.05,
      "formula_vp": "27500 / (1.05^2.5) = 24650"
    },
    "batna": 24650,
    "interpretacion": "Nuestro peor aceptable (si no hay acuerdo) es 24.650€ en dinero de hoy"
  },
  "evaluacion_oferta": {
    "oferta_contraparte": 45000,
    "batna": 24650,
    "diferencia": 20350,
    "beneficio_vs_litigio": "82.6%",
    "decision": "ACEPTAR_OFERTA"
  },
  "recomendacion": {
    "nivel_confianza": "ALTA (0.92)",
    "razon": "La oferta supera el BATNA en €20.350 (82.6% del BATNA)",
    "accion": "Aceptar oferta de 45.000€ o contrapropuesta entre 35.000-45.000€",
    "nota": "Solo si no cambian probabilidades de éxito (ej. descubrimiento de prueba crítica)"
  },
  "analisis_multipartes": {
    "estructura": "3 partes si incluimos tercero interesado",
    "escenarios_coaliciones": [
      {
        "coalicion": "Nosotros + Tercero vs. Contraparte",
        "ev_conjunto": 32100,
        "reparticion_posible": "Nosotros: 24650, Tercero: 7450"
      }
    ]
  },
  "impacto_financiacion_externa": {
    "financiador_solicita": "30% del premio",
    "ev_neto_postfinancia": "27500 × 0.70 = 19250",
    "ev_presente": "19250 / 1.05^2.5 = 17255",
    "nuevo_batna": 17255,
    "oferta_sigue_siendo_mejor": true,
    "nota": "Si financiador entra, BATNA baja, pero oferta sigue siendo preferible"
  },
  "sensibilidad": [
    {
      "variable": "prob_victoria_total",
      "valor_actual": 0.40,
      "umbral_indiferencia": 0.58,
      "interpretacion": "Si probabilidad sube a 58%, BATNA igualaría oferta (punto de indiferencia)"
    },
    {
      "variable": "costes_juicio",
      "valor_actual": 15000,
      "umbral_maximo_para_aceptar": 8500,
      "interpretacion": "Si costes suben a 8.500€, seguimos prefiriendo acuerdo"
    },
    {
      "variable": "tasa_descuento",
      "valor_actual": 0.05,
      "rango_sensibilidad": [0.03, 0.08],
      "ev_en_rango": [25100, 24200],
      "nota": "Resultado robusto a cambios en tasa"
    }
  ],
  "arbol_decision_visual": {
    "nodo_raiz": "DECISION: ¿LITIGAR O ACORDAR?",
    "rama_litigar": {
      "nodo_azar": "Sentencia",
      "rama_victoria_total": {
        "probabilidad": 0.40,
        "resultado_neto": "100000 - 15000 = 85000"
      },
      "rama_victoria_parcial": {
        "probabilidad": 0.30,
        "resultado_neto": "60000 - 15000 = 45000"
      },
      "rama_derrota": {
        "probabilidad": 0.30,
        "resultado_neto": "-15000 - 12000 = -27000"
      },
      "ev_neto_litigio": 27500,
      "ev_presente": 24650
    },
    "rama_acordar": {
      "probabilidad": 1.0,
      "resultado_seguro": 45000,
      "ventaja_vs_litigio": 20350
    }
  },
  "referencias_legales": [
    "Ley 5/2012 de mediación: Art. 2 (objeto) - BATNA es base de negociación en mediación previa obligatoria",
    "Ley 60/2003 de arbitraje: Art. 32 - Acuerdo transaccional durante arbitraje",
    "Art. 19 CC: Transacción = contrato que pone fin a litigio (requisito: ambas partes renuncien a parte de pretensión)",
    "STS 1141/2019: Criterio de razonabilidad en aceptación de acuerdos (BATNA es referente implícito)"
  ],
  "simulacion_monte_carlo": {
    "iteraciones": 10000,
    "variables_aleatorias": ["prob_victoria", "costes_reales", "duracion"],
    "percentiles_ev": {
      "p10": 18900,
      "p50": 24650,
      "p90": 31200
    },
    "probabilidad_batna_menor_45000": 0.87,
    "interpretacion": "En 87% de escenarios aleatorios, la oferta es mejor que litigar"
  }
}
```

## Ejemplo Práctico: Disputa de Arrendamiento Comercial

**Caso**: Desahucio por falta de pago. Arrendador reclama 60.000€ (12 meses + intereses + daños). Inquilino ofrece pagar 35.000€ ahora.

**Escenario 1: Juzgado de lo Civil (No especializado)**
- Probabilidad estimada victoria total: 65% (caso claro, prueba documental contundente)
- Probabilidad parcial (6 meses): 20%
- Costes juicio: 8.000€
- Duración: 18 meses (1.5 años)
- Tasa descuento: 5%

**Cálculo BATNA**:
```
EV_bruto = 0.65 × 60000 + 0.20 × 30000 + 0.15 × 0
         = 39000 + 6000 = 45000€

EV_neto = 45000 - 8000 = 37000€

BATNA = 37000 / (1.05^1.5) = 35400€
```

**Análisis**: Oferta (35.000€) < BATNA (35.400€) → Rechazar y litigar (marginal).

**Escenario 2: Añadimos financiador (litigation funding)**
- Financiador entra con 30% del premio
- EV_neto_postfinancia = 37000 × 0.70 = 25900€
- BATNA_nuevo = 25900 / 1.05^1.5 = 24800€

**Recomendación**: Ahora oferta (35.000€) > BATNA_nuevo (24.800€) → Aceptar (diferencia: €10.200).

---

## Fórmulas Detalladas

### Valor Esperado Bruto del Litigio

```
EV_bruto = Σ (P_escenario_i × Resultado_i)

Para 3 escenarios (victoria total, parcial, derrota):
EV = (P_total × Cantidad)
   + (P_parcial × Cantidad_parcial)
   + (P_derrota × 0)
```

### Deducción de Costes

```
EV_neto = EV_bruto - Costes_nuestros - (P_derrota × Costes_condena_contraparte)
```

Nota: Costes condena solo aplican si perdemos (ponderado por P_derrota).

### Descuento Temporal (Valor Presente)

```
BATNA = EV_neto / (1 + r)^n

donde:
  r = tasa descuento anual (típicamente 4-6%)
  n = duración en años (incluir apelación si procede)
```

Interpretación: €100 hoy > €100 en 2.5 años. El factor (1.05^2.5 ≈ 1.13) refleja el coste de esperar.

### Nash Equilibrium Bilateral

```
Si zona de negociación existe: [BATNA_demandante, BATNA_demandado]

Equilibrio cooperativo proporcional:
Acuerdo_optimo = BATNA_demandante + (BATNA_demandado - BATNA_demandante) × α

donde α ∈ [0,1] refleja poder negociador
```

### Simulación Monte Carlo

Iterar 10.000 veces:
1. Variar P_total, P_parcial (distribuciones normales, σ=0.05)
2. Variar costes (±20% uniforme)
3. Variar duración (±6 meses)
4. Calcular BATNA en cada iteración
5. Generar distribución de resultados (percentiles, probabilidad de aceptación)

---

## Análisis de Sensibilidad

Para cada variable clave, calcular:
- **Umbral de indiferencia**: ¿Qué valor de variable hace BATNA = Oferta?
- **Rango de robustez**: Cambio en resultado si variable ± 10%

Ejemplo:
```
Probabilidad victoria total:
  - Actual: 40% → BATNA 24.650€
  - Umbral: 58% → BATNA = 45.000€ (oferta)
  - Cambio: +18 pp de probabilidad causa cambio decisión
```

---

## Marco Legal y Referencias

### Ley 5/2012 de Mediación (Obligatoria previa)

- **Art. 2**: Mediación como alternativa antes de litigio
- **Art. 10**: Sesiones individuales (BATNA se calcula antes)
- **Art. 12**: Acuerdos mediados tienen valor de transacción (Art. 19 CC)

### Ley 60/2003 de Arbitraje

- **Art. 2**: Arbitraje como alternativa a juzgados
- **Art. 32**: Durante arbitraje, partes pueden llegar a acuerdo (sale del proceso)
- BATNA = EV(arbitraje) típicamente > EV(juzgados) por especialización

### Código Civil

- **Art. 19**: Transacción requiere renuncia recíproca (ambas partes ceden parte)
  - Validez: ambas renuncian a derecho discutido
  - BATNA es argumento racional para justificar renuncia
- **Art. 1.699**: Mediación como causal de no responsabilidad

### Jurisprudencia

- **STS 1141/2019**: Criterio de "razonabilidad" de acuerdos
  - Tribunal valida transacción si ambas partes renuncian proporcionalmente
  - BATNA sirve como benchmark de "razonable"

---

## Limitaciones Reconocidas

1. **Probabilidades subjetivas**: Los datos de entrada (P_victoria) son estimaciones. Usar Judicial Profiler para mejorar.
2. **Factores no monetarios**: Reputación, precedente, relación comercial futura no se capturan.
3. **Asunción racionalidad**: Modelo asume ambas partes maximizan valor; en realidad hay sesgo, emociones, restricciones de liquidez.
4. **Cambios probatorios**: Si aparece prueba nueva (descubrimiento tardío), recalcular BATNA.
5. **Multipartes complejo**: Con 3+ partes, coaliciones son dinámicas; modelo simplifica.

---

## Escenarios Procesales LEC

### Modelo de Costas (Arts. 394-398 LEC)

El impacto de costas es decisivo en el BATNA. Seguir criterios:

**Vencimiento objetivo** (Art. 394 LEC):
- Parte que pierde en su pretensión: condena a costas
- Cantidad: "costas, incluyendo gastos de representación, peritos e impuestos"
- Estimación estándar: 10-40% del valor de condena (variable por jurisdicción)

| Escenario | Estimación | Ratio Costas |
|---|---|---|
| Victoria total (100% reclamado) | Condenamos a contraparte a 100% costas | 15-25% × Condena |
| Victoria parcial (60%) | Regla proporcional (prorrateo 60%) | 10-15% × Condena parcial |
| Derrota total | Condena a nosotros a costas | 15-25% × Nuestros costes × 1.5 |
| Desestimación parcial con estimación | Cálculo complejo; ver STS jurisprudencia | Caso-por-caso |

**Aplicación en BATNA**:
```
EV_neto_con_costas = (P_victoria_total × Cantidad × 0.85)
                   + (P_victoria_parcial × Cantidad_parcial × 0.90)
                   - (P_derrota × Costes_nuestros × 1.25)
```

Nota: Factor 0.85/0.90 refleja deducción de costas de condena; factor 1.25 en derrota incluye condena a costas del contraparte.

### Impacto de Carga de Prueba (Art. 217 LEC)

**Dinámica probatoria**: Quien tiene mejor acceso a prueba debe aportar; en defecto, se presume desfavorable.

| Tipo Litigio | Carga Estándar | Impacto EV |
|---|---|---|
| Incumplimiento contractual | Demandante (prueba del contrato + incumplimiento) | -10% EV si prueba débil |
| Responsabilidad civil (daño/culpa) | Demandante | -15% EV si no hay prueba directa |
| Garantía de producto (vicio oculto) | Demandado (Art. 217.2 LEC) | +10% EV si somos demandante |
| Hechos negativos | Muy difícil demandante | -20% EV |

**Recomendación**: Si análisis BATNA muestra EV bajo por carga probatoria débil, considerar:
- Actuación de prueba de oficio (Art. 429 LEC)
- Pericial técnica que fortalezca posición
- Reconocimiento de hechos en escrito de contestación (obliga a demandante a contraprueba)

### Medidas Cautelares (Arts. 721-747 LEC)

Impacto en BATNA de solicitud/oposición a cautelares:

**Coste de caución** (Art. 741 LEC):
- Demandante solicita cautelar: tribunal exige caución por posible daño a demandado
- Caución típica: 10-30% del objeto del litigio
- Impacto BATNA: Restar caución de EV inicial si se solicita + mantiene durante proceso

**Timing** (efecto psicológico):
- Cautelar decretada temprano: fortalece posición negociadora demandante (+5-10% en BATNA)
- Cautelar denegada: debilita posición (-5-10%)
- En mediación, considerar estado de cautelar como variable

### Ejecución Provisional (Arts. 524-537 LEC)

Sentencia favorable en primera instancia puede ejecutarse provisionalmente mientras se tramita apelación:

**Valor estratégico**:
- Si es probable sentencia favorable pero recurso previsible, ejecución provisional mejora posición
- Dinero en cuenta de depósito judicial genera presión para acuerdo
- Ajustar BATNA: Si ejecutable provisionalmente, agregar valor temporal

```
BATNA_mejorado = BATNA_base × 1.10  (si ejecución provisional probable)
```

### Recursos (Apelación, Casación)

Impacto de recursos en BATNA (antes de sentencia):

| Recurso | Duración Media | Reversal Rate | Impacto BATNA |
|---|---|---|---|
| **Apelación** (Art. 455 LEC) | 2-3 años adicionales | 20-40% (según materia) | Descuento 15% + coste +€8-12k |
| **Casación** (Art. 477 LEC) | 1-2 años adicionales | 10-15% (muy restrictivo) | Descuento 5% + coste +€5-8k |
| **Cassación para unificación** (Arts. 488-492) | 1-2 años | Muy raro (< 5% éxito) | Descuento 2% + coste +€3-5k |

**Ejemplo ajuste para riesgo de apelación**:
```
Si tasa reversal en materia = 30%, y apelación cuesta €10k adicionales:

EV_sin_recurso = €50.000
EV_con_riesgo_apelación = (0.70 × €50.000) + (0.30 × -€10.000)
                        = €35.000 - €3.000 = €32.000
```

Descontar este impacto del BATNA inicial si contraparte probable apele.

---

## Cláusulas Escalonadas MED-ARB

### Estructura Estándar: Negociación → Mediación → Arbitraje → Jurisdicción

Típicamente en contratos comerciales:

```
┌─────────────────────────────────────────┐
│ Paso 1: NEGOCIACIÓN                     │
│ - Plazo: 30 días tras aviso de disputa  │
│ - Participantes: Ejecutivos + abogados  │
│ - BATNA: No negociar = pasar a paso 2   │
└────────────────┬────────────────────────┘
                 │
        (si no acuerdo en 30 días)
                 ▼
┌─────────────────────────────────────────┐
│ Paso 2: MEDIACIÓN (Ley 5/2012)          │
│ - Plazo: 60-90 días (típico)            │
│ - Coste: €5.000-15.000                  │
│ - Resultado: ~40% acuerdos (estadística)│
│ - BATNA: Si falla, pasar a paso 3       │
└────────────────┬────────────────────────┘
                 │
        (si mediación falla)
                 ▼
┌─────────────────────────────────────────┐
│ Paso 3: ARBITRAJE (Ley 60/2003)         │
│ - Plazo: 6-12 meses                     │
│ - Coste: €50.000-200.000 (ambas partes) │
│ - Especialización: Sector específico    │
│ - Confidencialidad: Total               │
│ - Ejecutabilidad: Convenio Nueva York   │
│ - BATNA: Si falla, pasar a paso 4       │
└────────────────┬────────────────────────┘
                 │
        (si arbitraje requiere)
                 ▼
┌─────────────────────────────────────────┐
│ Paso 4: JURISDICCIÓN ORDINARIA          │
│ - Plazo: 3-5 años                       │
│ - Coste: €20.000-80.000                 │
│ - Publicidad: Pública (sentencia)       │
│ - Riesgo: Apelación hasta Cassación     │
└─────────────────────────────────────────┘
```

### Árbol de Decisión: Optimización por Escalón

En cada escalón, recalcular BATNA y evaluar si continuar o aceptar oferta:

```json
{
  "escalon_1_negociacion": {
    "plazo_dias": 30,
    "coste_incremental": 0,
    "batna_inicial": 24650,
    "oferta_recibida": 20000,
    "decision": "RECHAZAR (oferta < BATNA)",
    "accion": "Pasar a mediación"
  },
  "escalon_2_mediacion": {
    "plazo_dias": 60,
    "coste_incremental": 8000,
    "batna_ajustado": 24650 - 8000/2 = 20650,
    "oferta_mediador": 28000,
    "decision": "ACEPTAR (oferta > BATNA ajustado)",
    "accion": "Acuerdo de transacción (Art. 19 CC)",
    "razon": "Ganancia de €7.350 vs litigios"
  },
  "escalon_3_arbitraje_si_falla_med": {
    "plazo_meses": 9,
    "coste_arbitrador": 75000,
    "coste_nuestro_incremental": 45000,
    "batna_post_media_fallida": 24650 - 120000 = 95350_NEGATIVO,
    "decision": "SIN INTERES (BATNA ya negativo)",
    "recomendacion": "Nunca debería llegar aquí; median falló significa ofertas muy alejadas"
  }
}
```

### Costes Comparados por Escalón

Presupuesto típico (España, 2025):

| Escalón | Duración | Coste Bajo | Coste Medio | Coste Alto | Éxito Acuerdo |
|---|---|---|---|---|---|
| **Negociación Directa** | 1-2 meses | €500 | €2.000 | €5.000 | ~25% |
| **Mediación** (Ley 5/2012) | 2-3 meses | €3.000 | €8.000 | €15.000 | ~40% |
| **Arbitraje** (Ley 60/2003) | 8-12 meses | €30.000 | €90.000 | €200.000 | 100% (decisión vinculante) |
| **Jurisdicción** (LEC) | 2-4 años | €15.000 | €40.000 | €80.000 | 100% (sentencia) |

**Nota**: Costes de arbitraje/jurisdicción divididos típicamente entre partes (excepto condena en costas).

### Decisión Óptima en Cada Escalón (Ley 5/2012 + Ley 60/2003)

**Mediación es óptima si**:
- BATNA todavía incierto (probabilidades varían mucho)
- Relación comercial continua deseable (industria B2B)
- Confidencialidad crítica
- Coste de arbitraje/jurisdicción > 10 × coste mediación

**Arbitraje es óptimo si**:
- Mediación falló o rechazada
- Especialización técnica necesaria (construcción, IT, finanzas)
- Ejecutabilidad transfronteriza crítica (Convenio Nueva York)
- Confidencialidad absoluta exigida

**Jurisdicción ordinaria si**:
- Precedente importante (STS sentará jurisprudencia)
- Terceros afectados (imposible arbitrio confidencial)
- Materia no arbitrable (familia, laboral parcialmente)

### Impacto en Oferta Negociadora (Análisis Bilateral)

Cuando contraparte conoce escalas:

```
Mi BATNA: €24.650 (jurisdicción pura)
Mi BATNA en mediación: €24.650 - €4.000 (mi mitad coste) = €20.650
Contraparte BATNA: €18.000 (estimado)
Contraparte BATNA en mediación: €18.000 - €4.000 = €14.000

Zona de acuerdo: [€20.650, €14.000] es muy estrecha
→ Mediador propone €17.000 como split
→ Yo gano €17.000 vs €20.650 neto (pierdo €3.650) pero evito riesgo

Decisión: RECHAZAR (BATNA jurisdicción > oferta) vs ACEPTAR si incertidumbre probatoria > €3.650
```

---

## Descargo de Responsabilidad: No Sustituye Criterio del Abogado ni Voluntad del Cliente

### Uso Ético Obligatorio

**Esta herramienta es modelo matemático, no asesoramiento jurídico.**

El BATNA calculado es **estimación**, no predeterminación:

**Factores NO cuantificados**:
- Reputación de abogados (tu bufete vs. contraparte)
- Sentimientos irracionales (orgullo, venganza)
- Restricciones de liquidez (necesidad cash inmediata)
- Relaciones comerciales futuras (cliente quiere mantener contraparte)
- Precedente estratégico (caso "test" que sentará jurisprudencia)

**Procedimiento correcto de uso**:

1. **Abogado calcula BATNA** con esta herramienta
2. **Abogado explica** al cliente: "BATNA es €X, pero depende de [variables]"
3. **Abogado presenta opciones**:
   - "Aceptar oferta €Y si > BATNA"
   - "Rechazar si < BATNA"
   - "Ambiguo si muy cerca de BATNA"
4. **Cliente decide**, considerando:
   - Factores económicos (modelo sí captura)
   - Factores personales/estratégicos (modelo NO captura)
5. **Documentar decisión** en acta: "Cliente, informado de BATNA €X, autoriza rechazar oferta €Y por motivos [...]"

### Descargo en Interface de Usuario

**Pantalla que aparece antes de usar BATNA Calculator**:

> **IMPORTANTE: LIMITACIONES DE ESTA HERRAMIENTA**
>
> Este cálculo de BATNA es una **estimación matemática** basada en probabilidades que usted proporciona. **NO sustituye**:
>
> 1. **Criterio profesional del abogado**: Solo usted como letrado puede valorar calidad de prueba, abogados en juego, historia de juez
> 2. **Voluntad del cliente**: El cliente final decide si acepta/rechaza oferta, considerando factores que van más allá del dinero
> 3. **Cambios probatorios**: Si aparece prueba nueva, recalcule BATNA
> 4. **Asunción de racionalidad**: Modelo asume decisiones puramente económicas; puede no aplicarse si emociones, orgullo o precedente son drivers
>
> **Responsabilidad**: El abogado debe usar este output como **una variable más** en su análisis, no como **la decisión**.
>
> □ Entiendo las limitaciones y asumo responsabilidad profesional

### Limitaciones Reconocidas (Transparencia)

| Limitación | Consecuencia | Cómo Mitigar |
|---|---|---|
| **Probabilidades subjetivas** | BATNA es tan bueno como inputs (garbage in, garbage out) | Usar Judicial Profiler para P_victoria; documentar asunciones |
| **Factores no monetarios** | Reputación, precedente, relación comercial no se cuantifican | Análisis cualitativo del abogado en paralelo |
| **Cambios dinámicos** | Si descubrimiento nuevo cambia probabilidades, BATNA caduca | Recalcular cada 2 semanas si litigio activo |
| **Racionalidad limitada** | Clientes a veces irracional (orgullo, aversión pérdida) | Sesión de coaching con cliente sobre sesgos cognitivos |
| **Multipartes complejo** | Con 3+ partes, coaliciones dinámicas | Simplificar a bilateral o consultar especialista |

---

## Referencias

Para metodología detallada en:
- Simulación Monte Carlo: Ver `/references/batna-monte-carlo.md`
- Nash Equilibrium en negociación: Ver `/references/game-theory-aplicada.md`
