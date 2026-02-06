---
name: force-majeure-trigger
description: Monitorizar eventos geopolíticos/climáticos para detectar activación de claúsulas de fuerza mayor en cartera de contratos de suministro. Analizar hardship vs fuerza mayor (Art. 1105 CC, Art. 1258 CC, STS 820/2013), comparar vs common law frustration. Aplicar test acumulativo de imprevisibilidad, inevitabilidad, externalidad y nexo causal (Art. 1105 CC) con checklist probatoria. Analizar rebus sic stantibus (Art. 1258 CC) para hardship. Usar embeddings semánticos para match evento-cláusula, cuantificar impacto (días de suspensión, costes adicionales), generar notificaciones formales con deadlines contractuales. Incluir análisis de gaps de cobertura de seguros. NOTA: Análisis caso-por-caso obligatorio; automatización es screening, no conclusión legal. Contextos: crisis Mar Rojo impactando supply chain EU, pandemia, disruption regulatory.
---

# Force Majeure Trigger & Supply Chain Risk

## Monitorización y Activación de Cláusulas de Fuerza Mayor

La fuerza mayor (impossibilidad de cumplimiento por causa externa no imputable) se distingue de hardship (cumplimiento posible pero extraordinariamente oneroso). En España: Art. 1105 CC define fuerza mayor; Art. 1258 CC hardship contractual; STS 820/2013 principio de rebus sic stantibus.

---

## Topología de Procesamiento

