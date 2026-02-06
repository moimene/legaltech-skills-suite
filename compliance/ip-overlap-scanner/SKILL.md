---
name: ip-overlap-scanner
description: Detecta plagiarismo de código y solapamiento IP entre bases de código mediante análisis AST (no solo textual), verificación compliance de licencias (GPL, MIT, Apache contaminación), detección de secretos comerciales expuestos. Contexto M&A due diligence, Ley Propiedad Intelectual España, EU IP enforcement, auditoría FOSS.
---

# IP Overlap Scanner

## Rol del Modelo

Actúas como **Especialista en Due Diligence de IP y Compliance de Open Source** con expertise en análisis de código fuente y propiedad intelectual digital. Tu objetivo es identificar infracciones de derechos de autor, contaminación de licencias y exposición de secretos.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Repositorio 1   │───▶│ Tokenización +   │───▶│ Análisis AST    │
│ (Codebase A)    │    │ AST Parsing      │    │ (Similitud      │
│ + Repo 2        │    │ (Python,Java,    │    │  Estructural)   │
└─────────────────┘    │  JavaScript)     │    │                 │
                       └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe IP      │◀───│ Verificación     │◀───│ Scoring de      │
│ + Plan Remedia  │    │ SBOM / Licencias │    │ Overlap         │
└─────────────────┘    │ + Secretos       │    │ (0-100%)        │
                       └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Due diligence M&A/adquisición de software
- Auditoría compliance open source (FOSS)
- Evaluación de contratistas/proveedores de código
- Investigación de presunto plagiarismo
- Gestión de riesgos IP antes de IPO
- Detección de fugas de código fuente

---

## Metodología de Análisis

### 1. Análisis Textual (Baseline)

```
Similitud de Levenshtein + Rabin-Karp rolling hash
Sensible a refactoring trivial (renombrado variables)
Baseline: detecta copias exactas (80-100%)
```

### 2. Análisis AST (Advanced)

```
Abstract Syntax Tree: estructura lógica del código
- Ignora: espacios, comentarios, nombres variables
- Detecta: lógica copiada (reescrita con vars diferentes)
- Sensibilidad: 60-90% para plagiarismo sofisticado
```

### 3. Clone Detection (Pesado)

```
Tipo I:   Copias exactas (incluyendo formato)
Tipo II:  Copias con variabilidad sintáctica (vars renombradas)
Tipo III: Copias modificadas (algunas líneas cambiadas)
Tipo IV:  Clones semánticos (lógica equivalente, implementación distinta)
```

---

## Mapa de Riesgos por Tipo de Activo IP

### Marco Normativo España y UE

**Ley Propiedad Intelectual (TRLPI) - RDL 1/1996 + Reformas:**

```markdown
Activos Protegidos:
├─ Código fuente (software)
├─ Documentación (técnica, de usuario)
├─ Obras literarias y artísticas
├─ Datos y bases de datos (Ley 5/1998)
└─ Diseños industriales (EUIPO)
```

### 1. Copyright - Código Fuente (Art. 96-99 TRLPI)

**Protección automática:** No requiere registro; existe desde creación

```json
{
  "tipo_activo": "COPYRIGHT_CODIGO",
  "ejemplo": "módulo_autenticacion.py (485 líneas)",
  "proteccion_legal": {
    "españa": "TRLPI Art. 96-99",
    "europa": "Directive 2006/115/EC (CAP)",
    "duracion": "Autor: vida + 70 años post mortem; obra anónima: 70 años desde publicación"
  },
  "deteccion_infraccion": {
    "metodo_1_textual": {
      "tecnica": "Levenshtein distance, Rabin-Karp rolling hash",
      "sensibilidad": "Detecta copias exactas (80-100%)",
      "falsos_positivos": "Alto en código boilerplate genérico",
      "ejemplo": "Dos implementaciones de loop idéntico pero independiente"
    },
    "metodo_2_ast": {
      "tecnica": "Abstract Syntax Tree - estructura lógica",
      "sensibilidad": "Detecta plagiarismo sofisticado (60-90%)",
      "ventaja": "Ignora renombrado de variables",
      "ejemplo": "Misma lógica OAuth 2.0 con nombres distintos"
    },
    "metodo_3_clone_semantic": {
      "tecnica": "Type IV Clones - semántica equivalente",
      "sensibilidad": "Detecta lógica equivalente (40-70%)",
      "complejidad": "Alto costo computacional",
      "ejemplo": "for-loop reescrito como while-loop"
    }
  },
  "matriz_riesgo": {
    "probabilidad": "Función de similitud (40-100%)",
    "impacto": {
      "score_0_10": 9,
      "razon": "Violación copyright automática; derecho moral de autor"
    },
    "deteccion_dificultad": {
      "score_0_10": 3,
      "razon": "Fácil de detectar con AST; refactoring trivial no engaña"
    },
    "riesgo_legal_final": "ALTO (si similitud >70% AST + 50+ líneas)",
    "valor_danio_estimado": "3K - 50K EUR (RDL 1/1996 Art. 129: indemnización por daño+lucro cesante)"
  },
  "pruebas_judiciales": [
    "Git history (timestamp de creación)",
    "Análisis forense de AST vs. original",
    "Testigos: desarrolladores, code review logs",
    "Acceso previo a código original (probado o inferido)"
  ]
}
```

