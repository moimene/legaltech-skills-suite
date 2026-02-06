---
name: vat-carousel-flag
description: Detecta patrones de fraude VAT carousel en datasets de facturas mediante análisis de trading chains, missing traders, buffer companies y análisis de redes de comercio intracomunitario conforme Directiva IVA.
---

# VAT Carousel Flag

## Rol del Modelo

Actúas como **Especialista en Fraude de IVA** con conocimiento profundo de esquemas carousel. Tu objetivo es identificar patrones de fraude antes de que el comercio circular cause pérdidas fiscales.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Dataset de      │───▶│ Análisis de       │───▶│ Identificación  │
│ Facturas        │    │ Trading Chains    │    │ de Missing      │
│ (CSV/JSON)      │    │ & Network         │    │ Traders         │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Scoring de Riesgo │◀───│ Flags de        │
│ Fraude          │    │ por Patrón        │    │ Anomalía        │
│                 │    │                   │    │ (Velocidad,     │
└─────────────────┘    └──────────────────┘    │  Montantes,     │
                                                │  Jurisdicciones)│
                                                └─────────────────┘
```

---

## Cuándo Usar

- Auditoría de proveedores para riesgo de fraude
- Validar cadenas de suministro intracomunitarias
- Investigación pre-compra en operaciones B2B
- Análisis de riesgo para deducción de IVA
- Cumplimiento de obligaciones de due diligence
- Responder a requerimientos de Administración

---

## Patrones de Fraude Carousel Típicos

| Patrón | Descripción | Red Flag |
|--------|-------------|----------|
| **Missing Trader** | Empresa que desaparece sin pagar IVA, tras recauda deducción | Empresa desaparece 3-6 meses tras facturación |
| **Buffer Company** | Intermediaria sin actividad real, solo circula dinero | Márgenes <1%, movimiento masivo sin activos |
| **Circular Trading** | A→B→C→A, mismos productos sin transformación | Mismo producto regresa a origen sin cambio |
| **Phantom Shipper** | Facturas sin movimiento físico de mercancía | Dirección entrante ≠ dirección salida sin transporte |
| **Inversion of Supply** | Facturas falsas de exportación → importación desde EU | Importación masiva sin registro aduanal |

### Ejemplo Real de Carousel

```
2024-01-15: Proveedor ES factura electrodomésticos a Distribuidor IT (Grupo A)
  Importe: 500.000€ / IVA: 105.000€
  Operación: Venta intracomunitaria (0% IVA)

2024-01-20: Distribuidor IT factura a Comerciante DE (Grupo B)
  Mismo producto / Importe: 520.000€ / IVA: 109.200€
  Proveedor IT tiene 20% margen

2024-02-01: Comerciante DE factura a Importador HU (Grupo C)
  Mismo producto / Importe: 540.000€
  Proveedor DE desaparece (insolvencia, cancelación administrativa)
  RED FLAG: Missing Trader, empresa IT nunca pago IVA en IT

2024-02-15: Importador HU vende a Distribuidor ES (eslabón missing)
  Operación jamás completada o simulada
  Pérdida fiscal total: 105.000€ (IT) + 109.200€ (DE) = 214.200€
