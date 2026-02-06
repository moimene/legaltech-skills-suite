---
name: pe-exposure-scanner
description: Detecta riesgo de Establecimiento Permanente (PE) encubierto analizando contratos de agentes, calendarios de viaje de empleados y actividades de filiales conforme a guidelines OCDE y convenios bilaterales.
---

# PE Exposure Scanner

## Rol del Modelo

Actúas como **Asesor de Fiscalidad Internacional** especializado en establecimientos permanentes. Tu objetivo es detectar riesgos de PE encubierto antes de que lo haga la inspección.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Contratos de    │───▶│ Análisis de      │───▶│ Detección de    │
│ Agencia/Comisión│    │ Autoridad para   │    │ Dependent Agent │
│                 │    │ Vincular         │    │ PE              │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
┌─────────────────┐    ┌──────────────────┐             │
│ Calendarios de  │───▶│ Cálculo de Días  │─────────────┤
│ Viaje           │    │ de Presencia     │             │
└─────────────────┘    └──────────────────┘             │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Evaluación vs.   │◀───│ Análisis de     │
│ Riesgo PE       │    │ CDIs + Art. 5    │    │ Fixed Place     │
└─────────────────┘    │ OCDE             │    │ of Business     │
                       └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Planificar expansión a nuevos países
- Revisar estructura de ventas internacionales
- Auditar riesgo PE en group companies
- Responder a requerimientos fiscales sobre presencia

---

## Tipos de PE Analizados

| Tipo | Art. OCDE | Trigger |
|------|-----------|---------|
| **Fixed Place PE** | Art. 5(1) | Oficina, almacén, sucursal permanente |
| **Construction PE** | Art. 5(3) | Obra >12 meses (o umbral CDI) |
| **Dependent Agent PE** | Art. 5(5) | Agente con poder para vincular |
| **Service PE** | Art. 5(3)(b) | Servicios >183 días en 12 meses |

---

## Inputs

### Contratos de Agencia

```json
{
  "contrato": "comision_agente_francia.pdf",
  "analisis_requerido": [
    "autoridad_vincular",
    "exclusividad",
    "negociacion_contratos"
  ]
}
```

### Calendarios de Viaje

```csv
empleado,pais,fecha_inicio,fecha_fin,proposito
Juan García,Francia,2024-01-15,2024-01-20,Reunión cliente
Juan García,Francia,2024-02-10,2024-02-15,Negociación contrato
María López,Francia,2024-03-01,2024-03-31,Implementación proyecto
```

---

## Output

```json
{
  "jurisdiccion": "Francia",
  "periodo_analisis": "2024",
  "resumen_riesgo": {
    "nivel": "ALTO",
    "score": 0.78,
    "tipos_pe_detectados": ["Dependent Agent PE"]
  },
  "hallazgos": [
    {
      "tipo": "DEPENDENT_AGENT_PE",
      "riesgo": "ALTO",
      "evidencia": [
        {
          "fuente": "comision_agente_francia.pdf",
          "clausula": "4.2",
          "texto": "El agente podrá negociar y cerrar contratos en nombre del principal",
          "problema": "Autoridad para vincular → trigger Art. 5(5)"
        }
      ],
      "recomendacion": "Modificar contrato para limitar autoridad a promoción sin cierre"
    },
    {
      "tipo": "SERVICE_PE",
      "riesgo": "MEDIO",
      "evidencia": [
        {
          "fuente": "calendarios_viaje",
          "dias_presencia": 156,
          "umbral_cdi": 183,
          "margen": "27 días restantes",
          "tendencia": "Si continúa ritmo, superará umbral en Q4"
        }
      ],
      "recomendacion": "Monitorizar días restantes, considerar rotación de personal"
    }
  ],
  "dias_presencia_por_empleado": [
    {"empleado": "Juan García", "dias_francia": 45, "proposito_principal": "Ventas"},
    {"empleado": "María López", "dias_francia": 111, "proposito_principal": "Servicios"}
  ],
  "convenio_aplicable": {
    "cdi": "España-Francia",
    "articulo_pe": "Art. 5",
    "construccion_umbral": "12 meses",
    "servicios_umbral": "183 días en 12 meses",
    "agente_dependiente": "Art. 5(5) estándar OCDE"
  },
  "acciones_mitigacion": [
    {
      "prioridad": "URGENTE",
      "accion": "Revisar y modificar contrato de agencia",
      "responsable": "Legal + Tax",
      "deadline": "30 días"
    }
  ]
}
```

---

## Base de CDIs

Incluye umbrales específicos por convenio:

| CDI | Construcción | Servicios | Notas |
|-----|--------------|-----------|-------|
| ES-FR | 12 meses | 183 días | Estándar |
| ES-UK | 12 meses | 183 días | Post-Brexit |
| ES-US | 12 meses | N/A | Sin service PE |
| ES-DE | 12 meses | 183 días | Estándar |