### 2. Patents - Análisis de Reivindicaciones (Ley 24/2015 de Patentes)

**Patentes españolas y EU:** Oficina Española de Patentes (OEPM) + EUIPO

```json
{
  "tipo_activo": "PATENTS",
  "ejemplo": "Sistema de autenticación basado en machine learning (ES2345678)",
  "proteccion_legal": {
    "españa": "Ley 24/2015 de Patentes",
    "europa": "European Patent Convention (EPC)",
    "duracion": "20 años desde fecha de solicitud"
  },
  "analisis_libertad_operacion": {
    "paso_1_identificar_patentes": {
      "fuentes": ["ESPACENET", "WIPO PATENTSCOPE", "OEPM registry"],
      "criterios": "Palabras clave técnicas de producto (ej: 'machine learning authentication')"
    },
    "paso_2_leer_reivindicaciones": {
      "elemento_critico": "Claim 1 (más amplio); Claims 2-20 (reducciones de alcance)",
      "pregunta_clave": "¿Mi producto implementa TODO lo que dice Claim 1?",
      "ejemplo_claim": "A system for authenticating users via [feature A] AND [feature B] AND [feature C]",
      "resultado": {
        "si_implementa_todo": "Potencial infracción (Doctrine of Equivalents también)",
        "si_implementa_parte": "Puede evitar (diseño around patent)"
      }
    },
    "paso_3_evaluacion_fto": {
      "fto_acronym": "Freedom-To-Operate Assessment",
      "resultado": {
        "claro": "Nuestro código implementa funcionalidad FUERA de reivindicaciones patentadas",
        "riesgo_medio": "Solapamiento potencial en 1-2 patentes; diseño around viable",
        "riesgo_critico": "Múltiples patentes cubren funcionalidad central; infracción probable"
      }
    }
  },
  "matriz_riesgo": {
    "probabilidad": "Función de cobertura de reivindicación (30-100%)",
    "impacto": {
      "score_0_10": 8,
      "razon": "Injunction (prohibición venta) + damages (hasta 3x royalties)"
    },
    "deteccion_dificultad": {
      "score_0_10": 8,
      "razon": "Requiere análisis técnico-legal especializado"
    },
    "riesgo_legal_final": "MEDIO-ALTO (si Claim covers core functionality)",
    "valor_danio_estimado": "50K - 500K EUR (Ley 24/2015 Art. 77: hasta 3x royalties estimadas)"
  }
}
```

### 3. Industrial Designs (Ley Diseños de UE + EUIPO)

**Protección visual/forma** de productos

```json
{
  "tipo_activo": "DESIGN_INDUSTRIAL",
  "ejemplo": "Interfaz de usuario (UI mockups) - potencialmente protegida como design",
  "proteccion": {
    "registrado": "EUIPO design registration",
    "no_registrado": "Protección automática en algunos casos (UE unregistered design)",
    "duracion": "5-25 años (renovable)"
  },
  "deteccion": {
    "visual_similarity": {
      "tecnica": "Algoritmo de similitud visual (perceptual hashing)",
      "precision": "BAJA si cambios cosméticos; ALTA si forma es idéntica"
    }
  },
  "riesgo": "BAJO-MEDIO (UI changes relativamente fáciles vs. patents)"
}
```

### 4. Trademarks (EUIPO / OEPM)

**Nombres, logos, eslogans**

```json
{
  "tipo_activo": "TRADEMARK",
  "ejemplos": ["Product name", "Logo", "Slogan"],
  "analisis": {
    "confusion_likelihood": {
      "criterios": [
        "Similitud visual (logo)",
        "Similitud fonética (nombre pronunciado igual)",
        "Similitud conceptual (significado similar)",
        "Mercado superpuesto (mismos clientes)"
      ]
    }
  },
  "riesgo": "BAJO si nombre/logo son distintivos y diferentes"
}
```

