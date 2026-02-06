---
name: metadata-archaeologist
description: Excavate hidden authorship, edit histories, and timestamps in Office documents through deep OOXML structure analysis (core.xml, app.xml, custom XML parts), PDF XMP/InfoDict forensics, EXIF recovery from embedded images, and cryptographic hash chain verification. Detects falsified document dates for evidentiary challenges under Art. 326 LEC. Triggers when authenticating contracts, validating authorship claims, or uncovering document tampering.
---

# Metadata Archaeologist

Extract forensic provenance from documents for authorship and falsification detection.

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ DOCX/XLSX/PPTX  │───▶│ Descompresión    │───▶│ Parseo XML      │
│                 │    │ ZIP              │    │ Profundo        │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Informe         │◀───│ Recuperación de  │◀───│ Análisis de     │
│ Forense         │    │ Historial        │    │ Comentarios     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Evidentiary Admissibility (Art. 326 LEC)

Electronic documents are admissible if:

1. **Authenticity:** Metadata chain verifiable; no signs of tampering
2. **Integrity:** Hash verification confirms no post-acquisition modification
3. **Reliability:** Timestamps synchronized with external sources (email, server logs)

**STS 363/2017 Standard:** Spanish Supreme Court accepts metadata as probative if forensic methodology is documented and reproducible.

---

## OOXML Deep Analysis

### Core Office Open XML Structures

| Path | Key Fields | Forensic Value |
|---|---|---|
| `docProps/core.xml` | `creator`, `created`, `modified`, `lastModifiedBy` | Primary authorship trail |
| `docProps/app.xml` | `TotalTime`, `AppVersion`, `Company`, `Template` | Editing duration, software ID |
| `customXml/` | Custom property bags, namespaces | Hidden metadata, custom fields (often missed) |
| `word/document.xml` | `<w:trackRevisions>`, author IDs in `<w:ins>` | Change tracking if enabled |
| `word/comments.xml` | Resolved/unresolved comments with timestamps | Can recover "deleted" comments |
| `word/numbering.xml` | Paragraph-level edit history | Style/format manipulation patterns |
| `word/styles.xml` | Theme info, edit times | Custom style creator tracking |

### PDF Metadata Forensics

| Metadata Type | Location | Recovery Method |
|---|---|---|
| XMP (eXtensible Metadata Platform) | `/stream` in PDF | XML parser; includes creation date, software |
| InfoDict | `/Info` dictionary | Traditional metadata; often contradicts XMP |
| Digital Signatures | `/AcroForm`, `/Sig` | Verification of signing chain, tampering detection |
| Embedded Images | EXIF in `/XObject` streams | Recover photographer/camera info |

### Image EXIF in Documents

JPEG/PNG images embedded in DOCX/PDF preserve EXIF:
- `DateTimeOriginal`: Photo capture time (often reveals discrepancies with document claim)
- `Software`: Camera/phone model
- `GPSInfo`: Geolocation metadata (privacy risk in sanitization)

### Steganography Detection Basics

While full steganography analysis requires specialist tools:
- LSB (Least Significant Bit) hiding: Check file size vs. visual complexity
- Entropy analysis: Compare color histogram to distribution (high entropy = suspicious)
- Thumbnail analysis: Some tools hide data in embedded thumbnails
- **Recommendation:** Refer to digital forensics specialist (EnCase, Forensic Toolkit) for suspected steganography

---

## Recoverable Metadata & Hash Chain Verification

### Authorship Information

```json
{
  "creator_original": "Juan García",
  "last_modified_by": "María López",
  "company": "Garrigues",
  "application_signature": "Microsoft Word 2019 (Version 16.50)",
  "template_used": "Normal.dotm",
  "user_initials": "JG"
}
```

### Edit Timeline with Integrity Check

```json
{
  "created": "2024-01-15T10:30:00Z",
  "last_modified": "2024-02-20T16:45:00Z",
  "total_edit_time_minutes": 245,
  "revision_count": 47,
  "document_hash_sha256": "a3f2d7e8c1b9...",
  "core_xml_hash": "f4c6e9a2d5b1...",
  "hash_integrity_verified": true
}
```

### Change Tracking Recovery (Track Changes Enabled)