```

---

## Inputs

```json
{
  "dataset": {
    "facturas": [
      {
        "id": "FAC-2024-001",
        "fecha": "2024-01-15",
        "proveedor_cif": "ES12345678A",
        "proveedor_nombre": "Tech Imports SL",
        "cliente_cif": "IT87654321B",
        "cliente_nombre": "Milano Solutions Ltd",
        "importe_neto": 500000,
        "iva_aplicado": 105000,
        "tipo_operacion": "Venta intracomunitaria",
        "producto_descripcion": "Componentes electrónicos",
        "cantidad": 1000,
        "precio_unitario": 500
      },
      {
        "id": "FAC-2024-002",
        "fecha": "2024-01-22",
        "proveedor_cif": "IT87654321B",
        "proveedor_nombre": "Milano Solutions Ltd",
        "cliente_cif": "DE11111111Z",
        "cliente_nombre": "Berlin Tech GmbH",
        "importe_neto": 520000,
        "iva_aplicado": 109200,
        "tipo_operacion": "Venta intracomunitaria",
        "producto_descripcion": "Componentes electrónicos",
        "cantidad": 1000,
        "precio_unitario": 520
      }
    ],
    "periodo_analisis": "2024-01-01_2024-06-30"
  },
  "parametros_analisis": {
    "detectar_missing_traders": true,
    "detectar_circular_trading": true,
    "detectar_buffer_companies": true,
    "analizar_jurisdicciones_riesgo": true,
    "threshold_riesgo": 0.65
  }
}
```

---

## Output

```json
{
  "resumen_riesgo": {
    "nivel_general": "ALTO",
    "score_fraude": 0.78,
    "patrones_detectados": 3,
    "operaciones_analizadas": 127,
    "operaciones_con_riesgo": 14
  },
  "operaciones_alto_riesgo": [
    {
      "id": "FAC-2024-001_FAC-2024-002",
      "tipo_patrón": "MISSING_TRADER_CHAIN",
      "riesgo": "ALTO",
      "score": 0.92,
      "evidencia": {
        "proveedor_origen": "Tech Imports SL (ES12345678A)",
        "intermediario": "Milano Solutions Ltd (IT87654321B)",
        "destinatario_final": "Berlin Tech GmbH (DE11111111Z)",
        "dias_entre_operaciones": 7,
        "mismo_producto": true,
        "incremento_precio": "4%"
      },
      "flagas": [
        "Intermediario IT activo solo 40 días en período",
        "Milano Solutions Ltd sin registro aduanal de importación",
        "Factura de 500K€ a intermediario, 520K€ a tercero (margen bajo 4%)",
        "Dirección Milan en dirección de oficinas virtuales (riesgo compartido)"
      ],
      "perdida_fiscal_estimada": 109200,
      "recomendacion": "RECHAZAR operación, investigar cadena completa, reportar SEPBLAC si sospecha blanqueo"
    },
    {
      "id": "FAC-2024-045_FAC-2024-046_FAC-2024-047",
      "tipo_patrón": "CIRCULAR_TRADING",
      "riesgo": "MUY ALTO",
      "score": 0.95,
      "evidencia": {
        "ciclo": "Proveedor_ES → Distribuidor_HU → Importador_RO → Proveedor_ES",
        "duracion_ciclo_dias": 14,
        "producto_transformacion": "NINGUNA",
        "volumen_total": 2400000,
        "numero_ciclos_detectados": 3
      },
      "flags": [
        "Mismos componentes regresan a origen en 14 días",
        "Todas las empresas tienen dirección en plataformas cloud",
        "Incrementos de precio marginal (0.5-2%)",
        "Operaciones simultáneas en diferentes zonas horarias"
      ],
      "perdida_fiscal_estimada": 504000,
      "recomendacion": "URGENTE: No operar con cadena, alertar Agencia Tributaria, considerar ejercer derecho de oposición a deducción"
    }
  ],
  "analisis_por_jurisdiccion": {
    "ES": {
      "operaciones": 23,
      "riesgo_promedio": 0.35,
      "perdida_potencial": 45000
    },
    "IT": {
      "operaciones": 18,
      "riesgo_promedio": 0.72,
      "missing_traders_detectados": 2,
      "perdida_potencial": 189300
    },
    "DE": {
      "operaciones": 12,
      "riesgo_promedio": 0.45,
      "perdida_potencial": 78000
    },
    "HU": {
      "operaciones": 31,
      "riesgo_promedio": 0.81,
      "buffer_companies_detectadas": 1,
      "perdida_potencial": 215600
    }
  },
  "empresas_sospechosas": [
    {
      "cif": "IT87654321B",
      "nombre": "Milano Solutions Ltd",
      "riesgo": "ALTO",
      "razon": "Missing trader - desapareció tras facturación masiva",
      "importe_facturado": 520000,
      "registro_aduanal": "NO REGISTRADO",
      "duracion_actividad": "45 días",
      "accion_recomendada": "No operar con esta entidad, reportar Agenzia delle Entrate"
    },
    {
      "cif": "HU12345678X",
      "nombre": "Budapest Commerce Ltd",
      "riesgo": "MEDIO-ALTO",
      "razon": "Buffer company - múltiples operaciones circulares",
      "margen_promedio": 0.8,
      "rotacion_inventario": 340,
      "accion_recomendada": "Realizar due diligence exhaustivo antes de operación"
    }
  ],
  "network_analysis": {
    "nodos": 8,
    "aristas": 12,
    "ciclos_cerrados": 3,
    "grafo_imagen": "Attachment: network_graph.png"
  },
  "cumplimiento_normativo": {
    "directiva_iva": "2006/112/CE - Art. 143bis (anti-fraude)",
    "obligacion_diligencia": "Verificar solvencia y existencia de contrapartida",
    "reporta_sepblac": "SI si sospecha blanqueo de capitales",
    "prescripcion": "4 años, extendible a 10 con fraude"
  }
}
```

---

## Cálculo de Margen Anómalo

Detección automática de márgenes <2% en operaciones intracomunitarias (indicativo de buffer):

```python
margen_porcentaje = ((precio_venta - precio_compra) / precio_compra) * 100
if margen_porcentaje < 2 and volumen > 100000:
    flag_buffer_company = True
    riesgo = "ALTO"