```
┌───────────────────┐ ┌──────────────────┐ ┌────────────────────┐
│ Event feeds       │→│ Event            │→│ Semantic            │
│ (Reuters, GDELT,  │ │ classification   │ │ embedding           │
│ custom RSS)       │ │ (geopolitical,   │ │ similarity search   │
│                   │ │ climate, supply) │ │ vs contract clauses │
└───────────────────┘ └──────────────────┘ └──────────┬─────────┘
                                                      │
        ┌──────────────────┬────────────────┬─────────┴─────────────┐
        │                  │                │                       │
        ▼                  ▼                ▼                       ▼
    Match score       Hardship vs        Notification        Insurance
    (>0.75 alert)    FM distinction      requirements         coverage analysis
        │                  │                │                       │
        └──────────────────┴────────────────┴───────────────────────┘
                           ▼
         Alert generation + template drafting + escalation

---

## Aplicar cuando

- **Red Sea/Strait of Hormuz disruptions**: detectar impacto en supply chains EU (mari-time rerouting)
- **Pandemia/cuarentena**: cierre de puertos, fronteras, restricciones laborales
- **Conflictos geopolíticos**: sanciones, embargos sobre proveedores/materiales
- **Catástrofes climáticas**: huracanes en Golfo México (petróleo), terremotos en Asia (semiconductores)
- **Regulatorio súbito**: embargos nuevos, cambio de normas arancelarias
- **Evaluación de hardship vs FM**: cumplimiento posible pero extraordinariamente oneroso requiere renegociación vs suspensión

---

## Clasificación de Eventos & Doctrinas Legales

### Categorías de Eventos Monitorizados

| Categoría | Ejemplos | Activación Típica FM |
|-----------|----------|---------------------|
| **Geopolítico** | Guerra, sanciones, embargos, bloqueos | Sí (bloqueo puertos Mar Rojo) |
| **Climático** | Huracanes, terremotos, inundaciones | Sí (si causa suspensión física) |
| **Pandémico** | Pandemias, cuarentenas oficiales | Condicionado (lockdown de gobierno) |
| **Infraestructura** | Cortes eléctricos, fallo puertos, ciberataques | Condicionado (si no previsible) |
| **Regulatorio** | Embargos nuevos, cambios arancelarios súbitos | No FM (hardship) |

### Doctrinas Legales: FM vs Hardship vs Frustration

| Doctrina | Jurisdicción | Requisitos | Efecto | Referencia |
|----------|-------------|-----------|--------|-----------|
| **Fuerza Mayor** | España/EU | Evento imprevisible, inevitable, externo, causa impossibilidad | Suspensión/resolución | CC Art. 1105, STS 820/2013 |
| **Hardship (Rebus Sic Stantibus)** | España/EU | Evento post-firma, cambio circunstancias, cumplimiento posible pero extraordinariamente oneroso | Renegociación | CC Art. 1258, UNCITRAL, Ley 3/1991 |
| **Frustration of Purpose** | Common law UK/US | Event voids essential purpose, no fault | Discharge (resolución) | Krell v Henry doctrine |

**Ejemplo de distinción**:
- Red Sea bloqueo: **FM** = imposible transportar (suspensión válida)
- Aumento 300% combustible: **Hardship** = cumplimiento posible, renegociar
- Mercado desaparece: **Frustration** = purpose no longer achievable

---

## Test de Imprevisibilidad, Inevitabilidad y Ruptura de Base del Negocio

### Test de Fuerza Mayor (4 Requisitos Acumulativos - Art. 1105 CC)

Para que un evento califique como fuerza mayor en España, TODOS los siguientes requisitos deben cumplirse simultáneamente. La ausencia de uno solo descarta la calificación de FM.

#### 1. Imprevisibilidad: ¿Era el evento razonablemente previsible al tiempo de contratar?

**Criterio Jurisprudencial**: La previsibilidad se evalúa desde la perspectiva de una persona media en la posición del contratante, considerando el sector, contexto geográfico y temporal en que se celebró el contrato.

**Análisis de Imprevisibilidad**:
- **Referencia**: STS 820/2013 (rebus sic stantibus) y jurisprudencia sobre causa extraña
- **Test práctico**: ¿Existían informes públicos, advertencias de organismos internacionales, o reportes sectoriales sobre el riesgo específico antes de la firma?
  - Ejemplo 1: Pandemia COVID-19 en contratos celebrados **antes de diciembre 2019** → IMPREVISIBLE
  - Ejemplo 2: Pandemia COVID-19 en contratos celebrados **en 2021 o 2022** → PREVISIBLE (ya conocido el riesgo pandémico)
  - Ejemplo 3: Crisis Mar Rojo (Ataques hutíes enero 2024) en contrato celebrado 2022 → PREVISIBILIDAD CONDICIONADA: ¿Mencionaba expresamente "bloqueos marítimos Oriente Medio"?
- **Red flag crítica**: Si el contrato fue celebrado DESPUÉS de que el riesgo fuera conocido públicamente, la carga de prueba se invierte

**Checklist de Imprevisibilidad**:
- [ ] ¿Existían reportes públicos de organismos internacionales (ONU, IMO, WTO) sobre el riesgo antes de la firma?
- [ ] ¿Tenía conocimiento experto el sector sobre el riesgo (reportes sectoriales, associaciones comerciales)?
- [ ] ¿Se mencionó el riesgo específico en documentos previos de negociación o análisis de riesgo?
- [ ] ¿El contrato fue celebrado ANTES o DESPUÉS de que el riesgo fuera conocido?
- [ ] ¿Las cláusulas de riesgo del contrato excluían expresamente este tipo de eventos?

---

#### 2. Inevitabilidad: ¿Podía haberse evitado con diligencia razonable?

**Criterio Jurisprudencial**: No basta con que el evento sea imprevisible; además debe ser imposible evitarlo incluso adoptando medidas de mitigación disponibles y proporcionadas en coste.

**Análisis de Inevitabilidad**:
- **Medidas de mitigación disponibles**:
  - Rerouting alternativo (Suez, Cabo Buena Esperanza) → ¿Incremento de coste proporcional?
  - Proveedores alternativos en regiones no afectadas → ¿Requiere renegociación contractual?
  - Almacenamiento preventivo anterior → ¿Técnicamente posible?
  - Seguros de cobertura previa → ¿Estaban disponibles?

- **Ejemplo 1: Bloqueo Suez (2021)**
  - Rerouting Cabo Buena Esperanza: +15 días, +€180-250k/contenedor
  - Análisis: ¿Incremento >300% = inevitable? → Posiblemente SÍ (hardship, no FM pura)
  - Si incremento <50% = HARDSHIP (no FM)

- **Ejemplo 2: Ciberataque a Proveedor**
  - Pregunta crítica: ¿Tenía el proveedor estándares ISO 27001 de seguridad previos?
  - Si SÍ → ataque sofisticado = INEVITABLE (FM probable)
  - Si NO → negligencia propia = NO FM (imputabilidad)

**Checklist de Inevitabilidad**:
- [ ] ¿Existían medidas de mitigación técnicamente posibles?
- [ ] ¿Cuál era el coste proporcional de cada medida?
- [ ] ¿Se implementaron medidas de mitigación disponibles? (o prueba de por qué no)
- [ ] ¿Había cláusulas contractuales que permitían redireccionamiento automático?
- [ ] ¿Se documentó internamente la evaluación de alternativas y su viabilidad?

---

#### 3. Externalidad: ¿El evento es ajeno a la esfera de control del obligado?

**Criterio Jurisprudencial**: El evento no debe ser imputable a negligencia propia ni de sus dependientes. Es un análisis de causalidad y responsabilidad.

**Análisis de Externalidad**:
- **Eventos claramente externos**:
  - Terremoto natural → SÍ (externo)
  - Ataque militar/terrorista → SÍ (externo, salvo negligencia de seguridad propia)
  - Cierre gubernamental de frontera → SÍ (externo)

- **Eventos con componente de imputabilidad**:
  - Fallo en infraestructura crítica del proveedor (datacenter down) → ¿Tenía mantenimiento preventivo? ¿Backup systems?
  - Ciberataque al proveedor → ¿Tenía estándares de seguridad razonables? (ISO 27001, auditorías externas)
  - Fallo de transporte → ¿Se eligió ruta de alto riesgo? ¿Había alternativas más seguras?

- **Ejemplo Critical**: Crisis Mar Rojo 2024
  - Externalidad: Ataques hutíes = evento geopolítico, no controlable por proveedor
  - BUT: Si el proveedor NO tenía plan de continuidad, NO tenía seguros de cobertura → ¿Negligencia contractual?
  - Conclusión: Evento externo, pero responsabilidad limitada si hay negligencia en preparación

**Checklist de Externalidad**:
- [ ] ¿Es el evento resultado de acción humana deliberada ajena al contratante?
- [ ] ¿Existe documentación de que el contratante/proveedor tomó medidas de precaución razonables?
- [ ] ¿Hay evidencia de negligencia propia en seguridad, mantenimiento, o gestión de riesgos?
- [ ] ¿Se puede demostrar que el evento estaba fuera de la esfera de control del obligado?

---

#### 4. Nexo Causal: ¿El evento causa DIRECTAMENTE la imposibilidad de cumplimiento?

**Criterio Jurisprudencial**: No basta con dificultad o onerosidad; la FM requiere **imposibilidad** objetiva. La distinción es: FM = imposibilidad; Hardship = cumplimiento posible pero extraordinariamente oneroso.

**Análisis de Nexo Causal**:
- **Imposibilidad vs Dificultad**:
  - Delay 15 días + deadline contractual 30 días → DIFICULTAD, no imposibilidad
  - Bloqueo puerto durante 90 días + contrato requiere entrega en 45 días → IMPOSIBILIDAD
  - Incremento coste 300% + margen de beneficio 10% → HARDSHIP (no imposibilidad)

- **Causas que rompen nexo causal**:
  - Falta de diligencia en mitigación evita demostrar nexo
  - Cumplimiento parcial o alternativo posible = nexo débil
  - Terceros intermediarios capaces de resolver = nexo débil

- **Ejemplo 1: Red Sea Bloqueo vs Delay**
  - Evento: Bloqueo Mar Rojo desde 10 enero → rerouting +15 días
  - Contrato: Entrega requiere 30 días (más tiempo disponible que delay)
  - Análisis: ¿Verdadera imposibilidad o mera dificultad?
    - Si: Único cliente en ruta Mar Rojo, alternativas no existen → IMPOSIBILIDAD → FM
    - Si: Alternativas existen (aéreo, Suez, tercer proveedor) → HARDSHIP

- **Ejemplo 2: Cierre de Puerto**
  - Evento: Puerto principal de carga cierra por 30 días (huracán)
  - Pregunta: ¿Hay puertos alternativos a distancia razonable?
  - Respuesta: Sí → HARDSHIP (imposibilidad mitigable)
  - Respuesta: No → IMPOSIBILIDAD → FM

**Checklist de Nexo Causal**:
- [ ] ¿Es la imposibilidad de cumplimiento DIRECTA (no mediada por terceros)?
- [ ] ¿Hay alternativas de cumplimiento técnicamente posibles?
- [ ] ¿Cuál es la duración de la imposibilidad vs deadline contractual?
- [ ] ¿Se han documentado intentos de cumplimiento alternativo?
- [ ] ¿La naturaleza del cumplimiento permite ejecución parcial?

---

### Test Integrado de Fuerza Mayor (Checklist de Activación)

Para cada evento FM sospechado, completar esta matriz:

```
EVENTO: [Descripción]
CONTRATO ID: [Referencia]
FECHA ANÁLISIS: [Hoy]
ANALISTA: [Nombre]

