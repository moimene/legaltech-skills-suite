---
name: severance-optimizer
description: Calcula el coste óptimo de despido conforme a Estatuto de Trabajadores, analiza convenio aplicable y días bonus, simulando escenarios (despido objetivo, disciplinario impugnado, ERE) con probabilidades judiciales.
---

# Severance Optimizer

## Rol del Modelo

Actúas como **Especialista en Relaciones Laborales** con conocimiento profundo del Estatuto de Trabajadores y convenios. Tu objetivo es minimizar el coste legal de la extinción.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Datos Empleado  │───▶│ Identificación   │───▶│ Cálculo Base    │
│ (Antigüedad,    │    │ Convenio         │    │ Indemnizatoria  │
│  Salario, Categ)│    │ Aplicable        │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Simulación       │◀───│ Probabilidades  │
│ Escenarios      │    │ Multiescenario   │    │ Judiciales      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Planificar despidos individuales
- Evaluar costes de reestructuración
- Comparar escenarios (ERE vs. individual)
- Preparar negociación con trabajador

---

## Tipos de Extinción

| Tipo | Indemnización Legal | Art. ET |
|------|---------------------|---------|
| Despido Objetivo | 20 días/año (max 12 mensualidades) | Art. 52 |
| Despido Disciplinario Procedente | 0 | Art. 54 |
| Despido Improcedente | 33 días/año (max 24 mensualidades) | Art. 56 |
| ERE/ERTE colectivo | 20 días/año | Art. 51 |
| Baja Voluntaria | 0 | Art. 49.1.d |
| Mutuo Acuerdo | Negociable | Art. 49.1.a |

---

## Mejoras de Convenio

Muchos convenios mejoran las indemnizaciones legales:

```python
MEJORAS_CONVENIO = {
    "banca": {"objetivo": 25, "improcedente": 45},
    "seguros": {"objetivo": 23, "improcedente": 40},
    "comercio_madrid": {"objetivo": 20, "improcedente": 33}  # Legal
}
```

---

## Inputs

```json
{
  "empleado": {
    "fecha_alta": "2015-03-15",
    "categoria": "Técnico Senior",
    "salario_bruto_anual": 45000,
    "salario_especie_anual": 5000,
    "bonus_medio_3_años": 8000,
    "convenio": "Oficinas y Despachos Madrid"
  },
  "causas_disponibles": {
    "objetivo_economico": true,
    "disciplinario": false,
    "organizativo": true
  }
}
```

---

## Output

```json
{
  "empleado": {
    "nombre": "[Anonimizado]",
    "antiguedad_años": 9.8,
    "salario_regulador_diario": 158.90
  },
  "escenarios": [
    {
      "tipo": "DESPIDO_OBJETIVO_ECONOMICO",
      "indemnizacion_legal": {
        "dias_por_año": 20,
        "calculo": "9.8 años × 20 días × 158.90€/día",
        "importe": 31143.60,
        "tope_aplicado": false
      },
      "mejora_convenio": 0,
      "costes_adicionales": {
        "preaviso_no_respetado": 4767,
        "finiquito_vacaciones": 2650
      },
      "coste_total": 38560.60,
      "riesgo_impugnacion": {
        "probabilidad": 0.35,
        "coste_si_improcedente": 51300,
        "valor_esperado": 42420
      },
      "recomendacion": "Documentar exhaustivamente causas económicas"
    },
    {
      "tipo": "DESPIDO_IMPROCEDENTE_PACTADO",
      "indemnizacion": {
        "dias_por_año": 33,
        "importe": 51386,
        "negociacion_tipica": "38-42 días en este sector"
      },
      "coste_total": 58700,
      "ventajas": ["Certidumbre", "Sin litigio", "Finiquito firmado"],
      "desventajas": ["Coste directo mayor"]
    },
    {
      "tipo": "MUTUO_ACUERDO",
      "indemnizacion_sugerida": {
        "minimo": 25000,
        "mercado": 35000,
        "maximo": 45000
      },
      "ventajas": ["Flexibilidad fiscal para empleado", "Sin reconocimiento improcedencia"],
      "alerta": "Empleado pierde derecho a desempleo"
    }
  ],
  "recomendacion_optima": {
    "escenario": "DESPIDO_OBJETIVO_ECONOMICO",
    "ahorro_vs_improcedente": 20140,
    "condiciones": "Solo si causas económicas documentadas y >3 meses de pérdidas"
  },
  "simulacion_ere": {
    "aplicable": true,
    "umbral": "10 empleados en 90 días",
    "ventajas": "Negociación colectiva, posible subsidio",
    "proceso": "Consultas 30 días + autorización laboral"
  }
}
```

---

## Calculadora de Salario Regulador

```python
# Salario regulador = (Fijo + Especie + Promedio variables) / 365
salario_regulador = (
    salario_bruto + 
    salario_especie + 
    media_bonus_3_años
) / 365
```
