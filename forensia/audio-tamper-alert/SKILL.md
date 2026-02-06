---
name: audio-tamper-alert
description: Authenticate audio recordings for forensic evidence by detecting tamper via spectrogram analysis, Electric Network Frequency (ENF) continuity per ISO/IEC 27037, codec re-encoding patterns, phase discontinuities, voice identification consistency, and chain-of-custody compliance. Assess admissibility under STS 678/2014 (secret recordings) and Ley 2/2024. Triggers when validating employment disputes, contract negotiations, or threat recordings.
---

# Audio Tamper Alert

Authenticate recordings for forensic admissibility and detect manipulation via multi-method analysis.

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Audio WAV/MP3   │───▶│ Conversión a     │───▶│ FFT             │
│                 │    │ WAV sin pérdida  │    │ Espectrograma   │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                       ┌──────────────────┐             │
                       │ Análisis de      │◀────────────┘
                       │ Frecuencia Red   │
                       │ (ENF)            │
                       └────────┬─────────┘
                                │
                       ┌────────▼─────────┐    ┌─────────────────┐
                       │ Detección de     │───▶│ Informe de      │
                       │ Discontinuidades │    │ Autenticidad    │
                       └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Autenticar grabaciones aportadas como prueba
- Detectar cortes o silencios insertados
- Verificar continuidad temporal
- Identificar manipulación de voz

---

## Multi-Method Detection Techniques

### 1. Spectrogram Analysis

Time-frequency visualization (Fast Fourier Transform):
- Detect abrupt amplitude gaps (edits, cuts)
- Identify environment changes (background noise shift = different location/time)
- Spot compression artifacts (lossy codec banding)
- Analyze vocal formants for consistency across sections

**Tool Workflow:** Librosa/SciPy → matplotlib display; look for visual discontinuities.

### 2. Electric Network Frequency (ENF) Analysis per ISO/IEC 27037

Power grid frequency (50 Hz EU, 60 Hz Americas) is embedded in background hum:
- If recording contains continuous electrical hum (indoor recordings), ENF phase is continuous
- Edits cause ENF phase jumps (>1° discontinuity = suspect)
- ENF database matching: Compare extracted ENF to regional power grid variations over time
  - ENFSI ENF database (European Network of Forensic Science Institutes) provides grid profiles
  - STS 678/2014 recognizes ENF as admissible forensic indicator in Spanish courts

**Limitation:** ENF undetectable in outdoor/ambient recordings without electrical hum.

### 3. Voice Identification Consistency

- Formant frequency stability: Vocal tract resonance should remain constant per speaker
- Jitter/shimmer patterns: Micro-variations in pitch are speaker-unique
- Spectral centroid: Changes >100 Hz suggest different speaker or post-processing
- MFCC (Mel-Frequency Cepstral Coefficients) clustering: Detect speaker switching

### 4. Codec Analysis & Re-encoding Detection

Identify tampering via compression fingerprints:
- **Lossless (WAV, FLAC):** No compression artifacts; trustworthy for forensics
- **MP3 re-encoding:** Repeated encoding leaves compression fingerprints (MDCT frame edges)
- **AAC/M4A tampering:** Variable bitrate (VBR) metadata reveals encoding history
- **Detection method:** Compare entropy across frequency bands; re-encoding shows >5% energy difference

### 5. Phase Discontinuity & Temporal Analysis

- Phase coherence breaks at edit junctions (cross-correlation <0.85 at boundary)
- Click/pop artifacts: Zero-crossing anomalies at splice points
- Time-alignment mismatch: Silence duration inconsistencies

---

## Manipulation Indicators & Severity

| Indicator | Severity | Forensic Implication | ISO/IEC 27037 Status |
|---|---|---|---|
| ENF Phase Discontinuity >1° | CRITICAL | Temporal cut confirmed | Admissible |
| Speaker Formant Jump | CRITICAL | Different speaker spliced in | Requires voice expert |
| Codec Re-encoding Evidence | HIGH | Post-hoc tampering probable | Document tool/version |
| Background Noise Shift | MEDIUM | Location/time change; may be innocent | Context-dependent |
| Click/Pop at Boundary | MEDIUM | Poor editing technique | Suggests amateur tampering |
| Inserted Silence (Digital) | CRITICAL | Content deletion | Highly suspicious |
| Compression Inconsistency | LOW | VBR re-encoding; less conclusive | Requires specialist |