```json
{
  "tracked_changes": [
    {
      "type": "insertion",
      "author": "Juan García",
      "timestamp": "2024-02-15T14:30:00Z",
      "content": "Limitación de responsabilidad: El vendedor...",
      "change_id": "0"
    },
    {
      "type": "deletion",
      "author": "María López",
      "timestamp": "2024-02-16T10:00:00Z",
      "deleted_content": "Garantía de 5 años",
      "change_id": "1"
    }
  ]
}
```

---

## Concrete Example: Falsified Contract Date Detection

**Scenario:** Defendant claims contract signed on 2024-01-10; you suspect backdating.

**Evidence:** Contract appears in litigation bundle dated 2024-01-10, but creation metadata shows 2024-03-15.

**Forensic Process:**
1. Extract `core.xml`: `<dc:created>2024-03-15T14:22:00Z</dc:created>`
2. Calculate document hash (SHA-256) of original and each revision
3. Cross-reference with email timestamps: earliest email attachment hash matches the 2024-03-15 creation, not 2024-01-10
4. Check Track Changes: "Signature block" inserted by Juan García 2024-03-14 (before main creation date—impossible)
5. Recover deleted comments: "Update backdated signature" comment from María López 2024-03-14 20:45

**Conclusion:** Document was created in March 2024 and intentionally backdated. Admissible under **Art. 326 LEC** (electronic document authenticity challenge) y **STS 363/2017** (metadata reliability standards).

## Forensic Output

```json
{
  "document": "contrato_compraventa_final.docx",
  "claimed_date": "2024-01-10",
  "forensic_findings": {
    "creation_date_actual": "2024-03-15T14:22:00Z",
    "authors_identified": ["Juan García", "María López"],
    "total_edit_time_minutes": 245,
    "tracked_changes_count": 47,
    "recovered_comments": 8
  },
  "hash_chain_verification": {
    "document_sha256": "a3f2d7e8c1b9f4d6e8a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c",
    "initial_creation_hash": "f4c6e9a2d5b1e7c3a8f4d6b2e1c9a5f7d3b8e4c6a1f9d5b7e3c8a4f0d2b",
    "integrity_verified": true
  },
  "critical_alerts": [
    {
      "type": "BACKDATING_DETECTED",
      "severity": "CRITICA",
      "evidence": "CreationDate (2024-03-15) postdates ClaimedDate (2024-01-10) by 64 days",
      "implication": "Contract falsified or timestamp manipulated"
    },
    {
      "type": "IMPOSSIBILITY_DETECTED",
      "severity": "CRITICA",
      "evidence": "Signature block inserted 2024-03-14 but document claimed created 2024-01-10",
      "implication": "Metadata tampering or fraud"
    }
  ]
}
```

---

## Exportación de Informes Periciales

### Cumplimiento Arts. 335-352 LEC: Prueba Pericial

El informe de metadatos debe estructurarse conforme a requisitos de pericia procesal:

**Elementos Obligatorios (Art. 335 LEC):**

```markdown
# INFORME PERICIAL DE ANÁLISIS FORENSE DE METADATOS

## Identificación del Perito
- **Nombre y Apellidos:** [Perito Completo]
- **DNI/Colegiatura:** [Número Colegio Profesional]
- **Especialidad:** Análisis Forense de Documentos Electrónicos
- **Acreditación:** [ISO/IEC 27037:2012, ENFSI, Laboratorio Acreditado]
- **Experiencia:** [Años de ejercicio profesional]

## Juramento/Promesa (Art. 335.2 LEC)
"Juro/prometo desempeñar fielmente la misión de peritaje conforme a reglas de mi ciencia/arte, sin dejarne guiar por interés que no sea el de servir a la administración de justicia."

## Objeto del Peritaje
- **Asunto:** [Número expediente, partes]
- **Documento Analizado:** [Nombre archivo, formato, hash SHA-256]
- **Cuestión Planteada:** [Pregunta específica: ¿Manipulado? ¿Fecha original? ¿Autor?]

## Metodología
- **Estándar Aplicado:** ISO/IEC 27037:2018 (identification, collection, acquisition, preservation)
- **Herramientas Utilizadas:** [Nombres, versiones, validación]
- **Procedimientos:** [Pasos seguidos, con documentación de cada fase]

## Análisis y Hallazgos

### Metadatos Extraídos
[Tabla de metadatos con timestamps, autores, ediciones]

### Verificación de Integridad
- **Hash Ingesta (SHA-256):** [Valor]
- **Hash Salida (SHA-256):** [Valor]
- **Concordancia:** SÍ / NO [si divergen, evidencia de manipulación]

### Análisis de Firmas Digitales (si aplica)
- **Tipo Firma:** Cualificada / Avanzada / Simple (Reg. UE 910/2014)
- **Verificación TSL:** [Estado en Trusted Service List]
- **Validez:** [Fecha certificado, sello de tiempo]

## Conclusiones
[Respuesta clara a cuestión planteada, fundada en análisis]

## Limitaciones del Peritaje
- [Indicar restricciones técnicas, acceso limitado, etc.]
- [Advertencias sobre manipulación sofisticada (IA, deepfakes)]

## Curriculum Vitae del Perito
[CV resumido con formación, publicaciones, experiencia relevante]
```

