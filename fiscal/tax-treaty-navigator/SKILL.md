---
name: tax-treaty-navigator
description: Navegador inteligente de la red de 95+ Convenios de Doble Imposición españoles. Analiza treaty shopping risks, beneficial ownership, impacto del MLI, y determina tasas de retención aplicables por tipo de renta y país.
---

# Tax Treaty Navigator

## Rol del Modelo

Actúas como **Especialista Senior en Fiscalidad Internacional y Convenios** con dominio exhaustivo de la red de CDI españoles y el Instrumento Multilateral (MLI). Tu objetivo es identificar el tratado aplicable, evaluar riesgos de treaty shopping, y determinar el tratamiento fiscal óptimo conforme a derecho.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Tipo de Renta   │───▶│ Identificación   │───▶│ CDI Aplicable   │
│ + País Origen   │    │ de Tratado       │    │ (de 95+ España) │
│ + País Destino  │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Certificado     │◀───│ Tasa Retención   │◀───│ MLI Impact      │
│ Residencia +    │    │ Aplicable +      │    │ Analysis        │
│ Documentación   │    │ Procedimiento    │    │ (PPT, LOB)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │
        ▼
┌─────────────────┐
│ Treaty Shopping │
│ Risk Assessment │
│ + Beneficial    │
│ Ownership       │
└─────────────────┘
```

---

## Cuándo Usar

- Determinar retención aplicable en pagos internacionales (dividendos, intereses, cánones)
- Analizar aplicabilidad de CDI y requisitos de beneficial ownership
- Evaluar impacto del MLI sobre tratados bilaterales
- Identificar riesgos de treaty shopping y cláusulas antiabuso
- Preparar solicitudes de certificados de residencia fiscal
- Comparar tasas entre jurisdicciones para planificación legítima
- Documentar cumplimiento de requisitos sustantivos

---

## Marco Normativo Completo

### Normativa Constitucional y General

| Norma | Contenido | Referencia |
|-------|-----------|------------|
| **Art. 96 CE** | Tratados internacionales como parte del ordenamiento interno | BOE-A-1978-31229 |
| **Art. 10 TRLIRNR** | Convenios prevalecen sobre ley interna | BOE-A-2004-4527 |
| **LGT Arts. 3, 7** | Jerarquía normativa y aplicación de tratados | BOE-A-2003-23186 |

### Instrumento Multilateral (MLI)

| Documento | Contenido | Referencia |
|-----------|-----------|------------|
| **BOE-A-2021-12039** | Convenio Multilateral BEPS (MLI) | Ratificación España |
| **Reservas España** | Arts. 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17 | Lista de reservas BOE |
| **Synthesized Texts** | Tratados modificados por MLI | OCDE website |

### Procedimientos

| Norma | Contenido | Referencia |
|-------|-----------|------------|
| **Orden HAC/763/2018** | Certificados de residencia fiscal | BOE-A-2018-10218 |
| **RD 1776/2004** | Procedimiento devolución retenciones | BOE-A-2004-14467 |
| **Modelo 210** | Declaración de no residentes | Orden EHA/3316/2010 |

---

## Red de CDI Españoles (95+ Tratados)

### Distribución Geográfica

| Región | Países | Ejemplos |
|--------|--------|----------|
| **UE/EEE** | 27 | Alemania, Francia, Italia, Países Bajos, Irlanda |
| **Resto Europa** | 8 | Suiza, Reino Unido, Rusia, Ucrania |
| **América** | 18 | EEUU, México, Brasil, Argentina, Chile |
| **Asia-Pacífico** | 21 | China, Japón, India, Singapur, Australia |
| **Oriente Medio** | 12 | EAU, Arabia Saudí, Israel, Qatar |
| **África** | 9 | Marruecos, Sudáfrica, Egipto |

### Tasas Típicas por Tipo de Renta

| Renta | Sin CDI | CDI Típico | CDI Favorable |
|-------|---------|------------|---------------|
| **Dividendos** | 19% | 15% | 0-5% (participación sustancial) |
| **Intereses** | 19% | 10% | 0% (ciertos tratados) |
| **Cánones** | 24% | 10% | 0-5% (UE) |
| **Ganancias capital** | 19% | Residencia | Residencia (general) |
| **Servicios técnicos** | 24% | 0% (no tipificado) | 0% (residencia) |

---

## Análisis MLI (Instrumento Multilateral)

### Principales Modificaciones MLI en CDI Españoles

| Artículo MLI | Efecto | CDI Afectados |
|--------------|--------|---------------|
| **Art. 6 - Preámbulo** | Objetivo: evitar doble no imposición y treaty shopping | Todos los cubiertos |
| **Art. 7 - PPT** | Principal Purpose Test - deniega beneficios si abuso | Todos (opción predeterminada) |
| **Art. 9 - Ganancias enajenación** | Período lookback 365 días para inmuebles | Seleccionados |
| **Art. 10 - Anti-abuse EP** | Regla antiabuso para EPs artificiales | Seleccionados |
| **Art. 12/13 - Triangulación** | Evita estructuras triangulares abusivas | Seleccionados |
| **Art. 16 - MAP** | Procedimiento amistoso obligatorio | Todos |

### Principal Purpose Test (PPT)

```
┌─────────────────────────────────────────────────────────────────┐
│ PRINCIPAL PURPOSE TEST (Art. 7 MLI)                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ Un beneficio del CDI NO se concederá si es razonable concluir   │
│ que obtener ese beneficio fue UNO DE LOS PROPÓSITOS PRINCIPALES │
│ de cualquier acuerdo o transacción.                             │
│                                                                  │
│ EXCEPCIÓN: Se concede si demostrar que haberlo concedido en     │
│ esas circunstancias está en consonancia con el objeto y fin     │
│ del CDI.                                                         │
│                                                                  │
│ Factores de análisis:                                            │
│ ┌─────────────────┬─────────────────┬─────────────────┐         │
│ │ Sustancia       │ Timing de       │ Coherencia con  │         │
│ │ Económica       │ Transacción     │ Objeto CDI      │         │
│ └─────────────────┴─────────────────┴─────────────────┘         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Beneficial Ownership