---

## Concrete Example: Employment Dispute Recording

**Scenario:** Employee claims manager made verbal threat; manager denies. Recordings submitted from both parties (different devices).

**Chain-of-Custody Issues:** Employee's recording: MP3 (compressed), obtained "3 months later" from phone backup. Manager's defense: same meeting recorded on office digital recorder (WAV).

**Forensic Process:**

1. **Employee's MP3:** Convert to WAV for lossless analysis; detect re-encoding fingerprints (evidence of post-recording manipulation)
2. **Manager's WAV:** Analyze ENF phase; cross-reference with ENFSI database for 2024-09-15 Madrid grid profile
3. **Voice Consistency:** Extract MFCCs for both recordings
   - Employee's: Speaker A forms consistent (authentic)
   - Manager's: Speaker B's formants jump at timestamp 00:23:15 (suspicious; different speaker spliced in?)
4. **Comparative Analysis:** Both recordings contain identical words at same timestamps (00:12:34–00:18:46), but:
   - Employee's version has ENF discontinuity at 00:15:20 (likely edited)
   - Manager's version has continuous ENF matching 2024-09-15 Madrid grid (likely authentic)

**Legal Conclusion:** Manager's recording more forensically reliable under **STS 678/2014** (secret recordings) and **Ley 2/2024** (recording admissibility with chain-of-custody caveats). Employee's version inadmissible due to tampering indicators.

## Forensic Output

```json
{
  "file": "amenaza_manager.mp3",
  "duration_seconds": 1847,
  "format": {
    "codec": "MP3",
    "sample_rate": 44100,
    "bitrate_kbps": 128,
    "channels": 1
  },
  "chain_of_custody": {
    "acquisition_date": "2024-12-10",
    "source_device": "iPhone backup",
    "original_recording_date_claimed": "2024-09-15",
    "hash_sha256": "d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c"
  },
  "authenticity_analysis": {
    "authenticity_score": 0.28,
    "verdict": "PROBABLE_TAMPERING",
    "confidence": 0.89,
    "admissibility_sts678": false
  },
  "findings": [
    {
      "type": "ENF_DISCONTINUITY",
      "timestamp": "00:15:20",
      "phase_jump_degrees": 3.2,
      "severity": "CRITICAL",
      "implication": "Temporal cut in recording; content may be deleted or spliced"
    },
    {
      "type": "CODEC_RE_ENCODING",
      "severity": "HIGH",
      "evidence": "MDCT frame artifacts consistent with repeated MP3 encoding",
      "implication": "Audio processed after original recording"
    }
  ],
  "confidence_timeline": [
    {"from_sec": "0:00:00", "to_sec": "00:15:20", "confidence": 0.92, "status": "Authentic"},
    {"from_sec": "00:15:20", "to_sec": "00:15:22", "confidence": 0.15, "status": "Likely Edited"},
    {"from_sec": "00:15:22", "to_sec": "01:30:47", "confidence": 0.55, "status": "Compromised"}
  ]
}
```

---

## Legal Framework for Recording Admissibility

### STS 678/2014: Secret Recordings

Spanish Supreme Court standard for recorded conversations:
- Admissible if relevant to case
- **Chain of custody required:** Document recording date, device, circumstances
- **Forensic authentication recommended:** ENF analysis strengthens admissibility
- **Privacy caveat:** Ley Orgánica 1/1982 (right to honor) may require judicial authorization for recordings

### Ley 2/2024: Recording Procedures in Labor Disputes

Updated framework for employment recordings:
- Recordings in workplace permitted only if party owns/uses recording device
- Secret recordings (without consent) admissible only if probative necessity shown
- Forensic authentication via ENF/codec analysis supports admissibility motion

## Limitations & Specialist Referral