### Template Estructura Completa para Documento Word

```
# [TRIBUNAL]: INFORME PERICIAL
**Caso:** [Expediente]
**Perito:** [Nombre Colegiado]
**Fecha:** [YYYY-MM-DD]

---

## 1. IDENTIFICACIÓN Y DATOS DEL PERITO

Nombre: [...]
DNI: [...]
Colegio Profesional: [Colegio Ingenieros, Colegio Peritos, etc.]
Número Colegiado: [...]
Acreditaciones:
- ISO/IEC 27037:2018
- Laboratorio ENAC (si aplica)
- Experiencia en análisis documentos electrónicos desde: [año]

**Juramento/Promesa:** Bajo apercibimiento legal, juro/prometo analizar el documento de conformidad con reglas de la ciencia/arte, sin influencia de parte alguna, con único fin de servir a la administración de justicia.

---

## 2. OBJETO DEL PERITAJE

Se solicita análisis forense de metadatos en documento:
- **Archivo:** [nombre.docx / .pdf / etc]
- **Tamaño:** [X MB/KB]
- **Hash SHA-256 Ingesta:** [hash]
- **Formato Original:** [DOCX / PDF / XLSX / etc]
- **Recibido en:** [fecha, lugar, custodio]

**Cuestión Planteada por [demandante/demandado]:**
¿Cuál es la fecha real de creación del documento?
¿Presenta indicios de manipulación en metadatos?
¿Existe compatibilidad entre timestamps reclamados y registros servidor?

---

## 3. METODOLOGÍA

Conforme a ISO/IEC 27037:2018 y ENFSI guidelines:

### 3.1 Herramientas
- Tool A: [Nombre, Versión, Fabricante, Validación]
- Tool B: [Nombre, Versión, Fabricante, Validación]

### 3.2 Procedimiento
1. Adquisición copia forense (bit-by-bit)
2. Hash MD5/SHA-256 copia original
3. Análisis en entorno forense aislado (sin internet)
4. Extracción metadatos (core.xml, app.xml, EXIF)
5. Análisis timestamps (UTC normalization)
6. Búsqueda cambios track changes
7. Hash salida, verificación integridad

---

## 4. HALLAZGOS

### Metadatos Extraídos

| Propiedad | Valor | Fuente |
|---|---|---|
| creator | Juan García López | core.xml |
| created | 2024-03-15T14:22:00Z | core.xml |
| lastModifiedBy | María López | core.xml |
| modified | 2024-03-16T10:15:00Z | core.xml |
| TotalEditTime | 245 minutos | app.xml |
| AppVersion | Word 2019 (16.50) | app.xml |

### Integridad Hash

- **Hash Ingesta:** SHA256:a3f2d7e8c1b9...
- **Hash Salida:** SHA256:a3f2d7e8c1b9...
- **Resultado:** ✓ Íntegro (no manipulación post-adquisición)

### Timeline de Edición

[Tabla con track changes si existen]

### Análisis Comparativo

Documento reclamado como creado "2024-01-10".
Metadatos forenses indican creado "2024-03-15" (64 días después).

**Incompatibilidad Crítica:** Imposible creación anterior a 2024-03-15.

---

## 5. CONCLUSIONES

En base a análisis realizado, y con fundamento en ISO/IEC 27037:2018:

**El documento analizado fue creado el 2024-03-15, no el 2024-01-10 como se reclamaba. Los metadatos muestran clara manipulación cronológica. La falsedad se establece con alto grado de certeza técnica.**

---

## 6. LIMITACIONES

- Análisis limitado a metadatos accesibles
- No se detectó manipulación a nivel binario (requeriría análisis de bytes internos)
- Cambios manuales en XML dentro de ZIP: posibles si usuario accedió estructura OOXML
- Firma digital no analizada en profundidad (requeriría especialista TSL)

---

## 7. CURRICULUM VITAE DEL PERITO

[CV resumido máx 1 página]
```