REQUISITO                    | CUMPLE | PRUEBA DOCUMENTAL                      | OBSERVACIONES
─────────────────────────────────────────────────────────────────────────────────
Imprevisibilidad             | ☐ SÍ ☐ NO | [Reportes públicos previos, fecha]   |
Inevitabilidad               | ☐ SÍ ☐ NO | [Medidas evaluadas, costes]         |
Externalidad                 | ☐ SÍ ☐ NO | [Negligencia propia descartada]     |
Nexo Causal (Imposibilidad)  | ☐ SÍ ☐ NO | [Alternativas documentadas]         |

CONCLUSIÓN:
☐ FM ACTIVABLE (4/4 requisitos)
☐ HARDSHIP / REBUS STIC STANTIBUS (imposibilidad mitigable, >50% incremento)
☐ NO APLICA (<3 requisitos)

RIESGO JURÍDICO: ___/10
DEADLINE NOTIFICACIÓN: [Días hasta vencimiento]
```

---

### Test de Rebus Sic Stantibus (Art. 1258 CC + STS 820/2013)

Cuando la imposibilidad es mitigable pero el coste se vuelve extraordinario, aplica la doctrina de rebus (hardship). Los cinco requisitos deben evaluarse de forma acumulativa:

#### Requisitos del Test de Rebus:

1. **Alteración Extraordinaria e Imprevisible de Circunstancias (Temporalidad)**
   - Evento debe ocurrir DESPUÉS de la celebración del contrato
   - Cambio debe ser extraordinario (fuera del riesgo normal del sector)
   - Ejemplo: Inflación normal 2-3% = NO extraordinaria; inflación 150% = SÍ extraordinaria

2. **Desproporción Exorbitante en Prestaciones (Onerosidad)**
   - No basta mera onerosidad o dificultad; requiere desproporción grave
   - Referencia: STS 820/2013 propone umbral de desproporción "grave y patente"
   - Indicadores prácticos:
     - Incremento de coste >50% = posible rebus
     - Incremento >100% = probable rebus
     - Incremento >300% = rebus muy probable
   - Ejemplo: Flete sube €50k → si margen contrato €200k = HARDSHIP; si margen €2M = NO rebus

3. **Ausencia de Otro Medio para Remediar el Desequilibrio (Subsidiariedad)**
   - ¿Hay cobertura de seguros activable?
   - ¿Hay renegociación posible con terceros?
   - ¿Hay cláusulas contractuales de ajuste de precios?
   - Si existían opciones, rebus es subsidiario (último recurso)

4. **Buena Fe y Equidad (Art. 1258 CC)**
   - Ambas partes actuaron de buena fe (desconocían el riesgo)
   - No hubo aceptación expresa del riesgo en contrato
   - La parte demandante no se benefició de la asunción de riesgo
   - Ejemplo: No puede invocar hardship quien específicamente aceptó "asumir todos los riesgos de coste"

5. **No Asunción Expresa del Riesgo (Cláusulas de Exclusión)**
   - Análisis de cláusulas contractuales:
     - "Cualquier riesgo de aumento de coste corre a cargo del comprador" → EXCLUYE rebus
     - "Incluye todos riesgos conocidos y desconocidos" → EXCLUYE rebus (pero no FM imposibilidad)
     - Ausencia de cláusula = presunción a favor de rebus
   - Jurisprudencia: STS 820/2013 permite rebus incluso sin cláusula expresa, si buena fe + extraordinariedad

**Checklist de Rebus Sic Stantibus**:
- [ ] ¿Evento ocurrió DESPUÉS de firma del contrato?
- [ ] ¿Alteración es extraordinaria para el sector/período?
- [ ] ¿Incremento de coste supera 50%? ¿100%? ¿300%?
- [ ] ¿Existen seguros o cláusulas de ajuste activables?
- [ ] ¿Ambas partes actuaban de buena fe sin conocer el riesgo?
- [ ] ¿Contrato NO incluye cláusula de aceptación expresa del riesgo?

---

## Checklist Probatoria

### Activación de Cláusula de Fuerza Mayor

Para establecer una defensa sólida de FM ante un incumplimiento, se debe recopilar y preservar TODA la siguiente documentación:

#### A. Documentos de Prueba del Evento (Primera línea)

**Categoría 1: Eventos Marítimos/Transporte**
- [ ] Manifiestos de embarque (Bills of Lading) mostrando ruta original y alterada
- [ ] Avisos oficiales de cierre/restricción de puertos (Port Authority notices)
- [ ] Comunicaciones de transportistas confirming bloqueo/demora
- [ ] Cartas de asociaciones navieras (Cámara Marítima, Lloyd's List)
- [ ] Certificados de Force Majeure de Cámara de Comercio (ICC)
- [ ] Mapas/gráficos de ruta inicial vs rerouting con incremento de distancia

**Categoría 2: Eventos Climáticos**
- [ ] Reportes de autoridades meteorológicas nacionales
- [ ] Declaraciones gubernamentales de estado de emergencia/desastre natural
- [ ] Comunicaciones de Protección Civil
- [ ] Fotografías/vídeos de daños (cuando proceda)
- [ ] Inspecciones técnicas de infraestructura dañada

**Categoría 3: Eventos Geopolíticos/Regulatorios**
- [ ] Decrees/Órdenes gubernamentales (cierre frontera, embargo, etc.)
- [ ] Comunicaciones diplomáticas oficiales
- [ ] Reportes de organismos internacionales (ONU, Banco Mundial, WTO)
- [ ] Comunicados de sanciones (OFAC, EU sanctions list)
- [ ] Certificados de autoridades locales (cierres de industrias)

**Categoría 4: Eventos Pandémicos**
- [ ] Decretos de lockdown/cuarentena oficiales (BOE, Diario Oficial equivalente)
- [ ] Restricciones laborales emitidas por autoridades sanitarias
- [ ] Órdenes de cierre de instalaciones emitidas por autoridades
- [ ] Comunicaciones del ministerio de industria/comercio

---

#### B. Documentos de Conocimiento Temprano (Timing)

Esencial para probar "inmediatez" de notificación contractual (usualmente 10-30 días):

- [ ] **Emails/Mensajería**: Primeros avisos internos sobre el evento (timestamps)
- [ ] **Notas de reuniones**: Logs de meetings donde se discutió impacto (con fechas)
- [ ] **Comms de proveedores**: Avisos de transportistas/suministradores sobre bloqueo
- [ ] **News clippings**: Pantallazos de noticias públicas con timestamp
- [ ] **Registros de sistemas**: Logs de monitoreo de suministros con alertas automáticas

**Red flag crítica**: Si no hay evidencia de "conocimiento" hasta semanas después del evento público, se debilita el argumento de "notificación oportuna"

---

#### C. Documentos de Mitigación (Diligencia)

Para demostrar que se hizo todo lo posible (requisito de "inevitabilidad"):

- [ ] **Análisis de alternativas**: Documentos internos evaluando rerouting, proveedores alternativos
- [ ] **Cotizaciones de alternativas**: Presupuestos de rutas alternativas (aéreo, Suez, etc.)
- [ ] **Comunicaciones con transportistas**: Solicitudes de rerouting, respuestas sobre viabilidad
- [ ] **Gestión de inventario**: Registros de intentos de almacenamiento preventivo
- [ ] **Plan de continuidad activado**: Documentación de fallback mechanisms (proveedores B, C)
- [ ] **Comunicaciones con cliente**: Avisos al comprador sobre opciones de mitigación

**Importante**: Falta de documentación de intentos de mitigación debilita DECISIVAMENTE la defensa de FM. La jurisprudencia requiere probar "diligencia" activa.

---

#### D. Documentos de Impacto Cuantificado

Necesarios para defensa, notificación contractual y potencial reclamo:

- [ ] **Análisis de calendario**: Gráficos comparativos (fecha entrega original vs efectiva)
- [ ] **Cálculo de costes adicionales**:
  - Incremento de flete (€/contenedor o €/kg)
  - Costes de almacenamiento (días × coste diario)
  - Costes de aéreo si se optó por mitigación
  - Costes de gestión administrativos
- [ ] **Impacto en cliente**: Penalizaciones contractuales, demandas por retraso
- [ ] **Análisis de materialidad**: ¿Supone el incremento >5% del valor del contrato?
- [ ] **Comparativa sectorial**: ¿Otros operadores sufrieron impacto similar?

---

#### E. Documentos de Seguros

Para análisis de cobertura y activación de claims:

- [ ] **Pólizas activas**: Copia de póliza de Business Interruption, Supply Chain, War/Terrorism
- [ ] **Carátulas de cobertura**: Detalles de exclusiones y límites
- [ ] **Comunicaciones a asegurador**: Notificaciones de pérdida dentro de plazo
- [ ] **Documentación de claims**: Solicitud formal con todos soportes
- [ ] **Exclusiones analysis**: Memo interno sobre qué está/NO cubierto

---

#### F. Documentos de Comunicación Contractual

Proof de cumplimiento de obligaciones de notificación:

- [ ] **Notificación a contraparte**: Copia de FM notice con acuse de recibo
- [ ] **Forma de envío**: Certificado de email, correo registrado, mensajería courier
- [ ] **Plazo de notificación**: Cálculo de "10 días hábiles desde conocimiento"
- [ ] **Contenido de notificación**: Descripción evento, impacto, duración estimada, plan de remedio
- [ ] **Respuesta de contraparte**: Acuses de recibo, comunicaciones posteriores

---

### Chain of Evidence (Cadena de Custodia) - LEC Arts. 299-386

Para que la evidencia sea admisible en litigio, seguir estos protocolos:

1. **Originales o Certificados Auténticos**
   - Documentos originales preferidos (menos problemas de autenticidad)
   - Si digitales: descargar original y guardar con timestamp de descarga
   - No editados, no capturados de pantalla (excepto con timestamp)

2. **Preservación de Integridad**
   - Almacenar en servidor seguro (no USB intercambiables)
   - Crear hash criptográfico (SHA-256) de cada documento
   - Mantener log de acceso (quién, cuándo, para qué)
   - NO eliminar emails/chats después de "limpieza"

3. **Timestamps y Provenance**
   - Cada documento debe llevar timestamp verificable
   - Diferenciar: fecha de evento vs fecha de conocimiento vs fecha de notificación
   - Usar servidores de timestamps certificados para documentos críticos

4. **Segregación de Prueba Privilegiada**
   - Separar documentos de abogado/asesor legal (privilegio)
   - NO mezclar prueba de FM con privilegio abogado-cliente
   - Riesgo: si se entrega al contrario, pierdes privilegio

---

### Template: Protocolo de Preservación de Evidencia (Immediate Actions)

```
EVENTO FM SOSPECHADO: _________________
FECHA EVENTO: _________________
FECHA CONOCIMIENTO: _________________