- **Lossless WAV required** for definitive analysis (MP3 destroys forensic evidence)
- **ENF detection requires indoor electrical hum** (outdoor/ambient recordings have limited detectability)
- **Sophisticated manipulation** (vocoder synthesis, trained AI) may evade detection; refer to specialized forensic lab
- **Voice deepfakes:** Emerging threat; refer to AENIAC certification if suspected

## Integration & Tools

```bash
# Open-source workflow
ffmpeg -i recording.mp3 -c:a pcm_s16le output.wav    # Convert to WAV
librosa + scipy + matplotlib                          # ENF + spectrogram analysis

# Recommended professional referral:
# AENIAC-certified audio forensics expert for court testimony
```

---

## Marco Procesal: Admisibilidad de Audio (LEC)

### Art. 299.2 LEC: Medios de Reproducción

La Ley de Enjuiciamiento Civil regula la prueba por imagen, sonido o reproducción:

> "Se admitirán como prueba los medios de reproducción de la palabra, imagen y sonido, así como los datos incorporados en soportes informáticos o electrónicos, conforme a lo que se establezca por vía reglamentaria."

**Implicación Forense:** Audio digital es prueba válida SI se acredita:
1. **Autenticidad:** Origen documentado, cadena custodia íntegra
2. **Integridad:** Sin manipulación post-grabación (hash, metadata, análisis forense ENF)
3. **Fiabilidad:** Certificado técnico sobre fidelidad reproducción

### Art. 382 LEC: Instrumentos de Grabación

Amparo específico a grabaciones como instrumentos de captación:

> "Podrán utilizarse como prueba los instrumentos de filmación, de grabación de sonido o de imagen fija, así como los soportes de datos informáticos, siempre que se garantice la integridad de la información contenida en los mismos."

**Requisitos Obligatorios:**
- Identificación unívoca del archivo (hash SHA-256)
- Preservación íntegra desde captura hasta presentación
- Declaración jurada del poseedor (origen, cadena custodia)
- Análisis forense si se cuestiona autenticidad

### Art. 384 LEC: Instrumentos de Archivo de Datos

Protección de archivos digitales como prueba:

> "Los instrumentos que permiten archivar, reproducir o transmitir datos, mediante soportes informáticos o electrónicos, tendrán la consideración de documento electrónico a efectos probatorios."

**Aplicación Audio Digital:**
- Grabación almacenada en cloud, teléfono, servidor = "documento electrónico"
- Presunción de veracidad si procedencia documentada
- Impugnación requiere prueba contraria sobre manipulación

### Requisitos de Autenticidad y Cadena de Custodia

| Requisito | Evidencia Requerida | Estándar Aplicable |
|---|---|---|
| **Origen** | Declaración poseedor + metadatos archivo (timestamp creación) | Art. 299.2 + 382 LEC |
| **Continuidad** | Registro custodia (quién, cuándo, dónde, condiciones almacenamiento) | ISO/IEC 27037:2012 |
| **Integridad** | Hash SHA-256 ingesta + hash salida (sin variación) | ENFSI guidelines |
| **Autenticidad** | Análisis forense ENF + espectrógrama (si impugnada) | STS 678/2014 |
| **Confidencialidad** | Acta de custodia bajo llave, acceso restringido personal autorizado | Art. 384 implicaciones RGPD |

### Derecho a Privacidad y Grabaciones (Art. 18 CE)

**Conflicto Constitutional:** Art. 18 CE protege "derecho al honor, intimidad personal y familiar y a la propia imagen."

**Ley Orgánica 1/1982:** Regula derecho protección honor, intimidad, propia imagen.

**Criterios Admisibilidad Grabaciones Sin Consentimiento:**

1. **Necesidad Probatoria:** ¿Es la grabación única prueba disponible de hechos relevantes?
2. **Proporcionalidad:** ¿Lesión privacidad justificada por valor probatorio?
3. **Publicidad Limitada:** Si admitida, ¿puede redactarse para minimizar exposición privacidad?
4. **Procedimiento:** ¿Fue grabación según Ley 2/2024 (labor disputes) o requiere autorización judicial previa?