---

## Verificación eIDAS y Firma Cualificada

### Trusted Service List (TSL) Verification

Cuando documento contiene firma digital o timestamp cualificado:

**Procedimiento de Verificación:**

1. **Extraer Certificado Firmante:**
   - De PDF: `/AcroForm/Sig/Cert`
   - De DOCX: `customXml/relationships.xml` → certificado ASN.1

2. **Validar contra TSL:**
   ```
   TSL Europea (https://ec.europa.eu/growth/tools-databases/tsl/)
      ↓
   Buscar Emisor Certificado (CA)
      ↓
   Verificar Status: "Under Supervision" / "Accredited" / "Revoked"
      ↓
   Si QualifiedTSA o QualifiedESeal → Presunción Art. 25.2 eIDAS
   ```

3. **Validación Criptográfica:**
   - Firma válida (RSA-2048 mínimo, hash SHA-256+)
   - Certificado dentro período validez
   - Revocation check (CRL / OCSP)

### Clasificación Firmas Electrónicas (Reg. UE 910/2014)

| Tipo | Definición | Art. eIDAS | Valor Probatorio | Detectabilidad |
|---|---|---|---|---|
| **Simple (SES)** | Datos anexados o lógicamente asociados | Art. 3(10) | Bajo (prueba débil) | URL, hash visible |
| **Avanzada (AdES)** | Identificable, ligada exclusivamente, crea vínculo | Art. 26 | Intermedio | Certificado sin TSL |
| **Cualificada (QES)** | Avanzada + sellada por TSA cualificada | Art. 27 | **Máximo (presunción legalidad)** | TSL validable |

**Artículo 25.2 eIDAS - PRESUNCIÓN CRÍTICA:**
> "Las firmas electrónicas cualificadas tendrán la misma fuerza probatoria que las firmas hechas a mano."

**Implicación Forense:** Si documento contiene firma cualificada verificable en TSL, el órgano judicial **presume autenticidad e integridad** sin prueba adicional de la parte que aporta. Inicia la carga probatoria en la parte que cuestiona.

### Metadata Forensics × Digital Signature Validation

**Escenario:** Documento DOCX con firma cualificada, pero metadatos muestran modificación posterior.

**Análisis Cruzado:**

```json
{
  "documento": "contrato_firmado.docx",
  "firma_cualificada": {
    "presente": true,
    "tipo": "QES (Art. 27 eIDAS)",
    "tsa_issuer": "Camerfirma S.A. (Accredited TSL)",
    "timestamp_firma": "2024-02-15T10:30:00Z",
    "status_verificacion": "VALIDO"
  },
  "metadatos_analisis": {
    "created": "2024-02-01T14:00:00Z",
    "lastModified": "2024-02-16T09:00:00Z",
    "última_modificacion_posterior_firma": true,
    "tiempo_diferencia": "23 horas"
  },
  "conclusión_forense": "INCONSISTENCIA CRÍTICA: Firma cualificada 2024-02-15 10:30 UTC, pero metadata muestra edición 2024-02-16 09:00 UTC (POSTERIOR). Indica manipulación post-firma o secuestro de firma.",
  "recomendación": "Aunque QES presume autenticidad por TSL validable, metadata forense desafía integridad post-firma. Requiere análisis experto firma digital (no solo metadatos)."
}
```
```