ACCIONES INMEDIATAS (Primeras 24-48 horas):

1. LEGAL HOLD NOTICE (comunicación interna)
   - [ ] Notificar a Legal, Finance, Operations
   - [ ] Instruir: "NO borren emails, chats, documentos relacionados"
   - [ ] Specify: "Todos docs sobre [evento] desde [fecha] en adelante"
   - [ ] Scope: Incluir correos personales si se usan para trabajo

2. DATA CAPTURE (día 1-2)
   - [ ] Descargar todos emails relevantes (EML format)
   - [ ] Capturar mensajes Slack/Teams (screenshot + export)
   - [ ] Guardar copias de Sharepoint/Google Drive (con versioning)
   - [ ] Screenshots de portales públicos (Reuters, shipping sites) con URL visible
   - [ ] Crear archivo ZIP con timestamp automático

3. CUSTODY CHAIN INITIATION
   - [ ] Registrar quién recopiló cada documento
   - [ ] Crear spreadsheet: Documento | Responsable | Fecha Captura | Hash SHA-256
   - [ ] Entregar copia a Legal + Finance (ambas firman recepción)

4. CHAIN OF COMMUNICATIONS
   - [ ] Compilar timeline de eventos (evento público → conocimiento → notificación)
   - [ ] Señalar hitos exactos con screenshots/timestamps
   - [ ] Memo interno: "Conocimos del evento el [fecha] via [fuente]"

