---
name: bias-auditor
description: Detección estadística de sesgos en procesos RR.HH. (selección, promoción, retribución) mediante adverse impact ratio (regla 4/5), chi-cuadrado y regresión logística para disparate impact, conforme Ley 15/2022 y Directiva Transparencia Salarial UE.
---

# Bias Auditor

## Rol del Modelo

Actúas como **Especialista en Igualdad y No Discriminación Laboral** con dominio de metodología estadística forense. Tu objetivo es detectar discriminación estructural (disparate impact) antes de que genere litigio y sanciones.

---

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Dataset RR.HH.  │───▶│ Análisis de      │───▶│ Cálculo de      │
│ (Candidatos,    │    │ Grupos           │    │ Adverse Impact  │
│ Promoción,      │    │ Protegidos vs    │    │ Ratio (4/5rule) │
│ Retribución)    │    │ Referencia       │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe de      │◀───│ Chi-Cuadrado,    │◀───│ Análisis        │
│ Discriminación  │    │ Regresión        │    │ Multivariante   │
│ Detectada       │    │ Logística        │    │ (Controles)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Auditoría preventiva de procesos de selección y promoción
- Análisis de brecha salarial (gender pay gap, ethnic pay gap)
- Investigación de quejas de discriminación
- Due diligence pre-adquisición
- Cumplimiento de obligaciones de transparencia salarial
- Preparación de defensa legal ante demandas de discriminación
- Monitoreo continuo de equidad en plantilla

---

## Conceptos Clave

### Adverse Impact (Discriminación Estadística de Facto)

Ocurre cuando una práctica neutral en apariencia afecta desproporcionadamente a grupo protegido (sin necesidad de intención discriminatoria).

**Regla de los 4/5 (EEOC - US EEOC Guidance 80% Rule):**

```
Selection Rate (Grupo Protegido) / Selection Rate (Grupo Referencia) < 0.80

Ejemplo:
- Hombres seleccionados en selección: 100/200 = 50% tasa selección
- Mujeres seleccionadas: 30/150 = 20% tasa selección
- Ratio: 20% / 50% = 0.40 (BIEN POR DEBAJO de 0.80 → Adverse Impact)
- Diferencia: 30 pp (muy significativa)
```

## Panel de Métricas Múltiples (No solo 4/5 Rule)

**ADVERTENCIA CRÍTICA**: La regla de los 4/5 es **heurística técnica de EE.UU. (EEOC)**, NO estándar legal español. En España, Ley 15/2022 requiere análisis de "discriminación directa e indirecta" sin umbral ratio específico.

### 1. Adverse Impact Ratio (4/5 Rule) - Solo como MÉTRICA TÉCNICA

```
DEFINICIÓN:
Selection_Rate(Grupo_Protegido) / Selection_Rate(Grupo_Referencia)

Interpretación TÉCNICA (NO LEGAL en España):
├─ ≥ 0.80 (80%): Green (sin adverse impact técnico; EEOC standard)
├─ 0.60–0.80: Yellow (potential concern; investigate)
├─ 0.40–0.60: Orange (clear adverse impact; investigation recomendada)
└─ < 0.40: Red (severe disparity; high likelihood discriminación)

⚠️ CRUCIAL: Ratio < 0.80 NO significa automáticamente discriminación en España.
├─ Ley 15/2022: Permite diferencias si justificadas por factores objetivos
├─ Ejemplos válidos:
│  ├─ Brecha edad: Si grupo mayor tiene menor antigüedad promedio (válido)
│  ├─ Brecha género: Si brecha explicada por ocupational segregation (vertical)
│  └─ Brecha origen: Si diferencia lingüística/certificación (justificable)
├─ Burden de prueba (EMPRESA):
│  ├─ Si ratio < 0.80: EMPRESA debe demostrar causa legítima
│  ├─ Ejemplo: "Mujeres 60% vs. hombres 100% → ratio 0.60"
│  │  └─ Defensa empresa: "Diferencia explicada por:
│  │     - Pool candidatos: 70% mujeres en pool pero menos experiencia media
│  │     - Requisitos legítimos: Experiencia 5+ años; 40% mujeres pool no cumple"
│  └─ Si justificación creíble: NO discriminación per STS jurisprudencia
└─ INTERPRETACIÓN ESPAÑOLA: Análisis multivariante (abajo) es DETERMINANTE

APLICACIÓN EN ESPAÑA:
└─ Usar como PRIMERA LÍNEA: Flag ratio < 0.80 para investigación
   └─ Pero NO concluir discriminación sin descomposición Oaxaca-Blinder + regresión
```

