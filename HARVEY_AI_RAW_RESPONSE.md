# Harvey AI - Validación Jurídica LegalTech Skills Suite
## Respuesta completa exportada desde Harvey AI (eu.app.harvey.ai)
### Sesión: "LegalTech Suite Validation and Evaluation"
### URL: https://eu.app.harvey.ai/assistant/assist/409690812
### Fecha: Febrero 2026
### Fuente jurisdiccional: Spain (28 citas BOE.es)

---

## Prompt enviado

Actua como equipo legal multidisciplinar Magic Circle (socios de Litigios, M&A, Fiscal, Laboral, Compliance). Valida juridicamente esta suite de 27 skills LegalTech para TEE. Evalua: 1) Rigor juridico (refs normativas correctas/vigentes), 2) Viabilidad tecnica, 3) Etica/deontologia, 4) Calidad 1-10, 5) Mejoras para 10/10.

LITIGIOS: 1.Judicial Profiler (NLP sentencias CENDOJ, Art.24 CE, LOPJ), 2.BATNA Calculator (Game Theory, Ley 5/2012, Ley 60/2003), 3.Discovery Gap Hunter (BM25, Art.328-334 LEC, Haya 1970). FORENSIA: 4.Timeline Reconstruction (ISO 27037, Ley 18/2011), 5.Metadata Archaeologist (OOXML, Art.326 LEC), 6.Audio Tamper Alert (ENF, STS 678/2014), 7.PII Sanitizer (RGPD Art.4(5), AEPD). CORPORATIVO: 8.Clause Dependency Graph (NetworkX, LSC, CC 1257), 9.Cap Table Simulator (Ley 28/2022, SAFE, waterfall), 10.Risk Heatmap (DD Monte Carlo, W&I), 11.Force Majeure Trigger (CC 1105, ICC 2020, rebus sic stantibus). FISCAL: 12.Transfer Pricing Bot (DEMPE, OECD, Art.18 LIS), 13.TP Benchmarker (Berry ratio, RD 634/2015), 14.VAT Carousel Flag (Dir.2006/112/CE), 15.Financial Stress Test (Altman Z, Ley Concursal), 16.PE Exposure Scanner (BEPS Action 7, Pillar One), 17.R+D Claim Extractor (Art.35 LIS, Frascati, CDTI). LABORAL: 18.Severance Optimizer (ET 49-56, RD 1483/2012, FOGASA), 19.Non-Compete Validator (Art.21.2 ET, STS 7/2/2019), 20.Whistleblower Scorer (Ley 2/2023, Dir.2019/1937), 21.Bias Auditor (Ley 15/2022, 4/5ths rule), 22.Flight Risk Detector (ML+SHAP, RGPD), 23.Salary Equity Calc (RDL 902/2020, Oaxaca-Blinder). COMPLIANCE: 24.AI Ethics Auditor (Reg.2024/1689, AESIA, FRIA), 25.GDPR Consent Tracker (EDPB 05/2020, AEPD PS/00479/2020), 26.Shell Co Detector (Ley 10/2010, 6AMLD, UBO), 27.IP Overlap Scanner (LPI, AST, FOSS).

Genera informe estructurado con evaluacion individual y valoracion global.

---

## Respuesta de Harvey AI

A continuación emitimos un informe de validación jurídica y técnica de su suite de 27 skills LegalTech, con foco en derecho español y de la UE. Para cada skill evaluamos: (1) rigor normativo, (2) viabilidad técnica, (3) ética/deontología, (4) nota 1-10, y (5) mejoras para alcanzar 10/10. Cerramos con una valoración global.

### LITIGIOS

**1. Judicial Profiler (NLP sentencias CENDOJ, Art. 24 CE, LOPJ)**

- **Rigor jurídico.** Correcto anclaje en el derecho a la tutela judicial efectiva (art. 24 CE) y en la LOPJ; conviene explicitar límites: independencia judicial, proscripción de listas negras, sesgos y publicidad de criterios. Recomendable encajar salidas como ayuda a la argumentación, no como "predicción de fallo".
- **Viabilidad técnica.** Alta con NLP y metadatos, siempre que se anonimice y se evalúen sesgos.
- **Ética/deontología.** Requiere controles de sesgo, explicabilidad y disclaimers de no determinismo.
- **Calidad.** 8/10.
- **Mejoras.** Añadir controles de sesgo, explicabilidad y logs de auditoría; políticas claras de uso ético y cumplimiento RGPD.