### Doctrina TJUE (Denmark Cases)

Los casos C-116/16 y C-117/16 establecen requisitos sustantivos:

| Requisito | Descripción | Evidencia |
|-----------|-------------|-----------|
| **No conduit** | Entidad no actúa como mero conducto | Retención fondos, reinversión |
| **Poder disposición** | Titular con facultad de decidir uso | Actas de decisión, governance |
| **Riesgo económico** | Asume riesgo sobre la renta | Análisis funcional |
| **Sustancia real** | Empleados, oficinas, actividad | Documentación operativa |

### Red Flags de Treaty Shopping

| Indicador | Riesgo | Mitigación |
|-----------|--------|------------|
| Entidad constituida poco antes de pago | ALTO | Documentar razones empresariales |
| Sin empleados en jurisdicción del tratado | ALTO | Añadir sustancia o reconsiderar |
| Back-to-back arrangements | MUY ALTO | Evitar estructuras circulares |
| Misma estructura para múltiples inversores | ALTO | Individualizar análisis |
| Cambio de residencia fiscal previo a transacción | MEDIO | Documentar motivación |

---

## Inputs

```json
{
  "operacion": {
    "tipo_renta": "DIVIDENDOS",
    "pais_fuente": "ES",
    "pais_destino": "NL",
    "importe_bruto": 5000000,
    "moneda": "EUR",
    "fecha_pago": "2024-06-15"
  },
  "pagador": {
    "nombre": "TechSpain Holding SL",
    "nif": "B12345678",
    "tipo_entidad": "Sociedad de responsabilidad limitada",
    "residencia_fiscal": "ES"
  },
  "beneficiario": {
    "nombre": "TechGroup BV",
    "tax_id": "NL123456789B01",
    "residencia_fiscal": "NL",
    "certificado_residencia": true,
    "fecha_certificado": "2024-01-15"
  },
  "participacion": {
    "porcentaje": 100,
    "periodo_tenencia_meses": 24,
    "tipo_participacion": "Directa"
  },
  "analisis_sustancia": {
    "empleados_beneficiario": 8,
    "oficina_propia": true,
    "actividad_real": "Gestión de participaciones y tesorería grupo",
    "consejo_administracion_local": true,
    "decisiones_tomadas_localmente": true
  },
  "estructura_grupo": {
    "upe": "TechCorp Inc (US)",
    "cadena": ["TechCorp Inc (US)", "TechGroup BV (NL)", "TechSpain Holding SL (ES)"],
    "otros_beneficiarios_finales": "TechCorp Inc (US)"
  }
}
```

---

## Output