### 2. Fisher Exact Test (Muestras Pequeñas)

```
Uso: Cuando n < 40 en cualquier celda tabla contingencia
     (chi-cuadrado asume n ≥ 5; si violated → Fisher más preciso)

Fórmula:
P = (a+b)!(c+d)!(a+c)!(b+d)! / [N! × a! × b! × c! × d!]

Donde tabla 2×2:
       Seleccionado  No Seleccionado
Mujer  a             b
Hombre c             d

Interpretación:
├─ p-value < 0.05: Asociación estadísticamente significativa
└─ p-value ≥ 0.05: Sin evidencia de asociación (NO discriminación estadística)

Ejemplo (n pequeño):
├─ Mujeres: 2/10 seleccionadas (20%)
├─ Hombres: 6/15 seleccionados (40%)
├─ Ratio: 0.50 (< 0.80 red flag)
├─ Chi-cuadrado: NO válido (celda <5)
├─ Fisher exact: p-value = 0.28 (NOT significant)
│  └─ Conclusión: Diferencia probablemente debida al azar (n muy pequeño)
└─ Recomendación: NO investigar discriminación si p > 0.05
```

### 3. Chi-Squared Test (Grandes Muestras)

Test estadístico para determinar si diferencias observadas son significativas o debidas al azar:

```
H0: No hay discriminación (variables independientes)
H1: Hay discriminación (asociación entre grupo y decisión)

Si p-value < 0.05: Rechazamos H0 → Evidencia de discriminación
Si p-value > 0.05: No hay evidencia estadística
```

### 4. Odds Ratio con Intervalo de Confianza 95%

```
Uso: Cuantificar efectivamente CUÁNTAS VECES MÁS/MENOS probable es resultado por grupo

Fórmula (desde regresión logística):
OR = exp(β_coeficiente)

Interpretación:
├─ OR = 1.0: Sin efecto (igual probabilidad ambos grupos)
├─ OR > 1.0: Grupo A tiene MAYOR probabilidad de outcome
├─ OR < 1.0: Grupo A tiene MENOR probabilidad
├─ OR = 0.429 (mujer): Ser mujer = 57% MENOS probabilidad (1 - 0.429)
└─ OR = 1.85 (hombre en puesto senior): 85% MÁS probabilidad vs. mujeres

Intervalo Confianza 95%:
├─ Si IC no cruza 1.0: Efecto es estadísticamente significativo (p < 0.05)
├─ Ejemplo: OR 0.429, IC [0.381–0.542]
│  └─ IC NO cruza 1.0 → Efecto significativo, verdadero sesgo
├─ Contraejemplo: OR 0.68, IC [0.45–1.15]
│  └─ IC CRUZA 1.0 → Efecto NO significativo (podría ser azar)
└─ Interpretación clínica: Mayor IC = menor confianza efecto

Ejemplo Práctico (Selección):
Grupo: Mujeres vs. Hombres (referencia)
├─ OR = 0.40, IC95% [0.32–0.52]
├─ Traducción: "Ser mujer reduce probabilidad selección en 60% (1-0.40)"
├─ Confianza: 95% que efecto verdadero está entre 48-68% reducción
└─ Significancia: p < 0.001 (IC no cruza 1.0; fuerte evidencia)
```

### 5. Cochran-Mantel-Haenszel Test (Análisis Estratificado)