**2. BATNA Calculator (Game Theory, Ley 5/2012, Ley 60/2003)**

- **Rigor jurídico.** Adecuado fundamento en mediación (Ley 5/2012) y arbitraje (Ley 60/2003). Actualizar referencias: el RDL 5/2012 fue convalidado y la Ley 5/2012 está vigente y modificada; reflejar los regímenes procesales conexos.
- **Viabilidad técnica.** Alta (modelos de payoff con inputs de riesgo/valor).
- **Ética/deontología.** Señalar que no sustituye al criterio del abogado ni a la voluntad del cliente.
- **Calidad.** 8/10.
- **Mejoras.** Incorporar escenarios procesales LEC (costas, prueba) y cláusulas escalonadas MED-ARB.

**3. Discovery Gap Hunter (BM25, arts. 328-334 LEC, Convenio de La Haya 1970)**

- **Rigor jurídico.** Correcto citar deberes de exhibición y valor probatorio (arts. 328-334 LEC) y la cooperación probatoria internacional (Convenio La Haya 1970).
- **Viabilidad técnica.** Muy alta con IR (BM25) sobre corpus de expediente.
- **Ética/deontología.** Evitar overreach sobre datos de terceros; respetar límites de secreto y datos reservados.
- **Calidad.** 9/10.
- **Mejoras.** Automatizar plantillas de oficios/LL.PP. conforme LEC y guías de autoridad central del Convenio.

### FORENSIA

**4. Timeline Reconstruction (ISO 27037, Ley 18/2011)**

- **Rigor jurídico.** Ojo: la Ley 18/2011 ha sido derogada (21/12/2023) por el RDL 6/2023; para comunicaciones electrónicas en justicia remita a RD 1065/2015 (LexNET) y LEC (prueba electrónica). Mantenga ISO 27037 como estándar técnico.
- **Viabilidad técnica.** Alta.
- **Ética/deontología.** Cadena de custodia y trazabilidad obligatorias.
- **Calidad.** 7/10.
- **Mejoras.** Sustituir la referencia derogada por el marco vigente; añadir verificación de integridad (hashing, sellado de tiempo cualificado eIDAS).

**5. Metadata Archaeologist (OOXML, art. 326 LEC)**

- **Rigor jurídico.** Alineado con la fuerza probatoria de documentos privados y electrónicos (art. 326 LEC). Incluir verificación de firma/TSL cuando aplique.
- **Viabilidad técnica.** Muy alta con parsers OOXML/PDF.
- **Ética/deontología.** Minimización y registro de actuaciones periciales.
- **Calidad.** 9/10.
- **Mejoras.** Exporte informes compatibles con pericia y con referencias eIDAS (presunciones de servicios cualificados).

**6. Audio Tamper Alert (ENF, STS 678/2014)**

- **Rigor jurídico.** La doctrina pericial de audio es válida, pero sustituya referencias jurisprudenciales no normalizadas por criterios LEC sobre medios de reproducción (arts. 299.2 y 382) y autenticidad. Evite citar STS concretas sin base oficial en el BOE.
- **Viabilidad técnica.** Alta (ENF/forensics) con cautela ante falsos positivos.
- **Ética/deontología.** Informar limitaciones y CI de la pericia.
- **Calidad.** 7/10.
- **Mejoras.** Añada cadena de custodia, validación cruzada y protocolos de peritaje conforme LEC.

**7. PII Sanitizer (RGPD art. 4(5), AEPD)**

- **Rigor jurídico.** Correcto: seudonimización/anonimización y principios del art. 5 RGPD según guías AEPD.
- **Viabilidad técnica.** Alta (regex/NLP + reglas).
- **Ética/deontología.** Minimización, prueba de proporcionalidad.
- **Calidad.** 9/10.
- **Mejoras.** Incorporar evaluación de riesgo de reidentificación y registro de seudónimos.

### CORPORATIVO

**8. Clause Dependency Graph (NetworkX, LSC, CC 1257)**