**Jurisprudencia STS:** Grabación clandestina admisible si:
- Probanza de hecho esencial
- No obtención fraudulenta
- Proporcionalidad respetada (publicidad limitada en procedimiento)

---

## Protocolo de Peritaje Conforme LEC

### Arts. 335-352 LEC: Requisitos Prueba Pericial

**Art. 335.1 LEC:** Define peritaje como "prueba consistente en el dictamen de peritos sobre cuestiones que requieren conocimientos científicos, artísticos, técnicos o prácticos."

**Art. 335.2 LEC - JURAMENTO/PROMESA OBLIGATORIO:**

> "Los peritos deberán cumplir las obligaciones de abstención, imparcialidad y confidencialidad. Bajo apercibimiento legal, prestarán juramento o promesa de desempeñar fielmente la misión que les ha sido confiada, conforme a reglas de su ciencia o arte."

**Declaración Obligatoria en Audio Report:**

```
"Bajo apercibimiento legal, juro/prometo desempeñar fielmente
la misión de peritaje de autenticidad de grabación de audio,
conforme a estándares de análisis forense (ISO/IEC 27037:2018,
ENFSI guidelines), sin dejanne guiar por interés que no sea el
de servir a la administración de justicia."
```

### Arts. 343-352 LEC: Procedimiento Contradictorio

**Art. 343 LEC:** Cada parte puede nombrar perito independiente.

**Art. 344 LEC:** Tribunal puede ordenar junta de peritos (peritaje contradictorio).

**Implicación Audio Forensics:**
- Informe debe permitir réplica del perito contrario
- Metodología debe ser reproducible (mismos pasos → mismo resultado)
- Si hay discrepancia entre peritos, tribunal valora credibilidad de cada uno

### Validación Cruzada: Métodos Independientes

**Mínimo 2 métodos distintos para credibilidad:**

1. **Método 1 - Análisis ENF (Electric Network Frequency):**
   - Extrae frecuencia red (50/60 Hz) de hum de fondo
   - Compara contra ENFSI database de grid variations
   - Resultado: curva ENF debe ser continua; saltos = ediciones

2. **Método 2 - Análisis Espectral:**
   - FFT time-frequency plot (espectrograma visual)
   - Detecta cambios abruptos en contenido frecuencial
   - Examina formantes vocales, ruido de fondo

3. **Método 3 - Análisis Temporal:**
   - Discontinuidades fase
   - Patrones zero-crossing
   - Artifacts codec (si MP3/AAC)

**Validación Cruzada Ejemplo:**

```json
{
  "validacion_cruzada": {
    "metodo_1_enf": {
      "analisis": "ENFSI database matching 2024-09-15 Madrid grid",
      "resultado": "Fase continua 0:00:00 - 0:15:20; salto 3.2° en 0:15:20",
      "conclusion": "EDICION DETECTADA"
    },
    "metodo_2_espectrograma": {
      "analisis": "FFT time-frequency 2D plot",
      "resultado": "Discontinuidad visual intensidad en 0:15:20; cambio abrupto amplitud",
      "conclusion": "EDICION DETECTADA"
    },
    "metodo_3_temporal": {
      "analisis": "Zero-crossing rate, cross-correlation boundaries",
      "resultado": "Coherencia <0.85 en borde 0:15:20; click artifact 5ms",
      "conclusion": "EDICION DETECTADA"
    },
    "veredicto_final": "TRES MÉTODOS INDEPENDIENTES CONCUERDAN: Grabación editada en timestamp 0:15:20"
  }
}
```

### Intervalos de Confianza y Limitaciones

**Confidence Intervals por Tipo Análisis:**

| Análisis | CI (95%) | Limitaciones |
|---|---|---|
| **ENF Matching** | ±2.5 minutos (si grid database disponible) | No aplica outdoor/sin hum eléctrico |
| **Spectrograma Visual** | ±500ms (edición obvia) | Manipulación sofisticada evade detección |
| **Codec Fingerprint** | ±3% (si MP3 reencoded) | No detecta edición en WAV lossless |
| **Voz Identificación MFCC** | ±0.95 speaker probability | Deepfakes/vocoder pueden engañar |

