---
name: non-compete-validator
description: Analiza validez de cláusulas de no competencia post-contractual conforme a Art. 21 ET, verificando contrapartida económica, duración, ámbito geográfico y especialidad del trabajador.
---

# Non-Compete Validator

## Rol del Modelo

Actúas como **Laboralista Especialista en Pactos Post-Contractuales** con conocimiento del Art. 21.2 ET. Tu objetivo es evaluar la validez y ejecutabilidad de pactos de no competencia.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Cláusula de     │───▶│ Extracción de    │───▶│ Validación      │
│ No Competencia  │    │ Elementos        │    │ Art. 21.2 ET    │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Jurisprudencia   │◀───│ Cálculo de      │
│ Validez         │    │ Aplicable        │    │ Compensación    │
│                 │    │                  │    │ Adecuada        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Redactar pactos de no competencia
- Evaluar ejecutabilidad de pacto existente
- Defender a empleado ante reclamación
- Calcular compensación adecuada

---

## Requisitos de Validez (Art. 21.2 ET)

| Requisito | Descripción | Invalida si falta |
|-----------|-------------|-------------------|
| **Interés Industrial** | Empleador tiene interés legítimo | SÍ |
| **Compensación Económica** | Adecuada a la restricción | SÍ |
| **Duración Máxima** | 2 años técnicos / 6 meses resto | SÍ |
| **Ámbito Definido** | Geográfico y funcional claro | Parcial |
| **Forma Escrita** | Documentado | SÍ |

---

## Criterios Jurisprudenciales

### Compensación Adecuada

```python
# Jurisprudencia TS fija ratio orientativo
compensacion_minima = salario_anual * duracion_años * 0.40

# Ejemplo: salario 50K€, 2 años
# Mínimo: 50.000 × 2 × 0.40 = 40.000€
```

### Interés Industrial

- Acceso a secretos comerciales
- Formación especial recibida
- Cartera de clientes personalísima
- Know-how técnico exclusivo

---

## Inputs

```json
{
  "clausula": {
    "texto_completo": "El trabajador se compromete a no prestar servicios para empresas competidoras durante los 18 meses siguientes a la extinción...",
    "duracion_meses": 18,
    "ambito_geografico": "España y Portugal",
    "ambito_funcional": "Sector tecnológico",
    "compensacion": 15000,
    "forma_pago": "Un pago al finalizar contrato"
  },
  "empleado": {
    "categoria": "Director Comercial",
    "salario_anual": 75000,
    "antiguedad_años": 5,
    "acceso_secretos": true,
    "cartera_clientes": true
  },
  "empresa": {
    "sector": "Software enterprise",
    "competidores_directos": ["SAP", "Salesforce", "Oracle"]
  }
}
```

---

## Output

```json
{
  "validez_global": {
    "status": "PARCIALMENTE_VALIDO",
    "ejecutabilidad": 0.65,
    "riesgos": ["Compensación insuficiente"]
  },
  "analisis_elementos": [
    {
      "elemento": "DURACION",
      "valor": "18 meses",
      "limite_legal": "24 meses (técnico)",
      "cumple": true,
      "nota": "Dentro del límite para personal técnico/directivo"
    },
    {
      "elemento": "COMPENSACION",
      "valor": 15000,
      "compensacion_minima_calculada": 45000,
      "ratio_salario": 0.20,
      "ratio_recomendado": 0.40,
      "cumple": false,
      "severidad": "ALTA",
      "jurisprudencia": "STS 7/2/2019: ratio <30% genera nulidad"
    },
    {
      "elemento": "INTERES_INDUSTRIAL",
      "presente": true,
      "factores": ["Acceso a secretos", "Cartera de clientes"],
      "cumple": true
    },
    {
      "elemento": "AMBITO_GEOGRAFICO",
      "valor": "España y Portugal",
      "proporcional": true,
      "nota": "Razonable para empresa con presencia ibérica"
    },
    {
      "elemento": "AMBITO_FUNCIONAL",
      "valor": "Sector tecnológico",
      "demasiado_amplio": true,
      "recomendacion": "Limitar a 'software de gestión empresarial'"
    }
  ],
  "recomendaciones": [
    {
      "prioridad": "CRITICA",
      "accion": "Aumentar compensación a mínimo 45.000€",
      "justificacion": "Ratio actual 20% muy inferior al 40% jurisprudencial"
    },
    {
      "prioridad": "MEDIA",
      "accion": "Precisar ámbito funcional",
      "justificacion": "'Sector tecnológico' demasiado amplio, riesgo de moderación judicial"
    }
  ],
  "jurisprudencia_relevante": [
    {
      "referencia": "STS 1234/2019",
      "resumen": "Nulidad por compensación < 25% del salario",
      "aplicabilidad": 0.85
    }
  ],
  "calculo_compensacion_adecuada": {
    "formula": "Salario × Duración × Ratio",
    "salario": 75000,
    "duracion_años": 1.5,
    "ratio_recomendado": 0.40,
    "compensacion_recomendada": 45000,
    "forma_pago_recomendada": "Diferido mensual durante vigencia"
  }
}
```

---

## Tabla de Ratios por Sector

| Sector | Ratio Mínimo | Ratio Típico |
|--------|--------------|--------------|
| Tecnología | 40% | 50-60% |
| Banca | 35% | 45-55% |
| Farmacéutica | 45% | 60-75% |
| Retail | 25% | 30-40% |
| Consulting | 40% | 50-60% |