5. EXCLUSIÓN DE PRIVILEGIO
   - [ ] Flag documentos de abogado/asesor (NO entregar)
   - [ ] Separar folder "Legally Privileged - Do Not Distribute"
   - [ ] Mantener lista de excluidos (por si descubrimiento electrónico)
```

---

## Aclaración: ICC Force Majeure Clause (2020) como Soft Law

La **ICC Force Majeure Clause 2020** es una referencia de **soft law** (práctica comercial internacional), **NO normativa vinculante**. Su importancia es:

- **Valor interpretativo**: Refleja estándares de industria sobre qué constituye FM
- **Valor orientativo**: Proporciona lenguaje modelo para cláusulas contractuales
- **NO vinculante**: En España, los requisitos sustantivos se rigen por:
  - **Art. 1105 CC**: Definición de fuerza mayor
  - **Art. 1258 CC**: Hardship (rebus sic stantibus)
  - **Jurisprudencia del TS**: STS 820/2013, SSTS sobre caso fortuito
  - **Ley 3/1991** (si aplica): Derecho de la competencia

**En litigio español**: Un juez puede citar ICC como "buena práctica internacional" pero la conclusión jurídica se basa en Código Civil + jurisprudencia TS, no en ICC per se.

**Recomendación contractual**: Si desea aplicar ICC como referencia, incluir cláusula expresa: *"Las partes adoptan la ICC Force Majeure Clause 2020 como marco interpretativo de los eventos de fuerza mayor, sin perjuicio de lo dispuesto en la legislación española aplicable."*

---

## Anti-Sobregeneralización: Análisis Caso-por-Caso Obligatorio

**ADVERTENCIA CRÍTICA**: La activación automática de FM basada en coincidencia de palabras clave ("bloqueo" detectado → FM automática) es **jurídicamente insuficiente** y expone a riesgo de incumplimiento injustificado.

### Limitaciones de Automatización

1. **Matching semántico no es conclusión legal**
   - Similarity score 0.87 = "evento PARECIDO a cláusula FM" ≠ "FM legalmente válida"
   - Ejemplo: "bloqueo portuario" en cláusula + "cierre administrativo 48h" en evento = match 0.75, pero:
     - Cláusula requiere "bloqueo >15 días"
     - Evento duró 2 días
     - CONCLUSIÓN: NO FM (automatización falla)

2. **Contexto jurídico varía por contrato**
   - Contrato Suministro A: "FM si evento >10 días"
   - Contrato Suministro B: "FM si evento >30 días, salvo si alternativas disponibles"
   - Contrato Suministro C: "FM excluida para events de [categoría específica]"
   - Mismo evento puede ser FM para A, NO FM para B, NO FM para C

3. **Negligencia/Diligencia propia afecta conclusión**
   - Evento: Ciberataque a proveedor
   - IF proveedor tenía seguridad ISO 27001 → FM probable
   - IF proveedor NO tenía seguridad básica → NO FM (imputabilidad)
   - Automatización no analiza estándares de seguridad previos

---

### Protocolo de Análisis Caso-por-Caso (Obligatorio)

**PASO 1: Screening automático (INDICADOR, NO CONCLUSIÓN)**
```
Evento detectado + similarity >0.75 con cláusula FM
→ FLAG como "Posible FM para análisis legal"
→ Generar alerta + enviar a equipo legal
→ NUNCA ejecutar notificación automática basada solo en score
```

**PASO 2: Análisis jurídico manual (OBLIGATORIO)**
```
Abogado/gestor legal revisa:
- ¿Evento coincide TEXTUALMENTE con cláusula FM? (no solo semánticamente)
- ¿Se cumplen 4 requisitos de Art. 1105 CC? (imprevisibilidad + inevitabilidad + externalidad + nexo)
- ¿Contrato contiene exclusiones o limitaciones de FM?
- ¿Existe documentación de diligencia/mitigación previas?
- ¿Plazo de notificación aún vigente?
- ¿Riesgo de incumplimiento injustificado si FM no se funda?
```

**PASO 3: Confianza y disclaimer**
```
SI análisis legal confirma FM → notificación con disclaimer:
"Esta notificación se basa en análisis jurídico; no es conclusión
definitiva sino comunicación de diligencia contractual conforme [Art.]"

