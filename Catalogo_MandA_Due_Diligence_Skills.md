# CATÁLOGO DE DUE DILIGENCE LEGAL EN M&A

## Especificación Funcional, Legal y Técnica — Cinco Skills Clave

**Versión 1.0 — Febrero 2026**
**CONFIDENCIAL — Uso interno**

---

## Tabla de Contenidos

1. [Introducción y Alcance](#1-introducción-y-alcance)
2. [Requisitos Transversales](#2-requisitos-transversales)
3. [SKILL 1: Contracts CoC & Consents Mapper](#3-skill-1-contracts-coc--consents-mapper)
4. [SKILL 2: Contingencies & Off-Balance Harvester](#4-skill-2-contingencies--off-balance-harvester)
5. [SKILL 3: Regulatory & FDI Notifications Planner](#5-skill-3-regulatory--fdi-notifications-planner)
6. [SKILL 4: People & Labor Exposure Analyzer](#6-skill-4-people--labor-exposure-analyzer)
7. [SKILL 5: Privacy, Cyber & IT Readiness Scanner](#7-skill-5-privacy-cyber--it-readiness-scanner)
8. [Anexo: Verificación de Referencias Normativas](#8-anexo-verificación-de-referencias-normativas)

---

## 1. Introducción y Alcance

El presente documento constituye la especificación funcional, legal y técnica detallada de cinco skills orientadas a due diligence legal en procesos de M&A, diseñadas para una gran firma legal en España. Estas skills abordan los "trabajos pesados y repetitivos" típicos de una due diligence compradora, automatizando las tareas de mayor volumen documental sin sustituir el juicio profesional del abogado.

Las cinco skills cubren los siguientes streams de due diligence: contratos y consentimientos (cambio de control), contingencias y obligaciones fuera de balance, regulatorio e inversiones extranjeras (FDI), laboral y recursos humanos, y privacidad, ciberseguridad y tecnología.

Cada ficha incluye: propósito, usuarios objetivo, alcance legal con referencias normativas verificadas, datos de entrada y salida, lógica y arquitectura, controles de calidad y compliance, KPIs, riesgos y plan de pruebas.

### Metodología de Verificación

Todas las referencias normativas citadas han sido verificadas individualmente contra fuentes oficiales (BOE, EUR-Lex, IASB, CNMC). Se ha comprobado la existencia, título oficial, fecha de publicación, referencia BOE y contenido clave de cada norma. Las verificaciones se documentan en el Anexo A de este documento. Se ha identificado una corrección relevante: el RD 664/1999 sobre inversiones exteriores ha sido derogado y sustituido por el RD 571/2023 (en vigor desde 01/09/2023).

---

## 2. Requisitos Transversales

Estas cinco skills comparten los siguientes requisitos comunes que deben implementarse de forma homogénea:

### 2.1 Gobierno de Datos y Seguridad

- **Control de accesos por rol (RBAC):** Roles diferenciados de preparador, revisor y socio/partner con permisos granulares por carpeta y tipo de documento. Acceso basado en necesidad de conocimiento (need-to-know), con segregación por deal y por stream de DD.
- **Cifrado:** AES-256 en reposo y TLS 1.3 en tránsito. Claves gestionadas en HSM (Hardware Security Module) o KMS cloud certificado.
- **Registros inmutables de evidencias:** Cada acción (lectura, extracción, clasificación, modificación) genera un registro con hash SHA-256, timestamp, usuario y acción realizada. Retención mínima conforme a obligaciones de custodia profesional (mínimo 6 años conforme al art. 30 del Código de Comercio, o superior si aplica normativa sectorial).
- **Entornos de revisión segregados:** Sandboxes aislados por deal. Sin acceso cruzado entre deals activos. Destrucción segura al cierre del mandato conforme a instrucciones del cliente.
- **Conformidad con RGPD/LOPDGDD:** Minimización de datos personales, base de legitimación documentada (interés legítimo del adquirente en la DD), seudonimización cuando sea factible, evaluación de impacto si se procesan datos especiales.

### 2.2 Explicabilidad (Explainability)

- Cada hallazgo o resultado enlaza directamente al fragmento documental fuente (página, párrafo, cláusula) y a la regla de extracción o clasificación aplicada.
- Posibilidad de override justificado: el revisor puede reclasificar un hallazgo con registro de la justificación y el criterio alternativo.
- Trazabilidad completa: cadena desde documento fuente → extracción → clasificación → scoring → hallazgo → recomendación.

### 2.3 Orquestación e Integración

- Integración bidireccional con el data room virtual (Datasite, Intralinks, Firmex, etc.): ingesta automática de nuevos documentos y actualización de índices.
- Conexión con el case management del deal para convertir hallazgos en issues con owner, prioridad y fecha objetivo.
- API REST para integración con herramientas de gestión del deal (deal tracker, checklists de closing conditions, SPA negotiation tools).
- Webhooks para notificaciones en tiempo real de nuevos hallazgos críticos.

### 2.4 Versionado Temporal

- Capacidad de congelar "cortes" de DD por fecha para trazabilidad con versiones del SPA y disclosure schedules.
- Cada corte genera un snapshot inmutable del estado de todos los hallazgos, clasificaciones y recomendaciones.
- Comparación diff entre cortes para identificar cambios entre iteraciones de negociación.
- Vinculación directa entre hallazgos y cláusulas específicas del SPA (R&Ws, indemnidades, condiciones suspensivas, escrows).

### 2.5 Entregables

- **Dashboards ejecutivos por stream** (Legal/Regulatorio/Laboral/IT): vista consolidada de hallazgos por severidad, estado de resolución, y evolución temporal.
- **Paquetes de soporte** listos para anexar a informes de DD: red flags, tablas de issues, recomendaciones priorizadas.
- **Materiales de negociación:** Inputs directos para negociación de R&Ws (representations & warranties), indemnidades específicas, escrows, y condiciones suspensivas/resolutivas.
- **Formatos de exportación:** PDF (informe final), Excel (matrices de datos), Word (secciones para DD report), PowerPoint (resumen ejecutivo para comité de inversión).

---

## 3. SKILL 1: Contracts CoC & Consents Mapper

**Cambio de control, cesiones, exclusividades y consentimientos**

### 3.1 Propósito

Automatizar la lectura masiva de contratos en un data room para detectar cláusulas de cambio de control (CoC), prohibiciones de cesión (anti-assignment), exclusividades, cláusulas MFN (Most Favoured Nation), terminaciones por cambio de control, preavisos obligatorios, cláusulas de no competencia y non-solicit, y construir el plan integral de consentimientos y notificaciones del deal. El objetivo es reducir drásticamente el tiempo de revisión contractual masiva (típicamente cientos o miles de contratos) sin comprometer la exhaustividad, garantizando que ningún consentimiento crítico quede sin identificar antes del signing o closing.

El plan de consentimientos generado debe incluir la secuencia temporal óptima (qué notificaciones enviar en signing vs. closing, cuáles requieren respuesta activa vs. mero aviso), las plantillas de comunicación adaptadas a cada tipo de cláusula, y la identificación de los "deal-breakers" (contratos cuyo consentimiento es condición suspensiva o cuya pérdida tendría impacto material).

### 3.2 Usuarios Objetivo

| Área | Perfil y Necesidad |
|------|-------------------|
| M&A / Corporate | Lideran la DD contractual. Necesitan la matriz de consentimientos para negociar condiciones suspensivas en el SPA y disclosure schedules. |
| Financiero / Banca de Inversión | Evalúan el impacto de cláusulas de CoC en la valoración: contratos clave que podrían perderse, ingresos en riesgo, costes de waiver. |
| Operaciones Post-Closing | Ejecutan el plan de consentimientos tras el signing. Necesitan templates, cronograma y tracking de obtención. |
| Asesoría Legal de la Target | Colaboran en la identificación de contratos y facilitan el acceso a contrapartes para waivers. |
| Comité de Inversión | Reciben el resumen ejecutivo de riesgos contractuales para la decisión de go/no-go. |

### 3.3 Alcance Legal y Referencias Normativas

#### 3.3.1 Derecho Civil y Mercantil de Contratos

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **Código Civil (arts. 1112, 1205, 1255)** | Art. 1255: libertad contractual (pacta sunt servanda) — las cláusulas de CoC y anti-assignment son válidas en tanto no contravengan la ley, la moral o el orden público. Art. 1112: transmisibilidad general de derechos. Art. 1205: novación de obligaciones requiere consentimiento del acreedor cuando cambia el deudor. |
| **Código de Comercio** | RD de 22 de agosto de 1885, según enmendado. Regula contratos mercantiles. Aplicable a contratos comerciales de la target (distribución, suministro, franquicia). |
| **RDL 1/2010 (Ley de Sociedades de Capital)** | BOE-A-2010-10544. Relevante para: transmisión de participaciones/acciones con restricciones estatutarias (derechos de adquisición preferente, autorización del órgano de administración), pactos parasociales que limitan la transmisibilidad, y cambio de control indirecto cuando la target es sociedad participada. |

#### 3.3.2 Normativa Sectorial Relevante

| Sector | Norma | Impacto en CoC |
|--------|-------|---------------|
| Arrendamientos urbanos | Ley 29/1994 (LAU) | Art. 32: cesión y subarriendo de locales de negocio requiere consentimiento del arrendador salvo pacto en contrario. Art. 34: derechos del arrendatario en caso de enajenación de la finca. |
| Financiación | Contratos de crédito sindicado (LMA estándar) | Cláusulas de CoC típicas: mandatory prepayment, eventos de default, consent requirements para cambio de control del prestatario. |
| Licencias de propiedad intelectual | Ley de Propiedad Intelectual (RDL 1/1996) y Ley 24/2015 (Patentes) | Cesión de licencias puede requerir consentimiento del licenciante según términos contractuales. |
| Concesiones administrativas | Ley 9/2017 (Contratos del Sector Público) | Art. 214 y ss.: cesión de contratos públicos requiere autorización del órgano de contratación. Cambio de control del contratista puede requerir notificación. |
| Subvenciones | Ley 38/2003 (General de Subvenciones) | Cambio de control puede constituir causa de reintegro si altera las condiciones que motivaron la concesión. |

#### 3.3.3 Derecho Laboral (intersección)

| Norma | Relevancia |
|-------|-----------|
| **Estatuto de los Trabajadores (RDL 2/2015), art. 44** | BOE-A-2015-11430. Sucesión de empresa: subrogación automática de trabajadores y obligaciones laborales. Aplica en transmisión de unidad productiva autónoma, no necesariamente en share deal puro (pero sí en asset deal o fusión). |

### 3.4 Datos de Entrada

| Categoría | Detalle | Formato esperado |
|-----------|---------|-----------------|
| Data room de contratos | Contratos comerciales (distribución, suministro, servicios, franquicia), contratos de financiación (créditos, pólizas, bonos), arrendamientos (locales, oficinas, naves), licencias (IP, software, marca), JV y acuerdos de accionistas. | PDF, DOCX, escaneados (OCR) |
| Metadatos contractuales | Fechas (firma, inicio, vencimiento, renovación automática), importes (valor anual, acumulado, mínimos garantizados), contrapartes (nombre, NIF/CIF, jurisdicción), estado (vigente, en negociación, terminado). | CSV, Excel, API del data room |
| Organigrama de la target | Estructura societaria completa: matriz, filiales, participaciones, jurisdicciones. Necesario para identificar cambio de control directo e indirecto. | PDF, Excel, diagrama |
| SPA en negociación (si disponible) | Borrador del contrato de compraventa: condiciones suspensivas, disclosure schedules, definición de "cambio de control" pactada. | DOCX |
| Contratos priorizados por management | Lista de contratos que la target considera "materiales" o "top clients/suppliers". | Excel |

### 3.5 Salidas

#### 3.5.1 Matriz Principal de Consentimientos

Tabla por contrato con los siguientes campos:

| Campo | Descripción |
|-------|------------|
| ID contrato | Identificador único, enlace a documento fuente |
| Contraparte | Nombre, NIF, jurisdicción |
| Tipo de cláusula detectada | CoC directo, CoC indirecto, anti-assignment, exclusividad, MFN, non-solicit, non-compete, terminación por conveniencia, interlocking |
| Texto exacto de la cláusula | Fragmento literal extraído, con página y párrafo |
| Criticidad (scoring) | Alta (deal-breaker) / Media (impacto material) / Baja (riesgo residual). Basado en valor del contrato, cliente clave, plazo corto de preaviso |
| Lead-time de aviso | Días de preaviso requeridos para notificación |
| Derecho de terminación | ¿La contraparte puede terminar por el CoC? Sí/No/Condicional |
| Condiciones para waiver | Qué se requiere para obtener la renuncia al derecho de terminación |
| Timing (signing vs. closing) | ¿La notificación/consentimiento debe obtenerse antes de signing, entre signing y closing, o post-closing? |
| Owner | Responsable de gestionar la obtención del consentimiento |
| Estado | Pendiente / En gestión / Obtenido / Denegado / No aplica |

#### 3.5.2 Plan de Consentimientos y Cronograma

- **Cronograma Gantt** con dependencias: qué consentimientos deben obtenerse secuencialmente (ej. lender consent antes de notificación a clientes).
- **Ruta crítica:** Identificación de los consentimientos que están en la ruta crítica del deal (condiciones suspensivas del SPA).
- **Plantillas de notificación** adaptadas por tipo de cláusula: notificación simple, solicitud de waiver, solicitud de consentimiento activo, comunicación de no-objeción.
- **Tracking dashboard:** Estado en tiempo real de cada consentimiento.

#### 3.5.3 Análisis de Riesgo Contractual

- **Impacto financiero estimado:** Ingresos/costes asociados a contratos con riesgo de terminación.
- **Concentración de riesgo:** Análisis Pareto de contratos por valor (top 20 contratos = X% del ingreso).
- **Input para SPA:** Recomendaciones para cláusulas de R&W, indemnidades específicas, y condiciones suspensivas.

### 3.6 Lógica y Motor de Reglas

#### 3.6.1 Pipeline de Procesamiento

```
Ingesta (OCR/PDF) → Parsing → Segmentación de cláusulas → Clasificación NLP →
Scoring de criticidad → Deduplicación → Grafo de dependencias → Plan de consentimientos
```

**Paso 1 — Ingesta y OCR:** Procesamiento de documentos del data room. OCR para escaneados (Tesseract + modelos especializados para contratos). Conversión a texto estructurado con preservación de formato (tablas, anexos, side letters).

**Paso 2 — Segmentación de cláusulas:** Identificación de secciones contractuales por patrones (headings, numeración, términos clave). Aislamiento de cláusulas individuales como unidades de análisis.

**Paso 3 — Clasificación NLP:** Modelo de clasificación multicategoría entrenado para detectar:
- **CoC directo:** "cambio de control", "change of control", "transmisión de acciones/participaciones", "modificación sustancial del accionariado"
- **CoC indirecto:** "control directo o indirecto", "cambio en la persona que en última instancia controla", "ultimate beneficial owner"
- **Anti-assignment:** "prohibición de cesión", "no podrá ceder ni transmitir", "assignment prohibited"
- **Exclusividad:** "exclusiva", "exclusive", "derecho preferente", "first refusal"
- **MFN:** "nación más favorecida", "most favoured nation", "condiciones no menos favorables"
- **Non-solicit / Non-compete:** "no competencia", "no captación", "non-solicitation"
- **Terminación por conveniencia:** "resolución anticipada", "terminación sin causa", "termination for convenience"
- **Preaviso:** "con un preaviso de", "notificación previa de X días/meses"

**Paso 4 — Scoring de criticidad:** Fórmula multifactorial:
- Valor del contrato (% sobre ingresos totales de la target)
- Clasificación del cliente/proveedor (clave / estratégico / estándar)
- Plazo de preaviso (corto = mayor riesgo)
- Sustituibilidad de la contraparte (alta / media / baja)
- Impacto en covenants financieros
- Presencia de penalización económica por terminación

**Paso 5 — Deduplicación:** Agrupación de contratos relacionados (master agreement + addenda + side letters) para evitar doble conteo y garantizar análisis integral del grupo contractual.

**Paso 6 — Grafo de dependencias:** Modelización de dependencias entre consentimientos: ej. el consentimiento del pool bancario puede ser prerequisito para notificar a clientes (para evitar trigger de default bajo los covenants).

**Paso 7 — Plan de consentimientos:** Cálculo de la ruta crítica temporal, asignación de owners, generación de templates.

#### 3.6.2 Diccionarios Sectoriales

Diccionarios especializados por tipo de contrato para mejorar la detección en redacciones atípicas:
- **Financiación:** Diccionario LMA (Loan Market Association) con terminología estándar de facility agreements.
- **Inmobiliario:** Terminología LAU y arrendamientos comerciales.
- **Tecnología:** Cláusulas de licencia, SaaS, escrow de código fuente.
- **Distribución/Franquicia:** Exclusividad territorial, MFN, non-compete post-terminación.

### 3.7 Arquitectura Técnica

| Capa | Descripción |
|------|------------|
| **Ingesta (OCR/PDF→parsing)** | Motor OCR multilenguaje (ES/EN/FR/PT). Parser de documentos con detección de estructura (secciones, anexos, firmas). Indexación full-text con Elasticsearch. Capacidad: procesamiento de 500+ contratos/hora. |
| **Modelo de clasificación de cláusulas** | Modelo NLP fine-tuned sobre corpus de contratos M&A españoles. Clasificación multicategoría con confidence score. Soporte para español e inglés. Reentrenamiento periódico con feedback de revisores (active learning). |
| **Grafo de dependencias** | Base de datos de grafos (Neo4j o similar): nodos = contratos y contrapartes, aristas = dependencias y relaciones. Cálculo de ruta crítica con algoritmo de programación lineal. |
| **Orquestador de tareas** | Workflows de firma/notificación con estados (pendiente, en gestión, obtenido, denegado). Integración con email/CRM para seguimiento. Alertas de vencimiento de plazos. |
| **Generador documental** | Templates parametrizables de notificaciones y solicitudes de waiver. Generación en Word/PDF con datos del contrato y la cláusula insertados automáticamente. |
| **Dashboard** | Panel de control con vista por deal: matriz de consentimientos, Gantt de ruta crítica, KPIs de cobertura y estado. Drill-down a documento fuente. |

### 3.8 Controles de Calidad y Compliance

- **Evidencias de lectura y extracción:** Cada documento procesado genera un log con: timestamp de ingesta, hash del documento, resultado de OCR (confidence), cláusulas detectadas con confidence score.
- **Revisión humana obligatoria en top-N contratos:** Los N contratos de mayor criticidad (configurado por deal, típicamente top 20-50) requieren revisión humana completa antes de cerrar el análisis. El sistema marca estos contratos y no permite cerrar el stream sin la revisión.
- **Control de versiones de redlines:** Si un contrato se actualiza en el data room (nueva versión o redline), el sistema detecta el cambio, reprocesa y genera un diff de hallazgos.
- **Segregación por carpeta sensible:** Contratos sujetos a privilegio profesional o restricciones de acceso (clean team / dirty team) gestionados en entornos segregados.
- **Four-eyes principle:** Ningún hallazgo de criticidad "Alta" se cierra sin validación de un segundo revisor.

### 3.9 KPIs de Rendimiento

| KPI | Objetivo | Método de medición |
|-----|----------|-------------------|
| % contratos revisados con extracción completa | ≥ 99% del data room | Contratos procesados / Contratos en data room |
| TAT por contrato crítico | ≤ 4 horas desde ingesta hasta hallazgo revisado | Timestamp ingesta → timestamp aprobación |
| Precisión de clasificación de cláusulas | ≥ 95% (validado en muestreo QA) | Muestreo aleatorio estratificado, revisión humana |
| Nº consentimientos obtenidos antes de closing | ≥ 100% de condiciones suspensivas | Tracking del plan de consentimientos |
| Reducción de hallazgos tardíos | ≥ 90% vs. proceso manual baseline | Hallazgos post-closing en deal actual vs. deals anteriores |
| Tasa de falsos negativos | < 2% en contratos con CoC | Muestreo de control en contratos "sin hallazgos" |

### 3.10 Riesgos y Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|-----------|
| Falsos negativos en redacciones atípicas | Media | Muy Alto | Diccionarios sectoriales actualizables. Active learning con feedback de revisores. Muestreo estratificado de control (5% de contratos "limpios" revisados manualmente). |
| Contratos escaneados con baja calidad OCR | Alta | Alto | Pipeline de mejora de imagen (deskew, denoising, contrast). Umbral mínimo de confidence OCR: documentos por debajo se marcan para revisión manual. |
| Side letters o addenda no indexadas | Media | Alto | Reglas de deduplicación que vinculan addenda al master agreement. Alerta cuando se detecta referencia a documento no presente en el data room. |
| Idiomas múltiples en contratos internacionales | Media | Medio | Soporte multilingüe (ES/EN/FR/PT/DE). Marcado automático de contratos en idiomas no soportados para revisión manual. |
| Volumen excesivo de contratos (>10.000) | Baja | Medio | Procesamiento en batch con priorización por valor/criticidad. Escalado horizontal de la infraestructura. |

### 3.11 Plan de Pruebas

#### Caso 1: CoC implícitos
Contrato de distribución con cláusula que no usa la expresión "cambio de control" pero establece que "cualquier modificación en la composición accionarial que altere la persona que ejerce el control efectivo" genera derecho de terminación. Verificar: detección correcta como CoC indirecto; scoring adecuado.

#### Caso 2: Need-to-consent solo para cesión
Contrato de arrendamiento donde la cesión requiere consentimiento del arrendador, pero no hay cláusula de CoC. En un share deal no se activa; en un asset deal, sí. Verificar: clasificación correcta como anti-assignment (no CoC); marcado diferenciado según estructura del deal.

#### Caso 3: Cláusulas escalonadas (notificación + no-objeción)
Contrato de financiación sindicada con mecanismo de consentimiento en dos fases: notificación con 30 días de antelación, seguida de periodo de no-objeción de 15 días. Si hay objeción, mandatory prepayment. Verificar: detección de ambas fases; cálculo correcto de lead-time total (45 días); clasificación como criticidad alta.

#### Caso 4: Evergreen con aviso mínimo
Contrato de servicios con renovación automática anual y preaviso de terminación de 60 días antes del vencimiento anual. CoC genera derecho a no renovar. Verificar: cálculo correcto de la próxima ventana de aviso; alerta si el closing cae fuera de ventana.

#### Caso 5: Side letters modificando el contrato principal
Master agreement sin CoC, pero side letter firmada 2 años después que añade cláusula de CoC con consent requirement. Verificar: vinculación correcta de la side letter al master; detección del CoC añadido; no duplicación en la matriz.

#### Caso 6: Contratos en múltiples idiomas
Grupo de contratos del mismo proveedor: master en inglés, addendum en español, side letter en francés. Verificar: procesamiento correcto de los tres idiomas; consolidación en un único grupo contractual; extracción coherente.

---

## 4. SKILL 2: Contingencies & Off-Balance Harvester

**Garantías, avales, rentas, compromisos ocultos y obligaciones fuera de balance**

### 4.1 Propósito

Localizar, clasificar y cuantificar de forma sistemática las obligaciones fuera de balance y contingencias relevantes de la target que podrían impactar la valoración, la estructura del deal o las obligaciones post-closing. El alcance incluye: fianzas y avales (bancarios, corporativos, a primer requerimiento), garantías de producto (warranties), arrendamientos operativos y opciones asociadas, contratos de mantenimiento a largo plazo, cartas de confort (comfort letters), líneas de factoring/confirming/descuento, pactos de recompra (buy-back), derechos de opción (put/call/ROFO/ROFR), cláusulas de indemnity y hold harmless, y cross-defaults entre instrumentos financieros.

El resultado debe proporcionar al equipo de M&A y al equipo financiero una visión completa de la "deuda oculta" y las obligaciones contingentes, con cuantificación (importes máximos, condicionales y probabilísticos) y recomendación de remedios (release, novación, escrow, ajuste de precio, indemnidad específica).

### 4.2 Usuarios Objetivo

| Área | Perfil y Necesidad |
|------|-------------------|
| M&A / Corporate | Evaluación integral de obligaciones no visibles en balance para negociación de precio y condiciones del SPA. |
| Financiero / Banca de Inversión | Impacto en Enterprise Value y Equity Value: ajustes a deuda neta (debt-like items), normalización de EBITDA. |
| Auditoría / Contabilidad | Conciliación de contingencias declaradas en notas a estados financieros vs. documentación contractual real. |
| Seguros / Reaseguros | Evaluación de pólizas de D&O, RC producto, y cobertura de garantías. |
| Integración Post-Closing | Plan de transición: qué garantías deben novarse, qué avales deben sustituirse. |

### 4.3 Alcance Legal y Referencias Normativas

#### 4.3.1 Marco Contable

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **PGC (RD 1514/2007)** | BOE-A-2007-19884. Plan General de Contabilidad. NRV 15 (Provisiones y Contingencias): reconocimiento cuando existe obligación presente, es probable la salida de recursos, y se puede estimar fiablemente. Contingencias: se revelan en memoria pero no se provisionan si no son probables. NRV 16 (Pasivos por retribuciones a largo plazo al personal). |
| **IAS 37** | Norma Internacional de Contabilidad 37 (Provisiones, Pasivos Contingentes y Activos Contingentes). IASB, versión actualizada 2022. Criterio de reconocimiento: obligación presente (legal o implícita), probable salida de recursos, estimación fiable. Pasivos contingentes: no se reconocen, se revelan. |
| **NIIF 16** | Norma Internacional de Información Financiera 16 (Arrendamientos). Efectiva desde 01/01/2019. Elimina la distinción operativo/financiero para arrendatarios: casi todos los arrendamientos se reconocen en balance. Excepciones: short-term (≤12 meses) y low-value assets. |

#### 4.3.2 Marco Legal

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **Código Civil (arts. 1822-1856)** | Régimen de la fianza (garantía personal). Arts. 1822-1830: fianza en general. Arts. 1831-1836: efectos entre fiador y acreedor. Relevante para avales corporativos intragrupo. |
| **Código de Comercio (arts. 439 y ss.)** | Afianzamiento mercantil. Art. 439: carácter solidario del aval mercantil salvo pacto. |
| **TRLC (RDL 1/2020)** | BOE-A-2020-4859. Texto Refundido de la Ley Concursal. Relevante para: cláusulas ipso facto y su limitación en pre-insolvencia, cross-default y aceleración de deuda, tratamiento de garantías reales y personales en concurso. Modificado en 2022 para transponer Directiva (UE) 2019/1023 sobre reestructuraciones preventivas. |
| **Ley 5/2015 (Fomento de la Financiación Empresarial)** | Régimen de cesión de créditos, titulización y factoring. Relevante para identificar líneas de factoring/confirming que constituyen financiación off-balance. |

### 4.4 Datos de Entrada

| Categoría | Detalle | Fuentes típicas |
|-----------|---------|----------------|
| Contratos financieros | Facility agreements, pólizas de crédito, contratos de factoring/confirming/descuento, swap/derivados, garantías corporativas | Data room — carpeta financiera |
| Contratos comerciales | Garantías de producto, contratos de mantenimiento, arrendamientos, pactos de recompra | Data room — carpetas comerciales |
| Garantías y avales | Avales bancarios emitidos y recibidos, garantías a primer requerimiento, fianzas corporativas, comfort letters | Data room + información de entidades financieras |
| Notas a estados financieros | Memoria de cuentas anuales: notas de provisiones, contingencias, compromisos, información fuera de balance | Data room — carpeta financiera |
| Minutas de órganos de gobierno | Actas de Consejo de Administración, Junta General, comités de JV/partnership | Data room — carpeta corporativa |
| Correspondencia con contrapartes | Cartas de entidades financieras (circularización), correspondencia con aseguradoras, reclamaciones pendientes | Data room + management Q&A |

### 4.5 Salidas

#### 4.5.1 Registro Maestro de Obligaciones Off-Balance

| Campo | Descripción |
|-------|------------|
| ID obligación | Identificador único, enlace a documento fuente |
| Tipo | Aval bancario / Garantía corporativa / Comfort letter / Arrendamiento / Factoring / Put/Call / ROFO/ROFR / Indemnity / Cross-default / Recompra / Mantenimiento LT |
| Contrapartes | Beneficiario, garante, intermediario financiero |
| Importe máximo | Cuantía máxima de la obligación (en €) |
| Importe condicional | Cuantía sujeta a ocurrencia de trigger |
| Probabilidad estimada | Alta (>50%) / Media (25-50%) / Baja (<25%) / Remota (<5%) |
| Triggers de activación | Eventos que activan la obligación (default, CoC, incumplimiento de KPIs, etc.) |
| Vencimiento | Fecha de expiración o renovación |
| Cross-default | ¿Vinculada a otras obligaciones? Identificación de la cadena |
| Reaseguros/contragarantías | Existencia de cobertura de seguro o contragarantía que mitiga el riesgo |
| Impacto en precio | Ajuste propuesto a Enterprise Value / Equity Value |
| Remedio recomendado | Release, novación, escrow, ajuste de precio, indemnidad específica en SPA, R&W |

#### 4.5.2 Alertas de Cross-Default

- Mapa de cadenas de cross-default: visualización de cómo el default en un instrumento puede acelerar otros.
- Escenarios de cascada: simulación de impacto si se activa un trigger.
- Identificación de "single points of failure" financieros.

#### 4.5.3 Recomendaciones para el SPA

- **Debt-like items:** Lista de obligaciones off-balance que deben incluirse en la definición de "Deuda Financiera Neta" del SPA para ajuste de precio.
- **R&Ws específicas:** Declaraciones y garantías que deben exigirse al vendedor sobre la completitud del disclosure de contingencias.
- **Indemnidades:** Indemnidades específicas para contingencias identificadas de alta probabilidad o importe material.
- **Escrow:** Propuesta de retención en escrow para contingencias de probabilidad media con importe material.
- **Condiciones suspensivas:** Si alguna contingencia requiere resolución previa al closing.

### 4.6 Lógica y Motor de Reglas

#### 4.6.1 Pipeline de Extracción

```
Extracción multifuente → Normalización contable → Clasificación →
Cuantificación → Deduplicación → Cross-referencing → Scoring → Recomendaciones
```

**Paso 1 — Extracción semántica:** Detección de patrones clave en documentos:
- Garantías: "garantía", "aval", "fianza", "hold harmless", "indemnity", "comfort letter", "letter of awareness"
- Opciones: "opción de compra/venta", "put", "call", "ROFO", "ROFR", "right of first refusal/offer"
- Factoring: "cesión de créditos", "factoring", "confirming", "descuento", "anticipos sobre facturas"
- Recompra: "pacto de recompra", "buy-back", "compromiso de adquisición"
- Cross-default: "incumplimiento cruzado", "cross-default", "cross-acceleration"

**Paso 2 — Normalización contable:** Conversión de importes a moneda base (EUR). Ajuste temporal (valor presente de obligaciones a largo plazo). Clasificación según PGC/IAS 37 (provisión, pasivo contingente, compromiso).

**Paso 3 — Cuantificación:** Extracción del importe máximo de la obligación. Cuando el importe no es determinado ("best efforts", "all losses"), flag de "importe indeterminado" con solicitud de aclaración a management.

**Paso 4 — Deduplicación:** Vinculación de la misma obligación reportada en múltiples fuentes (ej. aval aparece en contrato de financiación, en nota a memoria, y en carta del banco). Consolidación en un único registro con referencias cruzadas.

**Paso 5 — Cross-referencing:** Reconciliación de obligaciones contractuales vs. notas a memoria. Alerta cuando hay obligaciones contractuales no reflejadas en estados financieros (undisclosed contingencies).

### 4.7 Arquitectura Técnica

| Capa | Descripción |
|------|------------|
| **Pipeline de extracción multifuente** | Procesamiento paralelo de documentos financieros, comerciales y corporativos. NLP especializado en terminología financiera y jurídica (ES/EN). |
| **Normalizador contable** | Motor de normalización que clasifica obligaciones según PGC NRV 15/IAS 37. Conversión de divisas. Cálculo de valor presente. |
| **Motor de deduplicación** | Matching de obligaciones por: contraparte, importe, fecha, tipo. Fuzzy matching para variaciones en denominaciones. Consolidación con preservación de todas las fuentes. |
| **Tablero de riesgos y escenarios** | Dashboard interactivo con: registro maestro, mapa de cross-default, simulación de cascadas, impacto en valoración. Drill-down a documento fuente. |
| **Generador de recomendaciones** | Motor de reglas que propone remedios según tipo, importe y probabilidad. Templates para cláusulas de SPA. |

### 4.8 Controles de Calidad y Compliance

- **Cuadre con notas de memoria:** Reconciliación automática entre obligaciones detectadas y las reveladas en estados financieros. Alerta obligatoria cuando hay discrepancias.
- **Doble control en importes máximos:** Verificación cruzada del importe máximo de garantías/avales contra límites de pólizas y capacidad financiera del garante.
- **Logging de supuestos:** Cada cuantificación que requiera estimación (probabilidad, importe condicional) se documenta con los supuestos utilizados, la base normativa (IAS 37) y el profesional responsable.
- **Segregación de información sensible:** Información de derivados, estructuras de financiación y rating interno se gestionan en entorno restringido.
- **Reconciliación con circularización bancaria:** Los avales y garantías bancarias se reconcilian con las cartas de confirmación de las entidades financieras.

### 4.9 KPIs de Rendimiento

| KPI | Objetivo |
|-----|----------|
| Cobertura de fuentes documentales | 100% de documentos relevantes del data room procesados |
| Tasa de discrepancias detectadas vs. estado inicial | ≥ 20% de mejora en identificación de obligaciones vs. disclosure inicial de la target |
| Reducción de "surprises" en SPA | 0 contingencias materiales descubiertas post-signing que no estuvieran en el DD report |
| Precisión de cuantificación | ≤ 10% de desviación vs. cuantificación final acordada en negociación |
| Tiempo de procesamiento | ≤ 48 horas para procesamiento inicial del data room financiero completo |

### 4.10 Riesgos y Mitigación

| Riesgo | Mitigación |
|--------|-----------|
| Redacciones vagas ("best efforts", "reasonable endeavours") | Flags de estimación obligatorios. Ruta de aclaración estructurada con management Q&A. Escenarios worst/base/best case. |
| Cuantías "best efforts" no determinables | Clasificación como "importe indeterminado" con alerta de severidad alta. Propuesta de indemnidad abierta en SPA. |
| Obligaciones verbales o no documentadas | Inclusión en el cuestionario de management representations. R&W específica en SPA sobre completitud del disclosure. |
| Cross-defaults ocultos en documentación voluminosa | Extracción automática con cross-referencing. Revisión manual obligatoria de todos los facility agreements. |
| Comfort letters sin firma o sin valor jurídico vinculante | Clasificación diferenciada: comfort letter con lenguaje vinculante vs. meramente informativa. Análisis jurídico del grado de compromiso. |

### 4.11 Plan de Pruebas

#### Caso 1: Garantías cruzadas en pool bancario
Pool de financiación sindicada con 5 entidades donde la target ha emitido garantías cruzadas entre filiales. Cross-default vinculado a ratios de covenants. Verificar: detección de todas las garantías, mapping de la cadena de cross-default, cuantificación del importe máximo consolidado.

#### Caso 2: Comfort letters sin firma
Carta de confort emitida por la matriz de la target a favor de un proveedor estratégico. Documento sin firma, solo con membrete. Verificar: detección como contingencia potencial, clasificación correcta (vinculante/no vinculante según jurisprudencia), flag para revisión legal.

#### Caso 3: Opciones de compra encadenadas a KPIs
Acuerdo de JV donde la target tiene una opción put ejercitable si no se alcanzan determinados KPIs operativos en los próximos 3 años. Precio de ejercicio fijado por fórmula. Verificar: detección de la opción, extracción de la fórmula de precio, cuantificación del rango de importe, clasificación como debt-like item.

#### Caso 4: Arrendamientos con rent-free y escalados
Portfolio de 15 arrendamientos de oficinas con periodos de carencia (rent-free) y escalados anuales vinculados al IPC. Algunos con opción de compra. Verificar: detección de todas las condiciones especiales, cálculo del valor presente de compromisos, identificación de opciones.

#### Caso 5: Factoring sin recurso vs. con recurso
Líneas de factoring donde parte es sin recurso (true sale, off-balance) y parte con recurso (financiación encubierta). Verificar: clasificación correcta según naturaleza económica (no forma legal), cuantificación diferenciada, impacto en deuda neta.

---

## 5. SKILL 3: Regulatory & FDI Notifications Planner

**Licencias, autorizaciones sectoriales y control de inversiones extranjeras**

### 5.1 Propósito

Levantar el mapa completo de licencias, inscripciones y autorizaciones sectoriales de la target y sus filiales, detectar gaps (caducidades, incumplimientos, irregularidades), y determinar todas las notificaciones o autorizaciones administrativas exigibles por el deal, incluyendo el control de inversiones extranjeras directas (FDI) y la notificación de concentraciones (antitrust a nivel high-level), con rutas de actuación diferenciadas por signing y closing.

El resultado debe proporcionar al equipo de deal un plan de acción regulatorio completo que permita: (a) identificar condiciones suspensivas regulatorias para el SPA, (b) calcular lead-times de trámites para dimensionar el periodo entre signing y closing, (c) preparar la documentación soporte para cada autorización, y (d) identificar riesgos de pérdida de licencias por el cambio de control.

### 5.2 Usuarios Objetivo

| Área | Perfil y Necesidad |
|------|-------------------|
| Público-Regulatorio | Análisis de licencias sectoriales, trámites de autorización, gap analysis |
| M&A / Corporate | Condiciones suspensivas regulatorias en SPA, lead-times para dimensionar el gap signing-closing |
| Compliance | Verificación de cumplimiento regulatorio de la target, detección de irregularidades |
| Fiscal Internacional | Coordinación con FDI y estructuración del deal para optimizar trámites |
| Comité de Inversión | Evaluación de riesgo regulatorio para decisión de go/no-go |

### 5.3 Alcance Legal y Referencias Normativas

#### 5.3.1 Control de Inversiones Extranjeras (FDI)

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **Ley 19/2003, de 4 de julio** | BOE-A-2003-13471. Régimen jurídico de los movimientos de capitales y transacciones económicas con el exterior. Establece libertad de movimientos de capitales, con autorización previa para determinadas inversiones extranjeras directas. |
| **RD 571/2023, de 4 de julio** | Nuevo Reglamento de inversiones exteriores. Sustituye al derogado RD 664/1999 (BOE-A-1999-9938). En vigor desde 01/09/2023. Actualiza el régimen de declaración y autorización de inversiones extranjeras. |
| **RDL 34/2020, de 17 de noviembre** | Medidas de apoyo a la solvencia empresarial. Amplió temporalmente el régimen de suspensión de la liberalización de inversiones exteriores a inversores de UE/AELC en sectores estratégicos. Umbrales: inversiones en sociedades cotizadas O valor >500M€ en no cotizadas. Régimen extendido hasta 31/12/2026 por RDL 1/2025 (de 28 de enero). |
| **Reglamento (UE) 2019/452** | Marco para el control de inversiones extranjeras directas en la Unión. Mecanismo de cooperación entre Estados miembros y Comisión. Sectores estratégicos: infraestructuras críticas, tecnologías críticas, suministros esenciales, medios de comunicación. |

**NOTA IMPORTANTE:** El RD 664/1999 sobre inversiones exteriores ha sido DEROGADO y sustituido por el RD 571/2023. Cualquier referencia al RD 664/1999 debe actualizarse.

#### 5.3.2 Control de Concentraciones (Antitrust)

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **Ley 15/2007, de 3 de julio (LDC)** | Ley de Defensa de la Competencia. Define "concentración" (cambio duradero de control). Umbrales de notificación: cuota de mercado ≥30% o volumen de negocios combinado >240M€ (con al menos dos partes >60M€ en España). Obligación de suspensión hasta clearance. Organismo competente: CNMC. |
| **RD 261/2008, de 22 de febrero** | Reglamento de Defensa de la Competencia. Desarrolla procedimientos de notificación y análisis de concentraciones. Formulario de notificación y plazos. |
| **Reglamento (CE) 139/2004** | Reglamento comunitario de concentraciones. Si la operación tiene "dimensión comunitaria" (umbrales de volumen de negocios a nivel mundial y europeo), la competencia es exclusiva de la Comisión Europea. El skill debe determinar si la operación tiene dimensión comunitaria vs. nacional. |

#### 5.3.3 Normativa Sectorial (Selección)

| Sector | Norma principal | Requisitos de autorización por CoC |
|--------|----------------|-----------------------------------|
| Entidades de crédito | Ley 10/2014 (BOE-A-2014-6726) | Autorización previa del BCE/BdE para adquisición de participaciones significativas (≥10%, 20%, 30%, 50%) |
| Seguros | Ley 20/2015 (LOSSEAR) | Autorización de la DGSFP para adquisición de participaciones cualificadas |
| Energía | Ley 24/2013 (Sector Eléctrico), Ley 34/1998 (Hidrocarburos) | Autorización CNMC/MITECO para concentraciones en sector energético. Comunicación a la CNMC de participaciones en operadores |
| Telecomunicaciones | Ley 11/2022 (General de Telecomunicaciones) | Comunicación a la CNMC. Autorización para participaciones significativas en operadores con derechos de uso del espectro |
| Sanitario | Leyes autonómicas de ordenación sanitaria | Autorización de la comunidad autónoma para cambio de titularidad de centros sanitarios |
| Juego | Ley 13/2011 (Regulación del Juego) | Autorización de la DGOJ para cambio de control de operadores con licencia |
| Transporte | Ley 16/1987 (Ordenación de Transportes Terrestres) | Comunicación para cambio de titularidad de autorizaciones de transporte |
| Medios de comunicación | Ley 13/2022 (General de Comunicación Audiovisual) | Notificación/autorización para cambios de control en prestadores de servicios audiovisuales |
| Defensa | Ley 12/2012 y RD 679/2014 | Autorización para inversiones en empresas vinculadas a defensa nacional |

### 5.4 Datos de Entrada

| Categoría | Detalle |
|-----------|---------|
| Data room regulatorio | Licencias, inscripciones registrales, autorizaciones administrativas, renovaciones, expedientes sancionadores, correspondencia con reguladores |
| Actividad por centro/ubicación | Mapa de centros de actividad de la target con la actividad desarrollada en cada uno, jurisdicción, autoridad competente |
| Estructura accionarial | Cadena de participación completa (directa e indirecta), jurisdicción de cada entidad, nacionalidad de los UBOs (ultimate beneficial owners) |
| Parámetros del deal | Porcentaje de adquisición, tipo de operación (share deal/asset deal/fusión), cambio de control directo/indirecto, precio estimado, estructura de financiación |
| Jurisdicciones afectadas | Países donde la target o sus filiales tienen presencia, operaciones o activos |
| Datos financieros para umbrales | Volumen de negocios por país, cuota de mercado estimada (para análisis antitrust) |

### 5.5 Salidas

#### 5.5.1 Matriz Permiso-Centro-Riesgo

Tabla con:
- Licencia/autorización: tipo, número, autoridad emisora, centro/ubicación
- Estado: vigente / caducada / en renovación / pendiente
- Fecha de vencimiento y próxima renovación
- Riesgo por CoC: ¿el cambio de control afecta a esta licencia? (sí/no/condicional)
- Acción requerida: notificación, autorización previa, regularización, sustitución de titularidad, ninguna
- Lead-time estimado del trámite
- Timing: pre-signing / entre signing y closing / post-closing

#### 5.5.2 Gap Analysis

- Licencias faltantes: actividades reguladas sin la correspondiente autorización
- Caducidades: licencias vencidas no renovadas
- Incumplimientos: condiciones de licencia no cumplidas (ej. requisitos de capital, personal cualificado, seguros obligatorios)
- Plan de regularización con priorización y plazos

#### 5.5.3 Plan de Acción FDI/Antitrust

- Determinación de si la operación requiere autorización FDI (análisis de nacionalidad del adquirente, sector estratégico, umbrales)
- Determinación de si la operación requiere notificación de concentración (análisis de umbrales nacionales y comunitarios)
- Documentación soporte pre-preparada para cada filing
- Cronograma de filings con dependencias
- Criterios de condición suspensiva en SPA

### 5.6 Lógica y Motor de Reglas

#### 5.6.1 Árbol de Decisión por Sector

```
¿La target opera en sector regulado? →
  SÍ → ¿Qué tipo de actividad? → Energía/Financiero/Telecom/Sanidad/Juego/etc. →
    ¿Qué tipo de licencia tiene? → ¿El CoC afecta a la licencia? →
      SÍ → ¿Requiere autorización previa o notificación? → Lead-time → Timing (signing/closing)
      NO → Documentar y archivar
  NO → Verificar FDI/Antitrust genérico
```

#### 5.6.2 Triggers de FDI

- **Nacionalidad del adquirente:** Si el adquirente final es de fuera de la UE/AELC → régimen general de autorización previa para sectores estratégicos.
- **Régimen transitorio UE/AELC (RDL 34/2020 extendido a 31/12/2026):** Si el adquirente es UE/AELC → autorización previa solo si: (a) inversión en sociedad cotizada, O (b) valor >500M€.
- **Sectores estratégicos (Reglamento UE 2019/452):** Infraestructuras críticas, tecnologías clave (IA, robótica, semiconductores, ciber, aeroespacial, nuclear, nano/bio), suministros esenciales (energía, materias primas, alimentación, salud), medios de comunicación.
- **Umbrales de participación:** 10%, 20%, 30%, 50% (para sectores financieros regulados).

#### 5.6.3 Análisis Antitrust (High-Level)

- **Dimensión comunitaria (Reglamento 139/2004):** Volumen de negocios mundial combinado >5.000M€ Y al menos dos partes >250M€ en la UE (o umbrales alternativos 2/3 rule).
- **Dimensión nacional (Ley 15/2007):** Cuota de mercado combinada ≥30% O volumen de negocios combinado en España >240M€ (al menos dos con >60M€ cada una).
- **Si se cumplen umbrales:** Generación de checklist para notificación, estimación de plazos (Fase I: 1 mes; Fase II: 2 meses adicionales), identificación de solapamientos horizontales y verticales.

### 5.7 Arquitectura Técnica

| Capa | Descripción |
|------|------------|
| **Catálogo normativo** | Base de datos parametrizable por sector, tipo de actividad y jurisdicción. Incluye: norma aplicable, autoridad competente, tipo de trámite (notificación/autorización), lead-time típico, documentación requerida. Actualizable por equipo regulatorio. |
| **Motor de reglas** | Árbol de decisión codificado para determinar obligaciones por deal y sector. Inputs: estructura del deal, nacionalidad del adquirente, sector de la target, participación adquirida. |
| **Calendarizador con dependencias** | Motor de planificación que calcula la ruta crítica de trámites regulatorios. Dependencias: ej. la autorización FDI puede ser requisito previo a la notificación de concentración. Buffers configurables por tipo de trámite. |
| **Generador de checklist documental** | Templates de documentación por tipo de trámite: formularios de notificación, solicitudes de autorización, memorandums explicativos, poderes de representación. |
| **Dashboard regulatorio** | Panel con status de cada licencia y trámite: semáforo por riesgo, timeline, bottlenecks, progreso vs. plan. |

### 5.8 Controles de Calidad y Compliance

- **Evidencias de titularidades vigentes:** Cada licencia se vincula al documento que la acredita (resolución administrativa, inscripción registral, certificado). Verificación de autenticidad.
- **Validación cruzada con información pública:** Contraste de licencias declaradas por la target con registros públicos (BOE, registros mercantiles, registros sectoriales).
- **Control de versiones por iteración con autoridad:** Cuando se inicia un trámite, cada comunicación con la autoridad se registra con sello de tiempo.
- **Segregación de información FDI:** Los datos relativos a la estructura del adquirente y la estrategia de pricing se gestionan en entorno restringido (clean team regulatorio).

### 5.9 KPIs de Rendimiento

| KPI | Objetivo |
|-----|----------|
| % licencias verificadas | 100% de las licencias materiales de la target |
| Desviación real vs. plan de trámites | ≤ 15% de desviación en lead-times estimados |
| Nº condiciones suspensivas resueltas antes de closing | 100% de condiciones regulatorias cerradas |
| Gaps identificados en DD | ≥ 95% de gaps detectados antes de signing |
| Tiempo de elaboración del plan regulatorio | ≤ 5 días hábiles desde acceso al data room regulatorio |

### 5.10 Riesgos y Mitigación

| Riesgo | Mitigación |
|--------|-----------|
| Cambios regulatorios durante la transacción | Monitor legislativo de BOE y boletines autonómicos. Buffers temporales de 20-30% sobre lead-times estimados. |
| Criterios discrecionales de autoridades | Pre-filing Q&A cuando sea posible (especialmente en FDI y antitrust). Análisis de precedentes. |
| Licencias a nombre de personas físicas (no transferibles) | Identificación temprana y plan de migración (nueva solicitud a nombre del adquirente o designado). |
| Cambio de control indirecto no evidente | Análisis de la cadena completa de participación. Definiciones de "control" en cada norma sectorial (pueden variar). |
| Retrasos en la obtención de autorizaciones | Dimensionar el gap signing-closing con margen. Long-stop date en SPA con extensión automática para demoras regulatorias. |

### 5.11 Plan de Pruebas

#### Caso 1: Cambio de control indirecto en filial regulada
Adquisición del 100% de una holding luxemburguesa que a su vez posee el 70% de una operadora de telecomunicaciones española. Verificar: detección del cambio de control indirecto, identificación de la obligación de comunicación a CNMC bajo Ley 11/2022, clasificación como requisito pre-closing.

#### Caso 2: Traspaso de autorizaciones personales
Target en sector sanitario con licencias de centros sanitarios a nombre del administrador único (persona física). Verificar: flag de "licencia personal no transferible", plan de acción para solicitar nueva licencia a nombre de la entidad o nuevo titular.

#### Caso 3: Límites de participación extranjera
Fondo soberano de un país no-UE adquiere el 25% de una empresa española de defensa. Verificar: detección de la obligación de autorización bajo régimen FDI + Ley 12/2012 (defensa), lead-time estimado, documentación requerida, flag de alto riesgo.

#### Caso 4: Licencias por centro con distinto titular
Target con 12 centros de actividad en 4 comunidades autónomas, con licencias medioambientales y de actividad otorgadas a distintas entidades del grupo. Verificar: mapping correcto centro-entidad-licencia, identificación de qué licencias se ven afectadas por cada tipo de operación (share deal vs. asset deal por centro).

#### Caso 5: Concentración con dimensión comunitaria
Operación donde adquirente y target tienen volumen de negocios mundial combinado >5.000M€. Verificar: análisis correcto de umbrales comunitarios (incluyendo 2/3 rule), determinación de que la competencia es de la Comisión Europea, no de la CNMC, ajuste del plan de trámites.

---

## 6. SKILL 4: People & Labor Exposure Analyzer

**Plantilla, contratos, costes, pasivos laborales y retención de personas clave**

### 6.1 Propósito

Automatizar el barrido exhaustivo de la documentación laboral de la target para cuantificar riesgos y costes asociados a la fuerza laboral: estructura de plantilla, tipos de contrato y antigüedades, retribución variable (bonus, comisiones, stock options/RSUs/phantom shares), uso de ETT y subcontratas, convenios colectivos aplicables, horas extraordinarias y compliance laboral, litigios pendientes y actas de inspección, pactos de no competencia y confidencialidad, severance exposure bajo distintos escenarios de reestructuración, y retención de personas clave (key people).

El objetivo es proporcionar al equipo de deal una cuantificación fiable de los pasivos laborales (conocidos y contingentes) y los costes de integración/reestructuración post-closing, junto con un plan de retención de personas clave y un mapa de riesgos laborales priorizados.

### 6.2 Usuarios Objetivo

| Área | Perfil y Necesidad |
|------|-------------------|
| Laboral | Análisis jurídico de contratos, convenios, litigios y compliance laboral |
| M&A / Corporate | Cuantificación de pasivos laborales para negociación de precio y condiciones del SPA |
| Operaciones / RRHH | Plan de integración post-closing: retención, reestructuración, armonización de condiciones |
| Financiero | Provisionamiento de contingencias laborales, impacto en EBITDA normalizado |
| Comité de Inversión | Riesgo laboral como factor de go/no-go |

### 6.3 Alcance Legal y Referencias Normativas

#### 6.3.1 Estatuto de los Trabajadores y Normativa Conexa

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **Estatuto de los Trabajadores (RDL 2/2015)** | BOE-A-2015-11430. Norma fundamental del derecho laboral español. Artículos clave para M&A: art. 44 (sucesión de empresa: subrogación automática de trabajadores en transmisión de unidad productiva), art. 49 (causas de extinción), art. 51 (despido colectivo — ERE: umbrales, procedimiento de consultas, indemnización de 20 días/año), art. 52 (despido por causas objetivas: 20 días/año, máx. 12 meses), art. 53 (forma y efectos del despido objetivo), art. 56 (despido improcedente: 33 días/año, máx. 24 meses, o readmisión). NOTA: art. 52.d (despido por absentismo) fue derogado por RDL 4/2020. |
| **RD 1483/2012, de 29 de octubre** | BOE-A-2012-13419. Reglamento de despido colectivo (ERE), suspensión de contratos y reducción de jornada (ERTE). 48 artículos. Procedimiento de consultas, documentación obligatoria, plan de recolocación externa, comunicación a la autoridad laboral. |
| **Ley 10/2021, de 9 de julio** | BOE-A-2021-11472. Ley de trabajo a distancia. Aplicable cuando ≥30% de la jornada en periodo de 3 meses se realiza a distancia. Requiere acuerdo escrito, provisión de equipos por la empresa, derecho a desconexión digital. Relevante para: costes de equipamiento, acuerdos individuales a revisar, riesgo de incumplimiento. |
| **LISOS (RDL 5/2000, de 4 de agosto)** | BOE-A-2000-15060. Texto Refundido de Infracciones y Sanciones en el Orden Social. Clasificación de infracciones: leves, graves, muy graves. Prescripción: 3 años (5 años para Seguridad Social). Cuantías: leves (hasta 7.500€), graves (hasta 75.000€), muy graves (hasta 1.000.000€ en los casos más extremos). |

#### 6.3.2 Convenios Colectivos y Normativa Retributiva

| Norma | Relevancia |
|-------|-----------|
| **Art. 82-92 ET (RDL 2/2015)** | Régimen de convenios colectivos: ámbito de aplicación, ultraactividad, inaplicación (descuelgue), concurrencia. Esencial para identificar qué convenio(s) aplica(n) a la target y sus obligaciones. |
| **RD 902/2020 (Igualdad retributiva)** | BOE-A-2020-12215. Desarrollo del principio de igualdad retributiva entre hombres y mujeres. Obligación de registro retributivo, auditoría retributiva (>50 empleados), plan de igualdad. |
| **RD 901/2020 (Planes de igualdad)** | BOE-A-2020-12214. Obligación de plan de igualdad para empresas >50 trabajadores. Registro obligatorio en REGCON. |

#### 6.3.3 Seguridad Social y Relaciones Laborales

| Norma | Relevancia |
|-------|-----------|
| **TRLGSS (RDL 8/2015)** | Texto Refundido de la Ley General de la Seguridad Social. Cotizaciones, prestaciones, responsabilidad solidaria del sucesor en caso de subrogación. |
| **Ley 32/2006 (Subcontratación en construcción)** | Régimen específico de subcontratación en sector de construcción: cadena de responsabilidades, registro de empresas. |
| **Ley 14/1994 (ETT)** | Empresas de Trabajo Temporal. Límites a la cesión de trabajadores, supuestos de cesión ilegal (art. 43 ET). |

### 6.4 Datos de Entrada

| Categoría | Detalle | Tratamiento de datos personales |
|-----------|---------|-------------------------------|
| Listados de empleados | Headcount, categoría profesional, antigüedad, tipo de contrato, centro de trabajo, convenio aplicable | Seudonimizados: sin nombre ni DNI, solo ID numérico y datos agregados |
| Contratos individuales y anexos | Contratos laborales, pactos de no competencia, acuerdos de confidencialidad, inventor assignments, side letters retributivas | Acceso restringido (clean team laboral) |
| Políticas retributivas | Estructura salarial, bonus, comisiones, stock options/RSUs/phantom shares, benefits (coche, seguro, formación) | Datos agregados por nivel/categoría |
| CBA / Convenios colectivos | Convenios sectoriales y de empresa aplicables, acuerdos de inaplicación, pactos de empresa | Documentos públicos (REGCON) |
| Litigios y actas de inspección | Demandas laborales pendientes (despido, horas extra, clasificación profesional), actas de inspección de trabajo, requerimientos | Seudonimizados |
| Nóminas muestra | Muestreo estadístico de nóminas por categoría para verificar cumplimiento de convenio y cálculos | Seudonimizadas |
| ETT / Outsourcing | Contratos con ETTs y empresas de outsourcing, facturación, número de trabajadores, funciones, duración | Sin datos personales de los trabajadores |

### 6.5 Salidas

#### 6.5.1 Mapa de Plantilla

- **Dashboard de plantilla:** FTEs por centro, categoría, antigüedad, tipo de contrato, sexo, edad.
- **Pirámide de antigüedad:** Distribución de la plantilla por tramos de antigüedad (clave para calcular severance exposure).
- **Identificación de personal crítico (key people):** Lista de personas cuya salida tendría impacto material en el negocio, con análisis de sus condiciones contractuales (non-compete, retention, golden parachute).
- **Ratio de temporalidad:** % de contratos temporales vs. indefinidos. Alerta si supera umbrales sectoriales o legales.

#### 6.5.2 Riesgos Laborales Identificados

- **Fraude de ley en contratación temporal:** Contratos temporales encadenados que deberían ser indefinidos (art. 15.5 ET reformado por RDL 32/2021).
- **Cesión ilegal de trabajadores:** Trabajadores de ETT o subcontratas que realizan funciones propias de la plantilla bajo dirección efectiva de la target.
- **Incumplimientos retributivos:** Salarios por debajo de convenio, impago de complementos, horas extraordinarias no retribuidas.
- **Non-competes ineficaces:** Pactos de no competencia sin la compensación adecuada del art. 21.2 ET (puede generar nulidad del pacto y reclamación del trabajador).
- **Planes de igualdad:** Ausencia de plan de igualdad obligatorio (>50 trabajadores), registro retributivo incompleto.

#### 6.5.3 Cuantificación de Pasivos y Escenarios

- **Severance exposure por escenarios:**
  - Escenario 1: Despido colectivo (ERE) de X% de la plantilla → coste a 20 días/año + costes de plan social
  - Escenario 2: Despido objetivo individual → coste a 20 días/año, máx. 12 meses
  - Escenario 3: Despido improcedente → coste a 33 días/año, máx. 24 meses
  - Escenario 4: Mantenimiento de plantilla con armonización de condiciones
- **Litigios pendientes:** Cuantificación probabilística de contingencias por litigios (probable, posible, remota).
- **Inspecciones:** Estimación de riesgo por actas de inspección abiertas o potenciales.
- **Costes de integración:** Armonización de convenios, homologación de condiciones retributivas, costes de key people retention packages.

#### 6.5.4 Plan de Comunicaciones y Medidas Post-Closing

- **Plan de comunicación a empleados:** Timing y contenido de comunicaciones (pre-signing confidencial, post-signing general, day-1 post-closing).
- **Key people retention plan:** Propuesta de retention packages (bonus, aceleración de equity, extensión de non-compete con compensación adecuada).
- **Medidas de integración:** Cronograma de armonización de convenios, políticas y condiciones.

### 6.6 Lógica y Motor de Reglas

#### 6.6.1 Reglas de Análisis

- **Por tipo de contrato:** Detección de temporales encadenados (encadenamiento >18 meses en periodo de 24 meses o >2 contratos temporales en 18 meses desde RDL 32/2021), contratos formativos irregulares, falsos autónomos.
- **Por antigüedad:** Cálculo de indemnización por despido a 20 días/año (máx. 12 meses) y 33 días/año (máx. 24 meses) para cada tramo de la plantilla.
- **Muestreo estadístico de nóminas:** Muestreo aleatorio estratificado (por centro, categoría, convenio) con verificación de: cumplimiento de salario de convenio, complementos obligatorios, horas extraordinarias, cotizaciones sociales.
- **Detección de cláusulas sensibles:** Clasificación NLP de: non-compete (art. 21.2 ET), exclusividad (art. 21.1 ET), inventor assignment (Ley 24/2015 art. 15-20), golden parachute, retention bonus, aceleración de equity.
- **Proyección de costes de ajuste:** Modelo de coste por escenario de reestructuración, incluyendo: indemnizaciones, plan social, costes de outplacement (obligatorio en ERE >50 afectados), costes legales.

#### 6.6.2 Heatmap por Centro/Área

Visualización de riesgo laboral por dimensiones:
- Centro de trabajo (localización geográfica)
- Área funcional (comercial, producción, IT, administración)
- Tipo de riesgo (contractual, retributivo, seguridad, litigios)
- Severidad (crítico, alto, medio, bajo)

### 6.7 Arquitectura Técnica

| Capa | Descripción |
|------|------------|
| **Ingesta segura** | Data room con cifrado end-to-end. Seudonimización automática de datos personales en ingesta. Acceso solo para clean team laboral. |
| **Normalizador de HRIS** | Conversión de datos de diferentes sistemas de RRHH (SAP HR, Workday, Meta4, A3 Nom) a formato normalizado. Mapping de categorías profesionales, tipos de contrato, convenios. |
| **Extractor de cláusulas** | NLP especializado en derecho laboral español. Detección de: non-compete, exclusividad, golden parachute, retention, equity, inventor assignment. Confidence score por hallazgo. |
| **Motor de escenarios** | Simulador de costes de reestructuración con múltiples escenarios configurables. Inputs: % de reducción, centro afectado, tipo de despido. Outputs: coste total, coste por empleado, timeline. |
| **Dashboard con drill-down** | Panel interactivo con: mapa de plantilla, heatmap de riesgos, severance calculator, tracking de litigios. Drill-down desde KPI hasta documento fuente. |

### 6.8 Controles de Calidad y Compliance

- **Minimización de datos personales:** Solo datos estrictamente necesarios para el análisis. Seudonimización por defecto. Datos reales solo para key people con autorización específica.
- **Seudonimización:** ID numérico en lugar de nombre/DNI. Tabla de correspondencia custodiada por el DPO del despacho, accesible solo con autorización dual.
- **Revisión humana en casos críticos:** Litigios de alto importe, non-competes de key people, y posibles cesiones ilegales requieren validación de laboralista senior.
- **Segregación de accesos:** Información laboral separada de la financiera y comercial. Acceso diferenciado por rol (laboralista, financiero, socio).
- **Cumplimiento RGPD/LOPDGDD:** Base de legitimación (interés legítimo del adquirente en DD), información al vendedor sobre el tratamiento, evaluación de impacto si se procesan datos especiales (salud, afiliación sindical).

### 6.9 KPIs de Rendimiento

| KPI | Objetivo |
|-----|----------|
| Cobertura documental | ≥ 95% de documentos laborales del data room procesados |
| Precisión en muestreos de nómina | ≥ 99% de coincidencia entre cálculo de la skill y recálculo manual en QA |
| Fiabilidad del severance forecast | ≤ 5% de desviación vs. coste real de reestructuración post-closing |
| Nº de riesgos críticos mitigados pre-closing | 100% de riesgos clasificados como "críticos" con plan de mitigación antes de signing |
| Tiempo de elaboración del informe laboral | ≤ 7 días hábiles desde acceso al data room |

### 6.10 Riesgos y Mitigación

| Riesgo | Mitigación |
|--------|-----------|
| Datos incompletos (target no facilita toda la documentación) | Listado de documentos mínimos requeridos enviado al vendedor. R&W en SPA sobre completitud del data room laboral. |
| Múltiples convenios colectivos aplicables | Análisis de concurrencia y prioridad de convenios (art. 84 ET). Mapa de convenio por centro y categoría. |
| Litigios no reportados por la target | Verificación cruzada con registros judiciales (CENDOJ). R&W específica en SPA. |
| Cesiones ilegales no detectadas | Análisis funcional (no solo formal) de la relación con ETTs y subcontratas. Cuestionario management sobre integración funcional de externos. |
| Reforma laboral durante la transacción | Monitor de BOE laboral. Flexibilidad en el motor de reglas para actualizar umbrales y plazos. |

### 6.11 Plan de Pruebas

#### Caso 1: Contratos temporales encadenados
Trabajador con 4 contratos temporales sucesivos en 24 meses, misma empresa, mismo puesto. Verificar: flag de fraude de ley, cálculo de antigüedad acumulada como indefinido desde el primer contrato (art. 15.5 ET reformado), impacto en severance.

#### Caso 2: Bonus discrecional recurrente
Director comercial con bonus "discrecional" pagado ininterrumpidamente durante 6 años. Verificar: clasificación como condición más beneficiosa consolidada (no discrecional), inclusión en la base de cálculo de indemnización, cuantificación del riesgo.

#### Caso 3: Non-compete sin compensación adecuada
Pacto de no competencia post-contractual de 2 años para directivo con compensación del 10% del salario. Verificar: flag de posible nulidad (art. 21.2 ET requiere "compensación económica adecuada"), riesgo de reclamación por el trabajador, recomendación de renegociación o rescisión.

#### Caso 4: Subcontratación en actividad nuclear
Empresa de logística con el 40% de la plantilla operativa compuesta por trabajadores de una empresa de outsourcing que realizan funciones idénticas a los de plantilla, bajo supervisión directa de la target. Verificar: flag de posible cesión ilegal (art. 43 ET), cuantificación del riesgo (conversión a indefinidos de la target), impacto en headcount y costes.

#### Caso 5: ERE post-adquisición
Simulación de ERE afectando al 15% de la plantilla (200 trabajadores de 1.300). Verificar: cálculo correcto de indemnizaciones (20 días/año), coste del plan social, outplacement obligatorio (>50 afectados), timeline del procedimiento de consultas (30 días), coste total del escenario.

---

## 7. SKILL 5: Privacy, Cyber & IT Readiness Scanner

**Datos personales, ciberseguridad, dependencias tecnológicas y brechas contractuales**

### 7.1 Propósito

Revisar de forma integral el stack tecnológico, las prácticas de protección de datos y la postura de ciberseguridad de la target para identificar riesgos que puedan impactar el deal: incumplimientos de protección de datos (RGPD/LOPDGDD), vulnerabilidades de ciberseguridad, dependencias críticas de proveedores tecnológicos (vendor lock-in), riesgos de licencias de software (especialmente open source), insuficiencias en SLAs y DPAs (Data Processing Agreements) con proveedores cloud, y brechas contractuales en la cadena de suministro IT.

El resultado debe proporcionar al equipo de deal: (a) un mapa de tratamientos de datos con gaps de cumplimiento, (b) una evaluación de madurez de ciberseguridad, (c) un inventario de riesgos de licencias/OSS, (d) un playbook de remediación priorizado, y (e) condiciones de cierre recomendadas (parchear vulnerabilidades CVSS>8, actualizar DPAs, implementar escrows de código).

### 7.2 Usuarios Objetivo

| Área | Perfil y Necesidad |
|------|-------------------|
| Tecnología / IT | Evaluación técnica de la infraestructura, sistemas, arquitectura y seguridad de la target |
| Privacidad / DPO | Análisis de cumplimiento RGPD/LOPDGDD: tratamientos, bases de legitimación, transferencias internacionales, DPAs |
| M&A / Corporate | Riesgos tecnológicos como factor de valoración y negociación. Condiciones suspensivas IT en SPA |
| Integración | Plan de integración tecnológica post-closing: migración, consolidación, remediación |
| Ciberseguridad / CISO | Evaluación de la postura de seguridad: vulnerabilidades, incidentes, madurez, compliance |

### 7.3 Alcance Legal y Referencias Normativas

#### 7.3.1 Protección de Datos

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **RGPD (Reglamento UE 2016/679)** | Reglamento General de Protección de Datos. En vigor desde 25/05/2018. Aplicable directamente en España. Obligaciones clave: registro de actividades de tratamiento (art. 30), evaluación de impacto (EPIA, art. 35), DPA con encargados (art. 28), notificación de brechas (72 horas, art. 33), DPO obligatorio en determinados casos (art. 37), transferencias internacionales (Cap. V). Sanciones: hasta 20M€ o 4% del volumen de negocios anual global. |
| **LOPDGDD (LO 3/2018, de 5 de diciembre)** | BOE publicada 06/12/2018. Complementa el RGPD en España. Edad de consentimiento: 14 años. Derechos digitales en el ámbito laboral (desconexión digital, privacidad de dispositivos). Infracciones: leves (prescripción 1 año), graves (2 años), muy graves (3 años). Autoridad: AEPD. |

#### 7.3.2 Transferencias Internacionales de Datos

| Mecanismo | Estado |
|-----------|--------|
| Decisiones de adecuación | UE-EE.UU. (Data Privacy Framework, julio 2023), UK, Japón, Corea del Sur, Canadá (comercial), Israel, Nueva Zelanda, Argentina, Uruguay, entre otros |
| Cláusulas Contractuales Tipo (SCC) | Decisión de Ejecución 2021/914 de la Comisión. Nuevas SCC modulares (4 escenarios). Obligación de migración desde SCC antiguas completada. |
| Normas Corporativas Vinculantes (BCR) | Aprobadas caso por caso por autoridades de control. |
| Evaluación de impacto de transferencia (TIA) | Requerida por CJUE Schrems II (C-311/18) cuando se usan SCC. Evaluación del marco legal del país importador. |

#### 7.3.3 Ciberseguridad

| Norma | Contenido verificado y relevancia |
|-------|----------------------------------|
| **RDL 12/2018, de 7 de septiembre** | BOE-A-2018-12257. Seguridad de redes y sistemas de información (transposición NIS 1). Aplica a operadores de servicios esenciales y proveedores de servicios digitales. Desarrollado por RD 43/2021 (BOE-A-2021-1192). Obligaciones: gestión de riesgos, notificación de incidentes. |
| **Directiva NIS2 (UE) 2022/2555** | 14/12/2022. Plazo de transposición: 17/10/2024. España: NO transpuesta a febrero 2026. Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad aprobado en Consejo de Ministros el 14/01/2025, pendiente de tramitación parlamentaria. La Comisión Europea ha enviado dictamen motivado por incumplimiento (mayo 2025). Ampliará significativamente las obligaciones de ciberseguridad cuando se transponga. |
| **ENS (RD 311/2022, de 3 de mayo)** | BOE-A-2022-7191. Esquema Nacional de Seguridad. Actualiza el RD 3/2010. Aplica a sector público y proveedores de servicios IT al sector público. 74 controles de seguridad. Perfiles de cumplimiento por tipo de entidad. Obligatorio para proveedores de la Administración. |

#### 7.3.4 Propiedad Intelectual y Licencias

| Norma | Relevancia |
|-------|-----------|
| **RDL 1/1996 (Ley de Propiedad Intelectual)** | Régimen de derechos de autor sobre software (arts. 95-104). Obra por encargo vs. obra por cuenta ajena. Cesión de derechos. |
| **Licencias Open Source (GPL, LGPL, AGPL, MIT, Apache, etc.)** | Obligaciones de copyleft: GPL v2/v3 exige distribución del código fuente de obras derivadas. AGPL extiende a servicios de red. MIT/Apache: permisivas, sin copyleft. Riesgo: uso de código copyleft en producto propietario comercial. |

### 7.4 Datos de Entrada

| Categoría | Detalle |
|-----------|---------|
| Registro de Actividades de Tratamiento (RAT) | Art. 30 RGPD: finalidades, bases de legitimación, categorías de datos, destinatarios, transferencias, plazos de conservación |
| Políticas y DPAs | Políticas de privacidad (web, empleados, clientes), DPAs con encargados del tratamiento, cláusulas contractuales tipo (SCC), BCRs |
| Inventario de sistemas | Aplicaciones, bases de datos, servidores, redes. On-premise vs. cloud (IaaS/PaaS/SaaS). Proveedores, SLAs, criticidad |
| Diagramas de red | Arquitectura de red, segmentación, perímetro, accesos remotos, VPNs |
| Auditorías previas | Informes de auditoría de seguridad, tests de penetración, evaluaciones de vulnerabilidad, certificaciones (ISO 27001, SOC 2, ENS) |
| Contratos con proveedores IT | SaaS/PaaS/IaaS agreements, SLAs, DPAs, cláusulas de escrow de código, términos de lock-in, portabilidad |
| Informes de vulnerabilidades | Resultados de escaneos de vulnerabilidades (CVE/CVSS), estado de parcheado, excepciones |
| Lista de incidentes | Historial de incidentes de seguridad, brechas de datos notificadas/no notificadas, lecciones aprendidas |
| Inventario OSS | Componentes open source utilizados en los productos/servicios de la target, licencias, versiones |

### 7.5 Salidas

#### 7.5.1 Mapa de Tratamientos y Compliance Privacy

- **Mapa de tratamientos completo:** Catálogo de todos los tratamientos de datos personales con bases de legitimación, categorías de datos y destinatarios.
- **Gaps en RAT:** Tratamientos no documentados, bases de legitimación inadecuadas, plazos de conservación no definidos.
- **Gaps en DPAs:** Encargados del tratamiento sin DPA firmado, DPAs con cláusulas no conformes al art. 28 RGPD, SCC antiguas no migradas.
- **Transferencias internacionales:** Mapa de flujos de datos fuera del EEE. Mecanismo de legitimación de cada transferencia. Gaps: transferencias sin mecanismo válido.
- **Evaluación de impacto (EPIA):** Tratamientos que requieren EPIA y estado (realizada, pendiente, no realizada).

#### 7.5.2 Evaluación de Madurez de Seguridad

- **Scoring de madurez** (escala 1-5) por dominio: governance, gestión de accesos, seguridad de red, gestión de vulnerabilidades, respuesta a incidentes, continuidad de negocio, seguridad de desarrollo (SDLC), seguridad cloud.
- **Benchmarking** vs. estándares (ISO 27001, NIST CSF, ENS).
- **Vulnerabilidades priorizadas:** Lista de vulnerabilidades ordenadas por CVSS score × exposición. Recomendación de parcheado pre-closing para CVSS ≥ 8.0.

#### 7.5.3 Riesgos de Licencias y OSS

- **Inventario de componentes OSS** con licencia, versión, y vulnerabilidades conocidas (CVE).
- **Riesgos de copyleft:** Componentes con licencias copyleft (GPL, AGPL) integrados en productos propietarios. Flag de alto riesgo si hay distribución comercial.
- **Riesgo de vendor lock-in:** Proveedores con cláusulas de portabilidad inadecuadas, ausencia de escrow de código, dependencias single-vendor.
- **Cláusulas de indemnidad:** Verificación de que los contratos con proveedores incluyen indemnidad por infracción de IP de terceros.

#### 7.5.4 Playbook de Remediación y Condiciones de Cierre

- **Remediaciones pre-closing:** Lista priorizada de acciones que deben completarse antes del closing (ej. parchear vulnerabilidades CVSS>8, firmar DPAs faltantes, implementar escrows de código para proveedores críticos).
- **Remediaciones post-closing:** Plan de mejora a 90/180/365 días.
- **Condiciones de cierre propuestas:** Inputs para negociación del SPA (R&Ws sobre IT/privacy, indemnidades, escrow para remediaciones, condiciones suspensivas si el riesgo es material).

### 7.6 Lógica y Motor de Reglas

#### 7.6.1 Reglas de Compliance Privacy

- **Art. 30 RGPD (RAT):** Verificación de que cada tratamiento tiene: finalidad, base de legitimación, categorías de datos, categorías de interesados, destinatarios, transferencias internacionales, plazos de conservación, medidas de seguridad.
- **Art. 28 RGPD (DPA):** Verificación de que cada encargado tiene DPA con: instrucciones del responsable, confidencialidad, medidas de seguridad, subencargados autorizados, asistencia en derechos de interesados, devolución/destrucción, auditoría.
- **Cap. V RGPD (Transferencias):** Para cada flujo de datos fuera del EEE: ¿hay decisión de adecuación, SCC, BCR u otra garantía? ¿Se ha realizado TIA?
- **Art. 35 RGPD (EPIA):** ¿El tratamiento implica alto riesgo? (perfilado, datos especiales a gran escala, monitorización sistemática). Si sí, ¿se ha realizado EPIA?

#### 7.6.2 Scoring de Riesgo Técnico

- **CVSS scoring:** Priorización de vulnerabilidades por CVSS v3.1 base score × factor de exposición (interna/DMZ/internet).
- **Detección de licencias copyleft:** Scan del inventario OSS contra base de datos de licencias (SPDX). Flag automático para GPL, AGPL, copyleft fuerte integrado en código propietario.
- **Análisis de continuidad:** Evaluación de RPO (Recovery Point Objective) y RTO (Recovery Time Objective) declarados vs. evidencias de pruebas de DR.
- **Vendor lock-in scoring:** Evaluación por proveedor: portabilidad de datos (sí/no/parcial), escrow de código (sí/no), alternativas disponibles, coste estimado de migración.

#### 7.6.3 Cross-referencing con Skill 1

- Verificación de que los contratos con proveedores IT críticos identificados en esta skill están cubiertos en la matriz de consentimientos de la Skill 1 (CoC/assignment).
- Identificación de proveedores IT cuyo contrato tiene cláusula de CoC que podría afectar la continuidad de servicio post-closing.

### 7.7 Arquitectura Técnica

| Capa | Descripción |
|------|------------|
| **Conectores a repos de código** | Integración con GitHub/GitLab/Bitbucket para escaneo de dependencias OSS. Análisis de SBOM (Software Bill of Materials). |
| **Conectores CMDB/ISMS** | Ingesta de inventario de activos IT, configuraciones, y estado de parcheado desde CMDBs (ServiceNow, etc.) y sistemas ISMS. |
| **Escáner OSS** | Motor de análisis de licencias basado en SPDX/CycloneDX. Detección de componentes con vulnerabilidades conocidas (NVD/CVE). |
| **Analizador de contratos cloud** | NLP especializado para extracción de: SLAs (disponibilidad, RPO/RTO), DPAs, cláusulas de portabilidad, lock-in, indemnidad, escrow. |
| **Motor de scoring y priorización** | Scoring multicriteria: riesgo técnico (CVSS × exposición) + riesgo legal (cumplimiento RGPD) + riesgo de negocio (impacto operativo). Priorización para remediación. |
| **Tablero de riesgos** | Dashboard con mapa de tratamientos, scoring de madurez, vulnerabilidades, licencias OSS, vendor dependencies. Drill-down a evidencia. Enlaces a contratos relevantes de Skill 1. |

### 7.8 Controles de Calidad y Compliance

- **Pruebas de proporcionalidad y minimización:** El escaneo de sistemas de la target se limita a metadata y configuraciones. No se accede a datos de producción salvo en ventana aprobada por el vendedor con supervisión conjunta.
- **Cadena de custodia de informes:** Cada informe de vulnerabilidad o auditoría se clasifica como "Confidencial — DD" con hash de integridad y distribución controlada.
- **Exclusión de entornos productivos:** Por defecto, no se realizan tests de penetración activos ni escaneos intrusivos. Solo análisis de documentación y resultados de auditorías previas. Excepciones: con autorización escrita del vendedor y dentro de ventana técnica aprobada.
- **Seudonimización de datos de usuarios:** Si se procesan logs o datos de uso de sistemas, los identificadores de usuarios se seudonimizan.
- **NDA reforzado:** Todo el equipo IT/cyber de DD firma NDA específico que incluye obligaciones de destrucción de hallazgos técnicos al cierre del mandato.

### 7.9 KPIs de Rendimiento

| KPI | Objetivo |
|-----|----------|
| % DPAs adecuados | Identificación del 100% de encargados del tratamiento y verificación de DPA conforme |
| Nº vulnerabilidades críticas cerradas pre-closing | 100% de CVSS ≥ 9.0 remediadas; ≥ 80% de CVSS ≥ 8.0 |
| Cobertura de inventario OSS | ≥ 95% de componentes OSS identificados y licencias verificadas |
| Tiempo a remediación (TTR) | Propuesta de plan de remediación en ≤ 48 horas desde identificación de riesgo crítico |
| Precisión de scoring de madurez | ≤ 0.5 puntos de desviación vs. evaluación externa independiente |

### 7.10 Riesgos y Mitigación

| Riesgo | Mitigación |
|--------|-----------|
| Informes de auditoría desactualizados | Verificación de fecha de último informe. Flag si >12 meses. Recomendación de nueva evaluación como condición de cierre. |
| Shadow IT (sistemas no inventariados) | Análisis de gastos IT (facturas de cloud, SaaS) para identificar servicios no documentados. Cuestionario de management sobre "bring your own" y herramientas no autorizadas. |
| Acceso a datos sensibles durante la DD | Entornos espejo (sandbox) con datos seudonimizados. No acceso a producción. NDA reforzado con cláusulas de destrucción. |
| Transposición de NIS2 durante el deal | Monitor legislativo activo. Evaluación proactiva de cumplimiento NIS2 incluso antes de la transposición formal. Cláusula de ajuste en SPA. |
| Componentes OSS con vulnerabilidades zero-day | Monitorización continua de NVD/CVE durante el periodo de DD. Alerta inmediata si aparece CVE crítico en componente detectado. |

### 7.11 Plan de Pruebas

#### Caso 1: Transferencias internacionales sin SCC
Target con operaciones en Latinoamérica y proveedor de hosting en EE.UU. sin SCC ni adhesión al Data Privacy Framework. Verificar: detección del gap, clasificación como riesgo alto, propuesta de remediación (firma de SCC modulares, TIA), condición de cierre.

#### Caso 2: Dependencia de un único proveedor cloud sin escrow
Target con toda su infraestructura en un único proveedor cloud (single vendor), contrato sin cláusula de escrow de código fuente ni plan de portabilidad. Verificar: detección del vendor lock-in, scoring de riesgo alto, propuesta de negociación de escrow y plan de contingencia.

#### Caso 3: Bibliotecas copyleft en producto comercial
Producto SaaS de la target que integra una biblioteca con licencia AGPL v3. Distribución comercial a clientes. Verificar: detección del riesgo copyleft, flag de severidad máxima (obligación de liberar código fuente), cuantificación del impacto (pérdida de IP propietaria), remediación propuesta (sustituir componente o negociar licencia comercial).

#### Caso 4: Incidentes no notificados
En el data room aparecen menciones a un "incidente de seguridad" en un email interno, pero no hay registro formal de brecha ni notificación a la AEPD. Verificar: flag de posible incumplimiento del art. 33 RGPD, cuantificación del riesgo sancionador, inclusión en R&W del SPA, investigación adicional en management Q&A.

#### Caso 5: Cross-reference con Skill 1 (contratos IT con CoC)
Proveedor crítico de ERP cloud con cláusula de terminación por cambio de control del cliente. Verificar: detección en Skill 5 como dependencia crítica, cross-reference con Skill 1 (debe aparecer en matriz de consentimientos), plan de acción coordinado (obtener waiver antes de signing o negociar alternativa).

---

## 8. Anexo: Verificación de Referencias Normativas

Todas las referencias normativas citadas en este documento han sido verificadas individualmente contra fuentes oficiales. A continuación se presenta el resumen de verificación.

### A.1 Skill 1 — Contracts CoC & Consents Mapper

| Referencia | Estado |
|-----------|--------|
| Código Civil (arts. 1112, 1205, 1255) | **VERIFICADA.** Artículos vigentes sobre libertad contractual, transmisibilidad de derechos y novación. |
| Código de Comercio | **VERIFICADO.** RD de 22 de agosto de 1885, según enmendado. Regula contratos mercantiles. |
| RDL 1/2010 (LSC) | **VERIFICADO.** BOE-A-2010-10544. Ley de Sociedades de Capital. Transmisión de participaciones, gobierno corporativo. |
| RDL 2/2015 (ET), art. 44 | **VERIFICADO.** BOE-A-2015-11430. Sucesión de empresa, subrogación de trabajadores. |
| Ley 29/1994 (LAU) | **VERIFICADA.** Arrendamientos Urbanos. Art. 32 (cesión y subarriendo), Art. 34 (enajenación). |
| Ley 9/2017 (LCSP) | **VERIFICADA.** Contratos del Sector Público. Arts. 214 y ss. sobre cesión de contratos. |

### A.2 Skill 2 — Contingencies & Off-Balance Harvester

| Referencia | Estado |
|-----------|--------|
| PGC (RD 1514/2007) | **VERIFICADO.** BOE-A-2007-19884. NRV 15 (Provisiones y Contingencias), NRV 16 (Pasivos por retribuciones LP). |
| IAS 37 | **VERIFICADA.** IASB, versión actualizada 2022. Provisiones, pasivos contingentes y activos contingentes. |
| NIIF 16 | **VERIFICADA.** Arrendamientos. Vigente desde 01/01/2019. |
| Código Civil (arts. 1822-1856) | **VERIFICADO.** Régimen de fianza (garantía personal). |
| TRLC (RDL 1/2020) | **VERIFICADO.** BOE-A-2020-4859. Texto Refundido Ley Concursal. Cross-default, ipso facto clauses. Modificado 2022. |
| Ley 5/2015 | **VERIFICADA.** Fomento de la Financiación Empresarial. Cesión de créditos, factoring. |

### A.3 Skill 3 — Regulatory & FDI Notifications Planner

| Referencia | Estado |
|-----------|--------|
| Ley 19/2003 | **VERIFICADA.** BOE-A-2003-13471. Régimen de movimientos de capitales y FDI. |
| RD 571/2023 | **VERIFICADO.** Nuevo Reglamento de inversiones exteriores. Sustituye al derogado RD 664/1999. En vigor desde 01/09/2023. |
| RDL 34/2020 | **VERIFICADO.** FDI screening ampliado. Extendido hasta 31/12/2026 por RDL 1/2025. |
| Reglamento (UE) 2019/452 | **VERIFICADO.** Marco de control de inversiones extranjeras directas en la UE. |
| Ley 15/2007 (LDC) | **VERIFICADA.** Defensa de la Competencia. CNMC. Umbrales de notificación de concentraciones. |
| RD 261/2008 | **VERIFICADO.** Reglamento de Defensa de la Competencia. Procedimientos de concentraciones. |
| Reglamento (CE) 139/2004 | **VERIFICADO.** Reglamento comunitario de concentraciones. Dimensión comunitaria. |
| Ley 10/2014 | **VERIFICADA.** BOE-A-2014-6726. Entidades de crédito. Participaciones significativas. |
| RD 664/1999 | **DEROGADO.** BOE-A-1999-9938. Sustituido por RD 571/2023. No debe citarse como vigente. |

### A.4 Skill 4 — People & Labor Exposure Analyzer

| Referencia | Estado |
|-----------|--------|
| RDL 2/2015 (ET) | **VERIFICADO.** BOE-A-2015-11430. Arts. 44, 51, 52, 53, 56. NOTA: art. 52.d derogado por RDL 4/2020. |
| RD 1483/2012 | **VERIFICADO.** BOE-A-2012-13419. Reglamento de despido colectivo (ERE). 48 artículos. |
| Ley 10/2021 | **VERIFICADA.** BOE-A-2021-11472. Trabajo a distancia. Umbral: ≥30% jornada en 3 meses. |
| LISOS (RDL 5/2000) | **VERIFICADO.** BOE-A-2000-15060. Infracciones y Sanciones Orden Social. |
| RD 902/2020 | **VERIFICADO.** BOE-A-2020-12215. Igualdad retributiva. Registro y auditoría retributiva. |
| RD 901/2020 | **VERIFICADO.** BOE-A-2020-12214. Planes de igualdad obligatorios (>50 trabajadores). |
| TRLGSS (RDL 8/2015) | **VERIFICADO.** Ley General de Seguridad Social. Cotizaciones y responsabilidad del sucesor. |

### A.5 Skill 5 — Privacy, Cyber & IT Readiness Scanner

| Referencia | Estado |
|-----------|--------|
| RGPD (Reglamento UE 2016/679) | **VERIFICADO.** En vigor desde 25/05/2018. Directamente aplicable. |
| LOPDGDD (LO 3/2018) | **VERIFICADA.** BOE 06/12/2018. Complementa RGPD en España. |
| RDL 12/2018 | **VERIFICADO.** BOE-A-2018-12257. Transposición NIS. Desarrollado por RD 43/2021 (BOE-A-2021-1192). |
| Directiva NIS2 (UE) 2022/2555 | **VERIFICADA.** 14/12/2022. NO TRANSPUESTA en España (febrero 2026). Anteproyecto aprobado 14/01/2025, pendiente tramitación. Comisión Europea: dictamen motivado mayo 2025. |
| ENS (RD 311/2022) | **VERIFICADO.** BOE-A-2022-7191. Esquema Nacional de Seguridad. 74 controles. |
| SCC (Decisión 2021/914) | **VERIFICADA.** Cláusulas Contractuales Tipo modulares para transferencias internacionales. |
| CJUE Schrems II (C-311/18) | **VERIFICADA.** Sentencia de 16/07/2020. Invalida Privacy Shield, exige TIA para SCC. |

---

**Nota final:** La versión vigente de todas las normas ha sido comprobada a fecha de febrero de 2026. Se recomienda monitorizar el BOE, EUR-Lex y los boletines de las autoridades sectoriales para actualizaciones posteriores. En particular, debe seguirse de cerca la tramitación parlamentaria de la transposición de la Directiva NIS2, que ampliará significativamente las obligaciones de ciberseguridad cuando entre en vigor.

---

*Versión 1.0 — Febrero 2026 — Documento generado con verificación normativa exhaustiva.*
