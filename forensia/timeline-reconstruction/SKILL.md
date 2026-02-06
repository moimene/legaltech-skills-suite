---
name: timeline-reconstruction
description: Reconstruct absolute, unified chronologies from thousands of unordered emails, chats, and documents with UTC normalization, chain-of-custody compliance (ISO/IEC 27037), anomaly detection using 3-sigma thresholds, and timezone disambiguation for multi-jurisdiction forensic investigations. Triggers when establishing temporal facts in litigation, internal corporate investigations, or fraud discovery.
---

# Timeline Reconstruction

Reconstruct forensic timelines from dispersed communications with full evidentiary integrity for expert testimony.

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Emails/Chats/   │───▶│ Extracción       │───▶│ Normalización   │
│ PDFs            │    │ Metadatos        │    │ UTC             │
│                 │    │ (EXIF, Headers)  │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Timeline JSON + │◀───│ Detección Gaps   │◀───│ Ordenación      │
│ Visualización   │    │ Anómalos         │    │ Cronológica     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Reconstruir secuencia de hechos en litigio
- Investigaciones internas corporativas
- Due Diligence temporal de comunicaciones
- Detección de manipulación de fechas

---

## Timestamp Source Hierarchy & Forensic Reliability

| Document Type | Primary Source | Secondary | ISO/IEC 27037 Status |
|---|---|---|---|
| Email (EML) | `Date` SMTP header | Received headers | Highly reliable (authenticated) |
| Email (MSG) | `SentTime` property | `ReceivedTime` | Subject to local clock manipulation |
| PDF | `ModDate` (XMP) | `/CreationDate` (Info dict) | Dependent on creator app accuracy |
| DOCX | `modified` (core.xml) | `LastSavedTime` | Vulnerable to manual editing of XML |
| XLSX | `created`/`modified` | Edit time in app.xml | Requires Track Changes verification |
| Image (JPEG) | EXIF `DateTimeOriginal` | EXIF `DateTimeDigitized` | Can be spoofed; geolocation useful |
| Chat Export | Message timestamp | Server-side logs preferred | Client-generated, verify server records |
| Logs | System clock synchronized | NTP offset data | Most reliable if authenticated |

**Chain of Custody Requirement (ISO/IEC 27037:2018):** Document acquisition timestamp, hash, and integrity for all sources. For maximum evidentiary reliability, employ *sellado de tiempo cualificado eIDAS* (qualified eIDAS timestamps per Regulation EU 910/2014) to cryptographically bind forensic evidence to immutable temporal markers, fulfilling RDL 6/2023 requirements for digital evidence admissibility in Spanish courts.

---

## Verificación de Integridad y Sellado de Tiempo

### Hash Chain para Evidencia Digital

Cada documento ingresado requiere cadena de integridad SHA-256 en tres puntos críticos:

1. **Hash de Ingesta:** SHA-256 al momento de adquisición forense
2. **Hash de Procesamiento:** SHA-256 tras normalización y análisis
3. **Hash de Salida:** SHA-256 en informe final (previene manipulación post-generación)

**Formato de Salida por Evento:** Cada entrada en timeline incluye:
```json
{
  "timestamp_utc": "2024-02-15T10:47:00Z",
  "documento_hash_entrada": "SHA256:ab12cd34ef56gh78ij90kl12mn34op56qr78st90uv12wx34yz56ab78cd90ef",
  "documento_hash_salida": "SHA256:xy98zw76uv54ts32rq10po98nm76lk54ji32hg10fe98dc76ba54zy98xw76uv"
}
```

### Sellado de Tiempo Cualificado (eIDAS Reg. UE 910/2014)

**Cuándo Aplicar:** Para cronologías con valor probatorio elevado (litigio, fraude empresarial).

**Verificación:** Todo sellado debe proceder de Proveedor de Servicios de Confianza Cualificado:
- **España:** Firmaprofesional, Camerfirma, Certicámara
- **EU:** TSA lista negra en Trusted Service List (TSL)

**Formato de Proof-of-Timestamp:**
```xml
<!-- RFC 3161 Time-Stamp Token -->
<timeStampToken>
  <contentInfo>
    <contentType>1.2.840.113549.1.7.2</contentType>
    <content>
      <signedData>
        <signerInfo>
          <signature>...</signature>
          <signingCertificate>
            <issuer>TSA Cualificada ES</issuer>
            <serialNumber>qualified</serialNumber>
          </signingCertificate>
        </signerInfo>
      </signedData>
    </content>
  </contentInfo>
</timeStampToken>
```