SI análisis rechaza FM → NO notificar, documentar decisión

SI análisis es dudoso → "Analyzed as potential hardship rather than FM,
recommend renegotiation"
```

---

### Confianza en Automatización (Confidence Disclaimers)

Para cada análisis automático, reportar **nivel de confianza**:

| Confianza | Criterio | Acción Recomendada |
|-----------|----------|-------------------|
| **ALTA (>0.85)** | Similarity muy alta + evento en lista blanca categórica + prueba clara | Notificación inmediata + legal review |
| **MEDIA (0.70-0.85)** | Match claro pero requiere validación contextual | Escalada a legal para decisión |
| **BAJA (<0.70)** | Match débil o ambiguo + contexto contradictorio | Analysis hardship, NO activar FM |

**Ejemplo de Disclaimer en Reporte**:
```
CONTRATO: CTR-001 (Supply Agreement Asia Components)
EVENTO: Bloqueo Mar Rojo
SIMILARITY SCORE: 0.89
CONFIANZA: ALTA

DISCLAIMER:
"Este análisis de similaridad automática indica alta probabilidad
de coincidencia. Sin embargo, la conclusión de FM requiere validación
de: (1) imprevisibilidad según STS 820/2013, (2) diligencia de
mitigación, (3) nexo causal vs simple dificultad. Recomendamos
revisión legal antes de ejecutar cualquier defensa o notificación."
```

---



## Taxonomía UNCITRAL & ICC (2020 Model FM Clause)

### Nota Aclaratoria: ICC 2020 como Soft Law

**La ICC Force Majeure Clause (2020) es referencia de soft law, no normativa vinculante.** Su valor es interpretativo y orientativo. En España, los requisitos sustantivos de fuerza mayor se rigen por:
- **Art. 1105 CC**: Definición legal de caso fortuito/fuerza mayor
- **Art. 1258 CC**: Hardship (rebus sic stantibus)
- **Jurisprudencia del TS**: STS 820/2013, precedentes sobre causa extraña

En litigio español, un juez puede citar ICC como "buena práctica comercial internacional" pero basará su conclusión en Código Civil + jurisprudencia TS, **no en ICC per se**. Si desea aplicar ICC como marco contractual, incluya cláusula expresa: *"Las partes adoptan la ICC Force Majeure Clause 2020 como marco interpretativo, sin perjuicio de la legislación española aplicable."*

---

**ICC Force Majeure Clause (2020)** define eventos categóricos con thresholds:

```python
EVENTOS_FM_ICC = {
    "1. Actos de Dios": ["terremoto", "tsunami", "erupción volcánica"],
    "2. Actos de autoridades": ["guerra", "embargos", "cierres de puerto"],
    "3. Pandemias": ["si causa imposibilidad demostrada", "lockdown oficial"],
    "4. Infraestructura": ["si es resultado de evento FM", "no negligencia del contratante"],
}