**Advertencia Obligatoria en Informe Pericial:**

```
LIMITACIONES DE LA PERICIA:

1. ENF Analysis: No detecta ediciones en grabaciones al aire libre
   o sin hum eléctrico identificable.

2. Espectrografía: Manipulación sofisticada (transcodificación múltiple,
   noise injection) puede evitar detección visual.

3. Identificación Voz: Deepfakes de IA entrenados pueden
   replicar patrones MFCC genuinos. Se recomienda análisis
   adicional de vocoders/síntesis.

4. Cadena Custodia: Si el archivo fue aportado por parte interesada
   sin custodia documentada, se reduce confianza sobre integridad.

5. Conclusión: Análisis indica PROBABLE MANIPULACIÓN, pero no
   certeza absoluta. Requiere valoración judicial conjuntamente
   con otras pruebas (testimonios, contexto, trazabilidad).
```

### Template: Estructura Informe Pericial Audio Forense

```markdown
# TRIBUNAL: [JUZGADO / AUDIENCIA PROVINCIAL / AUDIENCIA NACIONAL]

## INFORME PERICIAL SOBRE AUTENTICIDAD DE GRABACIÓN DE AUDIO

---

## 1. IDENTIFICACIÓN DEL PERITO

Nombre y Apellidos: [Completo]
DNI: [número]
Colegio Profesional: [Colegio Ingenieros / Colegio Peritos / etc.]
Número Colegiado: [número]
Especialidad: Análisis Forense de Grabaciones de Audio
Acreditación: ISO/IEC 27037:2018, AENIAC (si aplica)
Experiencia profesional: [años] años desde [año inicio]

**JURAMENTO/PROMESA (Art. 335.2 LEC):**
Bajo apercibimiento legal, juro/prometo desempeñar fielmente la misión
de peritaje conforme a reglas de la técnica de análisis forense de audio,
sin dejanne guiar por interés que no sea el de servir a la administración de justicia.

---

## 2. OBJETO DEL PERITAJE

Archivo de audio: [nombre_archivo.mp3/.wav/etc]
Tamaño archivo: [X MB]
Hash SHA-256 ingesta: [hash_valor]
Formato: [MP3 / WAV / M4A / etc]
Duración: [minutos:segundos]

Cuestión planteada por [demandante/demandado]:
"¿Ha sido la grabación de audio manipulada, editada o falsificada?
¿Existe continuidad técnica en la grabación original?"

---

## 3. METODOLOGÍA

Conforme a ISO/IEC 27037:2018, ENFSI guidelines, y STS 678/2014.

### Herramientas Utilizadas
- FFmpeg (v.4.4): Conversión codec lossless
- Librosa (v.0.10): Extracción características audio
- SciPy (v.1.8): Análisis espectral FFT
- Matplotlib (v.3.5): Visualización espectrogramas
- ENFSI ENF Database: Matching red eléctrica

### Procedimiento

1. Adquisición forense archivo original
2. Hash SHA-256 ingesta + documentación
3. Conversión a WAV lossless (si MP3/comprimido)
4. Análisis ENF (Electric Network Frequency) contra ENFSI database
5. Espectrografía FFT y análisis temporal
6. Validación cruzada (mínimo 2 métodos independientes)
7. Hash SHA-256 salida (verificación integridad)

---

## 4. HALLAZGOS

### 4.1 Características Archivo

| Propiedad | Valor |
|---|---|
| Formato Original | MP3 |
| Frecuencia Muestreo | 44100 Hz |
| Canales | 1 (mono) |
| Bitrate | 128 kbps |
| Duración | 30:47 (minutos:segundos) |

### 4.2 Análisis ENF

Resultado: **DISCONTINUIDAD CRÍTICA EN TIMESTAMP 12:34**
- Fase continua 0:00:00 - 12:34:00
- Salto fase 2.8° exacto en frontera 12:34:00 - 12:34:02
- Matching ENFSI Madrid 2024-09-15 grid: Confirma autenticidad hasta 12:34
- Post-12:34: Fase desplazada (compatible con edición/corte)

### 4.3 Análisis Espectrográfico

[Imagen: Espectrograma FFT completo con anotación salto en 12:34]

**Observación:** Intensidad, formantes vocales, y contenido armónico cambian abruptamente. Compatible con empalme audio.

### 4.4 Análisis Temporal

Cross-correlación boundaries: 0.78 (por debajo threshold 0.85)
Clic/pop artifacts: Detectado en ±10ms zona de edición

### 4.5 Análisis Codec

MP3 reencoding fingerprints: Detectados en 15% del archivo
Implicación: Archivo procesado en post-producción (posible re-grabación compilada)

---

## 5. CONCLUSIONES

Basado en validación cruzada de 3 métodos independientes (ENF,
espectrografía, análisis temporal):

**La grabación de audio presenta INDICIOS DE MANIPULACIÓN con
certeza técnica del 89%. Se detecta edición/corte aproximadamente
en timestamp 12:34:00.**

---

## 6. LIMITACIONES

- ENF análisis depende disponibilidad hum eléctrico
- Manipulación sofisticada podría evitar detección
- Análisis limitado a técnicas no invasivas
- Conclusions son "probable tampering" no certeza absoluta

---

## 7. CV PERITO

[Curriculum vitae resumido máx. 1 página]
```