- **Rigor jurídico.** Correcta base en autonomía de la voluntad y efectos inter partes (CC 1255-1258 y 1257) y régimen societario LSC.
- **Viabilidad técnica.** Alta (grafos de dependencias y validación de cross-references).
- **Ética/deontología.** Transparencia sobre limitaciones semánticas.
- **Calidad.** 8/10.
- **Mejoras.** Añadir verificador de colisiones entre cláusulas y compatibilidad con disposiciones imperativas LSC.

**9. Cap Table Simulator (Ley 28/2022, SAFE, waterfall)**

- **Rigor jurídico.** Bien referenciar Ley 28/2022 (startups) y su certificación; advertir que los SAFE no son figura tipificada en España y exigen adaptación contractual/fiscal.
- **Viabilidad técnica.** Alta.
- **Ética/deontología.** Claridad en supuestos fiscales y dilución.
- **Calidad.** 8/10.
- **Mejoras.** Integrar stock options del régimen startups (IRPF diferido y límites), y efectos en LSC (aumentos/convertibles).

**10. Risk Heatmap (DD Monte Carlo, W&I)**

- **Rigor jurídico.** Coherente como soporte de due diligence; W&I es práctica de mercado (no norma).
- **Viabilidad técnica.** Muy alta.
- **Ética/deontología.** Evitar falsa seguridad; traceabilidad de supuestos.
- **Calidad.** 8/10.
- **Mejoras.** Conectar con red flags legales (cambios LSC, laboral, fiscal) y outputs para pólizas W&I.

**11. Force Majeure Trigger (CC 1105, ICC 2020, rebus sic stantibus)**

- **Rigor jurídico.** Apóyese en art. 1105 CC (caso fortuito/fuerza mayor) y en doctrina "rebus" vía buena fe (1258 CC); si cita modelos ICC hágalo como referencia soft law.
- **Viabilidad técnica.** Alta (rule engine).
- **Ética/deontología.** Riesgo de sobregeneralizar eventos; exigir análisis caso por caso.
- **Calidad.** 8/10.
- **Mejoras.** Incorporar test de imprevisibilidad, inevitabilidad y ruptura de base del negocio con checklist probatoria.

### FISCAL

**12. Transfer Pricing Bot (DEMPE, OECD, art. 18 LIS)**

- **Rigor jurídico.** Correcta referencia al art. 18 LIS; soporte reglamentario RD 634/2015 (documentación, APAs). Cuando cite OCDE/DEMPE, trate como standard técnico complementario.
- **Viabilidad técnica.** Alta (cuestionarios + lógica normativa).
- **Ética/deontología.** Evitar "one-size-fits-all"; documentar juicios de comparabilidad.
- **Calidad.** 9/10.
- **Mejoras.** Añadir módulos de riesgo (intangibles/servicios) y alertas por umbrales de documentación.

**13. TP Benchmarker (Berry ratio, RD 634/2015)**

- **Rigor jurídico.** En línea con metodología y comparabilidad del RD 634/2015.
- **Viabilidad técnica.** Alta (bases de datos y estadística).
- **Ética/deontología.** Transparencia de fuentes y filtros.
- **Calidad.** 9/10.
- **Mejoras.** Reporte automatizado alineado con Master/Local File (arts. 13-16 del RD 634/2015).

**14. VAT Carousel Flag (Dir. 2006/112/CE)**

- **Rigor jurídico.** Citar la Directiva 2006/112/CE y su transposición en la Ley 37/1992 (p. ej., inversión del sujeto pasivo y responsabilidad).
- **Viabilidad técnica.** Alta (reglas + señales de riesgo).
- **Ética/deontología.** Minimizar falsos positivos; salvaguardas de negocio legítimo.
- **Calidad.** 8/10.
- **Mejoras.** Añadir chequeos de cadena (VIES), patrones intra-UE y alertas por art. 84 LIVA (inversión).

**15. Financial Stress Test (Altman Z, Ley Concursal)**