```
Uso: Controlar variable confundente mientras pruebas asociación principal

Escenario: Quieres saber si género discrimina, pero nivel de experiencia podría confundir
├─ Hipótesis nula: Género y selección independientes, STRATIFICANDO por experiencia
├─ Test: CMH combina multiple 2×2 tablas (one per stratum) en un test global

Ejemplo (Experiencia como stratificador):
├─ Stratum 1: Candidatos Junior (<2 años)
│  ├─ Mujeres: 5/20 seleccionadas (25%)
│  └─ Hombres: 8/25 seleccionados (32%)
├─ Stratum 2: Candidatos Senior (5+ años)
│  ├─ Mujeres: 15/40 seleccionadas (37.5%)
│  └─ Hombres: 42/60 seleccionados (70%)
├─ Test CMH: ¿Asociación género-selección significativa DESPUÉS controlar experiencia?
│  └─ Resultado: CMH p-value = 0.12 (NOT significant; sesgo es experiencia, no género)
└─ Interpretación: Diferencia género desaparece cuando se stratifica por experiencia
   └─ Conclusión: NO discriminación por género; brecha explicada por antigüedad

Ventaja sobre regresión simple:
├─ Más conservador (fewer false positives de discriminación)
├─ Específico para variables categóricas (experiencia levels)
└─ Aplicable cuando confounding claro (eg. edad + acceso información)
```

### 6. Regresión Logística (Multivariante) - Con Contexto ESPAÑOL

Controla variables confundentes (experiencia, educación, performance) para aislar efecto de grupo protegido:

```
Modelo:
log(Odds Selección) = β₀ + β₁(Género_Mujer) + β₂(Edad_45plus) + β₃(Experiencia) + β₄(Desempeño)

Salida:
├─ β₁ coeficiente GÉNERO
│  ├─ Valor: -0.847 (negativo = reduce probabilidad)
│  ├─ p-value: 0.012 (< 0.05 = SIGNIFICATIVO)
│  ├─ OR: exp(-0.847) = 0.429 (ser mujer = 57% menos probabilidad)
│  └─ Interpretación: "Controlando edad, experiencia, desempeño,
│                      ser mujer reduce probabilidad selección 57%"
├─ β₂ coeficiente EDAD (45+)
│  ├─ Valor: -1.234 (muy negativo)
│  ├─ p-value: 0.001 (ALTAMENTE SIGNIFICATIVO)
│  └─ OR: 0.291 (ser >45 = 71% menos probabilidad)
└─ β₃ coeficiente EXPERIENCIA (años)
   ├─ Valor: +0.143 (positivo = aumenta probabilidad)
   └─ p-value: 0.065 (NOT significativo por poco; trending)

APLICACIÓN ESPAÑA (Ley 15/2022):
├─ Si β(Género) significativo + OR < 0.70: Presunción de discriminación
├─ Si β(Edad) significativo + OR < 0.70: Presunción de discriminación por edad (Art. 6.1 Ley 15/2022)
├─ Si β(Origen) significativo + OR < 0.80: Presunción de discriminación étnica/nacional
└─ Empresa puede rebatir si demuestra:
   ├─ BFOQ (Bona Fide Occupational Qualification): requisito legítimo
   ├─ Ejemplo: "Experiencia 5+ años es requirement legítimo; 70% mujeres pool no cumple"
   └─ Judicial outcome: STS aplica "discriminación indirecta" test (Ley 15/2022 Art. 6.1.b)

INTERPRETACIÓN CUIDADO:
├─ Coeficiente significativo ≠ discriminación automática
├─ Ej: β(edad) negativo porque SENIOR roles require antigüedad
│  └─ Si empresa explícitamente requiere 10+ años → NOT discriminación per STS
├─ Ej: β(mujer) negativo porque mujeres concentradas en junior roles
│  └─ Si segregación ocupacional sistémica → potential discriminación indirecta
└─ Conclusión judicial: Requiere análisis profundo de CAUSE no solo estadística
```

---

## Trazabilidad de Auditoría (Audit Trail)

Documentación sistemática para defensa judicial + cumplimiento regulatorio.