---

## Cadena de Custodia de Audio

### Registro Integral de Trazabilidad

**Formulario ISO/IEC 27037:2012 Específico para Audio:**

```
CADENA DE CUSTODIA - GRABACIÓN DE AUDIO
═══════════════════════════════════════════════════════════════

Caso: [Expediente Judicial]
Investigador Principal: [Nombre, DNI, Acreditación]

┌───────────────────────────────────────────────────────────┐
│ GRABACIÓN ORIGINAL                                        │
├───────────────────────────────────────────────────────────┤
│ Descripción: [Audio MP3 12:34 duración, "conversación"]  │
│ Formato Original: [MP3 / WAV / M4A / etc]                │
│ Identificador: SHA256:d4e5f6a7b8c9...                    │
│ Tamaño: [X MB]                                           │
│ Fuente: [Teléfono / Grabadora / Servidor / Nube]         │
│ Dispositivo/Plataforma: [iPhone / Android / Dropbox]     │
│ Poseedor Original: [Nombre, DNI]                         │
│ Declaración Poseedor:                                    │
│   - Cuándo obtuvo: [YYYY-MM-DD HH:MM:SS]                │
│   - Cómo obtuvo: [grabación propia / descarga / etc]    │
│   - Acceso/Modificación Posteriores: SÍ / NO (especificar) │
│ Firma Poseedor: [Certificado Digital o Autógrafa]       │
│ Sello Forense Ingesta: SHA256, timestamp, perito        │
└───────────────────────────────────────────────────────────┘

TRANSFERENCIAS Y CUSTODIA:

Transferencia 1:
  De: [Poseedor Original] → A: [Perito Forense A]
  Fecha: [YYYY-MM-DD HH:MM:SS UTC]
  Método Entrega: [USB encriptada / transferencia online / etc]
  Hash Verificado: SHA256 [valor] ✓ Coincide
  Condiciones Almacenamiento: [Cifrado AES-256, custodia bajo llave]
  Firma: [Certificado X.509 Perito A]

Transferencia 2 (si aplica):
  De: [Perito A] → A: [Perito B / Tribunal]
  Fecha: [YYYY-MM-DD HH:MM:SS UTC]
  Hash Verificado: SHA256 [valor] ✓ Coincide
  Condiciones: [Caja fuerte tribunal, sello evidente de manipulación]
  Firma: [Certificado X.509 Perito B o Secretario Juzgado]

SELLOS EVIDENTE MANIPULACIÓN:
  [ ] Cinta precinto adhesiva sellada
  [ ] Sello lacre tribunal
  [ ] Fotografia custodia [link/descripción]
  [ ] Testigos presentes: [Nombres, DNI]
```

---