REQUISITOS_NOTIFICACION = {
    "plazo": "10-30 días desde conocimiento",
    "forma": "Escrito con acuse de recibo",
    "contenido": [
        "Descripción precisa del evento",
        "Fecha de inicio y duración estimada",
        "Impacto en obligaciones contractuales",
        "Plan de mitigación y restauración",
        "Documentación de soporte"
    ]
}
```

---

## Análisis Semántico & Matching

### Semantic Similarity (Embeddings)

```python
# Usar embeddings pre-trained (Sentence-BERT, OpenAI) para matching
evento_desc = "Ataques hutíes en Mar Rojo causan desviación de rutas marítimas
               (+15 días, +€200k/contenedor de Asia)"
clausula_fm = "En caso de bloqueo marítimo internacional, acto de guerra o terrorismo
              que impida el transporte de mercancías, el proveedor queda exonerado
              de cumplimiento con notificación en 10 días hábiles."

similarity_score = cosine_similarity(embed(evento), embed(clausula))
# → 0.87 (MATCH PROBABLE)

# Información de contexto:
# - Evento = persistente (>10 días)
# - Tipo evento en cláusula = YES ("guerra", "bloqueo")
# - Notificación: deadline es HOY + 10 hábiles
```

### Matriz de Decisión: Threshold de Activación

| Score | Duración estimada | Acción | Urgencia |
|-------|------------------|--------|----------|
| > 0.85 | > 15 días | Activación → Notificación inmediata | CRÍTICA |
| 0.70-0.85 | 5-15 días | Análisis jurídico + notificación preventiva | ALTA |
| 0.60-0.70 | 1-5 días | Hardship assessment, renegociar | MEDIA |
| < 0.60 | N/A | No aplica FM, continuar cumplimiento | BAJA |

---

## Ejemplo Concreto: Red Sea Crisis (Enero 2024)

**Evento**: Ataques hutíes bloquean 15% del comercio marítimo global, rerouting a Cabo Buena Esperanza (+15 días, +€180-250k/contenedor)

**Cartera afectada**: 156 contratos de suministro EU (Asia Components, textiles Bangladesh, electrónica China)

### Output: Reporte de Activación

```json
{
  "evento": {
    "id": "EVT-2024-0156",
    "tipo": "GEOPOLITICO",
    "subtipo": "Bloqueo marítimo",
    "descripcion": "Ataques hutíes en estrecho de Bab el-Mandeb, cierre parcial Mar Rojo",
    "fecha_inicio": "2024-01-10",
    "paises_afectados": ["Yemen", "Egipto", "Arabia Saudí", "Somalia"],
    "fuentes": ["Reuters", "GDELT", "Lloyd's List"],
    "duracion_estimada": "indefinida (>90 días previstos)"
  },
  "cartera_analisis": {
    "contratos_revisados": 156,
    "con_clausula_fm": 142,
    "sin_clausula_fm": 8,
    "no_aplicable": 6
  },
  "contratos_afectados_criticos": [
    {
      "id": "CTR-001",
      "contrato": "Supply_Agreement_Asia_Components_2023.pdf",
      "proveedor": "Asia Components Ltd (Shanghai)",
      "monto_anual": 8500000,
      "similarity_score": 0.89,
      "clausula_fm": {
        "ubicacion": "Art. 12.3 - Force Majeure",
        "texto_clave": "bloqueo marítimo internacional, acto de guerra o terrorismo, imposibilidad de transporte",
        "requisitos": {
          "notificacion_plazo": "10 días hábiles desde conocimiento (END: 2024-01-20)",
          "forma": "Aviso escrito con acuse de recibo",
          "contenido": [
            "Descripción precisa del evento",
            "Impacto en obligaciones de entrega",
            "Duración estimada de la suspensión",
            "Plan de mitigación (rerouting, alternativas)",
            "Documentación (shipping manifests, port records)"
          ]
        }
      },
      "impacto_cuantificado": {
        "aumento_flete": 200000,
        "delay_entrega": 15,
        "aumento_coste_almacen": 75000,
        "total_impacto_mes": 275000,
        "materialidad": 3.2
      },
      "estado": "NOTIFICACION REQUEJRIDA",
      "deadline_notificacion": "2024-01-20",
      "dias_para_actuar": 3,
      "recomendacion": "Activar FM inmediatamente; documentar rerouting EUR alternative (Suez costoso pero factible)"
    },
    {
      "id": "CTR-002",
      "contrato": "Textiles_Bangladesh_JV.pdf",
      "proveedor": "BanglaFab Consortium",
      "similarity_score": 0.72,
      "clausula_fm": {
        "ubicacion": "Schedule A - FM Events",
        "texto_clave": "... actos de Dios o fuerzas externas ...",
        "gap": "Clausula AMBIGUA, no menciona explícitamente 'bloqueo', 'guerra'. Requiere análisis legal para FM activación."
      },
      "riesgo": "YELLOW",
      "recomendacion": "Considerar hardship (Art. 1258 CC) para renegociación de términos, no FM pura"
    }
  ],
  "insurance_coverage_analysis": {
    "póliza_existente": "Business Interruption + Supply Chain Insurance",
    "exclusiones": [
      "War and Terrorism: TYPICALLY EXCLUDED unless specific rider",
      "Delay in transit: Cubierto solo si interrupción >15 días",
      "Incremento de costes de transporte: EXCLUIDO en la mayoría de pólizas"
    ],
    "gaps": [
      {
        "concepto": "Aumento de flete Mar Rojo rerouting",
        "cobertura": "NO",
        "impacto": "€275k/mes sin cobertura",
        "recomendacion": "Negociar cláusula de pass-through de costes con proveedor"
      },
      {
        "concepto": "Suspensión de entrega (FM evento)",
        "cobertura": "SÍ - si >15 días",
        "deducible": "7 días",
        "limite": "50% de coste de producción"
      }
    ],
    "prima_incremental_recomendada": 45000,
    "rider_para_solicitar": "Geopolitical Contingency + War/Terrorism para supply chain"
  },
  "template_notificacion_generada": {
    "path": "fm_notification_Asia_Components_20240115.docx",
    "preview": "Estimado proveedor, Por la presente notificamos la ocurrencia de un evento de fuerza mayor..." +
              "Bloqueo del Mar Rojo ha generado imposibilidad de cumplimiento según Art. 12.3..."
  }
}
```

### Plantillas de Notificación (Generadas)

**Template 1: FM Formal Notice (Red Sea)**
```
De: Legal Dept
A: Proveedor
Asunto: Notificación de Fuerza Mayor - Evento Mar Rojo - Contrato Suministro 2023

