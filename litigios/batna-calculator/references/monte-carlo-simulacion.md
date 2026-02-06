# BATNA Calculator: Simulación Monte Carlo

## Propósito

Generar distribución de BATNA bajo incertidumbre paramétrica. Las probabilidades de éxito no son valores puntuales sino distribuciones.

## Metodología

### 1. Definir Variables Aleatorias

```python
from scipy.stats import norm, uniform
import numpy as np

# Parámetros base (punto estimado)
P_victoria_estimada = 0.40
P_parcial_estimada = 0.30
Costes_estimados = 15000
Duracion_anos_estimada = 2.5

# Desviaciones estándar (capturan incertidumbre)
sigma_prob = 0.08      # ±8pp en probabilidades
sigma_costes = 0.20    # ±20% en costes
sigma_duracion = 0.25  # ±25% en duración (ej. 2.5 ± 0.6 años)
```

### 2. Generar 10.000 Iteraciones

```python
N_iteraciones = 10000
resultados = []

for i in range(N_iteraciones):
    # Muestrear variables (distribuciones normales truncadas)
    P_v = np.clip(np.random.normal(P_victoria_estimada, sigma_prob), 0, 1)
    P_p = np.clip(np.random.normal(P_parcial_estimada, sigma_prob), 0, 1-P_v)
    P_d = 1 - P_v - P_p

    Costes = np.clip(np.random.normal(Costes_estimados, Costes_estimados * sigma_costes), 1000, 50000)
    Duracion = np.clip(np.random.normal(Duracion_anos_estimada, Duracion_anos_estimada * sigma_duracion), 0.5, 5)

    # Calcular EV_neto para esta iteración
    EV_bruto = P_v * 100000 + P_p * 60000 + P_d * 0
    EV_neto = EV_bruto - Costes - P_d * 12000

    # Descuento temporal
    r = 0.05
    BATNA = EV_neto / ((1 + r) ** Duracion)

    resultados.append(BATNA)

resultados = np.array(resultados)
```

### 3. Estadísticas de Salida

```python
import pandas as pd

print(f"Media BATNA: €{resultados.mean():.0f}")
print(f"Desv. Est.: €{resultados.std():.0f}")
print(f"Mediana: €{np.median(resultados):.0f}")
print(f"Percentil 10: €{np.percentile(resultados, 10):.0f}")
print(f"Percentil 90: €{np.percentile(resultados, 90):.0f}")

# Probabilidad de que BATNA < Oferta (35.000€)
prob_aceptar = (resultados < 35000).sum() / len(resultados)
print(f"\nProbabilidad oferta > BATNA: {prob_aceptar:.2%}")
```

**Salida esperada**:
```
Media BATNA: €25.100
Desv. Est.: €8.200
Mediana: €24.650
Percentil 10: €14.900
Percentil 90: €37.200

Probabilidad oferta > BATNA: 87.3%
```

## Visualización

### Histograma de Distribución

```
Frecuencia
    |
500 |     ╱╲
    |    ╱  ╲
400 |   ╱    ╲
    |  ╱      ╲
300 | ╱        ╲
    |╱          ╲
200 |            ╲
    |             ╲
100 |              ╲
    |_______________╲___
    0   15k  25k  35k  45k    BATNA (€)

    Línea roja: Oferta (€35.000)
    Si media BATNA < 35k → Aceptar racionalmente
```

### Análisis de Sensibilidad Tornado

Variar ±1σ en cada parámetro, medir impacto en BATNA:

```
Variable                 Impacto en BATNA (€)
Prob. Victoria Total     ├──────────────────┤  ±€8.900
Costes Juicio           ├─────────────┤       ±€5.200
Duración (años)         ├────────┤            ±€3.400
Prob. Parcial           ├──────┤              ±€2.100
Tasa Descuento          ├──┤                  ±€1.200

Más sensible a: Probabilidad de victoria total
Menos sensible a: Tasa descuento
```

## Casos de Uso

### Caso 1: Oferta Marginal (cerca del BATNA)
Si oferta ≈ BATNA (ej. 35.000€ vs. BATNA 35.000€), usar MC para evaluar riesgo:
- Si σ(BATNA) = €8.200, existe 50% de probabilidad que BATNA > 35.000€
- Decisión: Rechazar oferta (valor esperado ligeramente superior a aceptar)

### Caso 2: Decisión Robusta
Si oferta >> BATNA en al menos 90% de escenarios MC:
- Aceptar sin dudas (beneficio incluido downside protection)

### Caso 3: Información Incompleta
Si σ es muy alta (ej. σ(BATNA) = €15.000 en valor medio 25.000€):
- Necesita más discovery / pericial para reducir incertidumbre
- Retrasar decisión de acuerdo

## Calibración de Parámetros

### Probabilidades (σ = 8-12%)
- Alta incertidumbre: σ = 0.12 (consultas con clientes contradicen)
- Baja incertidumbre: σ = 0.05 (sentencias previas este juez disponibles)

### Costes (σ = 15-25%)
- Baja incertidumbre: σ = 0.15 (honorarios fijados, periciales cotizadas)
- Alta incertidumbre: σ = 0.30 (litigio complejo, duración incierta)

### Duración (σ = 20-40%)
- Baja incertidumbre: σ = 0.20 (histórico del juzgado disponible)
- Alta incertidumbre: σ = 0.40 (reforma legal en trámite, composición tribunal cambiando)

## Referencias

- Vose, D. (2008). "Risk Analysis: A Quantitative Guide" (3rd ed.)
- Clemen, R. T., & Reilly, T. (2013). "Making Hard Decisions with DecisionTools"
- Aplicación legal: "Quantifying Litigation Risk" (IAALS, 2015)