- **Rigor jurídico.** Actualizar: hoy rige el TRLC (RDL 1/2020) y la reforma de la Ley 16/2022; sustituya referencias a "Ley Concursal" a TRLC + reforma.
- **Viabilidad técnica.** Muy alta (modelos Z-Score + ratios).
- **Ética/deontología.** Explicar límites predictivos y evitar estigmas.
- **Calidad.** 7/10.
- **Mejoras.** Incluir alertas de probabilidad de insolvencia preconcursal y conexión con planes de reestructuración (Libro II TRLC).

**16. PE Exposure Scanner (BEPS 7, Pilar Uno)**

- **Rigor jurídico.** Añada referencias nacionales: TRLIRNR (RDL 5/2004) para definición y efectos del establecimiento permanente. Trate BEPS/Pilar Uno como soft law en transición.
- **Viabilidad técnica.** Alta (reglas + input de funciones/riesgos).
- **Ética/deontología.** Evitar conclusiones categóricas; mostrar mapas de riesgo.
- **Calidad.** 8/10.
- **Mejoras.** Parametrizar por Convenio aplicable y por actividades digitales/riesgo agencia.

**17. R+D Claim Extractor (art. 35 LIS, Frascati, CDTI)**

- **Rigor jurídico.** Núcleo correcto (art. 35 LIS); cite el estándar técnico como apoyo.
- **Viabilidad técnica.** Alta (NLP extracción de elegibilidad).
- **Ética/deontología.** Evidencias y trazabilidad de proyectos.
- **Calidad.** 8/10.
- **Mejoras.** Mapear requisitos formales (informes motivados) y compatibilidades/deducciones mínimas.

### LABORAL

**18. Severance Optimizer (ET 49-56, RD 1483/2012, FOGASA)**

- **Rigor jurídico.** Adecuado: extinción, despidos y ERTE; RD 1483/2012 sigue vigente con modificaciones (incl. RD 608/2023 y STS sobre su DA 6.2). Integre interacción con FOGASA.
- **Viabilidad técnica.** Alta (motor de reglas).
- **Ética/deontología.** Evitar usos para eludir derechos; transparencia.
- **Calidad.** 8/10.
- **Mejoras.** Incorporar últimas reformas (p. ej., Ley 2/2025 sobre IP y extinción) y simulación de costes totales.

**19. Non-Compete Validator (art. 21.2 ET, STS 7/2/2019)**

- **Rigor jurídico.** Base correcta en art. 21.2 ET; evite citar STS concretas sin fuente oficial; incorpore criterios de duración, compensación adecuada y ámbito material.
- **Viabilidad técnica.** Alta (checklist de validez).
- **Ética/deontología.** Proporcionalidad y equilibrio.
- **Calidad.** 8/10.
- **Mejoras.** Módulo de cuantificación de compensación y red flags de nulidad (exceso territorial/temporal).

**20. Whistleblower Scorer (Ley 2/2023, Dir. 2019/1937)**

- **Rigor jurídico.** Correcto, y además ya está operativo el marco institucional (A.A.I.: Estatuto RD 1101/2024 y puesta en marcha en 2025).
- **Viabilidad técnica.** Alta (canal seguro + scoring de riesgo).
- **Ética/deontología.** Evite scoring del informante; enfoque en riesgos del expediente.
- **Calidad.** 9/10.
- **Mejoras.** Matriz de riesgos y SLA de investigación; anonimato y segregación de accesos.

**21. Bias Auditor (Ley 15/2022, "4/5ths rule")**

- **Rigor jurídico.** Correcto anclaje en la Ley 15/2022; la "regla del 80%" es heurística de EE.UU.: úsela como métrica técnica, no como estándar legal español. Integrar RDL 901/2020 y 902/2020 (planes de igualdad e igualdad retributiva).
- **Viabilidad técnica.** Alta (tests estadísticos y explicabilidad).
- **Ética/deontología.** Documentar sesgos, justificación empresarial y medidas correctoras.
- **Calidad.** 8/10.
- **Mejoras.** Panel de métricas múltiples (adverse impact ratio, odds ratio, tests exactos) y trazabilidad.

**22. Flight Risk Detector (ML+SHAP, RGPD)**