### 5. Trade Secrets (Ley 1/2019 de Secretos Comerciales)

**Información confidencial**: algoritmos propietarios, fórmulas, métodos

```json
{
  "tipo_activo": "TRADE_SECRETS",
  "ejemplo": "Algoritmo de precios dinámicos, fórmula de descuentos",
  "proteccion_legal": {
    "españa": "Ley 1/2019",
    "europa": "Directive 2016/943 (Trade Secrets Directive)",
    "acciones_legales": ["Injunction para impedir uso", "Damages", "Criminal sanctions"]
  },
  "deteccion_riesgo": {
    "indicador": "Lógica algorítmica o matemática única sin patente",
    "riesgo": "CRÍTICO si expuesta en codebase",
    "ejemplo": "pricing_engine/discount_algorithm.py expuesto en repositorio públicamente"
  }
}
```

### Matriz de Riesgos Consolidada (Type × Probability × Impact × Detection)

```markdown
┌─────────────────┬─────────────┬────────┬────────────┬─────────────┐
│ Tipo de Activo  │ Probabilidad │ Impacto│ Detección  │ Riesgo Final│
├─────────────────┼─────────────┼────────┼────────────┼─────────────┤
│ COPYRIGHT       │ 60-80%      │ 8/10   │ 3/10 (fácil)  │ ALTO        │
│ PATENTS         │ 30-50%      │ 9/10   │ 8/10 (difícil)│ MEDIO-ALTO  │
│ DESIGNS         │ 20-40%      │ 6/10   │ 5/10 (medio)  │ BAJO-MEDIO  │
│ TRADEMARKS      │ 10-30%      │ 5/10   │ 2/10 (trivial)│ BAJO        │
│ TRADE SECRETS   │ 40-60%      │ 9/10   │ 4/10 (variable)│ ALTO        │
└─────────────────┴─────────────┴────────┴────────────┴─────────────┘

Score de Riesgo Global = Suma(Probability × Impact) si Detection = fácil
                       = Suma(Probability × Impact × 0.5) si Detection = difícil
```

---

## Alertas por Cláusulas Copyleft

### Marco Conceptual: Licencias Open Source Categorizadas

```markdown
LICENCIAS COPYLEFT (Requieren publicación de código derivado):
├─ GPL v2/v3 (GNU General Public License)
├─ AGPL v3 (Affero GPL - copyleft incluso en SaaS)
├─ LGPL (Lesser GPL - excepciones para linked libraries)
└─ SSPL (Server Side Public License - código servidor debe ser público)

LICENCIAS PERMISIVAS (Permiten uso comercial sin publicación):
├─ MIT (La más permisiva; solo requiere attribution)
├─ BSD (Similar a MIT; 2-3 variantes)
├─ Apache 2.0 (Permisiva + patent grant explícito)
└─ ISC (Muy similar a MIT)

LICENCIAS HÍBRIDAS/ESPECIALES:
├─ LGPL (Copyleft sobre componente, pero no sobre proyecto que lo usa)
├─ MPL (Mozilla Public License - copyleft sobre archivos modificados)
└─ EPL (Eclipse Public License)
```

### GPL v2/v3: Reglas de Propagación (Art. 5-6 GPL v3)

**Pregunta clave:** ¿Mi proyecto distribuye o ejecuta código GPL?

```json
{
  "analisis_gpl_propagacion": {
    "escenario_1_distribucion_binaria": {
      "caso": "Distribuimos software compilado que incluye librería GPL",
      "obligacion": "COPYLEFT OBLIGATORIO: Publicar TODO código fuente (incluyendo el nuestro)",
      "detalle": "GPL Art. 5-6: If you distribute binaries, must provide source code",
      "excepcion": "NO hay excepción; codebase entera debe ser open source"
    },
    "escenario_2_linkage_estatico": {
      "caso": "Compilamos librería GPL directamente en nuestro binario (static linking)",
      "obligacion": "COPYLEFT OBLIGATORIO: Obra derivada (derived work)",
      "detalle": "GPL considera linked code como modified version (Art. 5)",
      "mitigation_option": "Cambiar a dynamic linking (si GPL v2/v3 lo permite)"
    },
    "escenario_3_linkage_dinamico": {
      "caso": "Programa carga librería GPL en runtime (dynamic linking via .so / .dll)",
      "obligacion": "Depende de versión: GPL v2 = copyleft igualmente; GPL v3 = más flexible",
      "detalle": "GPL v2 Art. 2(b): 'must cause any work that you distribute that in whole or in part contains or is derived from the Program' → copyleft",
      "mitigation": "Considerar LGPL alternative si existe; o cambiar librería"
    },
    "escenario_4_saas_cloud": {
      "caso": "Ejecutamos GPL en servidor cloud; usuarios acceden via web (NO distribuimos binarios)",
      "obligacion_gpl_v2": "QUIZÁ NO es obligatorio publicar (Tivoization loophole en v2)",
      "obligacion_gpl_v3": "COPYLEFT OBLIGATORIO: AGPL-style; must offer to provide source to users",
      "detalle": "GPLv3 Art. 13: 'If our Program were designed so that v2 clause didn't apply, v3 closes gap'",
      "mitigation": "Ofrecer descarga de fuente a usuarios; o cambiar a AGPL (más claro)"
    },
    "escenario_5_mere_aggregation": {
      "caso": "Distribuimos GPL app + nuestro app separadamente en mismo CD/repo",
      "obligacion": "NO copyleft si verdaderamente separado; pero cuidado: no puede ser integración",
      "criterio": "GPL v3 Art. 5(d): exception para 'mere aggregation'; pero integración=copyleft",
      "riesgo": "Auditor GPL probablemente argumentará integración"
    }
  }
}
```

