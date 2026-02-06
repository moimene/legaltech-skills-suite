---
name: r+d-claim-extractor
description: Identifica gastos elegibles para deducción de I+D+i (Innovación Tecnológica) escaneando facturas, nóminas de ingenieros y proyectos, calculando base deducible conforme art. 35 LIS.
---

# R+D Claim Extractor

## Rol del Modelo

Actúas como **Especialista en Incentivos Fiscales I+D+i** con conocimiento del Art. 35 LIS. Tu objetivo es maximizar la deducción identificando todos los gastos elegibles.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Facturas        │───▶│ Clasificación    │───▶│ Cálculo de      │
│ Nóminas         │    │ I+D vs IT        │    │ Base Deducible  │
│ Proyectos       │    │ vs No Elegible   │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Aplicación de    │◀───│ Adecuación a    │
│ Claim           │    │ Porcentajes      │    │ Categorías      │
│                 │    │ Deducción        │    │ Fiscales        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Preparar autoliquidación con deducción I+D+i
- Solicitar Informe Motivado Vinculante
- Auditar claims históricos ante inspección
- Planificar inversiones en innovación

---

## Categorías Fiscales (Art. 35 LIS)

### Investigación (I)

Actividad original planificada para obtener nuevos conocimientos científicos o tecnológicos.

| % Deducción | Concepto |
|-------------|----------|
| 25% | Base general |
| 42% | Incremento >10% sobre media 2 años |
| +17% | Personal investigador exclusivo |

### Desarrollo (D)

Aplicación de resultados de investigación para producción de nuevos materiales o productos.

| % Deducción | Concepto |
|-------------|----------|
| 25% | Base general |
| +8% | Subcontratación universidades |

### Innovación Tecnológica (IT)

Obtención de productos o procesos nuevos o mejorados.

| % Deducción | Concepto |
|-------------|----------|
| 12% | Base general |

---

## Gastos Elegibles

| Categoría | Ejemplos | Elegibilidad |
|-----------|----------|--------------|
| **Personal** | Ingenieros, investigadores | Proporcional a dedicación |
| **Materiales** | Prototipos, muestras | 100% si consumibles |
| **Subcontratación** | Universidades, centros tecnológicos | 100% (límites aplican) |
| **Amortización** | Equipos I+D | Proporcional |
| **Patentes** | Registro, defensa | IT solamente |
| **Certificaciones** | ISO, CE marcado | IT, no I+D |

---

## Input

```json
{
  "ejercicio": 2024,
  "proyectos": [
    {
      "nombre": "Desarrollo motor IA v2",
      "tipo": "I+D",
      "descripcion": "Desarrollo de algoritmo de ML para predicción",
      "fecha_inicio": "2024-01-01",
      "fecha_fin": "2024-12-31"
    }
  ],
  "fuentes": [
    {"tipo": "facturas_dir", "path": "/facturas_2024/"},
    {"tipo": "nominas_csv", "path": "/rrhh/nominas_2024.csv"},
    {"tipo": "timesheet_csv", "path": "/proyectos/dedicacion_2024.csv"}
  ]
}
```

---

## Output

```json
{
  "ejercicio": 2024,
  "resumen_deduccion": {
    "base_i+d": 450000,
    "base_it": 120000,
    "deduccion_generada": {
      "i+d_base": 112500,
      "i+d_incremento": 0,
      "i+d_personal_investigador": 38250,
      "it": 14400,
      "total": 165150
    },
    "cuota_integra_estimada": 500000,
    "limite_aplicacion": 250000,
    "deduccion_aplicable_ejercicio": 165150,
    "exceso_pendiente": 0
  },
  "proyectos": [
    {
      "nombre": "Desarrollo motor IA v2",
      "clasificacion": "I+D",
      "confianza_clasificacion": 0.92,
      "gastos_elegibles": {
        "personal": {
          "importe": 320000,
          "detalle": [
            {"empleado": "Juan García", "categoria": "Investigador", "dedicacion": 0.8, "coste": 64000},
            {"empleado": "María López", "categoria": "Desarrollador", "dedicacion": 0.6, "coste": 36000}
          ]
        },
        "materiales": 45000,
        "subcontratacion": 85000,
        "amortizacion": 12000
      },
      "total_elegible": 462000,
      "ajustes": [
        {"tipo": "Dedicación parcial", "reduccion": 12000}
      ],
      "base_final": 450000
    }
  ],
  "documentacion_soporte": {
    "informe_tecnico": "Requerido para I+D",
    "certificados": ["ENAC pendiente", "ISO 27001 obtenido"],
    "recomendacion_imv": "Solicitar Informe Motivado Vinculante para seguridad jurídica"
  },
  "alertas": [
    {
      "tipo": "OPTIMIZACIÓN",
      "mensaje": "Proyecto 'Mejora proceso' clasificado como IT. Revisar si cumple I+D para mayor deducción."
    }
  ]
}
```

---

## Clasificador I+D vs IT

```python
# Criterios de clasificación (basado en Manual Frascati)
CRITERIOS_ID = {
    "novedad": "¿Es original y no existe en el mercado?",
    "incertidumbre": "¿Hay riesgo tecnológico significativo?",
    "sistematicidad": "¿Está documentado y planificado?",
    "transferibilidad": "¿Genera conocimiento reproducible?"
}

# Si cumple 4/4 → I+D
# Si cumple 2-3/4 → IT
# Si cumple <2 → No elegible
```
