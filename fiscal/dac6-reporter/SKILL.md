---
name: dac6-reporter
description: Asistente especializado en identificación y reporte de mecanismos transfronterizos notificables bajo DAC6 (Directiva 2018/822/UE) y Ley 10/2020 española. Detecta hallmarks A-E, aplica main benefit test, genera modelos 234/235/236 y gestiona plazos de notificación.
---

# DAC6 Reporter

## Rol del Modelo

Actúas como **Experto Senior en Fiscalidad Internacional y Compliance DAC6** con especialización en la identificación de mecanismos de planificación fiscal agresiva. Tu objetivo es detectar operaciones potencialmente notificables, evaluar el cumplimiento del main benefit test, y generar la documentación requerida por la Agencia Tributaria.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Operación/      │───▶│ Detector de      │───▶│ Hallmarks       │
│ Mecanismo       │    │ Hallmarks        │    │ Identificados   │
│ Transfronterizo │    │ (A-E Analysis)   │    │ (16 indicadores)│
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Modelo 234/     │◀───│ Generador de     │◀───│ Main Benefit    │
│ 235/236         │    │ Declaración      │    │ Test            │
│ + Documentación │    │                  │    │ (si requerido)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │
        ▼
┌─────────────────┐
│ Calendario de   │
│ Plazos y        │
│ Alertas         │
└─────────────────┘
```

---

## Cuándo Usar

- Evaluar si una operación transfronteriza es notificable bajo DAC6
- Identificar hallmarks en reestructuraciones, financiaciones, o planificaciones internacionales
- Preparar modelos 234 (intermediario), 235 (contribuyente), 236 (actualización)
- Gestionar plazos de notificación (30 días desde diseño/implementación)
- Determinar quién tiene obligación de declarar (intermediario vs. obligado tributario)
- Documentar análisis de main benefit test
- Coordinar reporting entre jurisdicciones UE

---

## Marco Normativo Completo

### Normativa Europea

| Norma | Contenido | Referencia |
|-------|-----------|------------|
| **Directiva 2018/822/UE** | DAC6 - Obligación de información sobre mecanismos transfronterizos | DOUE L 139/1, 5.6.2018 |
| **Directiva 2011/16/UE** | DAC original - Cooperación administrativa fiscal | DOUE L 64/1, 11.3.2011 |
| **Reglamento 2020/262** | Prórroga plazos COVID-19 (6 meses) | DOUE L 67/1, 6.3.2020 |

### Normativa Española

| Norma | Contenido | Referencia BOE |
|-------|-----------|----------------|
| **Ley 10/2020, de 29 de diciembre** | Transposición DAC6 | BOE-A-2020-17264 |
| **RD 243/2021, de 6 de abril** | Desarrollo reglamentario DAC6 | BOE-A-2021-5765 |
| **Orden HAC/342/2021** | Modelo 234 (intermediarios) | BOE-A-2021-5850 |
| **Orden HAC/343/2021** | Modelo 235 (obligados tributarios) | BOE-A-2021-5851 |
| **Orden HAC/344/2021** | Modelo 236 (actualizaciones) | BOE-A-2021-5852 |
| **Art. 93 LGT** | Obligaciones de información | BOE-A-2003-23186 |

---

## Sistema de Hallmarks (Indicadores)

### Categoría A: Hallmarks Genéricos (requieren Main Benefit Test)

| Código | Hallmark | Descripción | Ejemplo |
|--------|----------|-------------|---------|
| **A.1** | Cláusula de confidencialidad | Obligación de mantener secreto el mecanismo frente a AEAT u otras Administraciones | NDA que prohíbe revelar estructura a autoridades |
| **A.2** | Honorarios vinculados | Comisión del intermediario depende de ventaja fiscal obtenida | Success fee basado en ahorro tributario |
| **A.3** | Documentación estandarizada | Mecanismo "off-the-shelf" sin personalización sustancial | Producto fiscal vendido a múltiples clientes |

### Categoría B: Hallmarks Específicos (requieren Main Benefit Test)

| Código | Hallmark | Descripción | Ejemplo |
|--------|----------|-------------|---------|
| **B.1** | Pérdidas adquiridas | Adquisición de entidad con pérdidas para compensar beneficios | Compra de sociedad con BINs por 1€ |
| **B.2** | Conversión de rentas | Transformar renta ordinaria en capital, exenta o no gravada | Dividendo → préstamo participativo |
| **B.3** | Operaciones circulares | Transacciones que neutralizan efecto económico entre vinculadas | Round-tripping de fondos |

### Categoría C: Hallmarks Transfronterizos Específicos

| Código | Hallmark | Descripción | Ejemplo |
|--------|----------|-------------|---------|
| **C.1.a** | Pagos deducibles no gravados | Gasto deducible en origen, ingreso no gravado en destino | Intereses deducibles a país sin IS |
| **C.1.b.i** | Doble no imposición CDI | Uso de CDI para evitar tributación en ambas jurisdicciones | Treaty shopping |
| **C.1.b.ii** | Tipo 0% o exención en destino | Pago a jurisdicción con tipo efectivo <1% | Pagos a jurisdicción off-shore |
| **C.1.c** | Regímenes preferentes | Destino con régimen fiscal privilegiado (Anexo RD 1080/91) | IP Box, holding regimes |
| **C.1.d** | Deducción múltiple | Mismo gasto deducido en más de una jurisdicción | Amortización duplicada |
| **C.2** | Amortización duplicada | Depreciación del mismo activo en varias jurisdicciones | Check-the-box + amortización |
| **C.3** | Eliminación doble imposición duplicada | Alivio duplicado por misma renta | Exención + crédito por mismo dividendo |
| **C.4** | Valoración diferida | Transfers con diferencias significativas de valoración | Activos transferidos a precio distinto |

### Categoría D: Intercambio Automático e Identificación Beneficial Owner

| Código | Hallmark | Descripción | Ejemplo |
|--------|----------|-------------|---------|
| **D.1** | Elusión de CRS | Mecanismo para evitar reporting Common Reporting Standard | Conversión de cuenta financiera |
| **D.2** | Cadena de titularidad opaca | Ocultación de beneficial owner | Uso de nominees o trusts opacos |

### Categoría E: Precios de Transferencia

| Código | Hallmark | Descripción | Ejemplo |
|--------|----------|-------------|---------|
| **E.1** | Safe harbour unilateral | Uso de safe harbour no bilateral OCDE | TP ruling unilateral ventajoso |
| **E.2** | Intangibles HTVs | Transferencia de intangibles difíciles de valorar | IP transfer a IP Box sin comparable |
| **E.3** | Reestructuración con reducción >50% | Transferencia funcional con caída de EBIT >50% en 3 años | Conversión de fabricante full-fledged a maquilador |

---

## Main Benefit Test

### Cuándo Aplica

El Main Benefit Test (MBT) es **obligatorio** para hallmarks de categorías A, B, y C.1 (excepto C.1.b.i y C.1.b.ii que no lo requieren).

### Metodología de Evaluación

```
┌─────────────────────────────────────────────────────────────────┐
│ MAIN BENEFIT TEST                                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ ¿Puede establecerse razonablemente que el BENEFICIO PRINCIPAL   │
│ o UNO DE LOS BENEFICIOS PRINCIPALES esperado del mecanismo      │
│ es obtener una VENTAJA FISCAL?                                  │
│                                                                  │
│ Factores a considerar:                                           │
│ ┌─────────────────┬─────────────────┬─────────────────┐         │
│ │ Sustancia       │ Motivación      │ Proporcionalidad│         │
│ │ Económica       │ Empresarial     │ Ventaja/Coste   │         │
│ └─────────────────┴─────────────────┴─────────────────┘         │
│                                                                  │
│ SI se cumple el test + hallmark identificado → NOTIFICABLE      │
│ NO se cumple el test → NO notificable (documentar análisis)     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Criterios de Evaluación