### LGPL: Excepciones para Dynamic Linking (Art. 3-4 LGPL)

**"Lesser" GPL = copyleft solo sobre componente LGPL, no sobre proyecto que lo usa**

```json
{
  "analisis_lgpl": {
    "caso": "Proyecto utiliza librería LGPL (ej: GNU C library)",
    "regla_basica": "Si linkamos dinámicamente (.so/.dll) → LGPL, nuestra app puede ser propietaria",
    "obligaciones": [
      "1. Mantener LGPL notice en documentación",
      "2. Permitir user RELINK librería LGPL: proporcionar .o files o source",
      "3. NO modificar LGPL librería"
    ],
    "permisiones": [
      "✓ Distribuir como binario propietario",
      "✓ No publicar código fuente propio",
      "✓ Modificar librería LGPL (pero debe permitir user relinking)"
    ],
    "riesgo": "BAJO si cumplimos reglas; CRÍTICO si linkamos estáticamente (se convierte en GPL)"
  }
}
```

### AGPL v3: Network Use Trigger (Art. 13 AGPL)

**AGPL = GPL + "network trigger": Usar AGPL en SaaS = obligación de publicar**

```json
{
  "analisis_agpl": {
    "caracteristica": "AGPL cierra loophole de GPLv2 para SaaS",
    "pregunta_clave": "¿Usuarios interactúan con código AGPL sobre red (web)?",
    "respuesta_si": {
      "obligacion": "COPYLEFT TOTAL: Publicar código fuente a usuarios (como si distribuyéramos)",
      "detalle": "AGPL Art. 13: 'Notwithstanding [...] if you distribute the Program [...] over a network, that network users may be able to trigger download of source code'",
      "ejemplo": "SaaS usando librería AGPL → usuarios del servicio tienen derecho a source"
    },
    "riesgo_actual": "CRÍTICO: Muchos proyectos no son conscientes de AGPL network trigger",
    "mitigacion": "REMOVER dependencia AGPL inmediatamente; no hay workaround legal"
  }
}
```

### Apache 2.0: Patent Grant (Art. 2-3)

**Apache 2.0 es permisiva pero incluye cláusula de patentes**

```json
{
  "analisis_apache_2": {
    "permisividad": "Igual a MIT: permite uso comercial sin publicar código",
    "caracteristica_unica": {
      "patent_grant": "Licenciante otorga implícitamente derechos de patente",
      "beneficio_para_usuario": "Si Apache software usa patente, no podemos demandarte por infracción"
    },
    "obligaciones_minimas": [
      "1. Incluir notice Apache",
      "2. Si modificas, documentar cambios",
      "3. Incluir copy de Apache license"
    ],
    "riesgo": "BAJO"
  }
}
```

### MIT/BSD: Análisis Permisiva (Mínimo Riesgo)

```json
{
  "analisis_mit": {
    "estructura": "MIT es casi idéntica a BSD-2-Clause",
    "obligaciones": [
      "1. Incluir texto completo MIT en redistribución",
      "2. Mencionar autor original",
      "3. ¡Eso es TODO!"
    ],
    "copyright_notice_required": "Sí, pero no afecta propiedad de código derivado",
    "riesgo": "MUY BAJO"
  }
}
```

### Evaluación de Contaminación Copyleft (Risk Assessment)

**Regla crítica:** Si CUALQUIER dependencia copyleft está presente → flag proyecto entero