```json
{
  "analisis_cdi": {
    "id_operacion": "CDI-2024-001",
    "fecha_analisis": "2024-05-20",
    "tipo_renta": "DIVIDENDOS",
    "corredor": "ES → NL"
  },
  "tratado_aplicable": {
    "cdi": "Convenio España-Países Bajos",
    "firma": "16/06/1971",
    "boe": "BOE-A-1972-1380",
    "protocolo_modificativo": "10/12/2010 (BOE-A-2012-9356)",
    "mli_aplicable": true,
    "mli_entrada_vigor": "01/01/2022"
  },
  "articulo_aplicable": {
    "numero": "Art. 10 (Dividendos)",
    "version": "Modificado por Protocolo 2010 + MLI",
    "texto_clave": "Los dividendos pueden someterse a imposición en el Estado de la fuente según su legislación, pero el impuesto así exigido no podrá exceder del..."
  },
  "tasa_retencion": {
    "sin_cdi": 0.19,
    "con_cdi_general": 0.15,
    "con_cdi_participacion_sustancial": 0.05,
    "tasa_aplicable": 0.05,
    "requisitos_tasa_reducida": [
      "Participación directa ≥25% capital (cumplido: 100%)",
      "Período tenencia ≥12 meses (cumplido: 24 meses)",
      "Beneficial owner legítimo"
    ],
    "cumple_requisitos": true
  },
  "impacto_mli": {
    "reservas_espana": ["Art. 9.4 no aplicado"],
    "reservas_paises_bajos": ["Art. 9.4 no aplicado"],
    "ppt_aplicable": true,
    "analisis_ppt": {
      "riesgo": "BAJO",
      "factores_positivos": [
        "Tenencia >2 años",
        "Sustancia real en NL (8 empleados)",
        "Decisiones locales documentadas",
        "Actividad empresarial genuina"
      ],
      "factores_negativos": [
        "UPE en US sin CDI favorable"
      ],
      "conclusion": "PPT probablemente superado - estructura con sustancia"
    }
  },
  "beneficial_ownership": {
    "analisis": "CUMPLIDO",
    "factores": {
      "sustancia_nl": {
        "score": 0.85,
        "evidencia": "8 empleados, oficina propia, consejo local"
      },
      "poder_disposicion": {
        "score": 0.90,
        "evidencia": "Decisiones de dividendos tomadas en NL, actas disponibles"
      },
      "no_conduit": {
        "score": 0.75,
        "evidencia": "Fondos retenidos parcialmente, reinversión en grupo",
        "nota": "Verificar que no hay obligación contractual de redistribución"
      }
    },
    "riesgo_global": "BAJO",
    "recomendacion": "Documentar actas de decisión y uso de fondos"
  },
  "treaty_shopping_risk": {
    "score": 0.25,
    "nivel": "BAJO",
    "red_flags_detectados": [
      {
        "flag": "UPE estadounidense como beneficiario final",
        "mitigacion": "Entidad NL con sustancia real, actividad propia",
        "impacto": "Bajo si sustancia documentada"
      }
    ],
    "sin_red_flags": [
      "Periodo tenencia largo",
      "Entidad establecida hace años",
      "Empleados suficientes",
      "Actividad empresarial real"
    ]
  },
  "calculo_fiscal": {
    "importe_bruto": 5000000,
    "tasa_aplicable": 0.05,
    "retencion": 250000,
    "importe_neto": 4750000,
    "ahorro_vs_sin_cdi": 700000
  },
  "procedimiento": {
    "aplicacion_tipo_reducido": "En origen (retención directa al 5%)",
    "documentacion_requerida": [
      {
        "documento": "Certificado de residencia fiscal NL",
        "modelo": "Formulario estándar Belastingdienst",
        "vigencia": "12 meses desde expedición",
        "estado": "Vigente (exp. 15/01/2024)"
      },
      {
        "documento": "Declaración de titularidad real",
        "modelo": "Formulario interno o affidavit",
        "contenido": "Confirmación de beneficial ownership"
      },
      {
        "documento": "Evidencia de participación",
        "modelo": "Certificado Registro Mercantil + Libro de socios",
        "contenido": "100% participación directa > 12 meses"
      }
    ],
    "modelo_hacienda": "Retención directa (no requiere modelo 210 por devolución)"
  },
  "directiva_matriz_filial": {
    "aplicable": true,
    "requisitos": {
      "participacion_minima": "≥5% (cumplido: 100%)",
      "tenencia_minima": "≥1 año (cumplido: 2 años)",
      "formas_juridicas": "Ambas en Anexo I Directiva 2011/96/UE"
    },
    "exencion_total": true,
    "nota": "Directiva Matriz-Filial permite exención total (0%) vs. 5% CDI",
    "recomendacion": "Aplicar Directiva 2011/96/UE para exención completa"
  },
  "comparativa_alternativas": [
    {
      "via": "CDI España-Países Bajos",
      "tasa": "5%",
      "retencion": 250000
    },
    {
      "via": "Directiva Matriz-Filial",
      "tasa": "0%",
      "retencion": 0,
      "recomendacion": "ÓPTIMA"
    },
    {
      "via": "Sin CDI ni Directiva",
      "tasa": "19%",
      "retencion": 950000
    }
  ],
  "recomendacion_final": {
    "via_optima": "Directiva Matriz-Filial 2011/96/UE",
    "tasa_final": "0%",
    "ahorro_total": 950000,
    "documentacion_adicional": "Certificado de cumplimiento de requisitos Directiva"
  },
  "alertas": [
    {
      "tipo": "INFO",
      "mensaje": "Directiva Matriz-Filial ofrece exención total vs. 5% CDI",
      "accion": "Verificar cumplimiento requisitos Directiva"
    },
    {
      "tipo": "INFO",
      "mensaje": "Certificado de residencia expira en 8 meses",
      "accion": "Renovar antes de siguiente distribución"
    }
  ],
  "compliance": {
    "normativa_aplicable": [
      "CDI España-Países Bajos (BOE-A-1972-1380)",
      "Protocolo 2010 (BOE-A-2012-9356)",
      "MLI (BOE-A-2021-12039)",
      "Directiva 2011/96/UE (Matriz-Filial)",
      "TRLIRNR Art. 10, 13, 31"
    ],
    "procedimiento_devolucion": "No requerido si exención aplicada en origen"
  }
}
```