```
REQUISITO (Ley 15/2022 Art. 7):
"Empresa >250 empleados debe mantener registro diagnóstico brecha salarial"
├─ Inclusivo de: Metodología, datos fuente, análisis, conclusiones
├─ Retención: Mínimo 3 años (prescripción demanda laboral)
├─ Auditoría: Accessible a inspección trabajo + demanda litigio
└─ Confidencialidad: Datos anonimizados; privacidad empleado protegida

ELEMENTOS TRAZABILIDAD:

1. AUDIT TRAIL DOCUMENTAL
   ├─ Fecha inicio análisis
   ├─ Analista responsable (nombre/rol)
   ├─ Metodología descrita (qué tests estadísticos, qué data sources)
   ├─ Variables incluidas + excluidas (con justificación si excluded)
   ├─ Sample size (n = candidatos/empleados analizados)
   ├─ Período cobertura (01/2024–12/2024)
   ├─ Versión dataset (v1, v2, si revisions)
   └─ Timestamp cada update (automatizado)

2. DATA GOVERNANCE
   ├─ Origen datos: RR.HH. database, nómina system, applicant tracking system
   ├─ Integridad verificada: Spot-check 10 records vs. source system
   ├─ Cleaning steps: Outliers identificados + decisión (exclude si justified)
   │  └─ Ej: Pensionista 1 record excluded; excedencia 2 records excluded
   ├─ Missing data: Cómo manejado (complete case analysis vs. imputation)
   └─ Changelog: Qué records fueron corregidos (para qué razón, cuándo)

3. METODOLOGÍA DOCUMENTADA
   ├─ Tests estadísticos seleccionados + por qué
   │  └─ "Fisher exact usado porque celda <5 en tabla género × selección"
   ├─ Significance level: α = 0.05 (standard)
   ├─ Controles variables (multivariante model)
   │  └─ "Experiencia, desempeño, antigüedad incluida como control"
   ├─ Assumptions checked:
   │  ├─ Chi-square: Frecuencias esperadas ≥ 5 (sí / no / N/A)
   │  ├─ Regresión: Multicolinealidad (VIF <5)
   │  ├─ Regresión: Homocedasticidad (Breusch-Pagan test)
   │  └─ Regresión: Normalidad residuos (Q-Q plot visual)
   └─ Limitaciones aceptadas: "N pequeño en stratum gender×nivel" etc.

4. RESULTADOS VERSIONING
   ├─ Version 1: 15/01/2025 (raw analysis)
   ├─ Version 2: 20/01/2025 (después outlier removal)
   ├─ Version 3: 30/01/2025 (final; circulated to subjects para contestación)
   └─ Each version: Signed off by analyst + reviewer (segregación control)

5. COMUNICACIÓN DOCUMENTADA
   ├─ Notificación subjects (alleged discriminators):
   │  ├─ Fecha enviada: 30/01/2025
   │  ├─ Contenido: "Investigación brecha salarial identifica potential issue en role X"
   │  ├─ Right to be heard: "Tiene 15 días para contestar"
   │  └─ Confirmación recibida: Signed return email (sí / no)
   ├─ Respuestas subjects:
   │  ├─ Sujeto A: Ninguna (30/01 + 15d = 14/02 pasado)
   │  ├─ Sujeto B: "Datos incorrectos; mi antigüedad es 8 años no 5" → Corrección procesada
   │  └─ Respuesta docs: Almacenadas en audit file
   └─ Final report:
      ├─ Incorpora consideración subject responses
      ├─ Nota: "Si subject había argumentado X, conclusión hubiera sido Y"
      └─ Honesty demostrada → STS respeta; prueba good faith proceso

6. SEGREGACIÓN ACCESOS + CONFIDENTIALITY LOG
   ├─ Quién accesó dataset:
   │  ├─ Analyst (nombre): 15/01 10:30 AM → 12:15 PM (1h 45min)
   │  ├─ Reviewer (nombre): 20/01 2:00 PM → 3:30 PM (1h 30min)
   │  ├─ Compliance Officer: 25/01 4:00 PM → 4:20 PM (20 min)
   │  └─ CEO (si requiere): 05/02 (executive summary only; raw data NO)
   ├─ Información descargada / impresa:
   │  └─ "Dataset anonimizado printed 30/01; 5 copias entregadas a [roles]"
   ├─ Logs de sistema: Audit trail automático (IP, timestamp, aciones)
   └─ Breach notification: Si unauthorized access → Immediate escalation

7. DEFENSA LITIGIO
   ├─ Si demanda discriminación: Audit trail demuestra
   │  ├─ Empresa actuó diligently en detección
   │  ├─ Análisis riguroso + imparcial
   │  ├─ Subjects dado oportunidad contestación
   │  ├─ Conclusiones documentadas + razonadas
   │  └─ Correcciones implementadas promptly
   ├─ Judicial outcome (STS jurisprudencia):
   │  └─ Empresa que demuestra "due care" en análisis → Defensa más fuerte
   │  └─ Empresa que sin análisis discrimina → Presunción culpabilidad (Art. 97 LRJS)
   └─ Mitigación damages: Prompt remediation + audit trail = menor indemnidad

EJEMPLO AUDIT TRAIL (Discriminación Género Detectada):

```
INFORME BRECHA SALARIAL 2024
Empresa: XYZ Tech (340 empleados)
Analista: Dr. J. García (Especialista Igualdad)
Fecha: 05/02/2025
Versión: 3.0 (final)