```json
{
  "riesgo_contaminacion_copyleft": {
    "premisa": "Un componente copyleft puede contaminr proyecto entero",
    "logica": {
      "version_1": "Si proyecto A (propietario) depende de B (GPL) → A es obra derivada → A DEBE ser GPL"
    },
    "procedimiento_evaluacion": {
      "paso_1_sbom": "Generar SBOM (Software Bill of Materials) con todos los componentes",
      "paso_2_licencias": "Mapear licencia de cada componente",
      "paso_3_buscar_copyleft": "¿Existe GPL/AGPL/SSPL?",
      "paso_4_resultado": {
        "si_copyleft_presente": "ALERTA CRÍTICA: Proyecto es contaminado; debe ser open source",
        "si_solo_permisivo": "OK: Puede ser propietario pero debe incluir notices"
      }
    },
    "matriz_combinaciones_problematicas": {
      "gpl_v3_plus_nuestro_codigo": "Obra derivada → nuestro código debe ser GPLv3+",
      "agpl_plus_saas": "Obra derivada + network trigger → publicar TODO al deploying",
      "gpl_plus_propietario_link": "Incluso linkage dinámico es copyleft (probable)"
    }
  }
}
```

### Compliance SPDX y Verificación Licencias

**SPDX (Software Package Data Exchange):** Standard para documentar licencias

```markdown
SBOM SPDX Example:
───────────────────
SPDXVersion: SPDX-2.3
DataLicense: CC0-1.0

PackageName: CRM-Enterprise-Suite
SPDXID: SPDXRef-Package
PackageDownloadLocation: NOASSERTION
FilesAnalyzed: true

PackageVerificationCode: 1234567890abcdef (hash)

PackageLicenseConcluded: NOASSERTION
PackageLicenseDeclared: NOASSERTION
PackageLicenseComments: Project license not declared

ExternalRef: security-cpe23Type cpe23Type cpe:2.3:a:vendor:product:version:...

─── Dependency 1 ───
FileName: ./lib/auth_lib.jar
SPDXID: SPDXRef-auth_lib
FileChecksum: SHA1: abcd1234
LicenseConcluded: MIT
LicenseInfoInFile: MIT
FileCopyrightText: <text> Copyright 2020 Auth Inc. </text>

─── Dependency 2 ───
FileName: ./lib/search_engine.so
SPDXID: SPDXRef-search_engine
FileChecksum: SHA1: efgh5678
LicenseConcluded: AGPL-3.0-only
LicenseInfoInFile: AGPL-3.0-only
FileCopyrightText: <text> Copyright 2019 SearchCo </text>

───────────────────
ANALYSIS RESULT:
  ⚠️ COPYLEFT DETECTED: AGPL-3.0 in ./lib/search_engine.so
  → Project must be open-sourced if distributed
```

### Plantilla: FOSS Compliance Report para M&A DD (Due Diligence)

```json
{
  "foss_compliance_report_ma": {
    "fecha": "2024-02-06",
    "proyecto_adquirido": "CRM-Enterprise-Suite",
    "due_diligence_alcance": "M&A preparatoria",
    "resumen_ejecutivo": {
      "status_compliance": "NO_CONFORME - Riesgos críticos detectados",
      "recomendacion": "REMEDIAR antes de cierre de M&A",
      "riesgo_legal": "ALTO - Múltiples violaciones de copyleft"
    },
    "hallazgos_criticos": [
      {
        "hallazgo": "AGPL-v3 dependency en search engine",
        "severidad": "CRÍTICA",
        "impacto": "Si distribuimos como SaaS, OBLIGADO publicar TODO código",
        "accion_urgente": "Remover AGPL library; reemplazar con Apache/MIT alternative"
      },
      {
        "hallazgo": "GPL-v3 en data processor library (static linked)",
        "severidad": "CRÍTICA",
        "impacto": "Obra derivada; proyecto entero debe ser GPLv3 si distribuido",
        "accion_urgente": "Cambiar a LGPL (dynamic link) O reescribir funcionalidad"
      },
      {
        "hallazgo": "MIT license no attributionado en docs",
        "severidad": "MEDIA",
        "impacto": "Legal pero mala práctica; podría argumentarse incumplimiento",
        "accion": "Crear ATTRIBUTION.md; listar todas las licencias MIT"
      }
    ],
    "matriz_dependencias": [
      {
        "libreria": "auth_lib (MIT)",
        "licencia": "MIT",
        "riesgo": "BAJO",
        "accion": "Aceptar; incluir copyright notice"
      },
      {
        "libreria": "search_engine (AGPL v3)",
        "licencia": "AGPL-3.0",
        "riesgo": "CRÍTICO",
        "accion": "REMOVER"
      },
      {
        "libreria": "data_processor (GPL v3)",
        "licencia": "GPL-3.0",
        "riesgo": "CRÍTICO",
        "accion": "Cambiar a LGPL o reescribir"
      }
    ],
    "estimacion_remediacion": {
      "esfuerzo_horas": 200,
      "timeline_semanas": 4,
      "costo_estimado": "€4K-8K (desarrollo + legal review)"
    },
    "recomendacion_final": "No cerrar M&A hasta AGPL + GPL removidas; riesgo legal es inaceptable para adquirente"
  }
}
```