| Factor | Peso | Indicadores Positivos (no notificable) | Indicadores Negativos (notificable) |
|--------|------|---------------------------------------|-------------------------------------|
| **Sustancia económica** | Alto | Empleados locales, activos reales, decisiones locales | Shell company, dirección remota |
| **Motivación empresarial** | Alto | Expansión mercado, sinergias, eficiencia | Sin razón no fiscal clara |
| **Proporcionalidad** | Medio | Ventaja fiscal marginal vs. inversión total | Ahorro fiscal desproporcionado |
| **Timing** | Medio | Operación planificada independiente de fiscalidad | Estructurada específicamente para ventaja |
| **Alternativas** | Bajo | Opción elegida por razones no fiscales | Alternativa con fiscalidad neutra descartada |

---

## Inputs

```json
{
  "mecanismo": {
    "descripcion": "Reestructuración de filial española con transferencia de IP a Irlanda",
    "tipo": "Reestructuración empresarial con transferencia de intangibles",
    "fecha_diseño": "2024-01-15",
    "fecha_implementacion": "2024-03-01",
    "jurisdicciones_implicadas": ["ES", "IE", "NL"],
    "partes": {
      "obligado_tributario": {
        "nombre": "TechCorp Spain SL",
        "nif": "B12345678",
        "residencia": "ES"
      },
      "entidades_vinculadas": [
        {
          "nombre": "TechCorp IP Ltd",
          "tax_id": "IE1234567",
          "residencia": "IE"
        }
      ]
    },
    "intermediarios": [
      {
        "nombre": "Despacho & Asociados SLP",
        "nif": "B87654321",
        "rol": "Asesor fiscal diseñador",
        "secreto_profesional": false
      }
    ]
  },
  "detalles_operacion": {
    "valor_transaccion": 15000000,
    "moneda": "EUR",
    "activos_transferidos": ["Patentes tecnológicas", "Software propietario", "Marca registrada"],
    "metodo_valoracion": "DCF basado en royalties proyectadas",
    "impacto_fiscal_estimado": {
      "ahorro_anual": 850000,
      "periodo_proyeccion": "10 años",
      "tipo_efectivo_origen": 0.25,
      "tipo_efectivo_destino": 0.0625
    }
  },
  "analisis_previo": {
    "motivacion_empresarial": "Centralización de gestión de IP para eficiencia operativa",
    "sustancia_destino": {
      "empleados": 3,
      "funciones": ["Gestión licencias", "Desarrollo incremental"],
      "activos_fisicos": "Oficina arrendada"
    }
  }
}
```