```

---

## Jurisdicciones de Riesgo Alto

Según reportes de fraude IVA (EMPAC 2024):

- **Hungría:** Fraude carrusel endemic, networks amplios
- **Polonia:** Buffers y missing traders frecuentes
- **Italia:** Missing trader INTRASTAT desajuste
- **Rumania:** Operaciones fantasma, no aduanales

---

---

## Patrones Intra-UE de Fraude Carrusel

### Esquemas Típicos de Carrusel

Los esquemas de carrusel tienen patrones muy reconocibles:

#### 1. Missing Trader (Operador Fantasma)

```
Patrón Temporal:
Mes 1-2: Empresa "A" factura a "B" → Recauda IVA, luego NO lo paga
Mes 2-3: Empresa "B" recibe factura, deduce IVA
Mes 3-4: Empresa "A" se DISUELVE O cancela registro (insolvencia aparente)

Red Flag Detectables:
- Empresa activa 40-90 días solamente
- Facturación masiva (> 500k€) en período muy corto
- Desaparición poco después de operación clave
- Dirección en "virtual office" o workspace compartido
- No hay registro aduanal (INTRASTAT) para importaciones declaradas
- Personal administrativo mínimo (1-2 personas)
```

**Heurísticas de Detección**:
- Días de actividad < 180 pero volumen > 1M€
- Ratio descuadre facturación vs. activos => liquidación anómala
- Dirección coincide con N+ empresas en mismo edificio

#### 2. Buffer Company (Intermediario de Baja Adición)

```
Patrón Característico:
A (Productor) → B (Buffer) → C (Distribuidor)
Margen A→B: 1-3%
Margen B→C: 1-3%

Red Flag:
- Márgenes < 2% para volumen > 100k€ (anómalo en mercado real)
- Tiempo de posesión inventario: días (no semanas)
- Sin cambio de packaging, descripción o especificación
- Documentación logística mínima o falsificada
```

**Heurísticas de Detección**:
- Ratio margen vs. volumen inverso (grandes volúmenes, márgenes minúsculos)
- Rotación inventario > 300 días/año (unrealistic)
- Balance sheet: Activos no justifican volumen de transacciones

#### 3. Circular Trading (A→B→C→A Cierre Ciclo)

```
Patrón Exacto:
Día 1: A vende a B (Producto X, 500k€)
Día 5: B vende a C (Producto X, 510k€)
Día 10: C vende a A (Producto X, 520k€) o desaparece

Red Flag CRÍTICA:
- Mismo producto regresa a origen en < 30 días
- Cero transformación o value-add
- Márgenes mínimos (0.5-2%)
- Múltiples ciclos repetidos (detectar patrón)
```

**Heurísticas de Detección**:
- Análisis de red: detectar ciclos cerrados en grafo de transacciones
- Duplicados de CNAE de productos (mismo SKU circula)
- Timing: días entre operaciones vs. standard logística real

#### 4. Phantom Shipper (Factura sin Movimiento Físico)

```
Patrón de Fraude Documental:
Factura: A (Spain) → B (Italy) → C (Germany)
Pero mercancía nunca sale almacén A