---

## Buscador de CDI por País

### Estructura de Base de Datos de Tratados

```json
{
  "tratados": [
    {
      "pais": "Alemania",
      "codigo_iso": "DE",
      "cdi_vigente": "BOE-A-2012-2190",
      "fecha_firma": "03/02/2011",
      "protocolo": "N/A",
      "mli_aplicable": true,
      "mli_entrada_vigor": "01/01/2022",
      "tasas": {
        "dividendos_general": 15,
        "dividendos_participacion": 5,
        "umbral_participacion": 10,
        "intereses": 0,
        "canones": 0
      },
      "articulos_clave": ["10", "11", "12", "13", "24"],
      "notas": "Exención intereses y cánones"
    },
    {
      "pais": "Estados Unidos",
      "codigo_iso": "US",
      "cdi_vigente": "BOE-A-1990-17358",
      "fecha_firma": "22/02/1990",
      "protocolo": "BOE-A-2019-8890",
      "mli_aplicable": false,
      "tasas": {
        "dividendos_general": 15,
        "dividendos_participacion": 10,
        "umbral_participacion": 25,
        "intereses": 10,
        "canones": 10
      },
      "articulos_clave": ["10", "11", "12", "13"],
      "lob_clause": true,
      "notas": "LOB restrictivo, EEUU no firma MLI"
    }
  ]
}
```

---

## Alertas Automáticas

| Trigger | Alerta | Prioridad | Acción |
|---------|--------|-----------|--------|
| Sin CDI con país destino | Retención máxima aplicable | CRÍTICA | Evaluar estructuras alternativas |
| MLI modifica tratado | Verificar reservas ambos países | ALTA | Consultar synthesized text |
| Participación < umbral CDI | Tasa general vs. reducida | MEDIA | Recalcular beneficio real |
| Certificado residencia >12 meses | Documento potencialmente inválido | ALTA | Solicitar renovación |
| Estructura conduit detectada | Riesgo PPT/Beneficial ownership | MUY ALTA | Revisar sustancia |
| Directiva UE aplicable | Posible exención total | INFO | Comparar CDI vs. Directiva |

---

## Consideraciones Éticas

1. **Legalidad:** La skill recomienda únicamente planificación fiscal conforme a derecho
2. **Transparencia:** Identifica todos los riesgos de treaty shopping sin ocultarlos
3. **Documentación:** Enfatiza la importancia de sustancia real sobre forma
4. **Actualización:** Incorpora cambios MLI y nuevos protocolos
5. **No elusión:** Distingue claramente planificación legítima de abuso

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| **Art. 96 CE** | CDI parte del ordenamiento interno |
| **TRLIRNR** | Aplicación de convenios, procedimientos de devolución |
| **MLI** | Modificaciones a tratados vigentes |
| **Directivas UE** | Matriz-Filial, Intereses y Cánones |
| **TJUE Denmark Cases** | Requisitos beneficial ownership |
| **Orden HAC/763/2018** | Certificados de residencia fiscal |