---

## Output

```json
{
  "analisis_dac6": {
    "mecanismo_id": "DAC6-2024-001",
    "fecha_analisis": "2024-01-20",
    "resultado": "NOTIFICABLE",
    "confianza": 0.92
  },
  "hallmarks_detectados": [
    {
      "codigo": "E.2",
      "nombre": "Transferencia de intangibles HTVs",
      "descripcion": "IP transfer valorada mediante DCF sin comparables verificables",
      "requiere_mbt": false,
      "evidencia": "Patentes + software sin mercado comparable público"
    },
    {
      "codigo": "C.1.c",
      "nombre": "Régimen preferente en destino",
      "descripcion": "IP Box irlandés con tipo efectivo 6.25%",
      "requiere_mbt": true,
      "mbt_resultado": true,
      "evidencia": "Diferencial de tipo efectivo: 25% → 6.25%"
    },
    {
      "codigo": "E.3",
      "nombre": "Reestructuración con reducción EBIT >50%",
      "descripcion": "Proyección de reducción de EBIT ES del 65% en 3 años",
      "requiere_mbt": false,
      "evidencia": "Pro-forma financiero adjunto"
    }
  ],
  "main_benefit_test": {
    "aplicado": true,
    "resultado": "CUMPLIDO (ventaja fiscal es beneficio principal)",
    "factores": {
      "sustancia_economica": {
        "score": 0.35,
        "comentario": "3 empleados, funciones limitadas, sustancia débil"
      },
      "motivacion_empresarial": {
        "score": 0.45,
        "comentario": "Eficiencia alegada, pero ahorro fiscal desproporcionado"
      },
      "proporcionalidad": {
        "score": 0.20,
        "comentario": "Ahorro 8.5M€ en 10 años vs. costes reestructuración ~200k€"
      }
    },
    "conclusion": "El beneficio fiscal es uno de los principales esperados del mecanismo"
  },
  "obligacion_notificacion": {
    "obligado_primario": "Intermediario (Despacho & Asociados SLP)",
    "razon": "Diseñador del mecanismo sin secreto profesional invocado",
    "plazo_legal": "30 días desde puesta a disposición (Art. 4 Ley 10/2020)",
    "fecha_limite": "2024-02-14",
    "modelo_aplicable": "234"
  },
  "generacion_modelo_234": {
    "datos_declarante": {
      "nif": "B87654321",
      "condicion": "Intermediario",
      "razon_social": "Despacho & Asociados SLP"
    },
    "datos_mecanismo": {
      "tipo": "Reestructuración con transferencia de IP",
      "hallmarks": ["E.2", "C.1.c", "E.3"],
      "jurisdicciones": ["ES", "IE"],
      "valor_operacion": 15000000,
      "fecha_primer_paso": "2024-03-01"
    },
    "datos_participantes": [
      {
        "tipo": "Obligado tributario",
        "nif": "B12345678",
        "nombre": "TechCorp Spain SL",
        "residencia": "ES"
      },
      {
        "tipo": "Entidad vinculada",
        "tax_id": "IE1234567",
        "nombre": "TechCorp IP Ltd",
        "residencia": "IE"
      }
    ],
    "resumen_mecanismo": "Transferencia de cartera de IP (patentes, software, marca) desde filial española a entidad irlandesa bajo régimen IP Box. Valoración DCF €15M. Ahorro fiscal proyectado €850k/año.",
    "numero_referencia_ue": "Pendiente asignación tras presentación"
  },
  "calendario_plazos": [
    {
      "evento": "Fecha límite presentación Modelo 234",
      "fecha": "2024-02-14",
      "dias_restantes": 25,
      "prioridad": "CRITICA",
      "responsable": "Intermediario"
    },
    {
      "evento": "Fecha límite si secreto profesional invocado",
      "fecha": "2024-02-14",
      "dias_restantes": 25,
      "prioridad": "ALTA",
      "responsable": "Obligado tributario (modelo 235)"
    },
    {
      "evento": "Plazo intercambio automático UE",
      "fecha": "2024-04-30",
      "dias_restantes": 100,
      "prioridad": "INFORMATIVA",
      "responsable": "AEAT"
    }
  ],
  "alertas": [
    {
      "tipo": "WARNING",
      "mensaje": "Sustancia económica en destino por debajo de umbrales recomendados",
      "accion": "Documentar justificación empresarial detallada"
    },
    {
      "tipo": "INFO",
      "mensaje": "Irlanda participará en intercambio automático - esperar consultas",
      "accion": "Preparar documentación de valoración robusta"
    }
  ],
  "documentacion_recomendada": [
    "Informe de valoración de intangibles (metodología DCF)",
    "Análisis funcional pre/post reestructuración",
    "Business case de centralización de IP",
    "Contratos de licencia y acuerdos de servicios",
    "Proyecciones financieras a 5 años",
    "Evidencia de sustancia en entidad receptora"
  ],
  "compliance": {
    "normativa_aplicable": [
      "Directiva 2018/822/UE (DAC6)",
      "Ley 10/2020 de obligación de información",
      "RD 243/2021 (desarrollo reglamentario)",
      "Orden HAC/342/2021 (modelo 234)"
    ],
    "sanciones_incumplimiento": {
      "no_presentacion": "Hasta 600.000€ (muy grave)",
      "presentacion_incompleta": "Hasta 300.000€ (grave)",
      "presentacion_fuera_plazo": "Hasta 20.000€ (leve)"
    },
    "intercambio_automatico": "La información será intercambiada automáticamente con IE y otros Estados miembros en 30 días desde recepción por AEAT"
  }
}
```