**Integración en Timeline JSON:**
```json
{
  "timestamp_utc": "2024-02-15T10:47:00Z",
  "timestamp_proof_rfc3161": "MIICaDCCAc2gAwIBAgIJAKwbx...",
  "tsa_issuer": "Firmaprofesional (ES)",
  "tsa_qualified_status": "QualifiedTSA",
  "timestamp_validity": "2024-02-15T10:47:00Z ± 1 segundo"
}
```

---

## Cadena de Custodia Digital

### Registro Obligatorio de Custodia

Cumplimiento con Art. 382 LEC: Instrumentos de filmación, grabación y semejantes.

**Formato de Formulario de Ingesta (ISO/IEC 27037:2012):**

```
CADENA DE CUSTODIA DIGITAL
════════════════════════════════════════════════════════════

Caso: [Número Expediente]
Investigador Principal: [Nombre, Acreditación]
Fecha Adquisición: [YYYY-MM-DD HH:MM:SS UTC]

┌─────────────────────────────────────────────────────────┐
│ EVIDENCIA #1                                            │
├─────────────────────────────────────────────────────────┤
│ Descripción: [Tipo doc, ej: Email EML]                 │
│ Identificador Único: [SHA256:...]                      │
│ Tamaño: [bytes]                                        │
│ Formato Original: [EML / DOCX / XLSX / etc]            │
│ Adquirido de: [Fuente, ej: servidor Office365]         │
│ Método Adquisición: [forense copy / export / backup]   │
│ Recibido por: [Nombre perito]                          │
│ Fecha/Hora: [YYYY-MM-DD HH:MM:SS UTC]                  │
│ Firma Digital: [Certificado X.509 del perito]          │
│ Observaciones: [Cadenas de email, anomalías]           │
└─────────────────────────────────────────────────────────┘

TRANSFERENCIAS POSTERIORES:
De: [Perito A] → A: [Perito B]
  Fecha: [YYYY-MM-DD HH:MM:SS UTC]
  Hash Verificado: SHA256 [checksum]
  Condiciones: [Sello criptográfico, custodia controlada]
  Firma: [Certificado X.509]

  Fecha: [YYYY-MM-DD HH:MM:SS UTC]
  Hash Verificado: SHA256 [checksum]
  Condiciones: [Almacenamiento encriptado, acceso restringido]
  Firma: [Certificado X.509]
```

### Requisitos Art. 382 LEC (Medios de Prueba Electrónica)

| Requisito | Implementación | Verificable |
|---|---|---|
| **Autenticidad** | Certificado digital perito + firma timestamp | X.509 chain validation |
| **Integridad** | Hash SHA-256 + sellado eIDAS | RFC 3161 verificable |
| **Trazabilidad** | Registro custodia con timestamps cualificados | Audit log encriptado |
| **Admisibilidad** | Protocolo ISO/IEC 27037:2012 documentado | Declaración del perito (Art. 335 LEC) |

### Checklist Cumplimiento ISO/IEC 27037:2012

**Identificación:**
- [ ] Evidencia identificada unívocamente (hash + descripción)
- [ ] Procedencia documentada (fuente, dispositivo, usuario)
- [ ] Contexto forense registrado (ej: servidor Office365, buzón activo)

**Recopilación:**
- [ ] Método no invasivo (copia forense, no alteración)
- [ ] Cadena custodial iniciada antes de adquisición
- [ ] Perito acreditado (certificado digital, DNI)

**Adquisición:**
- [ ] Hash original capturado en situ
- [ ] Dispositivo adquisición certificado
- [ ] Testigos presentes (si aplica)
- [ ] Timestamp cualificado al finalizar

**Preservación:**
- [ ] Almacenamiento: cifrado AES-256, acceso MFA
- [ ] Verificación integridad: hash diaria
- [ ] Custodia controlada: registro entrada/salida
- [ ] Cadena nunca interrumpida (sin testigos = inadmisible)

---

## Detección de Anomalías

### Statistical Gap Detection (3-Sigma Thresholds)

Identify unusual periods without activity using statistical methods:

```python
# Calculate inter-event intervals
intervals = [t2 - t1 for t1, t2 in consecutive_events]
mu = mean(intervals)
sigma = stdev(intervals)

# Anomaly threshold: 3-sigma rule
anomaly_threshold = mu + (3 * sigma)
suspicious_gaps = [gap for gap in gaps if gap > anomaly_threshold]
```

### Burst Detection & Automated Dispatch