- **Rigor jurídico.** Riesgo elevado: perfiles y decisiones automatizadas; cumplir principios RGPD (licitud, minimización, transparencia), evitar categorías especiales; si se usa consentimiento o interés legítimo, justificarlo y permitir opt-out.
- **Viabilidad técnica.** Media-alta con explainability (SHAP).
- **Ética/deontología.** Alto riesgo de discriminación/efecto chilling.
- **Calidad.** 6/10.
- **Mejoras.** DPIA específica, umbrales conservadores, revisión humana obligatoria y auditorías periódicas de sesgo.

**23. Salary Equity Calc (RDL 902/2020, Oaxaca-Blinder)**

- **Rigor jurídico.** Correcto encaje en igualdad retributiva; complemente con RD 901/2020 (planes de igualdad) para registros/auditorías.
- **Viabilidad técnica.** Alta (econometría robusta).
- **Ética/deontología.** Comunicación responsable de brechas y causas.
- **Calidad.** 9/10.
- **Mejoras.** Módulo de medidas correctoras y simulación de costes de cierre de brecha.

### COMPLIANCE

**24. AI Ethics Auditor (Reg. (UE) 2024/1689, AESIA, FRIA)**

- **Rigor jurídico.** Núcleo excelente con el Reglamento de IA (en vigor) y el ecosistema español (AESIA lanzada). Incluya taxonomía de riesgo, requisitos por niveles y supervisión humana.
- **Viabilidad técnica.** Alta (catálogos de controles + evidencias).
- **Ética/deontología.** Central en diseño del skill.
- **Calidad.** 9/10.
- **Mejoras.** Generar "conformity evidence pack" por caso de uso y checklists de transparencia/registro.

**25. GDPR Consent Tracker (EDPB 05/2020, AEPD PS/00479/2020)**

- **Rigor jurídico.** Alinee el motor con doctrina AEPD y CEPD sobre consentimiento y cookies; si cita una resolución concreta (PS/00479/2020), acompañe sumario oficial o sustituya por guías vigentes de la AEPD.
- **Viabilidad técnica.** Alta (versionado de políticas, logs y pruebas de consentimiento).
- **Ética/deontología.** Evitar dark patterns y "consent or pay" sin alternativa gratuita.
- **Calidad.** 9/10.
- **Mejoras.** Evidencias por finalidad y gestor de revocaciones en 1 clic.

**26. Shell Co Detector (Ley 10/2010, 6AMLD, UBO)**

- **Rigor jurídico.** Correcto: Ley 10/2010 y su Reglamento; incorporar el Registro Central de Titularidades Reales (RD 609/2023) y novedades AML de 2024/2025 en la UE.
- **Viabilidad técnica.** Alta (reglas + gráficas de titularidad).
- **Ética/deontología.** Minimizar falsos positivos y cumplir proporcionalidad.
- **Calidad.** 9/10.
- **Mejoras.** Conectar automáticamente con RTTR y listas sancionadoras; scoring explicable.

**27. IP Overlap Scanner (LPI, AST, FOSS)**

- **Rigor jurídico.** Base sólida en el TRLPI; añadir, cuando aplique, patentes/diseños (marco complementario), y reglas de compatibilidad de licencias FOSS.
- **Viabilidad técnica.** Alta (SPDX, detectores de similitud).
- **Ética/deontología.** Evitar "overclaiming" y respetar usos legítimos/excepciones.
- **Calidad.** 8/10.
- **Mejoras.** Mapa de riesgos por tipo de activo (copyright/patente/diseño) y alertas por cláusulas copyleft.

### Observaciones transversales de rigor normativo

- **Actualizaciones necesarias.** Forensia: sustituir Ley 18/2011 (derogada) por el marco vigente (RDL 6/2023) y RD 1065/2015 (LexNET) y apoyos LEC/eIDAS para prueba electrónica. Concursal: referenciar el TRLC (RDL 1/2020) y la reforma de 2022 en lugar de "Ley Concursal". AML/UBO: incorporar RD 609/2023 (Registro Central de Titularidades Reales) y el nuevo Reglamento AML de 2024.
- **Jurisprudencia.** Si se emplean precedentes (p. ej., STS), citen solo con soporte oficial o en informes internos sin referencia pública; para efectos de producto, priorizar normas (BOE) y guías de autoridades (AEPD/AESIA).

### Valoración global