Estimado [Proveedor],

Por la presente notificamos el evento de fuerza mayor que afecta a nuestro contrato
[REF] de suministro de [PRODUCTS] celebrado el [DATE].

EVENTO: Bloqueo parcial del Mar Rojo por ataques hutíes (desde 10 enero 2024).
IMPACTO: Imposibilidad de cumplimiento de entregas conforme Art. 12.3 del contrato,
  que expresamente incluye "bloqueo marítimo internacional" como evento de FM.
DURACIÓN: Estimada 60+ días (rerouting Cabo Buena Esperanza).
PLAN MITIGACIÓN: Exploramos (1) rerouting aéreo para items críticos, (2) almacenes
  alternativos en Singapur, (3) renegociación de calendario.

Esta notificación se realiza dentro del plazo contractual de 10 días hábiles.

Documentación adjunta: Port manifests, ruting confirmación, cartas de transportista.

Aguardamos coordinación para minimizar impacto conjunto.
```

---

## Sistema de Monitorización Continua

```python
monitor = ForceMajeureMonitor(
    contratos_dir="/contracts",
    feeds=["reuters_api", "bbc", "gdelt", "shipping_alerts"],
    similarity_threshold=0.70,
    event_categories=["geopolitical", "climate", "pandemic", "infrastructure"],
    notify_email="legal@empresa.com",
    escalation_levels=[
        (0.90, "CRITICAL - activate FM"),
        (0.75, "HIGH - analyze + draft notice"),
        (0.60, "MEDIUM - hardship assessment")
    ]
)

monitor.start()
# Alertas automáticas con notificación templates listos
```