- 10+ emails within 2 minutes = probable mail merge/automation
- Activity outside business hours (weekends, 02:00-06:00) with pattern match
- Identical timestamps across multiple recipients = potential spoofing

### Temporal Inconsistencies

- Response timestamp before original message (header manipulation)
- File modification before creation (clock tampering)
- Timezone shifts within same conversation thread (multi-device indicators)
- Email header timestamp vs. content date discrepancy >30 min (suspicious)

---

## Concrete Example: Corporate Fraud Investigation

**Scenario:** Embezzlement claims in construction contract; need to establish intent via email timeline.

**Input:** 2,500 emails, contract versions, bank transfers, chat exports (Jan 2023–Mar 2024)

**Process:**
1. Extract timestamps from EML headers (primary) + database logs (secondary)
2. Normalize all to UTC; flag timezone inconsistencies >30 min
3. Detect 3-sigma gaps: mean interval 8h, sigma 4h → threshold 20h
4. Identify burst: CFO sent 23 invoices in 3 minutes on 2024-02-15 10:47–10:50 UTC

**Key Finding:** Invoice batch timestamp conflicts with CFO's Outlook deleted-item recovery showing access from Venezuela IP 2024-02-15 02:47 UTC (8h earlier, different timezone). This breach in chain of custody undermines invoice authenticity.

**Expert Testimony Ready:** Timeline shows technical manipulability per *RDL 6/2023 (que deroga la Ley 18/2011)* standards and triggers Daubert reliability gate (Frye standard N/A in Spanish courts but STS standards apply).

## Output JSON

```json
{
  "timeline": {
    "periodo": {"inicio": "2024-01-15T08:30:00Z", "fin": "2024-03-22T17:45:00Z", "duracion_dias": 67},
    "cadena_custodia": {"hash_integral": "SHA256:ab12cd34...", "adquisicion": "2024-11-20T14:30:00Z", "iso27037_compliant": true}
  },
  "eventos": [
    {
      "timestamp_utc": "2024-02-15T10:47:00Z",
      "timestamp_local": "2024-02-15T11:47:00+01:00",
      "tipo": "EMAIL_BATCH",
      "de": "cfo@empresa.com",
      "cantidad": 23,
      "duracion_segundos": 180,
      "anomalia": "BURST_AUTOMATIZADO",
      "archivo_hash": "SHA256:xyz789..."
    }
  ],
  "anomalias_detectadas": [
    {
      "tipo": "GAP_ESTADISTICO",
      "timestamp": "2024-02-01T18:00:00Z",
      "duracion_dias": 13.6,
      "z_score": 3.4,
      "severidad": "CRITICA",
      "contexto": "Sin comunicaciones en período de supuesto envío de facturas"
    },
    {
      "tipo": "INCONSISTENCIA_TIMEZONE",
      "evidencia": "VPN access from Venezuela (UTC-4) vs. email timestamp (UTC+1)",
      "severidad": "CRITICA",
      "implicacion": "Posible manipulación de metadatos"
    }
  ]
}
```

---

## Evidentiary Reliability Framework

For expert testimony admissibility (STS jurisprudence):

| Factor | Standard | Verification |
|---|---|---|
| **Methodology** | ISO/IEC 27037:2018 | Documented chain of custody + hash verification |
| **Reproducibility** | Daubert Gate 3 | Same data → same timeline output |
| **Error Rate** | <5% timezone ambiguity | Multi-source timestamp triangulation |
| **Peer Review** | Published forensic standards | References ISO, ENFSI guidelines |

## References & Legal Basis

- **ISO/IEC 27037:2018:** Guidelines for identification, collection, acquisition and preservation of digital evidence
- **RDL 6/2023:** Current Spanish digital evidence framework (derogated Ley 18/2011); electronic evidence in Spanish judicial proceedings admissibility based on authenticity & integrity
- **RD 1065/2015 (LexNET):** Electronic judicial communications system; standardized timestamp certification and chain of custody for court-filed documents
- **eIDAS (Regulation EU 910/2014):** Qualified timestamps and advanced/qualified electronic signatures for forensic evidence integrity verification
- **Sellado de Tiempo Cualificado eIDAS:** Qualified timestamping mechanism for chain of custody verification in forensic investigations
- **STS 678/2014:** Secret recordings admissibility; applies to timestamped communications
- **CRESPO-PÉREZ Framework:** Daubert-equivalent reliability standard in Spanish courts for digital expert testimony

## Integration

```bash
# Require forensic tool (e.g., Encase, AccessData, or open-source)
# Document tool version, settings, and validation
# Generate PDF report with timeline visualization and chain-of-custody metadata
```
