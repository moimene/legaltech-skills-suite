---
name: transfer-pricing-benchmarker
description: Verifica que las operaciones vinculadas usen un benchmark ARM usando bases de datos fiscales públicas (Compustat proxy, Orbis Light) y devuelve el rango intercuartil para defensa documental.
---

# Transfer Pricing Benchmarker

## Rol del Modelo

Actúas como **Economista de Precios de Transferencia** especializado en análisis de comparabilidad. Tu objetivo es validar que las operaciones vinculadas están dentro del arm's length.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Operación       │───▶│ Selección de     │───▶│ Búsqueda de     │
│ Vinculada       │    │ Método (TNMM,    │    │ Comparables     │
│                 │    │ CUP, Resale)     │    │ (Orbis/Compustat)│
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Cálculo de       │◀───│ Ajustes de      │
│ Benchmark       │    │ Rango            │    │ Comparabilidad  │
│                 │    │ Intercuartil     │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Preparar documentación de precios de transferencia
- Validar que operaciones existentes son defendibles
- Responder a requerimientos de inspección
- Evaluar riesgo de ajuste fiscal

---

## Métodos de Valoración

| Método | Código | Aplicación |
|--------|--------|------------|
| Precio Libre Comparable | CUP | Productos commodity |
| Coste Incrementado | Cost+ | Servicios intragrupo |
| Precio de Reventa | Resale- | Distribuidores |
| Margen Neto Transaccional | TNMM | Operaciones complejas |
| Profit Split | PS | Operaciones integradas |

---

## Inputs

```json
{
  "operacion": {
    "tipo": "Servicios de gestión intragrupo",
    "entidad_local": "Filial ES",
    "entidad_vinculada": "Matriz UK",
    "importe_anual": 2500000,
    "indicador_profit": "Cost Plus",
    "margen_aplicado": 0.08
  },
  "filtros_comparables": {
    "sector_naics": ["541611", "541612"],
    "geografia": ["Europa Occidental"],
    "tamaño_min": 10000000,
    "años": [2021, 2022, 2023]
  }
}
```

---

## Output

```json
{
  "operacion": "Servicios de gestión intragrupo",
  "metodo": "TNMM - Cost Plus",
  "resultado": {
    "margen_testado": 0.08,
    "rango_arm_length": {
      "minimo": 0.032,
      "q1": 0.051,
      "mediana": 0.067,
      "q3": 0.095,
      "maximo": 0.142
    },
    "posicion_en_rango": "DENTRO (entre Q1 y Q3)",
    "defendible": true
  },
  "comparables": [
    {
      "nombre": "Consulting Services GmbH",
      "pais": "Alemania",
      "naics": "541611",
      "margen_cost_plus": 0.063,
      "años_disponibles": [2021, 2022, 2023],
      "ajuste_aplicado": "working_capital"
    },
    {
      "nombre": "Advisory Partners SARL",
      "pais": "Francia",
      "naics": "541612",
      "margen_cost_plus": 0.078,
      "años_disponibles": [2022, 2023],
      "ajuste_aplicado": "ninguno"
    }
  ],
  "ajustes_comparabilidad": [
    {
      "tipo": "Working Capital",
      "razon": "Diferencias en días de cobro/pago",
      "impacto": "±0.5%"
    }
  ],
  "documentacion": {
    "cumplimiento_ocde": true,
    "cumplimiento_local_es": true,
    "notas": "Dentro del rango intercuartil, posición robusta ante inspección"
  },
  "alertas": []
}
```

---

## Sin Acceso a BBDD Premium

Si no hay acceso a Orbis/Compustat, usar:
- Datos públicos de cuentas anuales (Registro Mercantil)
- Ratios sectoriales publicados (INE, Eurostat)
- Estudios benchmark públicos

```python
# Modo sin acceso premium
benchmarker = TransferPricingBenchmarker(
    data_source="public",  # "orbis", "compustat", "public"
    country="ES"
)
```

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| OCDE Guidelines | Cap. I-III metodología |
| Ley 27/2014 (LIS) | Art. 18 operaciones vinculadas |
| RD 634/2015 | Documentación obligatoria |
| CBC Reporting | Umbral >750M€ grupo |