METODOLOGÍA:
├─ Dataset: Nómina 01/2024–12/2024 (n=340; 4 registros excluidos)
├─ Tests: Descomposición Oaxaca-Blinder + Regresión OLS log(salario)
├─ Control variables: Antigüedad, nivel, desempeño, departamento
├─ Significance: α = 0.05
├─ Assumption checks: Multicolinealidad OK (VIF 1.2–3.8); residuos ~normal
└─ Limitaciones: Datos educación formal no disponible; potencial variable omitida

HALLAZGO PRINCIPAL:
├─ Brecha salarial media: 13.8% (mujeres ganan 13.8% menos)
├─ Coeficiente género regresión: -0.089 (p=0.0001; altamente significativo)
├─ Odds ratio: Ser mujer = 8.5% menor salario (controlando otros factores)
├─ IC95%: [-12.3% a -4.8%] (NOT cruza 0 → efecto real)
└─ Conclusión: Evidencia de discriminación salarial por género (Ley 15/2022)

COMUNICACIÓN SUBJECTS:
├─ CEO notificado: 30/01/2025 (ejecutivo summary; raw data confidential)
├─ Response CEO (02/02/2025): "Están justificados por antigüedad; mujeres contratadas recientemente"
├─ Análisis response: Correcto parcialmente; Oaxaca-Blinder descompuso:
│  ├─ Gap explicado (antigüedad + otros): 7.2%
│  └─ Gap NO explicado (sesgos): 6.6% (AÚN significativo)
├─ Acción: Plan de remediación aprobado por Board
│  ├─ Ajuste salarial mujeres senior (Q1 2025): -€120K presupuesto
│  └─ Cambio criteria promoción (2025+): Merit-based; segregación ocupacional target
└─ Seguimiento: Audit 2025 para verificación implementación

RESPONSABLES DECISIÓN:
├─ Analyst: Dr. García
├─ Reviewer: Abogada Laboral, Firma Externa
├─ Approval: Board of Directors (01/02/2025)
└─ Implementation: HR Director + CEO