---

## Módulos de Riesgo Específico

### Detector de Secreto Profesional

El intermediario puede invocar secreto profesional (Art. 5.2 Ley 10/2020) si:

| Condición | Efecto | Acción |
|-----------|--------|--------|
| Abogado/Procurador colegiado | Puede invocar secreto profesional | Obligación se traslada al obligado tributario |
| Asesor fiscal no colegiado | NO puede invocar secreto | Obligación permanece en intermediario |
| Secreto invocado | Notificar al OT en 5 días | Modelo 235 por el OT |

### Coordinación Multi-Jurisdiccional

```
┌─────────────────────────────────────────────────────────────────┐
│ INTERCAMBIO AUTOMÁTICO DAC6                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ España (AEAT) ◄──────────────────────────────────► Irlanda (IRA)│
│       │                                                   │     │
│       │         Número de Referencia Único UE             │     │
│       │         (evita duplicidades)                      │     │
│       ▼                                                   ▼     │
│ ┌─────────────┐                                   ┌─────────────┐│
│ │ Modelo 234  │                                   │ DAC6 Report ││
│ │ presentado  │                                   │ (si aplica) ││
│ └─────────────┘                                   └─────────────┘│
│                                                                  │
│ Plazo intercambio: trimestral (Ene, Abr, Jul, Oct)              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Alertas Automáticas

| Trigger | Alerta | Prioridad | Acción Recomendada |
|---------|--------|-----------|-------------------|
| Hallmark E.2 detectado | Intangibles HTVs requieren valoración robusta | ALTA | Preparar informe de valoración independiente |
| MBT cumplido + ahorro >500k€ | Operación de alto valor bajo escrutinio | CRÍTICA | Revisar sustancia económica en destino |
| <10 días para plazo | Proximidad deadline modelo 234/235 | CRÍTICA | Priorizar presentación |
| Múltiples jurisdicciones UE | Riesgo de notificación duplicada | MEDIA | Coordinar con asesores locales |
| Intermediario sin colegiación | No aplica secreto profesional | INFO | Confirmar obligación del intermediario |

---

## Consideraciones Éticas

1. **Transparencia:** La skill genera documentación objetiva, no busca evadir obligaciones de reporte
2. **Completitud:** Identifica TODOS los hallmarks aplicables, no solo los convenientes
3. **Conservadurismo:** Ante duda, recomienda notificación preventiva
4. **Trazabilidad:** Mantiene log de análisis para inspecciones futuras
5. **Confidencialidad:** Los datos procesados permanecen en entorno TEE sin transmisión

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| **Directiva 2018/822/UE** | Notificación de mecanismos transfronterizos con hallmarks |
| **Ley 10/2020** | Transposición española, plazos 30 días, sanciones |
| **RD 243/2021** | Formato y contenido de declaraciones |
| **Art. 93 LGT** | Obligación general de información tributaria |
| **RGPD** | Protección de datos de participantes en TEE |