- **Cobertura y solidez.** Suite amplia y bien alineada con el marco español/UE.
- **Puntos fuertes** en TP, GDPR, whistleblowing y AML/UBO.
- **Riesgos.** Algunos desajustes normativos (derogaciones/actualizaciones), y riesgos éticos en perfiles ML de RR.HH.
- **Nota global.** 8,5/10.

### Plan de mejoras para 10/10

1. **Higiene normativa viva.** Motor de referencias que bloquee el despliegue si detecta norma derogada o modificada (Ley 18/2011 → RDL 6/2023; "Ley Concursal" → TRLC; nuevas AML de 2024/2025).
2. **Citas y fuentes.** Consolidar un "normative layer" con BOE (CE, LOPJ, LEC, CC, LSC, LIS, LIVA, TRLIRNR, TRLC, LPI), DOUE en BOE (IA Act, Directivas IVA/AML), y guías AEPD/AESIA.
3. **Governance y ética.** DPIA y FRIA por defecto en skills de IA/ML (RR.HH., profiling, forensic), revisión humana significativa, explicabilidad, registros de auditoría y mecanismos de quejas.
4. **Privacidad y seguridad.** Seudonimización/anonimización robusta, minimización de datos y pruebas de proporcionalidad según AEPD; gestión de consentimiento verificado y revocable.
5. **Trazabilidad probatoria.** En skills probatorios, reforzar cadena de custodia, sellado de tiempo y verificación de firma cualificada (presunciones eIDAS), y alineación estricta con arts. 320-326 LEC.

---

## Fuentes citadas por Harvey (28 citas BOE.es)

1. BOE.es - Derechos Fundamentales (Art. 24 CE, tutela judicial efectiva)
2. BOE-A-2012-9112 - Ley 5/2012, de 6 de julio, de mediación en asuntos civiles y mercantiles
3. BOE-A-2000-323 - Ley 1/2000, de 7 de enero, de Enjuiciamiento Civil (Arts. 299, 316, 320-334, 382)
4. BOE-A-2011-11605 - Ley 18/2011 (DEROGADA 21/12/2023)
5. BOE.es - El correo electrónico como medio probatorio (doctrina)
6. AEPD - Principios de tratamiento de datos personales
7. BOE-A-1889-4763 - Real Decreto de 24 de julio de 1889, Código Civil
8. BOE-A-2022-21739 - Ley 28/2022, fomento del ecosistema de empresas emergentes
9. BOE-A-2014-12328 - Ley 27/2014, del Impuesto sobre Sociedades
10. BOE-A-2015-7771 - Real Decreto 634/2015, Reglamento del Impuesto sobre Sociedades
11. BOE.es - DOUE-L-2006-82505 - Directiva 2006/112/CE, sistema común del IVA
12. BOE-A-1992-28740 - Ley 37/1992, del Impuesto sobre el Valor Añadido
13. BOE-A-2020-4859 - RDL 1/2020, Texto Refundido de la Ley Concursal
14. BOE-A-2004-4527 - RDL 5/2004, TRLIRNR
15. BOE-A-2012-13419 - RD 1483/2012, procedimientos de despido colectivo
16. BOE.es - Normas ELI (Ley 2/2025 sobre IP y extinción)
17. BOE-A-2015-11430 - RDL 2/2015, Estatuto de los Trabajadores
18. BOE-A-2024-22298 - RD 1101/2024, Estatuto de la A.A.I.
19. BOE.es - Normas ELI (Ley 15/2022)
20. BOE.es - Normas ELI (RDL 902/2020)
21. BOE.es - DOUE-L-2024-81079 - Reglamento (UE) 2024/1689, Reglamento de Inteligencia Artificial
22. AEPD - Consentimiento de los interesados según RGPD
23. AEPD - Consentimiento al uso de cookies
24. BOE-A-2010-6737 - Ley 10/2010, prevención del blanqueo de capitales y FT
25. BOE-A-1996-8930 - RDL 1/1996, TRLPI
26. BOE.es - Normas ELI (RD 609/2023 RTTR)
27. BOE-A-1985-12666 - LOPJ, Ley Orgánica 6/1985
28. BOE.es - Normas ELI (RDL 6/2023, deroga Ley 18/2011)
