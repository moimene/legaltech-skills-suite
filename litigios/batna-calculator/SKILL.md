---
name: batna-calculator
description: Calcula el "Mejor Acuerdo Alternativo a una Negociación" (BATNA) usando Game Theory para decidir si ir a juicio o pactar, con árbol de decisión probabilístico y cálculo de Valor Esperado.
---

# BATNA Calculator

## Rol del Modelo

Actúas como **Economista Legal** especializado en Teoría de Juegos y Análisis de Decisiones. Tu objetivo es cuantificar objetivamente si conviene litigar o negociar.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Inputs:         │───▶│ Árbol de         │───▶│ Cálculo de      │
│ - Costes        │    │ Decisión         │    │ Valor Esperado  │
│ - Probabilidades│    │ Probabilístico   │    │ (EV)            │
│ - Tiempo        │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │ Análisis de      │◀───│ Comparación     │
                       │ Sensibilidad     │    │ Litigio vs.     │
                       │                  │    │ Acuerdo         │
                       └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Decidir si aceptar una oferta de acuerdo
- Evaluar el coste real de ir a juicio
- Comparar múltiples escenarios de resolución
- Negociar con datos objetivos

---

## Conceptos Clave

### BATNA (Best Alternative to Negotiated Agreement)

El peor resultado que podemos aceptar antes de rechazar un acuerdo. Si la oferta es peor que el BATNA, rechazar y litigar.

### Valor Esperado (EV)

```
EV = Σ (Probabilidad_i × Resultado_i)
```

---

## Inputs

| Parámetro | Tipo | Descripción | Ejemplo |
|-----------|------|-------------|---------|
| `cantidad_reclamada` | float | Cantidad que reclamamos | 100,000€ |
| `prob_victoria_total` | float | Probabilidad de ganar todo | 0.40 |
| `prob_victoria_parcial` | float | Probabilidad de ganar parte | 0.30 |
| `cantidad_parcial` | float | Cantidad estimada si gana parcial | 60,000€ |
| `costes_juicio` | float | Honorarios + tasas + periciales | 15,000€ |
| `costes_contraparte` | float | Costes si perdemos (condena en costas) | 12,000€ |
| `duracion_años` | float | Tiempo estimado hasta sentencia | 2.5 |
| `tasa_descuento` | float | Coste del dinero anual | 0.05 |
| `oferta_acuerdo` | float | Oferta de la contraparte (opcional) | 45,000€ |

---

## Output

```json
{
  "escenario": "Reclamación de 100.000€",
  "analisis": {
    "ev_litigio": 42500,
    "ev_litigio_neto": 27500,
    "ev_litigio_valor_presente": 24650,
    "batna": 24650,
    "oferta_acuerdo": 45000,
    "diferencia": 20350
  },
  "decision": {
    "recomendacion": "ACEPTAR_ACUERDO",
    "razon": "La oferta (45.000€) supera el BATNA (24.650€) en 20.350€",
    "confianza": 0.85
  },
  "sensibilidad": [
    {"variable": "prob_victoria_total", "umbral_indiferencia": 0.58},
    {"variable": "costes_juicio", "umbral_maximo": 8500}
  ],
  "arbol_decision": {
    "nodos": [
      {"id": 1, "tipo": "decision", "opciones": ["LITIGAR", "ACORDAR"]},
      {"id": 2, "tipo": "azar", "probabilidades": {"victoria": 0.4, "parcial": 0.3, "derrota": 0.3}},
      {"id": 3, "tipo": "resultado", "valor": 85000},
      {"id": 4, "tipo": "resultado", "valor": 45000},
      {"id": 5, "tipo": "resultado", "valor": -27000}
    ]
  }
}
```

---

## Fórmulas

### Valor Esperado del Litigio

```python
EV_litigio = (P_victoria × (Cantidad - Costes)) 
           + (P_parcial × (Cantidad_parcial - Costes))
           + (P_derrota × (-Costes - Costes_contraparte))
```

### Valor Presente Neto

```python
VPN = EV_litigio / (1 + tasa_descuento) ^ años
```

### BATNA

```python
BATNA = VPN  # El mínimo aceptable es el valor presente del litigio
```

---

## Análisis de Sensibilidad

La skill calcula umbrales de indiferencia:
- ¿Con qué probabilidad de victoria el juicio iguala la oferta?
- ¿Qué costes máximos harían preferible el acuerdo?

---

## Visualización

```
                    ┌─────────────────┐
                    │   DECISIÓN      │
                    └────────┬────────┘
              ┌──────────────┴──────────────┐
              ▼                             ▼
        ┌──────────┐                  ┌──────────┐
        │ LITIGAR  │                  │ ACORDAR  │
        └────┬─────┘                  └────┬─────┘
             │                             │
    ┌────────┼────────┐                    │
    ▼        ▼        ▼                    ▼
┌───────┐┌───────┐┌───────┐          ┌───────────┐
│VICTORIA││PARCIAL││DERROTA│          │ 45.000€   │
│85.000€ ││45.000€││-27.000€│         │ (seguro)  │
│ (40%)  ││ (30%) ││ (30%)  │         └───────────┘
└────────┘└───────┘└────────┘
         EV = 27.500€
```

---

## Limitaciones

- Las probabilidades son estimaciones subjetivas
- No considera factores no monetarios (reputación, precedente)
- Asume racionalidad de ambas partes
