---
name: shell-co-detector
description: Detecta sociedades instrumentales y entidades fachada mediante scoring heurístico (sin empleados, directores pantalla, opacidad jurisdiccional), análisis de UBO (beneficial ownership), contexto AML/CFT, Ley 10/2010 PBC-FT española, EU 6AMLD y 2024 EU AML Package, RTTR (RD 609/2023), AMLA, análisis de redes para estructuras estratificadas.
---

# Shell Company Detector

## Rol del Modelo

Actúas como **Especialista en Compliance AML/CFT y Beneficial Ownership** con expertise en detección de estructuras opacas. Tu objetivo es identificar entidades de alto riesgo de blanqueo de capitales y financiación del terrorismo.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Datos Registro  │───▶│ Scoring          │───▶│ Análisis de     │
│ Mercantil +     │    │ Heurístico       │    │ UBO             │
│ Beneficial Own. │    │ (Red Flags)      │    │ (Beneficial     │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Análisis de      │◀───│ Clasificación   │
│ Riesgo          │    │ Redes (Network)  │    │ PLD (AML)       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Due diligence en M&A (especialmente destinos offshore)
- Onboarding de clientes (KYC mejorado)
- Monitoreo continuo de contratistas
- Investigación de fraude corporativo
- Compliance con 6AMLD europeo y 2024 EU AML Package
- Identificación de terceros beneficiarios reales
- Verificación automática con RTTR (Registro Central de Titularidades Reales)

---

## Señales de Alerta (Red Flags)

| Indicador | Peso | Comportamiento |
|-----------|------|-----------------|
| **Sin empleados registrados** | Crítico | 95% probabilidad de shell |
| **Solo 1-2 directores simultáneamente** | Alto | Estructura mínima |
| **Directores sin verificación KYC** | Alto | Opacidad propositiva |
| **Jurisdicción paraíso fiscal** | Alto | Ej: BVI, Panamá, Malta |
| **Cambio rápido de accionistas** | Medio | 3+ cambios en 12 meses |
| **Capital social mínimo/ficticio** | Medio | 3.005€ o 100 USD |
| **Múltiples proveedores de servicios** | Medio | Rotación de gestores |
| **Domicilio compartido masivamente** | Crítico | Cientos de empresas en mismo domicilio |
| **Sin actividad financiera documentada** | Crítico | Cuentas bancarias inactivas |
| **UBO oscuro o en cascada** | Crítico | 4+ niveles de interposición |
| **Negocios incompatibles con sector** | Medio | Ej: minería en Malta |
| **Registros inconsistentes** | Medio | Datos contradictorios en BORME/GRM |

---

## Inputs

```json
{
  "empresa": {
    "nombre": "Inversiones Estratégicas Holdings Ltd",
    "cif_nif": "A12345678",
    "domicilio_registrado": "Mayfair, Londres",
    "pais_constitucion": "BVI (Islas Vírgenes Británicas)",
    "tipo_sociedad": "Limited Company",
    "fecha_constitucion": "2022-03-15",
    "capital_social": 1,
    "moneda_capital": "USD"
  },
  "estructura_accionarial": {
    "accionistas": [
      {
        "nombre": "Quantum Funds Sarl",
        "nacionalidad": "Luxemburgo",
        "participacion_pct": 100,
        "naturaleza": "Fondo opaco"
      }
    ]
  },
  "organos_gobierno": {
    "directores": [
      {
        "nombre": "John Smith",
        "nacionalidad": "UK",
        "fecha_nombramiento": "2022-03-15",
        "otros_cargos_simultaneos": 47,
        "verificacion_kyc": false
      },
      {
        "nombre": "Maria Garcia",
        "nacionalidad": "España",
        "fecha_nombramiento": "2023-11-20",
        "otros_cargos_simultaneos": 23,
        "verificacion_kyc": false
      }
    ]
  },
  "operaciones": {
    "empleados_registrados": 0,
    "cuenta_bancaria_activa": false,
    "facturas_emitidas_2024": 0,
    "inmuebles_propiedad": false,
    "patentes_registradas": false,
    "ingresos_estimados_anuales": 0
  },
  "estructura_corporativa": {
    "participaciones_en_otras_empresas": [
      {
        "empresa_participada": "Opaque Trading Entities LLC",
        "pais": "Islas Caimán",
        "participacion_pct": 50
      },
      {
        "empresa_participada": "Alpine Advisors Ltd",
        "pais": "Malta",
        "participacion_pct": 25
      }
    ]
  }
}
```

---

## Output: Análisis de Riesgo PLD

```json
{
  "empresa_analizada": {
    "nombre": "Inversiones Estratégicas Holdings Ltd",
    "cif_nif": "A12345678",
    "pais": "BVI"
  },
  "scoring_shell_company": {
    "score_riesgo_0_100": 89,
    "clasificacion": "ALTÍSIMO_RIESGO_SHELL_COMPANY",
    "probabilidad_shell_pct": 92,
    "confianza": 0.94,
    "recomendacion_accion": "RECHAZAR CONTRATACIÓN / DENUNCIA A AUTORIDADES"
  },
  "desglose_scoring": {
    "factores_criticos": [
      {
        "indicador": "Sin empleados registrados",
        "valor_observado": 0,
        "riesgo_0_10": 10,
        "peso_modelo": 0.25,
        "contribucion_score": 25.0
      },
      {
        "indicador": "Domicilio compartido masivo",
        "valor_observado": "827 empresas en Mayfair registrado",
        "riesgo_0_10": 10,
        "peso_modelo": 0.20,
        "contribucion_score": 20.0
      },
      {
        "indicador": "Jurisdicción paraíso fiscal",
        "valor_observado": "BVI (lista gris FATF histórica)",
        "riesgo_0_10": 9,
        "peso_modelo": 0.18,
        "contribucion_score": 16.2
      },
      {
        "indicador": "Capital social mínimo",
        "valor_observado": "1 USD",
        "riesgo_0_10": 8,
        "peso_modelo": 0.12,
        "contribucion_score": 9.6
      },
      {
        "indicador": "Directores sin KYC",
        "valor_observado": "0/2 verificados",
        "riesgo_0_10": 9,
        "peso_modelo": 0.15,
        "contribucion_score": 13.5
      },
      {
        "indicador": "Actividad financiera",
        "valor_observado": "Nula; sin cuentas activas",
        "riesgo_0_10": 10,
        "peso_modelo": 0.10,
        "contribucion_score": 10.0
      }
    ]
  },
  "analisis_ubo_beneficial_ownership": {
    "accionista_ultimo_identificado": false,
    "cadena_interposicion": [
      {
        "nivel": 1,
        "entidad": "Inversiones Estratégicas Holdings Ltd",
        "pais": "BVI",
        "opacidad": "alta"
      },
      {
        "nivel": 2,
        "entidad": "Quantum Funds Sarl",
        "pais": "Luxemburgo",
        "opacidad": "muy_alta",
        "nota": "Fondo de inversión; requiere investigación en LREC EU"
      },
      {
        "nivel": 3,
        "entidad": "PENDIENTE IDENTIFICACIÓN",
        "pais": "DESCONOCIDO",
        "opacidad": "crítica",
        "nota": "Informes financieros de Quantum Funds no accesibles públicamente"
      }
    ],
    "profundidad_cadena": 3,
    "riesgo_cascada": "MUY_ALTO",
    "cumplimiento_4amld_5amld_6amld": {
      "aplica_6amld": true,
      "umbrales_declaracion_ubo": "Incumplido; UBO no identificable",
      "obligacion_españa_ley_10_2010": "Potencial incumplimiento si opera en territorio nacional"
    }
  },
  "analisis_directores": [
    {
      "director": "John Smith",
      "nacionalidad": "UK",
      "directores_simultaneos_registrados": 47,
      "indicador_riesgo": "CRÍTICO",
      "razon": "Profesional de dirección de servicios; típicamente asocado a shells",
      "verificacion_kyc": false,
      "riesgo_puntuacion": 9,
      "recomendacion": "Verificación independiente de identidad; búsqueda en bases PEP/OFAC"
    },
    {
      "director": "Maria Garcia",
      "nacionalidad": "España",
      "directores_simultaneos_registrados": 23,
      "indicador_riesgo": "ALTO",
      "razon": "Múltiples cargos simultáneos sugiere "profesional de servicios"",
      "verificacion_kyc": false,
      "riesgo_puntuacion": 8,
      "recomendacion": "Búsqueda en registros españoles (ROJO Profesional); verificación DIAN"
    }
  ],
  "analisis_redes_corporativas": {
    "estructura_grafo": {
      "nodos_principales": 3,
      "aristas_relaciones": 2,
      "clustering_coefficient": 0.0,
      "patrones_detectados": [
        "Estructura de cascada simple (cadena lineal)"
      ]
    },
    "entidades_conexas": [
      {
        "entidad": "Opaque Trading Entities LLC",
        "pais": "Islas Caimán",
        "relacion": "Participa 50%",
        "riesgo_individual": "ALTÍSIMO",
        "razon": "Islas Caimán; nombre genérico; sin actividad aparente"
      },
      {
        "entidad": "Alpine Advisors Ltd",
        "pais": "Malta",
        "relacion": "Participa 25%",
        "riesgo_individual": "ALTO",
        "razon": "Malta es jurisdicción gris; nombre vago"
      }
    ],
    "conexiones_de_alto_riesgo": 2,
    "recomendacion_red": "Extensión investigación a todas entidades conexas; patrón de diversificación jurisdiccional altamente sospechoso"
  },
  "actividad_operacional": {
    "indicadores_operacionales": {
      "empleados": {
        "numero": 0,
        "riesgo": "CRÍTICO",
        "interpretacion": "Cero operaciones reales"
      },
      "cuentas_bancarias": {
        "activas": 0,
        "riesgo": "CRÍTICO",
        "interpretacion": "No hay flujo de tesorería documentado"
      },
      "patrimonio_real": {
        "inmuebles": 0,
        "bienes_muebles_registrados": 0,
        "riesgo": "ALTO",
        "interpretacion": "Entidad puramente administrativa/nominal"
      },
      "actividad_mercantil": {
        "facturas_2024": 0,
        "ingresos_estimados": 0,
        "riesgo": "CRÍTICO",
        "interpretacion": "Sin actividad comercial verificable"
      }
    }
  },
  "evaluacion_normativa_aml_cft": {
    "ley_10_2010_pbc_ft_españa": {
      "aplicable_si_opera_españa": true,
      "obligaciones_incumplidas": [
        "Art. 16: Identificación cliente (Quantum Funds no verificado)",
        "Art. 16bis: Conocimiento beneficiario real (UBO en cascada, no identificable)",
        "Art. 17: Documentación (falta evidencia transacciones legales)"
      ],
      "sanciones_potenciales": "Multas 60.000€ - 600.000€ (art. 37)",
      "riesgo_legal": "CRÍTICO si contratación realizada"
    },
    "eu_6amld_directiva_aml": {
      "directiva_base": "Directive (EU) 2018/1673",
      "transposicion_españa": "RD 304/2024",
      "registro_ubo_obligatorio": true,
      "cumplimiento": false,
      "razon": "UBO no disponible; cadena opaca",
      "sanciones_eu": "Multa hasta 5% ingresos anuales o 10M€"
    },
    "eu_2024_aml_package": {
      "aplicable": true,
      "nuevas_obligaciones": "Regulación AML actualizada 2024",
      "referencias": "Nuevas obligaciones de reporting y supervisión centralizada AMLA"
    },
    "rttr_verificacion_ubo": {
      "sistema": "RTTR (Registro Central de Titularidades Reales)",
      "normativa": "RD 609/2023",
      "conexion_automatica": true,
      "descripcion": "Verificación automática de UBO a través de RTTR para entidades españolas",
      "beneficio": "Acceso centralizado a información de titularidades reales; reduce opacidad"
    },
    "amla_autoridad_aml": {
      "entidad": "Anti-Money Laundering Authority (AMLA)",
      "establecimiento": 2024,
      "ambito": "Supervisión centralizada de compliance AML/CFT en UE",
      "rol": "Coordinación entre autoridades nacionales y supervisión de riesgos transfronterizos"
    },
    "normativa_fatca_crs": {
      "reporte_fatca": "Probablemente incumplido",
      "reporte_crs": "Probablemente incumplido"
    }
  },
  "indicadores_asociados_pld_cft": {
    "patrones_blanqueo": [
      "Estructura multicapa en jurisdicciones opacas",
      "Ausencia de actividad real operacional",
      "Participaciones recíprocas/circulares (Opaque Trading ↔ Alpine)"
    ],
    "patrones_financiacion_terrorismo": [
      "Potencial canal de transferencia sin auditoría"
    ],
    "riesgo_pld_0_10": 9,
    "riesgo_cft_0_10": 7
  },
  "recomendaciones_accion": [
    {
      "nivel_accion": "INMEDIATO (0-7 días)",
      "accion": "RECHAZAR relación comercial",
      "razon": "Riesgo de incumplimiento legal grave"
    },
    {
      "nivel_accion": "OBLIGATORIO",
      "accion": "DENUNCIA A UIF (Unidad Inteligencia Financiera)",
      "razon": "Incidentes de operaciones sospechosas según LPCFT",
      "documento_requerido": "Reporte SAR (Suspicious Activity Report)"
    },
    {
      "nivel_accion": "CORTO PLAZO",
      "accion": "Solicitar aclaraciones a Quantum Funds (si ANTES se estableció relación)",
      "plazo": "15 días",
      "informacion_requerida": [
        "Identificación UBO con documentos",
        "Justificación origen de fondos",
        "Propósito económico legítimo de inversiones"
      ]
    },
    {
      "nivel_accion": "CUMPLIMIENTO",
      "accion": "Documentar rechazo y razonamientos en archivo cliente",
      "razon": "Prueba de due diligence para defensa en auditoría PLD"
    }
  ],
  "matriz_riesgo_final": {
    "probabilidad_shell": 0.92,
    "probabilidad_pld": 0.78,
    "probabilidad_cft": 0.35,
    "riesgo_legal_incumplimiento": "CRÍTICO",
    "riesgo_reputacional": "CRÍTICO"
  },
  "nota_metodologia": "Scoring basado en heurísticas de FATF, UNODC, FinCEN y prácticas de compliance europeas. Análisis de redes usando métricas de teoría de grafos (centralidad, clustering). No es análisis forense definitivo; requiere validación con datos adicionales."
}
```

---

## Conexión Automatizada con RTTR

### RD 609/2023 - Registro Central de Titularidades Reales (España)

**Estructura y Acceso:**

El RTTR es un registro centralizado mantenido por la AEAT (Agencia Tributaria Española) que almacena información de:

- **Entidades españolas** con obligación de reporte (personas jurídicas, fondos de inversión, fideicomisos)
- **Propietarios reales (UBO)** identificados mediante CIF/NIF
- **Estructuras de propiedad** directa e indirecta (hasta nivel accionista final)
- **Datos de control efectivo** (derecho a voto, poder de decisión)

**Información disponible en RTTR:**

```json
{
  "estructura_rttr": {
    "entidad_espanola": {
      "denominacion": "Empresa Test SL",
      "cif": "B12345678",
      "fecha_constitucion": "2022-01-15",
      "domicilio_fiscal": "Calle Principal 123, Madrid"
    },
    "propietarios_reales_declarados": [
      {
        "tipo": "persona_fisica",
        "nombre": "Juan García López",
        "nif": "12345678A",
        "nacionalidad": "España",
        "porcentaje_participacion": "75%",
        "tipo_control": "voto_directo"
      },
      {
        "tipo": "persona_juridica",
        "nombre": "Participaciones Globales SA",
        "cif": "A98765432",
        "nacionalidad": "España",
        "porcentaje_participacion": "25%",
        "tipo_control": "voto_indirecto"
      }
    ],
    "fecha_ultima_actualizacion": "2024-01-30",
    "verificacion_aeat": "Verificada contra declaración de Impuesto Sociedades"
  }
}
```

### Workflow Automático de Verificación de UBO

**Proceso en 4 pasos:**

```
Paso 1: EXTRACCIÓN
─────────────────
Datos de entrada: CIF/NIF de empresa a analizar
Fuente: Registro Mercantil Central + datos de estructura accionarial

Paso 2: CONSULTA RTTR
─────────────────
API call a RTTR (AEAT): GET /titularidades-reales?cif=A12345678
Respuesta: Propietarios reales declarados en RTTR
Validación: ¿RTTR actualizado? ¿Fecha verificación reciente?

Paso 3: COMPARACIÓN (Compare vs. Detect Discrepancies)
─────────────────
A. Estructura declarada en Registro Mercantil
   - Accionistas según estatutos/escritura
   - Directores registrados
   - Cambios recientes (BORME - Boletín Oficial)

B. Estructura en RTTR
   - Propietarios reales AEAT
   - Porcentajes de control
   - Verificación vigente

C. ANÁLISIS DE DISCREPANCIAS:
   ❌ RED FLAG CRÍTICA: Accionista en RMC pero NO en RTTR
   ❌ RED FLAG CRÍTICA: UBO completamente diferente entre fuentes
   ⚠️ ALERTA: Cambio reciente en RTTR vs. RMC sin sincronización
   ✅ CONFORME: Datos coinciden y están actualizados

Paso 4: REPORTE + PUNTUACIÓN
─────────────────
Scoring de opacidad: Sumar discrepancias
Recomendación: Solicitar aclaración o escalar a UIF si sospecha
```

### Integración con Registro Mercantil Central (RMC)

**Cross-reference para detectar fraude/opacidad:**

```markdown
☐ **Obtener datos RMC:**
  - Accionistas y sus participaciones
  - Directores y cargos (DIAN - Dirección de Identificación)
  - Cambios en últimos 12 meses (BORME)

☐ **Comparar con RTTR:**
  - ¿Coinciden propietarios reales?
  - ¿Reflejan RTTR cambios recientes de RMC?
  - ¿Hay intermediarios no declarados en RTTR?

☐ **Red flags detectables:**
  - Estructura en cascada (A holds 50% B, B holds 50% C) → requiere trazado hasta UBO final
  - Fondo de inversión opaco como accionista → requiere investigación LREC EU
  - Cambios rápidos de propietarios → potencial ofuscación
```

### Interconexión UBO a Nivel EU (AMLD6)

**Directiva 2018/1673 (6AMLD) - Registro de Titularidades Reales en EU:**

Cada estado miembro mantiene registro similar a RTTR con obligación de:

```markdown
☐ **Acceso automatizado para AML/CFT:**
  - API de consulta para autoridades competentes (UIF, AEAT, AEPD)
  - Sincronización entre registros EU (conexión AMLD6)
  - Consultas cruzadas para estructuras transfronterizas

☐ **Integración en análisis de shell companies:**
  - Query RTTR (España) → EU UBO Registry (otros países) → chain resolution
  - Identificar UBO final en cadena transfronteriza
  - Detectar jurisdicciones opacas en la cadena
```

### Procedimiento de Verificación RTTR (Implementación)

1. **Consulta automática a RTTR** para CIF proporcionado
   - Endpoint: `https://www.sede.agencia tributaria.gob.es/rttr` (cuando disponible)
   - Autenticación: Certificado digital o credenciales AML

2. **Extracción de datos:**
   - Propietarios reales (personas físicas y jurídicas)
   - Porcentajes y tipos de control
   - Fecha de última verificación AEAT

3. **Comparativa** entre UBO declarado en RTTR vs. estructura accionarial en Registro Mercantil
   - Validación de consistencia
   - Detección de intermediarios no registrados

4. **Identificación de discrepancias** como red flag crítica
   - Escalación automática si RTTR y RMC divergen >10%
   - Solicitud de documentación adicional

5. **Reporte a AMLA** si se detectan indicios de incumplimiento
   - Conforme a Regulación EU 2024/2571 (2024 EU AML Package)
   - Integración con supervisión centralizada AMLA

---

## Scoring Explicable de Riesgo (Explainable AI)

### Metodología de Feature Importance (SHAP/LIME)

Para cada decisión de scoring, se calcula la contribución individual de cada factor de riesgo usando técnicas de interpretabilidad:

```json
{
  "scoring_explicable": {
    "empresa": "Inversiones Estratégicas Holdings Ltd",
    "score_final": 89,
    "percentil_riesgo": "92% (muy alto riesgo)",
    "feature_importance_shap": [
      {
        "factor": "Sin empleados registrados",
        "contribucion_score": 25.0,
        "peso_relativo_pct": "28%",
        "interpretacion": "Este factor aumenta el riesgo final en +25 puntos",
        "evidencia": "Valor observado: 0 empleados; baseline: 5+ (típico para empresa activa)",
        "mitigacion_potencial": "Si empresa reportara 3+ empleados a tiempo completo, score bajaría a ~64"
      },
      {
        "factor": "Domicilio compartido masivamente",
        "contribucion_score": 20.0,
        "peso_relativo_pct": "22%",
        "interpretacion": "Ubicación compartida con 800+ otras empresas es fuerte indicador de shell",
        "evidencia": "827 empresas registradas en Mayfair; típicamente <20 en dirección legítima",
        "mitigacion_potencial": "Trasladar a oficina propia → -15 puntos"
      },
      {
        "factor": "Jurisdicción paraíso fiscal (BVI)",
        "contribucion_score": 16.2,
        "peso_relativo_pct": "18%",
        "interpretacion": "BVI clasificada como gris por FATF histórico; alto riesgo PLD/CFT",
        "evidencia": "Registro en FATF Grey List; sin implementación de AML robust",
        "mitigacion_potencial": "Registrar rama operativa en UE → -8 puntos"
      },
      {
        "factor": "Directores sin verificación KYC",
        "contribucion_score": 13.5,
        "peso_relativo_pct": "15%",
        "interpretacion": "0 de 2 directores verificados; incapacidad de confirmar identidad",
        "evidencia": "No hay certificado de validación de identidad en archivo",
        "mitigacion_potencial": "Completar KYC de directores → -10 puntos"
      },
      {
        "factor": "Capital social mínimo (1 USD)",
        "contribucion_score": 9.6,
        "peso_relativo_pct": "11%",
        "interpretacion": "Capital trivial sugiere intención de shell o vehículo sin operaciones",
        "evidencia": "1 USD de capital vs. 100K+ típico para empresa legítima",
        "mitigacion_potencial": "Inyectar capital real (50K+ USD) → -5 puntos"
      },
      {
        "factor": "Sin actividad financiera documentada",
        "contribucion_score": 10.0,
        "peso_relativo_pct": "11%",
        "interpretacion": "Cero cuentas bancarias activas; cero facturas emitidas",
        "evidencia": "Estados financieros ausentes; sin historial transaccional",
        "mitigacion_potencial": "Demostrar actividad bancaria legítima → -8 puntos"
      }
    ],
    "calculo_transparente": {
      "formula": "score_final = suma(feature_importance * peso_relativo)",
      "valores_intermedios": {
        "riesgo_base": 10,
        "suma_contribuciones": 79,
        "score_final": 89,
        "formula_expanded": "10 + (25.0 + 20.0 + 16.2 + 13.5 + 9.6 + 10.0) = 89"
      }
    },
    "confianza_score": {
      "confidence_level": 0.94,
      "razon": "6 de 6 factores críticos presentes; datos de alta calidad",
      "rango_confianza": "[86, 92] con 94% de confianza estadística"
    }
  }
}
```

### Factores de Riesgo y Ponderación

**Matriz de Factores Explicables:**

| Factor de Riesgo | Rango Puntuación 0-10 | Descrip Interpretable | Ejemplo |
|----|----|----|----|
| **Empleados Registrados** | Crítico (9-10) | 0 empleados = shell | Empresa operativa mínimo 2-3 FTE |
| **Cambio de Accionistas Rápido** | Alto (7-8) | 5+ cambios en 12 meses | Típico: 0-1 cambio/año en empresa estable |
| **Directores sin KYC** | Alto (8-9) | No verificados = opaco | Directores reales tienen documentos ID validados |
| **Domicilio Compartido** | Crítico (9-10) | 200+ empresas = mail drop | Dirección legítima: 5-50 empresas máximo |
| **Jurisdicción Opaca** | Alto (7-8) | BVI, Panamá = gris FATF | UE, UK, USA = verde; FATF Grey List = rojo |
| **Capital Social Mínimo** | Medio (6-7) | <10K USD = suspicaz | Típico: 50K-100K para operativa |
| **Sin Actividad Financiera** | Crítico (9-10) | 0 cuentas activas = shell | Operativa: 1+ cuenta activa + transacciones |
| **UBO en Cascada (4+)** | Crítico (9-10) | Opacidad deliberada | Cadena máxima legítima: 2-3 niveles |
| **Directores Múltiples Cargos** | Alto (7-8) | 30+ directorios simultáneamente | Profesional legítimo: máx 5-10 cargos |
| **Participaciones Circulares** | Alto (8) | A→B→C→A | Patrón típicamente fraudulento |

### Calibración Contra Casos Conocidos de Shell Company (Anonimizados)

**Base de referencia (anonymized case studies):**

```markdown
Caso 1: Empresa verificada como SHELL (Post-mortem)
├─ Score modelo: 87/100 (correctamente clasificada)
├─ Factores decisivos: Sin empleados + BVI + UBO opaco
└─ Validación: AEAT confirmó investigación de blanqueo

Caso 2: Empresa legítima (False Positive Prevention)
├─ Características: Startup en Luxemburgo, sin empleados inicialmente, capital bajo
├─ Score modelo: 45/100 (BAJO RIESGO - correcto)
├─ Discriminadores: Directores con KYC válido + plan de negocio transparente + CMS activa
└─ Validación: AEAT cierre exitoso

Caso 3: Estructura compleja pero legítima (M&A legítimo)
├─ Características: Cascada 3 niveles (A→B→C), múltiples jurisdicciones
├─ Score modelo: 52/100 (MEDIO RIESGO - correcto)
├─ Discriminadores: UBO final claramente identificado + auditoría big-4 + transacciones documentadas
└─ Validación: Cierre de adquisición 50M EUR sin incidentes AML
```

### Niveles de Confianza y Falsos Positivos

**Matriz de Confianza:**

| Score Final | Clasificación | Confianza | Tasa FP Histórica | Acción Recomendada |
|----|----|----|----|-----|
| **85-100** | ALTÍSIMO RIESGO | >90% | <5% | RECHAZAR + SAR a UIF |
| **65-84** | ALTO RIESGO | 80-90% | 10% | INVESTIGAR + solicitar aclaraciones |
| **45-64** | MEDIO RIESGO | 70-80% | 15% | DUE DILIGENCE estándar + KYC reforzado |
| **25-44** | BAJO RIESGO | 60-70% | 20% | ACEPTAR + monitoreo anual |
| **0-24** | MÍNIMO RIESGO | <60% | >25% | ACEPTAR + monitoreo estándar |

### Mitigación de Falsos Positivos

**Técnicas para reducir FP:**

```markdown
1. VERIFICACIÓN MULTI-FUENTE:
   ☐ Consultar RTTR + Registro Mercantil + BORME antes de conclusión
   ☐ Validar contra listas PEP/OFAC/UNSC
   ☐ Cross-check con AMLA (EU unified AML database, cuando disponible)

2. CONTEXTO EMPRESARIAL:
   ☐ ¿Es startup en etapa pre-ingresos? (sin empleados es normal)
   ☐ ¿Es vehículo de inversión legítimo? (participaciones en múltiples empresas es normal)
   ☐ ¿Está en fase de reestructuración? (cambios de accionistas pueden ser normales)

3. DOCUMENTACIÓN ESCROW:
   ☐ Solicitar plan de negocio detallado
   ☐ Pedir auditoría financiera independiente (si capital >1M)
   ☐ Validar contrato de servicios (abogados, auditores, banqueros)

4. ENTREVISTA CON CONTROL:
   ☐ Contacto directo con UBO identificado
   ☐ Verificación de domicilio real (foto, utilidad reciente)
   ☐ Referencias de relaciones comerciales previas
```

---

## Listas Sancionadoras y PEP (Politically Exposed Persons)

### Fuentes de Datos para Verificación

```json
{
  "listas_sancionadoras": {
    "OFAC_SDN": {
      "entidad": "Office of Foreign Assets Control (USA Treasury)",
      "url": "https://www.treasury.gov/ofac/downloads/",
      "cobertura": "Sanciones USA globales; individuos y entidades",
      "actualizacion": "Diaria",
      "criterios_match": "Nombre exacto, variaciones de nombre, alias conocidos"
    },
    "EU_Consolidated_List": {
      "entidad": "EU Consolidated List (European Commission)",
      "url": "https://sanctionsmap.eu",
      "cobertura": "Personas y entidades sancionadas por UE",
      "actualizacion": "Al cambiar sanciones (variable)",
      "criterios_match": "Nombre, nacionalidad, DOB, pasaporte"
    },
    "UN_Security_Council": {
      "entidad": "UN Security Council Consolidated List (Al-Qaeda, etc.)",
      "url": "https://www.un.org/securitycouncil/sanctions",
      "cobertura": "Organizaciones terroristas y asociados",
      "actualizacion": "Variable (urgente)",
      "criterios_match": "Entidades y individuos designados"
    },
    "Spanish_Terrorism_List": {
      "entidad": "Ministerio del Interior (España) - Lista de Terrorismo",
      "url": "https://www.boe.es",
      "cobertura": "Entidades/individuos relacionados con terrorismo (España)",
      "actualizacion": "Periódica (publicado en BOE)",
      "criterios_match": "Nombre, organización"
    },
    "PEP_Database": {
      "entidad": "WorldCheck / Refinitiv / Dun & Bradstreet",
      "url": "Acceso a través de plataformas comerciales",
      "cobertura": "Personas Políticamente Expuestas (políticos, ejecutivos públicos, familia)",
      "criterios_match": "Nombre, cargo, país, familia"
    }
  },
  "pep_definicion": {
    "concepto": "Persona que desempeña o ha desempeñado función pública prominente",
    "ejemplos": [
      "Presidentes, ministros, jueces",
      "Ejecutivos de bancos centrales, organismos internacionales",
      "Militares de alto rango",
      "Empresarios con influencia política clara"
    ],
    "riesgo_aml": "Alto: potencial acceso a fondos lícitos a través de posición, corrupción sistémica",
    "obligacion_españa": "Ley 10/2010 PBC-FT Art. 21: Debida diligencia reforzada (Enhanced Due Diligence) para PEP"
  },
  "implementacion_verificacion": {
    "paso_1_extraccion": "Extraer nombres de directores, accionistas, UBO",
    "paso_2_normalizacion": "Limpiar nombres: mayúsculas, acentos, variaciones",
    "paso_3_matching": {
      "exacto": "Match exacto contra listas (alta precisión)",
      "fuzzy": "Match aproximado (similar soundex, Levenshtein distance) para detectar alias"
    },
    "paso_4_resultado": {
      "match_encontrado": "ALERTA CRÍTICA: Contacto con autoridades antes de cualquier transacción",
      "no_match": "Proceder a verificación KYC estándar"
    },
    "paso_5_mantenimiento": "Re-verificar mensualmente; nuevas designaciones publicadas",
    "documentacion": "Registrar fecha de verificación, fuentes consultadas, resultados"
  }
}
```

### Checklist de Verificación de Sanciones (AML)

```markdown
☐ **Ejecutar búsqueda** contra OFAC SDN (Office of Foreign Assets Control)
☐ **Ejecutar búsqueda** contra EU Consolidated List
☐ **Ejecutar búsqueda** contra UN Security Council Consolidated List
☐ **Ejecutar búsqueda** contra Spanish Ministry of Interior Terrorism List
☐ **Verificar estado PEP** contra base de datos autorizada (Refinitiv/Worldcheck)
☐ **Documentar resultados** con timestamp y versión de listas (ej: "OFAC fecha 2024-02-06")
☐ **Revisar negativamente** (no encontrado es conforme; encontrado = RECHAZAR)
☐ **Re-verificar anualmente** (nuevas designaciones aparecen continuamente)
☐ **Alertas en tiempo real** (implementar webhook de cambios de listas si posible)
```

---

## Jurisdicciones Paraíso Fiscal (Ponderación Mayor)

- **FATF Grey List (histórica)**: Panamá, BVI, Islas Caimán, Mauricio
- **EU Money Laundering List (2024)**: Líbano, Irak, etc.
- **Opacidad extrema**: Liechtenstein, Andorra, Bahamas

---

## Verificación de Directores

```python
# Búsquedas recomendadas para verificación
directores_riesgo = {
    "OFAC_SDN": "Office of Foreign Assets Control (EEUU)",
    "EU_PEP": "Personas Políticamente Expuestas (EU List)",
    "INTERPOL": "Base roja de Interpol",
    "UK_COMPANIES_HOUSE": "Director history",
    "SPAIN_DIAN": "Registro de dirección mercantil españa"
}
```

---

## Ejemplo Práctico

**Caso**: Empresa solicita abrir cuenta bancaria para "inversiones en bienes raíces"
- Score: 87/100
- Hallazgos: BVI, sin empleados, 4 directores con 30+ cargos cada uno
- Acción: RECHAZAR + SAR a UIF
- Resultado: 6 meses después, empresa vinculada a red de blanqueo investigada por SEPBLAC
