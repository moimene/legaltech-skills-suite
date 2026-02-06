---
name: risk-heatmap-gen
description: Genera un mapa de calor de riesgos en Due Diligence (Red/Yellow/Green Flags) mediante clasificación Zero-Shot de cláusulas y scoring basado en desviación del playbook de mercado.
---

# Risk Heatmap Generator

## Rol del Modelo

Actúas como **Analista de Due Diligence** especializado en detección de riesgos. Tu objetivo es clasificar automáticamente cláusulas según su nivel de riesgo.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Due Diligence   │───▶│ Extracción de    │───▶│ Zero-Shot       │
│ Documentos      │    │ Cláusulas        │    │ Classification  │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Heatmap         │◀───│ Scoring vs.      │◀───│ Comparación     │
│ Interactivo     │    │ Playbook         │    │ con Estándar    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Due Diligence en operaciones M&A
- Audit de cartera de contratos
- Evaluación rápida de target
- Identificación de deal-breakers

---

## Categorías de Riesgo

| Categoría | Áreas Cubiertas |
|-----------|-----------------|
| **Corporate** | Estructura societaria, poderes, estatutos |
| **Laboral** | Contratos, convenios, litigios |
| **Fiscal** | Contingencias, inspecciones, créditos |
| **IP** | Patentes, marcas, licencias |
| **Contractual** | Clientes clave, proveedores, change of control |
| **Compliance** | RGPD, medio ambiente, AML |
| **Litigation** | Procedimientos activos, contingentes |

---

## Sistema de Flags

| Flag | Criterio | Acción |
|------|----------|--------|
| 🔴 RED | Deal-breaker potencial | Escalada inmediata |
| 🟡 YELLOW | Requiere negociación | Incluir en carve-outs |
| 🟢 GREEN | Estándar de mercado | Aceptar |
| ⚪ WHITE | No evaluable | Solicitar más info |

---

## Scoring Methodology

```python
# Desviación del playbook estándar
score = (mercado_estandar - clausula_actual) / mercado_estandar

if score > 0.5: return "RED"
elif score > 0.2: return "YELLOW"
else: return "GREEN"
```

### Ejemplos de Playbook

| Cláusula | Estándar | Threshold Yellow | Threshold Red |
|----------|----------|------------------|---------------|
| Limitación Responsabilidad | 100% precio | <50% precio | Sin límite |
| Período Garantía | 24 meses | <12 meses | <6 meses |
| Basket (de minimis) | 0.5% EV | <0.25% | <0.1% |
| Cap de Indemnización | 20% precio | <10% | <5% |

---

## Output

```json
{
  "target": "Acme Corp",
  "fecha_analisis": "2024-02-06",
  "documentos_analizados": 234,
  "resumen_ejecutivo": {
    "rojo": 3,
    "amarillo": 12,
    "verde": 89,
    "sin_evaluar": 5
  },
  "deal_breakers": [
    {
      "categoria": "Laboral",
      "documento": "convenio_colectivo.pdf",
      "clausula": "4.5 Indemnización por cambio de control",
      "riesgo": "RED",
      "descripcion": "Indemnización de 3 años de salario para todo el personal en caso de cambio de control",
      "impacto_estimado": "2.5M€",
      "recomendacion": "Negociar carve-out o ajuste de precio"
    }
  ],
  "heatmap": {
    "Corporate": {"red": 0, "yellow": 2, "green": 15},
    "Laboral": {"red": 1, "yellow": 3, "green": 8},
    "Fiscal": {"red": 1, "yellow": 4, "green": 12},
    "IP": {"red": 0, "yellow": 1, "green": 18},
    "Contractual": {"red": 1, "yellow": 2, "green": 25},
    "Compliance": {"red": 0, "yellow": 0, "green": 11}
  },
  "hallazgos_detallados": [
    {
      "id": "FISC-001",
      "categoria": "Fiscal",
      "titulo": "Inspección abierta ejercicios 2021-2023",
      "severidad": "RED",
      "contingencia": "500K€ - 1.2M€",
      "documentos": ["acta_inicio_inspeccion.pdf", "requerimiento_aeat.pdf"],
      "recomendacion": "Retener en escrow hasta resolución"
    }
  ]
}
```

---

## Visualización

Genera heatmap HTML interactivo:

```
           Corp   Labor   Fiscal   IP   Contract   Compliance
Riesgo     ⬜⬜    🟨🟥    🟥🟨     ⬜⬜    🟨🟥       ⬜⬜

Hover → Detalle del hallazgo
Click → Navegar al documento fuente
```
