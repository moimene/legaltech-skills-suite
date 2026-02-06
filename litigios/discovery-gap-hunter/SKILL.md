---
name: discovery-gap-hunter
description: Detecta qué documentos faltan en la entrega de la contraparte durante exhibición documental, mediante análisis de referencias cruzadas y cotejo con inventario entregado.
---

# Discovery Gap Hunter

## Rol del Modelo

Actúas como **Paralegal Forense** especializado en gestión documental. Tu objetivo es detectar documentos referenciados pero no aportados en procedimientos de exhibición.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Documentos      │───▶│ Extracción de    │───▶│ Base de         │
│ Entregados      │    │ Referencias      │    │ Referencias     │
└─────────────────┘    │ ("Ver Anexo A")  │    └────────┬────────┘
                       └──────────────────┘             │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Reporte de      │◀───│ Cotejo con       │◀───│ Inventario      │
│ Gaps            │    │ Inventario       │    │ Documental      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Recepción de documentación en discovery/exhibición
- Auditoría de completitud documental
- Preparar requerimientos de documentos faltantes
- Detectar ocultación documental

---

## Metodología

### Fase 1: Extracción de Referencias

Patrones detectados:
- "Ver Anexo A", "Documento 3", "Exhibit B"
- "según el contrato de fecha..."
- "como consta en el acta de..."
- "adjunto email de fecha..."

### Fase 2: Construcción de Inventario

Generar lista de documentos efectivamente entregados:
- Nombre de archivo
- Hash MD5 (para deduplicación)
- Tipo de documento inferido

### Fase 3: Cotejo Inteligente

Matching fuzzy entre referencias y documentos:
- "Contrato de 15/03/2024" ↔ "2024-03-15_contrato.pdf"
- "Email de Juan" ↔ "email_juan_garcia_marzo.eml"

### Fase 4: Reporte de Gaps

Clasificación de hallazgos:
- **Faltante Crítico**: Documento central no aportado
- **Faltante Menor**: Referencia secundaria
- **Posible Match**: Documento con nombre diferente

---

## Inputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `documentos_dir` | directory | Carpeta con documentos entregados |
| `texto_principal` | file | Documento principal (demanda, escrito) |
| `inventario_csv` | file | Lista declarada de documentos (opcional) |

---

## Output

```json
{
  "analisis": {
    "documentos_entregados": 45,
    "referencias_detectadas": 62,
    "matches_confirmados": 38,
    "gaps_detectados": 18,
    "posibles_matches": 6
  },
  "gaps": [
    {
      "referencia": "Ver Anexo A - Contrato de Arrendamiento",
      "ubicacion": "Hecho Tercero, línea 45",
      "criticidad": "ALTA",
      "razon": "Documento central no aportado",
      "accion": "Requerir expresamente bajo apercibimiento art. 329 LEC"
    },
    {
      "referencia": "Email del Sr. Pérez de 12/01/2024",
      "ubicacion": "Hecho Quinto, línea 78",
      "criticidad": "MEDIA",
      "posibles_matches": ["email_perez_enero_2024.eml"],
      "accion": "Verificar si el adjunto corresponde a la fecha"
    }
  ],
  "estadisticas": {
    "tasa_completitud": 0.61,
    "gaps_criticos": 5,
    "gaps_menores": 13
  }
}
```

---

## Patrones de Referencia

```python
PATRONES = [
    r"(?:ver|véase|cfr\.?)\s+(?:anexo|documento|doc\.?)\s+(\w+)",
    r"(?:según|conforme)\s+(?:el|la)\s+(\w+)\s+de\s+fecha",
    r"(?:adjunto|acompaño)\s+(?:copia|original)\s+de",
    r"(?:exhibit|anexo)\s+([A-Z]|\d+)",
    r"doc(?:umento)?\.?\s*(?:nº|núm\.?|#)?\s*(\d+)",
]
```

---

## Acciones Recomendadas

| Gap Type | Acción Legal |
|----------|--------------|
| Crítico | Art. 329 LEC - Requerimiento bajo apercibimiento |
| Medio | Solicitar aclaración en audiencia previa |
| Menor | Documentar para alegaciones |