Red Flag:
- Dirección ENTRANTE ≠ Dirección SALIDA (sin transportista intermediario)
- No hay guías de transporte (AWB, CMR)
- INTRASTAT: Factura reportada pero mercancía no en aduanas
- "Transporte" a domicilio conocido = rechazo
```

**Heurísticas de Detección**:
- Validación de dirección física (Google Earth, registros aduanales)
- Comparativa factura vs. transporte documentado
- INTRASTAT cruzado: factura reportada pero importación no registrada

---

## Chequeos VIES Automatizados

### Flujo de Validación VIES

VIES (VAT Information Exchange System) es la base de datos oficial de la UE para VAT ID:

```
WORKFLOW CHEQUEO VIES:
┌─────────────────────┐
│ 1. Lectura NIF-IVA  │ (Format validation: 2-letter code + digits)
│ de Contrapartida    │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 2. Consulta VIES    │ (Hit en base de datos VIES comunitaria)
│ Real-Time           │ (EU central registry)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 3. Verificación:    │
│ - Empresa existe    │ (Sí/No/Incertidumbre)
│ - Status activo     │ (Sí/No)
│ - Nombre coincide   │ (Exacto/Parcial/No)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 4. Cross-Check SII  │ (España: Sistema de Suministro Inmediato)
│ AEAT Registry       │ (Facturas emitidas/recibidas simultáneas)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 5. Risk Scoring:    │
│ - Estado VIES +     │
│ - Antigüedad        │
│ - Volumen histórico │ (SII matching)
│ - Deudas AEAT       │
└────────────────────┘
```

### Parámetros de Validación VIES

| Elemento | Validación | Acción si Falla |
|---|---|---|
| **Formato NIF-IVA** | 2-letter country code + 9-14 dígitos | RECHAZAR operación; formato inválido |
| **Hit VIES** | Empresa registrada en base datos UE | FLAG RIESGO si "Incertidumbre"; verificar manualmente |
| **Status Activo** | VAT ID en situación normal (no suspenso) | FLAG RIESGO ALTO; considerar no operar |
| **Nombre Coincidencia** | Nombre en factura vs. VIES registry | FLAG si discrepancia (posible fraude documental) |
| **Antigüedad Registro** | VAT ID registrado hace >2 años | FLAG si < 6 meses (new high-risk entity) |
| **Volumen SII Histórico** | Actividad consistente en Sistema SII AEAT | FLAG si sin historial SII (operating without reporting?) |
| **Situación AEAT** | No suspensión de derechos, no deudas ejecutivas | RECHAZAR si suspensión de VAT deduction |

### Output Validación VIES Automática

```json
{
  "validacion_vies": {
    "nif_iva_contrapartida": "IT87654321B",
    "resultado_vies": "ACTIVO",
    "nombre_vies": "Milano Solutions Ltd",
    "nombre_factura": "Milano Solutions",
    "coincidencia_nombre": "PARCIAL (match 95%)",
    "estatus_operativo": "ACTIVE",
    "fecha_registro_vies": "2023-08-15",
    "antigüedad_meses": 16,
    "chequeo_sii_españa": {
      "operaciones_salida": 0,
      "operaciones_entrada": 3,
      "volumen_último_12m": 520000,
      "estado_deudas_aeat": "SIN DEUDAS",
      "suspension_temporal": false
    },
    "alertas": [
      "PARCIAL match en nombre (Milano Solutions Ltd vs. Milano Solutions)",
      "Historial SII débil: 3 operaciones en 12 meses (baja actividad)",
      "Dirección registrada en workspace virtual (riesgo compartido)"
    ],
    "score_vies": 0.68,
    "recomendacion": "OPERAR CON CAUTELA; considerar documentación additional de diligence"
  }
}
```

### Cross-Reference con Sistema SII (España)

El SII (Sistema de Suministro Inmediato de Información) reporta facturas en tiempo real a AEAT:

```
CROSS-CHECK LOGIC:
1. Si factura entrante de IT → Verificar IT ha reportado factura salida a ES en SII
2. Comparar: Importe + Fecha ± 3 días + descripción
3. Si SII IT ≠ SII ES → Posible discrepancia (ghost shipment)
4. Alertar si volumen acumulado no concuerda (red flag missing trader)
```

**Inputs para Validación Cruzada**:
- Número factura
- Fecha factura
- Importe exacto
- Descripción mercancía
- NIF-IVA de contrapartida

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| **Directiva 2006/112/CE** | Art. 143bis anti-fraude, verificación de solvencia; obligación diligencia debida |
| **Ley 37/1992 (LIVA)** | Transposición española de Directiva 2006/112/CE; marco normativo VAT español |
| **Art. 84 LIVA** | Inversión del sujeto pasivo (reverse charge mechanism) para operaciones intracomunitarias; uso para mitigación fraude |
| **RD 1619/2012** | Registro de operaciones intracomunitarias (INTRASTAT); declaración obligatoria |
| **Art. 8 Ley 58/2003** | Obligación de verificar realidad de operación (due diligence); responsabilidad por operaciones fraudulentas |
| **Ley 10/2010** | SEPBLAC, reportar si sospecha blanqueo; UIF Spanish Financial Intelligence Unit |
| **VIES Checks** | Validación de VAT ID intracomunitarios (Art. 143quinquies LIVA); base de datos AEAT para verificación de solvencia |
| **EMPAC Guidelines** | Identificación de high-risk patterns; European VAT fraud cooperation |
