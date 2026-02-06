---
name: cap-table-simulator
description: Simula dilución de acciones ante rondas de inversión, phantom shares y pools de opciones, modelando cascadas de liquidación (Liquidation Preference stack).
---

# Cap Table Simulator

## Rol del Modelo

Actúas como **Analista de Equity** especializado en estructuras de capital de startups. Tu objetivo es simular escenarios de dilución y liquidación.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Cap Table CSV   │───▶│ Parser de        │───▶│ Motor de        │
│ Eventos (Rondas)│    │ Instrumentos     │    │ Simulación      │
│                 │    │                  │    │ (Pandas/NumPy)  │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Cascada de       │◀───│ Cálculo de      │
│ Dilución        │    │ Liquidación      │    │ Waterfall       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Negociar term sheets con inversores
- Evaluar impacto de nueva ronda en fundadores
- Calcular valor de phantom shares/SARs
- Simular escenarios de exit (M&A, IPO)

---

## Instrumentos Soportados

| Instrumento | Descripción |
|-------------|-------------|
| Common Stock | Acciones ordinarias |
| Preferred Stock | Acciones preferentes (con liquidation pref) |
| SAFE | Simple Agreement for Future Equity |
| Convertible Note | Nota convertible |
| Stock Options (ESOP) | Opciones sobre acciones |
| Phantom Shares | Acciones sintéticas |
| Warrants | Warrants |

---

## Parámetros de Liquidation Preference

```python
LiquidationPreference(
    multiple=1.0,          # 1x, 2x, etc.
    participation=True,    # Participating vs Non-participating
    cap=3.0,              # Cap en participating (3x)
    seniority=1           # Orden en el stack
)
```

---

## Input: Cap Table

```csv
holder,instrument,shares,price_per_share,liquidation_pref,participation,seniority
Fundador A,Common,1000000,0.001,0,false,99
Fundador B,Common,1000000,0.001,0,false,99
Seed Fund,Preferred A,500000,1.00,1.0,true,1
Series A Lead,Preferred B,800000,5.00,1.0,false,2
ESOP Pool,Options,200000,5.00,0,false,99
```

---

## Eventos Simulables

| Evento | Efecto |
|--------|--------|
| Nueva Ronda | Dilución proporcional + nuevo inversor |
| Conversión SAFE | Conversión a equity según cap/discount |
| Ejercicio Opciones | Nuevas acciones emitidas |
| Exit M&A | Cascada de liquidación según pref |
| IPO | Conversión a common |

---

## Output: Simulación de Exit

```json
{
  "escenario": "Venta por 50M€",
  "cap_table_pre": {
    "total_shares": 3500000,
    "holders": [
      {"nombre": "Fundador A", "shares": 1000000, "porcentaje": 28.57},
      {"nombre": "Series A Lead", "shares": 800000, "porcentaje": 22.86}
    ]
  },
  "waterfall": {
    "total_proceeds": 50000000,
    "distribucion": [
      {
        "holder": "Series A Lead",
        "paso": 1,
        "concepto": "Liquidation Preference 1x",
        "importe": 4000000
      },
      {
        "holder": "Seed Fund",
        "paso": 2,
        "concepto": "Liquidation Preference 1x",
        "importe": 500000
      },
      {
        "holder": "Remaining (Pro-rata)",
        "paso": 3,
        "concepto": "Distribución proporcional",
        "importe": 45500000,
        "desglose": {
          "Fundador A": 13000000,
          "Fundador B": 13000000,
          "Seed Fund": 6500000,
          "Series A Lead": 10400000,
          "ESOP": 2600000
        }
      }
    ]
  },
  "resumen_final": [
    {"holder": "Fundador A", "total": 13000000, "porcentaje_exit": 26.0},
    {"holder": "Fundador B", "total": 13000000, "porcentaje_exit": 26.0},
    {"holder": "Seed Fund", "total": 7000000, "multiple": 14.0},
    {"holder": "Series A Lead", "total": 14400000, "multiple": 3.6}
  ]
}
```

---

## Análisis de Dilución

```python
# Simular nueva ronda
nueva_ronda = Ronda(
    nombre="Series B",
    valoracion_pre=30_000_000,
    inversion=10_000_000,
    tipo="Preferred"
)

dilution = simulate_round(cap_table, nueva_ronda)
# Fundadores pasan de 57% a 42.8%
```

---

## Visualización

Genera gráfico de barras apiladas:
- Pre-money vs. Post-money
- Distribución por holder
- Comparativa de escenarios de exit