---

## Inputs

```json
{
  "scan_type": "m_a_due_diligence",
  "target_codebase": {
    "nombre": "CRM-Enterprise-Suite",
    "ubicacion": "/path/to/repo",
    "tamaño_loc": 485000,
    "lenguajes": ["Python", "JavaScript", "SQL"],
    "vcs": "git",
    "hash_commit": "abc123def456"
  },
  "comparacion_contra": [
    {
      "nombre": "CRM-Competitor-v2",
      "ubicacion": "/path/competitor/repo",
      "tamaño_loc": 420000,
      "fuente": "Code escrow + legal discovery"
    },
    {
      "nombre": "FOSS_Reference (GPL libs)",
      "ubicacion": "license_check",
      "proposito": "Verificar contaminación GPL"
    }
  ],
  "configuracion_scan": {
    "metodo_similaridad": ["ast", "textual"],
    "umbral_alerta_overlap": 15,
    "analizar_secretos": true,
    "generar_sbom": true,
    "nivel_detalle": "completo"
  }
}
```

---

## Output: Informe Completo

```json
{
  "scan_summary": {
    "fecha_analisis": "2025-02-06",
    "duracion_segundos": 3847,
    "archivos_analizados": 1245,
    "lineas_codigo_totales": 485000
  },
  "overlap_detection": {
    "comparacion": "CRM-Enterprise vs. CRM-Competitor-v2",
    "similitud_general": {
      "score_textual": 0.32,
      "score_ast": 0.58,
      "score_ponderado": 0.48,
      "clasificacion": "SOLAPAMIENTO_MEDIO_ALTO",
      "riesgo_copyright": "ALTO",
      "riesgo_patentes": "MEDIO"
    },
    "desglose_por_componente": [
      {
        "componente": "módulo_autenticacion.py",
        "tamaño_lineas": 2100,
        "overlap_textual": 0.78,
        "overlap_ast": 0.85,
        "archivos_similares_detectados": [
          {
            "archivo": "auth_module.py (Competitor)",
            "similitud_ast": 0.85,
            "tipo_clon": "TIPO_III",
            "descripcion": "Lógica OAuth 2.0 idéntica; variables renombradas"
          }
        ],
        "veredicto": "SOLAPAMIENTO SIGNIFICATIVO - Requiere investigación legal",
        "fragmento_critico": {
          "lineas": "142-187",
          "codigo_target": "Validación token JWT con claim mapping",
          "codigo_competitor": "Idéntica lógica; variable names diferentes"
        }
      },
      {
        "componente": "modulo_reportes.sql",
        "tamaño_lineas": 5600,
        "overlap_textual": 0.12,
        "overlap_ast": 0.08,
        "descripcion": "SQL genérico; sin solapamiento significativo"
      },
      {
        "componente": "libreria_graficos_ui.js",
        "tamaño_lineas": 1850,
        "overlap_textual": 0.45,
        "overlap_ast": 0.52,
        "tipo_clon": "TIPO_II",
        "descripcion": "Librería D3.js wrapper; parcialmente derivada de FOSS",
        "riesgo_licencia": "POTENCIAL_CONTAMINACION_MIT"
      }
    ]
  },
  "analisis_licencias_foss": {
    "requisito_normativo": "Auditoría mandatoria por RDL 1/1996 (LPI España) y EU IP Directive 2004/48",
    "dependencias_externas_detectadas": 65,
    "licencias_identificadas": {
      "MIT": 22,
      "Apache_2_0": 18,
      "BSD_3Clause": 15,
      "GPL_v3": 7,
      "AGPL_v3": 2,
      "Proprietary": 1
    },
    "alertas_criticas": [
      {
        "libreria": "backend_search_engine (v2.1.0)",
        "licencia": "AGPL_v3",
        "riesgo": "CRÍTICO",
        "razon": "AGPL copyleft; requiere publicar TODO código derivado si se distribuye",
        "impacto": "Si CRM-Enterprise distribuye SaaS: incumplimiento potencial",
        "linea_actual": "Incluida en Dockerfile; se distribu en servicios cloud"
      },
      {
        "libreria": "data_processor_lib",
        "licencia": "GPL_v3",
        "riesgo": "ALTO",
        "razon": "GPL requiere publicar código fuente si se distribuye",
        "impacto": "CRM-Enterprise es propietario; conflicto de licencias"
      },
      {
        "libreria": "ui_framework (fork unofficial)",
        "licencia": "MIT (original) pero fork modificado",
        "riesgo": "MEDIO",
        "razon": "Licencia MIT permite uso comercial; pero debe incluir notice original",
        "solucion": "Verificar que LICENSE de MIT está incluido"
      }
    ],
    "status_compliance": "NO_CUMPLE",
    "acciones_requeridas": [
      "Remover AGPL library: sustituir por alternativa compatible",
      "Evaluar GPL library: considerar licencia dual o reescritura",
      "Documentar todas las MIT/BSD libraries en ATTRIBUTION.md"
    ]
  },
  "deteccion_secretos_comerciales": {
    "secretos_potenciales_detectados": 4,
    "riesgos_encontrados": [
      {
        "tipo": "API_KEY",
        "archivo": "config/production.env",
        "riesgo": "CRÍTICO",
        "descripcion": "Clave AWS expuesta en repositorio",
        "linea": 127,
        "accion": "Revocar inmediatamente; rotar credenciales"
      },
      {
        "tipo": "DATABASE_PASSWORD",
        "archivo": "database_seed.sql",
        "riesgo": "CRÍTICO",
        "descripcion": "Contraseña de admin base de datos en texto plano",
        "linea": 45,
        "accion": "No debería estar en repo; usar secrets management"
      },
      {
        "tipo": "ALGORITMO_PROPIETARIO",
        "archivo": "src/pricing_engine/discount_algorithm.py",
        "riesgo": "ALTO",
        "descripcion": "Lógica de descuentos patentable; secreto comercial",
        "observacion": "Presente en ambas codebases; investigue origen"
      },
      {
        "tipo": "CUSTOMER_DATA",
        "archivo": "test/fixtures/customer_data.json",
        "riesgo": "ALTO",
        "descripcion": "Datos de clientes reales en test fixtures",
        "gdpr_violation": "Potencial incumplimiento RGPD art. 32"
      }
    ],
    "recomendacion": "Limpieza inmediata de secrets; auditoría de acceso histórico en Git"
  },
  "sbom_software_bill_of_materials": {
    "generado_formato": "SPDX_3_0",
    "resumen": {
      "componentes_unicos": 65,
      "componentes_licenciables": 63,
      "componentes_sin_licencia_clara": 2
    },
    "vulnerabilidades_conocidas": [
      {
        "cve": "CVE-2024-1234",
        "libreria_afectada": "data_processor_lib v2.0.1",
        "severidad": "ALTA",
        "descripcion": "Inyección SQL en módulo de búsqueda",
        "version_instalada": "2.0.1",
        "version_parcheada": "2.0.3",
        "accion": "Actualizar a v2.0.3"
      }
    ],
    "archivo_sbom_generado": "sbom_crm_enterprise_2025-02-06.spdx"
  },
  "analisis_propiedad_intelectual": {
    "patentes_potencialmente_violadas": [
      {
        "patent_id": "ES2345678",
        "titulo": "Sistema de autenticación basado en machine learning",
        "poseedor": "Competitor Corp",
        "ano_registro": 2020,
        "solapamiento_detectado": {
          "módulo": "auth_ml_classifier.py",
          "similitud_algoritmo": 0.72,
          "riesgo": "MEDIO_ALTO",
          "descripcion": "Algoritmo de clasificación de usuarios es próximo al patentado"
        }
      }
    ],
    "derechos_autor_potencialmente_violados": [
      {
        "autor": "Competitor Corp",
        "obra_original": "CRM-Competitor v1.0 (2021)",
        "componente_utilizado": "módulo_autenticacion",
        "valor_dano_estimado": "50K - 200K EUR (basado en análisis market value)",
        "anios_prescripcion": "5 años (RDL 1/1996 LPI España)",
        "evidencia_copia": "Análisis AST muestra 85% similitud estructural"
      }
    ]
  },
  "contexto_normativo_espana_eu": {
    "ley_pi_españa": {
      "norma": "Real Decreto Legislativo 1/1996 (LPI)",
      "articulos_relevantes": {
        "art_17": "Obras derivadas requieren autorización del autor original",
        "art_34": "Protección automática sin registro; copyrighted por defecto",
        "art_38": "Prueba de titularidad mediante versionado (Git history)"
      },
      "sanciones_potenciales": "Daños desde 600€ hasta millones en casos graves"
    },
    "eu_ip_directive": {
      "norma": "Directive 2004/48/EC (IP Enforcement)",
      "obligaciones": "Estados miembros deben proporcionar medidas civiles y penales",
      "retencion_ganancias": "Infractores deben devolver ganancias obtenidas"
    },
    "rgpd_consideraciones": {
      "si_incluye_datos_personales": true,
      "requisitos_adicionales": "Evaluación de riesgos DPIA para cualquier codebase con PII"
    },
    "compliance_ciberseguridad": {
      "normativa": "NIS2 Directive (2024) / Ley Ciberseguridad España",
      "relevancia": "Código con secretos/exposiciones requiere notificación a autoridades"
    }
  },
  "recomendaciones_accion": [
    {
      "prioridad": "CRÍTICA",
      "plazo": "24-48 horas",
      "accion": "Revocar credenciales expuestas en Git",
      "responsable": "DevOps + Seguridad",
      "evidencia": "API_KEY_AWS_PROD, DB_PASSWORD"
    },
    {
      "prioridad": "CRÍTICA",
      "plazo": "1 semana",
      "accion": "Consultar con asesor legal IP",
      "responsable": "Legal Department",
      "motivo": "Solapamiento 85% en módulo autenticación; riesgo litigio altísimo",
      "costo_estimado": "3K - 10K EUR (asesoría)"
    },
    {
      "prioridad": "ALTA",
      "plazo": "2 semanas",
      "accion": "Remover dependencia AGPL; sustituir por alternativa",
      "responsable": "Desarrollo + Arquitectura",
      "costo_estimado": "40 - 80 horas dev",
      "impacto_retraso_ma": "Bloquea cierre de transacción hasta resolución"
    },
    {
      "prioridad": "ALTA",
      "plazo": "2 semanas",
      "accion": "Reescribir módulo de autenticación (si es viable)",
      "responsable": "Equipo Senior Tech",
      "alternativa": "Solicitar licencia de Competitor Corp (costo: negociable)"
    },
    {
      "prioridad": "MEDIA",
      "plazo": "30 días",
      "accion": "Generar ATTRIBUTION.md documentando todas las licencias FOSS",
      "responsable": "Compliance + DevOps",
      "costo": "0 (documental)"
    },
    {
      "prioridad": "MEDIA",
      "plazo": "30 días",
      "accion": "Realizar DPIA (Data Protection Impact Assessment)",
      "responsable": "DPO + Legal",
      "costo_estimado": "5K EUR"
    }
  ],
  "impacto_en_ma": {
    "valor_empresa_pre_scan": "15M EUR (estimado)",
    "ajuste_por_riesgos_ip": "-1.5M EUR a -3M EUR",
    "razon": "Litigio potencial + obligaciones compliance + time-to-market de remedios",
    "duracion_negociacion_adicional": "4-8 semanas",
    "recomendacion_vendedor": "Remediar antes de cierre o negociar ajuste de precio"
  },
  "certificacion_informe": {
    "analista": "IP Compliance Specialist",
    "metodos_utilizados": "AST Analysis (libsa2), Textual Similarity, SBOM Generation (SPDX)",
    "validacion_externa": "Recomendado: análisis forense independiente de módulo autenticación",
    "disclaimer": "Análisis técnico; no constituye asesoramiento legal. Requiere revisión por abogado especializado en IP."
  }
}
```

---

## Herramientas de Análisis

```python
# Análisis AST (Python)
import ast
import difflib

def ast_similarity(file1, file2):
    """Compara estructura AST de dos archivos Python"""
    with open(file1) as f1, open(file2) as f2:
        tree1 = ast.parse(f1.read())
        tree2 = ast.parse(f2.read())
    # Utilizar DECKARD (Detecting Code Clones) o similaridad de nodos AST
    return ast_node_similarity(tree1, tree2)

# Verificación de licencias
# - FOSSA: https://fossa.com (análisis SBOM/licencias)
# - Black Duck (Synopsys): escaneo de IP + vulnerabilidades
# - REUSE Software: compliance con LPI/EU standards
```

---

## Caso Práctico: M&A Fallido

**Escenario**: Acquirer evalúa startup de 50M EUR

**Hallazgos del scan**:
- 78% similitud AST con código de competidor patentado
- AGPL library sin disclosure
- 3 credenciales expuestas en Git histórico

**Resultado**: Adquisición se cancela tras 6 meses de legal review; Startup pierde 15M EUR en valuación

**Lección**: IP due diligence anticipada ahorra meses y millones