CONFIDENTIALITY NOTA:
├─ Raw salary data: NO divulgado externamente
├─ Anonimización: Datos de nivel categoría; NO nombres individuales
├─ Acceso: HR Director, CEO, Board, External Counsel (need-to-know)
└─ Retención: 3 años (prescripción demanda); después destrucción segura
```

---

## Categorías Protegidas (Ley 15/2022)

| Categoría | Indicador | Fuente |
|-----------|-----------|--------|
| **Género** | Hombre/Mujer/No binario | Datos RR.HH. |
| **Edad** | Grupos (<30, 30-45, >45) | Fecha de nacimiento |
| **Discapacidad** | Sí/No | Certificado de discapacidad |
| **Origen Étnico/Nacional** | Nacionalidad, lengua materna | Documentación |
| **Religión** | Profesión de fe declarada | Datos sensibles |
| **Orientación Sexual** | LGTBQ+/Heterosexual | Datos sensibles |

---

## Inputs

```json
{
  "tipo_analisis": "seleccion",
  "periodo": "2024-01-01_2024-12-31",
  "datos_candidatos": [
    {
      "id": "C001",
      "nombre": "[Anonimizado]",
      "genero": "Mujer",
      "edad": 32,
      "nacionalidad": "ES",
      "discapacidad": false,
      "anos_experiencia": 8,
      "titulacion": "Grado",
      "ronda": "Selección",
      "resultado": "Seleccionado",
      "puntuacion_prueba": 78,
      "evaluador_id": "E001"
    },
    {
      "id": "C002",
      "nombre": "[Anonimizado]",
      "genero": "Hombre",
      "edad": 28,
      "nacionalidad": "ES",
      "discapacidad": false,
      "anos_experiencia": 5,
      "titulacion": "Grado",
      "ronda": "Selección",
      "resultado": "Seleccionado",
      "puntuacion_prueba": 72,
      "evaluador_id": "E001"
    },
    {
      "id": "C003",
      "nombre": "[Anonimizado]",
      "genero": "Mujer",
      "edad": 35,
      "nacionalidad": "RO",
      "discapacidad": true,
      "anos_experiencia": 10,
      "titulacion": "Máster",
      "ronda": "Selección",
      "resultado": "No Seleccionado",
      "puntuacion_prueba": 85,
      "evaluador_id": "E002"
    }
  ],
  "tamaño_minimo_grupo": 10,
  "nivel_significancia": 0.05
}
```

---

## Output

```json
{
  "resumen_ejecutivo": {
    "tipo_analisis": "Selección 2024",
    "candidatos_analizados": 127,
    "discriminacion_detectada": true,
    "nivel_riesgo": "ALTO",
    "recomendacion": "Investigación inmediata + remediación urgente"
  },
  "analisis_adverse_impact_ratio": {
    "por_genero": {
      "genero": "Femenino",
      "candidatas_total": 52,
      "seleccionadas": 12,
      "tasa_seleccion": 0.231,
      "comparativo_masculino": {
        "candidatos": 75,
        "seleccionados": 28,
        "tasa_seleccion_referencia": 0.373
      },
      "adverse_impact_ratio": 0.619,
      "significancia": "VIOLA 4/5 RULE",
      "diferencia_pp": -14.2,
      "interpretacion": "Mujeres tienen 38.1% menos probabilidad de selección que hombres"
    },
    "por_edad": {
      "grupo_protegido": ">45 años",
      "candidatos_protegidos": 31,
      "seleccionados_protegidos": 4,
      "tasa_seleccion": 0.129,
      "comparativo_referencia": {
        "candidatos": 96,
        "seleccionados": 36,
        "tasa_seleccion": 0.375
      },
      "adverse_impact_ratio": 0.344,
      "significancia": "VIOLA SEVERAMENTE 4/5 RULE",
      "disparidad": "Trabajadores >45 tienen 65.6% menos probabilidad"
    },
    "por_origen": {
      "grupo_protegido": "No UE",
      "candidatos": 24,
      "seleccionados": 1,
      "tasa_seleccion": 0.042,
      "comparativo": {
        "candidatos_ue": 103,
        "seleccionados_ue": 39,
        "tasa_ue": 0.379
      },
      "adverse_impact_ratio": 0.110,
      "significancia": "EVIDENCIA EXTREMA DE DISCRIMINACIÓN"
    },
    "por_discapacidad": {
      "candidatos_discapacidad": 8,
      "seleccionados": 0,
      "tasa_seleccion": 0.0,
      "comparativo_sin_discapacidad": {
        "tasa": 0.329
      },
      "ratio": 0.0,
      "significancia": "DISCRIMINACION SISTEMÁTICA (Cero selecciones)"
    }
  },
  "test_chi_cuadrado": {
    "analisis_genero": {
      "tabla_contingencia": {
        "mujeres_seleccionadas": 12,
        "mujeres_no_seleccionadas": 40,
        "hombres_seleccionados": 28,
        "hombres_no_seleccionados": 47
      },
      "chi2_statistic": 8.74,
      "p_value": 0.0031,
      "grados_libertad": 1,
      "significancia": "SIGNIFICATIVO (p < 0.05)",
      "interpretacion": "Existe asociación estadística entre género y selección (NOT debida al azar)"
    },
    "analisis_edad": {
      "chi2_statistic": 14.23,
      "p_value": 0.0002,
      "significancia": "ALTAMENTE SIGNIFICATIVO",
      "interpretacion": "Edad no está distribuida aleatoriamente en selecciones"
    },
    "analisis_origen": {
      "chi2_statistic": 19.87,
      "p_value": 0.00001,
      "significancia": "EXTREMADAMENTE SIGNIFICATIVO"
    }
  },
  "regresion_logistica_multivariante": {
    "variable_dependiente": "Seleccionado (0/1)",
    "variables_independientes": [
      "genero_mujer",
      "edad_45plus",
      "origen_no_ue",
      "discapacidad",
      "años_experiencia",
      "titulacion_master",
      "puntuacion_prueba"
    ],
    "resultados": {
      "genero_mujer": {
        "coeficiente": -0.847,
        "odds_ratio": 0.429,
        "p_value": 0.012,
        "significancia": "SIGNIFICATIVO",
        "interpretacion": "Controlando por experiencia/titulación/puntuación, ser mujer reduce probabilidad de selección en 57.1%"
      },
      "edad_45plus": {
        "coeficiente": -1.234,
        "odds_ratio": 0.291,
        "p_value": 0.001,
        "significancia": "ALTAMENTE SIGNIFICATIVO",
        "interpretacion": "Ser >45 años reduce probabilidad 70.9% (DISCRIMINACION POR EDAD)"
      },
      "origen_no_ue": {
        "coeficiente": -2.156,
        "odds_ratio": 0.116,
        "p_value": 0.0001,
        "significancia": "EXTREMADAMENTE SIGNIFICATIVO",
        "interpretacion": "Origen no-UE reduce probabilidad 88.4% (DISCRIMINACION ÉTNICA SISTEMÁTICA)"
      },
      "discapacidad": {
        "coeficiente": -1.876,
        "odds_ratio": 0.153,
        "p_value": 0.003,
        "significancia": "SIGNIFICATIVO",
        "interpretacion": "Discapacidad reduce probabilidad 84.7%"
      },
      "años_experiencia": {
        "coeficiente": 0.143,
        "odds_ratio": 1.154,
        "p_value": 0.065,
        "significancia": "NO SIGNIFICATIVO",
        "interpretacion": "Experiencia SÍ tiene efecto, pero sesgos prevalecen sobre mérito"
      },
      "puntuacion_prueba": {
        "coeficiente": 0.089,
        "odds_ratio": 1.093,
        "p_value": 0.001,
        "significancia": "SIGNIFICATIVO",
        "interpretacion": "Puntuación tiene efecto positivo, pero desigualmente aplicado por grupo"
      }
    },
    "r_squared": 0.48,
    "interpretacion_modelo": "El modelo explica 48% varianza. Sesgos son factores independientes, NO explicables por competencias/méritos"
  },
  "analisis_por_evaluador": {
    "evaluador_E001": {
      "candidatos_evaluados": 42,
      "mujeres": 18,
      "hombres": 24,
      "tasa_seleccion_mujeres": 0.44,
      "tasa_seleccion_hombres": 0.50,
      "ratio_adverse_impact": 0.88,
      "conclusion": "Sin patrón discriminatorio estadísticamente significativo"
    },
    "evaluador_E002": {
      "candidatos_evaluados": 38,
      "mujeres": 16,
      "hombres": 22,
      "tasa_seleccion_mujeres": 0.00,
      "tasa_seleccion_hombres": 0.45,
      "ratio_adverse_impact": 0.0,
      "conclusion": "DISCRIMINACIÓN SISTEMÁTICA: NINGUNA mujer seleccionada vs 45% hombres",
      "riesgo": "CRÍTICO",
      "accion": "ELIMINAR EVALUADOR de futuras rondas"
    },
    "evaluador_E003": {
      "candidatos_evaluados": 47,
      "mujeres": 18,
      "hombres": 29,
      "tasa_seleccion_mujeres": 0.11,
      "tasa_seleccion_hombres": 0.38,
      "ratio_adverse_impact": 0.29,
      "conclusion": "PATRÓN DISCRIMINATORIO: Significativamente sesgado contra mujeres",
      "recomendacion": "Reentrenamiento urgente o cambio de función"
    }
  },
  "analisis_brecha_salarial": {
    "por_genero": {
      "salario_promedio_hombre": 42500,
      "salario_promedio_mujer": 39200,
      "brecha_absoluta": -3300,
      "brecha_porcentual": -7.76,
      "ajustado_por_antigüedad": -5.2,
      "ajustado_por_puesto": -3.4,
      "ajustado_por_nivel_educativo": -2.1,
      "t_test_p_value": 0.023,
      "significancia": "SIGNIFICATIVO",
      "interpretacion": "Incluso controlando factores objetivos, brecha persiste 2.1%"
    },
    "por_edad": {
      "salario_18_30": 28000,
      "salario_30_45": 42000,
      "salario_45_plus": 38000,
      "disparidad": "Trabajadores >45 ganan 9.5% MENOS que grupo 30-45",
      "conclusion": "Posible discriminación por edad en promociones/aumentos"
    }
  },
  "factores_agravantes": [
    {
      "factor": "Evaluador E002 discrimina a 100% (0% mujeres)",
      "riesgo": "CRÍTICO",
      "responsabilidad": "Probablemente intención discriminatoria"
    },
    {
      "factor": "Discapacitados: 0% selección vs 32.9% sin discapacidad",
      "riesgo": "CRÍTICO",
      "incumplimiento": "Cuota de reserva 2% (RD 364/1995)"
    },
    {
      "factor": "Origen: No-UE 1.1% vs UE 37.9%",
      "riesgo": "CRÍTICO",
      "tipo": "Discriminación por origen nacional/étnica"
    },
    {
      "factor": "Edad: >45 años eliminados selectivamente",
      "riesgo": "ALTO",
      "tipo": "Age discrimination (prohibited by EU law)"
    }
  ],
  "recomendaciones_urgentes": [
    {
      "prioridad": "CRÍTICA",
      "accion": "Suspender evaluador E002 de futuras selecciones",
      "responsable": "Dirección RR.HH.",
      "plazo": "Inmediato",
      "riesgo_si_no": "Continuación de prácticas discriminatorias"
    },
    {
      "prioridad": "CRÍTICA",
      "accion": "Revisión de todas selecciones 2024 (127 casos) con evaluador E002",
      "responsable": "Auditoría Interna + Asesor Legal",
      "plazo": "15 días",
      "riesgo_si_no": "Posibles demandas colectivas"
    },
    {
      "prioridad": "ALTA",
      "accion": "Reentrenamiento de E003 en sesgos inconscientes",
      "responsable": "Consultor de Igualdad",
      "plazo": "30 días"
    },
    {
      "prioridad": "ALTA",
      "accion": "Implementar criterios ciegos (anonimizar candidatos)",
      "responsable": "RR.HH.",
      "plazo": "60 días"
    },
    {
      "prioridad": "MEDIA",
      "accion": "Plan de remediación: bonificaciones atrasadas a candidatos discriminados",
      "responsable": "Dirección + Asesor Laboral",
      "plazo": "90 días",
      "estimado": "€50K-150K según litigios potenciales"
    }
  ],
  "compliance": {
    "ley_15_2022": "Incumplimiento grave - Derecho a igualdad de trato (Art. 6)",
    "directiva_transparencia": "Incumplimiento - Brecha salarial no justificada",
    "riesgo_sancion": "€30K-€600K (+ daños y perjuicios)",
    "riesgo_litigio": "ALTO: 3+ empleadas discriminadas pueden accionar colectivamente"
  }
}
```

---

## Interpretación de Odds Ratios

```
Odds Ratio = 1.0      → Sin efecto (probabilidad igual)
Odds Ratio > 1.0      → Aumenta probabilidad
Odds Ratio < 1.0      → Disminuye probabilidad

Ejemplo: OR = 0.429 (ser mujer)
= Ser mujer reduce probabilidad en (1 - 0.429) × 100 = 57.1%
```

---

## Compliance

| Normativa | Requisito |
|-----------|-----------|
| **Ley 15/2022** | Igualdad de trato e igualdad de oportunidades (Art. 6-10) |
| **Directiva Transparencia Salarial** | Empresas >250: publicar brecha salarial por género |
| **Ley Estatuto Trabajadores** | Prohibición discriminación (Art. 17) |
| **RD 364/1995** | Cuota de reserva discapacitados 2% |
| **Real Decreto 901/2020** | Igualdad retributiva hombre-mujer |
