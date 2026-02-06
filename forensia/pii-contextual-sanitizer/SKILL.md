---
name: pii-contextual-sanitizer
description: Intelligently redact personally identifiable information while preserving legal context, distinguishing public figures (judges, prosecutors) from private parties. Deploy spaCy legal NER model or Hugging Face legal-transformers for multi-language support (ES, EN, FR, DE). Generate k-anonymity compliant pseudonymization with AES-256-GCM reversible token encryption. Ensure RGPD Art. 4(5) pseudonymization compliance and AEPD anonymization guidelines for CENDOJ court decision publication. Triggers for sentencing anonymization, cross-border litigation documents, and data-minimization workflows.
---

# PII Contextual Sanitizer

Redact sensitive data while preserving litigation context across multi-language documents with cryptographically verifiable anonymization.

## Topología de Aplicación

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Documento       │───▶│ NER Legal        │───▶│ Clasificación   │
│ Original        │    │ (Named Entity    │    │ Público/Privado │
│                 │    │ Recognition)     │    │                 │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Documento       │◀───│ Token            │◀───│ Sustitución     │
│ Sanitizado      │    │ Reversible       │    │ Selectiva       │
└─────────────────┘    │ (Cifrado)        │    │                 │
                       └──────────────────┘    └─────────────────┘
```

---

## Cuándo Usar

- Preparar documentos para publicación de sentencias
- Anonimizar para formación/ejemplos
- Cumplimiento RGPD en gestión documental
- Compartir casos con terceros sin revelar identidades

---

## Named Entity Recognition (NER) Models & Deployment

### Recommended NER Solutions for Multi-Language

| Model | Languages | Accuracy | Cost | Use Case |
|---|---|---|---|---|
| **spaCy es_dep_news_trf** | Spanish | 95% | Open-source | Spanish court documents, CENDOJ prep |
| **Hugging Face legal-transformers** | EN, FR, DE, ES | 92% | Open/Paid | Cross-border litigation, EU directives |
| **Transformers + finetuning** | Multi (configurable) | 93%+ | Moderate | Organization-specific domain adaptation |
| **BERT-base-multilingual** | 100+ languages | 88% | Open-source | Quick deployment, lower precision |

**Recommendation:** Start with spaCy es_dep_news_trf for Spanish documents; escalate to Hugging Face transformers for EU multi-language bundles.

## Entities Detected & Pseudonymization Rules

### Private PII (REDACT)

| Entity | Example | Token | Anonymization Method |
|---|---|---|---|
| PERSONA_PRIVADA | "D. Juan García López" | [PERSONA_001] | k-anonymity: min 5 persons per token |
| DNI/NIE | "12345678A" | [DNI_XXX] | Suppress last 3 chars; irreversible in publication |
| TELEFONO | "+34 612 345 678" | [TEL_XXX] | Full number replaced; prefix preserved (optional) |
| EMAIL | "juan@gmail.com" | [EMAIL_XXX] | Domain generic, username redacted |
| DIRECCION | "C/ Mayor 15, 3ºB" | [DIR_XXX] | Suppress street number and floor; preserve locality |
| CUENTA_BANCARIA | "ES12 1234 5678..." | [IBAN_XXX] | Full IBAN replaced; country code optional |

### Public Entities (PRESERVE)

| Entity | Example | Action | Legal Basis |
|---|---|---|---|
| JUEZ | "Magistrado D. Garzón" | PRESERVE | Public official in exercise (AEPD guidelines) |
| FISCAL | "Fiscalía Provincial" | PRESERVE | Government prosecutor, public role |
| JUZGADO | "Juzgado nº 3 de Madrid" | PRESERVE | Court identifier, public record |
| ORGANISMO | "Agencia Tributaria" | PRESERVE | Government agency, public registry |
| EMPRESA_PUBLICA | "Renfe S.A." | EVALUATE | If named in CENDOJ publication list → preserve |

### Multi-Language Entity Detection Example

```
ORIGINAL (ES): "El demandado D. Juan García, residente en Madrid..."
ORIGINAL (EN): "The defendant Mr. John Smith, resident in New York..."
ORIGINAL (FR): "Le défendeur M. Jean Dupont, domicilié à Paris..."

OUTPUT (all languages):
ES: "El demandado [PERSONA_001], residente en [LOC_001]..."
EN: "The defendant [PERSONA_001], resident in [LOC_001]..."
FR: "Le défendeur [PERSONA_001], domicilié à [LOC_001]..."
```

---

## Reversible Token Encryption (AES-256-GCM)

Cryptographically secure pseudonymization preserving internal data retrieval:

```python
# Token generation with AES-256-GCM
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

original = "D. Juan García López"
token = "[PERSONA_A7F3]"

# Master key management (256-bit)
master_key = os.urandom(32)  # 256 bits
nonce = os.urandom(12)  # 96-bit nonce (GCM standard)

cipher = AESGCM(master_key)
ciphertext = cipher.encrypt(nonce, original.encode(), None)

# Storage: reversible_mapping.enc
# Entry: {token: (nonce, ciphertext)}
mapping = {
    "[PERSONA_A7F3]": (nonce.hex(), ciphertext.hex())
}
```

**Key Features:**
- **Authentication Tag:** GCM prevents tampering detection
- **Master Key Escrow:** Secure key management (HSM or encrypted Vault)
- **Decryption:** Authorized parties only (RGPD Art. 4(5) pseudonymization requirement met)

## Anonymity Metrics (k-anonymity & l-diversity)

Verify anonymization robustness:

```
k-anonymity: ≥5 individuals per token
- Each [PERSONA_001] represents minimum 5 distinct persons
- Prevents re-identification via quasi-identifiers

l-diversity: ≥2 distinct sensitive values per equivalence class
- If [PERSONA_001] includes both victims & defendants, l=2
- Prevents attribute disclosure
```

---

## Contextual Legal Rules & Procedural Role Preservation

### Rule 1: Public Official Exception

Preserve name when accompanied by public role:
```
ORIGINAL: "El demandado D. Juan García comunicó al Juez Fernando Pérez..."
OUTPUT:   "El demandado [PERSONA_001] comunicó al Juez Fernando Pérez..."
```
**Rationale:** Judicial role is public record; judicial independence protected under RGPD Art. 9(2)(g).

### Rule 2: Procedural Role Preservation

When name essential to litigation context:
```python
PRESERVE_ROLE_TITLES = {
    "juez", "magistrado", "fiscal", "procurador",
    "letrado", "procurador judicial", "perito judicial",
    "abogado del estado"
}

# If private person (e.g., "attorney John Smith") →
# Preserve "attorney" role, redact name → "[PERSONA_001] (counsel)"
```

### Rule 3: Institutional References

Preserve institutional context, redact persons:
```
ORIGINAL: "La empresa Garrigues asesorada por el despacho de D. Carlos López..."
OUTPUT:   "La empresa Garrigues asesorada por el despacho de [PERSONA_001]..."
```

### Rule 4: Dates, Locations, Events

Preserve for temporal/geographic context unless connected to identifiable person:
```
ORIGINAL: "Fue condenado el 15 de marzo de 2024 en el Juzgado nº 3 de Madrid"
OUTPUT:   "[PERSONA_001] fue condenado el 15 de marzo de 2024 en el Juzgado nº 3 de Madrid"
```

---

## Concrete Example: CENDOJ Court Decision Publication

**Scenario:** Supreme Court judgment needs anonymization before CENDOJ publication (Spanish case law database).

**Input Document:** 12-page judgment with 47 PII entities

**Processing:**
1. Deploy spaCy es_dep_news_trf on entire text
2. Detect: Juan García López (defendant), María Martínez (plaintiff), Judge Gómez, emails, addresses
3. Apply k-anonymity (k=5): Group similar entity types
4. Apply l-diversity: Ensure outcomes vary within entity groups
5. Generate reversible tokens for authorized retrieval (Ministry of Justice only)
6. Create CENDOJ-compliant publication

**Output Distribution:**
- **Public (CENDOJ):** Anonymized version with [PERSONA_001], [PERSONA_002], etc.
- **Restricted (Ministry):** Reversible token mapping secured with AES-256-GCM
- **Audit Trail:** Who accessed decrypted mapping, timestamp, purpose

## Sanitization Output & CENDOJ Compliance

```json
{
  "source_document": "sentencia_ts_2024_12345.pdf",
  "anonymized_document": "sentencia_ts_2024_12345_anon.pdf",
  "anonymization_timestamp": "2024-12-10T15:30:00Z",
  "statistics": {
    "entities_detected": 47,
    "entities_redacted": 32,
    "entities_preserved": 15,
    "k_anonymity_score": 5.2,
    "l_diversity_score": 2.1
  },
  "entities_processed": [
    {
      "original": "D. Juan García López",
      "token": "[PERSONA_001]",
      "entity_type": "PRIVATE_INDIVIDUAL",
      "role": "DEFENDANT",
      "occurrences": 12,
      "reversible": true
    },
    {
      "original": "Magistrado D. Fernando Gómez García",
      "token": null,
      "entity_type": "PUBLIC_OFFICIAL",
      "role": "JUDGE",
      "occurrences": 8,
      "preserved_reason": "Judicial independence; public record"
    }
  ],
  "encryption_metadata": {
    "algorithm": "AES-256-GCM",
    "reversible_mapping_file": "sentencia_12345_mapping.enc",
    "master_key_location": "AWS KMS / HSM",
    "access_control": "Ministry of Justice authorized personnel only"
  },
  "cendoj_ready": true
}
```

---

## Regulatory Compliance Framework

| Standard | Requirement | Implementation |
|---|---|---|
| **RGPD Art. 4(5)** | Pseudonymization definition | Irreversible tokens in public version; reversible escrow for authorized access |
| **RGPD Art. 17** | Right to erasure | Reversible tokens enable complete data purging from encrypted mapping |
| **LOPD-GDD** | Data minimization | k-anonymity ≥5 prevents individual re-identification |
| **AEPD Guidelines** | Anonymization techniques | Suppression + generalization + encryption per AEPD 2023 guidance |
| **Ley 15/2022** | Court judgment anonymization | Mandatory for CENDOJ publication; spaCy ES model recommended |
| **STS 363/2017** | Electronic document authenticity | Document hash + metadata preservation for audit trail |

## Integration & Deployment

```python
# Production workflow
from spacy_legal import load_model
from pii_sanitizer import DocumentSanitizer, EncryptionManager

# Load Spanish legal NER model
nlp = load_model("es_dep_news_trf_legal")

# Initialize sanitizer with encryption
sanitizer = DocumentSanitizer(
    nlp_model=nlp,
    encryption_algorithm="AES-256-GCM",
    master_key_source="AWS_KMS",
    k_anonymity_threshold=5,
    l_diversity_threshold=2
)

# Process document
result = sanitizer.sanitize_document(
    input_path="sentencia.pdf",
    preserve_public_figures=True,
    generate_reversible_tokens=True,
    output_format="PDF",
    cendoj_compliant=True
)

# Output includes:
# - sentencia_anon.pdf (public, anonymized)
# - sentencia_mapping.enc (reversible tokens, encrypted)
# - audit_trail.json (access control log)
```

## Evaluación de Riesgo de Reidentificación

### WP29/EDPB Opinion 05/2014 sobre Técnicas de Anonimización

Guidance crítica del Grupo de Trabajo Art. 29 (ahora EDPB) sobre cuándo datos son verdaderamente anónimos:

**Conclusión Clave:** Anonimización robusta requiere resistencia a "ataques" realistas, no solo teóricos.

### Tres Modelos de Ataque Re-identificación

#### 1. Singling Out (Aislamiento)

Capacidad atacante de aislar registro individual de grupo:

```
Ejemplo VULNERABLE:
Documento Original: "D. Juan García, DNI 12345678A, Juzgado Madrid"
Token: [PERSONA_001], [JUD_MADRID]

Riesgo: Si solo 1 abogado en Juzgado Madrid nacido 1975, token
revela identidad por cruce quasi-identifiers (edad + localidad).
```

**Prevención:** k-anonymity ≥5: Cada token [PERSONA_X] debe
representar MÍNIMO 5 individuos distintos.

#### 2. Linkability (Vinculabilidad)

Capacidad atacante de vincular 2 registros al mismo individuo:

```
Ejemplo VULNERABLE:
Documento 1 (público): "Condenado por fraude, [PERSONA_001]"
Documento 2 (público): "Fiscalía vs [PERSONA_001], 2024-03-15"

Riesgo: Si atacante tiene acceso a AMBOS documentos públicos,
puede vincular registros y confirmar identidad via contexto externo.
```

**Prevención:** Usar tokens DISTINTOS en documentos distintos,
aunque se refieran misma persona (si públicos separados).

#### 3. Inference (Inferencia)

Capacidad atacante deducir atributo sensible de registro anonimizado:

```
Ejemplo VULNERABLE:
"[PERSONA_001] condenado por delito sexual, registrado en VPR"

Riesgo: Aunque nombre anonimizado, "VPR" = Registro Delincuentes Sexuales.
Información sensible revelada (naturaleza delito) permite inferencias
discriminatorias aunque nombre oculto.
```

**Prevención:** l-diversity ≥2: Dentro grupo anonimizado,
mínimo 2 valores distintos para atributos sensibles.

### k-anonymity Configuration para Documentos Legales

**Threshold Recomendado: k ≥ 5**

Justificación: Documento legal típico con 30-50 PII, k=5 requiere
grupo mínimo 5 personas → hace diferenciación costosa para atacante.

**Cálculo Práctico:**

```
Caso: Sentencia con 15 demandados
Quasi-identifiers: edad, sexo, profesión, localidad
Grupos de equivalencia (misma combinación edad/sexo/profesión/localidad):
  - Grupo 1: [3 hombres, 45-50 años, abogados, Madrid] → k=3 (INSUFICIENTE)
  - Grupo 2: [8 mujeres, 30-35 años, enfermeras, Barcelona] → k=8 (OK)
  - Grupo 3: [2 hombres, 60+ años, jubilados, Sevilla] → k=2 (INSUFICIENTE)

ACCIÓN: Generalizar más Grupo 1 y 3 (aumentar rango edad, agrupar profesiones)
hasta alcanzar k≥5 en todos grupos.
```

### l-diversity y t-closeness para Atributos Sensibles

**l-diversity: ≥2 valores distintos sensible por grupo**

```json
{
  "grupo_anonimizado": "[PERSONA_001]",
  "ocurrencias": 5,
  "delitos_sentenciados": ["fraude", "fraude", "robo", "robo", "lavado dinero"],
  "l_diversity_value": 3,
  "calificacion": "PASS (≥2)"
}
```

**t-closeness: Distribución sensibles en grupo ≈ distribución población**

```
Modelo: Si documento público muestra 50% condenados por fraude,
50% por robo en población total, entonces grupo anonimizado
[PERSONA_X] debe mantener distribución ~50/50 fraude/robo.

t = max distance entre 2 distribuciones
Si t < 0.2 → Aceptable (≥80% similitud distribución)
Si t ≥ 0.2 → Riesgo inference (atacante deduce atributo)
```

### Quantitative Risk Scoring: Probabilidad Re-identificación

**Fórmula simplificada NIST (SP 800-188):**

```
Risk Score = (Probability Singling Out) × (Probability Linkability)
             × (Probability Inference)

Rango: 0 (sin riesgo) a 1 (riesgo máximo)

Threshold de Aceptabilidad: Risk Score ≤ 0.05 (≤5% probabilidad
re-identificación dado acceso a auxiliary data externa)
```

**Cálculo Ejemplo:**

```
Documento Original: Sentencia con 20 demandados

Singling Out Risk:
  - k=5 (mínimo grupo) → P_singling = 1/5 = 0.20

Linkability Risk:
  - Tokens distintos documentos → P_linkability = 0.15 (correlated via timestamps)

Inference Risk:
  - l-diversity=2 para delito → P_inference = 0.10

Risk Score = 0.20 × 0.15 × 0.10 = 0.003 (0.3%)
Veredicto: ACEPTABLE (<<0.05)
```

### Decision Matrix: Seudonimización vs. Anonimización

**Seudonimización (Art. 4(5) RGPD):** Datos reversibles con clave maestra

```
✓ Usar SEUDONIMIZACIÓN si:
  - Reversibilidad necesaria (ej: retractividad, derecho al olvido)
  - Comunicación restringida (solo autoridades judiciales acceso)
  - Risk Score < 0.05 con clave segura (AES-256-GCM)
  - Ejemplo: Documento interno tribunal con mapping encriptado

✗ NO usar seudonimización si:
  - Publicación pública (ej: CENDOJ)
  - Riesgo key compromise (breach)
  - Regulatory requirement anonimización total (algunos casos RGPD)
```

**Anonimización Irreversible:** Tokens impossibles de invertir

```
✓ Usar ANONIMIZACIÓN si:
  - Publicación pública (CENDOJ, jurisprudencia web)
  - Máximo grado protección privacidad requerido
  - Garantía irreversibilidad
  - Risk Score ≤ 0.01 y k≥8

✗ NO usar anonimización si:
  - Necesidad potencial re-identificación
  - Parte interesada requiere prueba (anonimización impide)
```

### Matriz de Decisión Completa

| Escenario | Seudonimización | Anonimización | Risk Score Objetivo |
|---|---|---|---|
| **CENDOJ Publicación** | No | Sí | ≤0.01 |
| **Documento Tribunal (Restricto)** | Sí | No | ≤0.05 |
| **Formación/Enseñanza** | Sí (intern) | Sí (público) | ≤0.05 |
| **Litigio Activo** | Sí (partes) | No | ≤0.10 |
| **Investigación Académica** | Sí (encriptado) | No | ≤0.05 |

---

## Registro de Seudónimos y Gestión de Claves

### Tabla de Mapeo Encriptada

**Estructura:**

```python
# Mapping Table (en disco, cifrado AES-256-GCM)

mapping_table = {
    "[PERSONA_001]": {
        "original": "[ENCRYPTED_AES256GCM]",
        "nonce": "a1b2c3d4e5f6g7h8i9j0",
        "created_timestamp": "2024-12-10T15:30:00Z",
        "expires_timestamp": "2027-12-10T15:30:00Z",
        "created_by": "perito@tribunal.es",
        "accessed_by": [
            {
                "user": "juez@tribunal.es",
                "timestamp": "2024-12-11T09:15:00Z",
                "purpose": "Sentence review",
                "ip_address": "[ENCRYPTED]"
            },
            {
                "user": "secretary@tribunal.es",
                "timestamp": "2024-12-11T10:00:00Z",
                "purpose": "Publication check (CENDOJ)",
                "ip_address": "[ENCRYPTED]"
            }
        ]
    },
    "[PERSONA_002]": { ... }
}
```

### Especificaciones de Cifrado

**Algoritmo:** AES-256-GCM (Galois/Counter Mode)

```
Parámetros:
- Key: 256 bits (32 bytes) de entropy alta
- Nonce: 96 bits (12 bytes) aleatorio, NUNCA reutilizado
- Authentication Tag: 128 bits (auto-generado GCM)
- Plaintext: "Juan García López"
- AAD (Additional Authenticated Data): "[PERSONA_001]" (token)

Resultado:
- Ciphertext: 32 bytes (XOR con keystream AES-CTR)
- Tag: 16 bytes (garantiza integridad)
- Nonce: 12 bytes (enviado con ciphertext, no secreto)

Verificación: Tag previene tampering. Si alguien modifica ciphertext,
decryption fallará con excepción authentication.
```

### Control de Acceso: MFA + RBAC

**Multi-Factor Authentication (MFA):**

```
Requisito: Acceso mapping table requiere:
1. Contraseña (factor conocimiento)
2. Token TOTP/U2F (factor posesión)
3. Biometría (factor inherencia) - OPCIONAL pero recomendado

Implementación:
  - Azure AD MFA / Okta
  - Todos accesos logeados con timestamp
  - Fallida MFA trigger alerta seguridad
```

**Role-Based Access Control (RBAC):**

| Rol | Acceso Lectura | Acceso Escritura | Proposito |
|---|---|---|---|
| **Juez** | SÍ | NO (solo lectura) | Revisión sentencias propias |
| **Secretario Juzgado** | SÍ (limitado) | NO | Verificación CENDOJ publicación |
| **Perito Forense** | NO | SÍ (creación inicial) | Generar mapping durante análisis |
| **Auditor Interno** | SÍ (logs solo) | NO | Revisión accesos compliance |
| **Ministerio Justicia** | SÍ (emergencias) | NO | Re-identificación casos especiales |

**Restricción:** Usuario accede solo su caso/expediente. Admin puede restringir por:
- Número expediente
- Rango fecha sentencia
- Localidad tribunal

### Política de Retención y Destrucción (RGPD Art. 5(1)(e))

**Art. 5(1)(e) RGPD - "Storage Limitation":**
> "Los datos personales se conservarán de forma que se permita
> la identificación de los interesados durante no más tiempo
> del necesario."

**Aplicación a Mapping Tables:**

```
Retención Máxima (calculada por tribunal):
  - Sentencia condenatoria: mapping conservado 15 años post-cumplimiento
  - Sentencia absolutoria: 5 años post-sentencia
  - Procedimiento en recurso: hasta resolución final + 5 años

Trigger Destrucción:
  - Vencimiento período retención
  - Solicitud RGPD Art. 17 (derecho olvido) por persona
  - Cese utilidad caso (no reversibilidad requerida)

Procedimiento Destrucción:
  1. Autorización Juez / DPO Tribunal
  2. Generación certificado destrucción
  3. Overwrite 3-pass Gutmann o certificado de destrucción HSM
  4. Acta de destrucción firmada digitalmente
  5. Registro destrucción en audit log (inmutable)

Prohibido: Simplemente "borrar" archivo sin verificación.
HSM/secure vault proporciona prueba criptográfica destrucción.
```

### Audit Log: Registro Acceso Inmutable

**Especificación Obligatoria (ISO/IEC 27001 A.12.4.1):**

```json
{
  "audit_log": [
    {
      "timestamp": "2024-12-11T09:15:32Z",
      "user_identifier": "juez@tribunal.es",
      "action": "READ",
      "resource": "[PERSONA_001]",
      "result": "SUCCESS",
      "ip_address": "192.168.1.100",
      "mfa_verified": true,
      "purpose": "Sentence review - Expediente 2024/12345",
      "duration_seconds": 42,
      "data_revealed": "Juan García López (decrypted)",
      "log_entry_hash": "SHA256:abcd1234...",
      "signed_by": "Auditor System Certificate"
    },
    {
      "timestamp": "2024-12-11T09:20:15Z",
      "user_identifier": "attacker@external.com",
      "action": "READ",
      "resource": "[PERSONA_001]",
      "result": "DENIED (MFA failed, wrong TOTP)",
      "ip_address": "203.0.113.45",
      "mfa_verified": false,
      "alert_generated": true,
      "alert_level": "CRITICAL"
    }
  ]
}
```

**Propiedades Auditoría:**

- **Inmutabilidad:** Cada entrada tiene hash anterior (blockchain-like)
- **Almacenamiento:** Base datos separada de mapping (acceso restringido auditor)
- **Rotación:** Logs archivados mensualmente, sin modificación post-cierre
- **Alertas Automáticas:**
  - Acceso fuera horario laboral
  - Múltiples fallos MFA
  - Acceso desde IP nueva
  - Acción NO AUTORIZADA (ej: WRITE sin permiso)

### Procedimientos Emergencia: Re-identificación bajo Orden Judicial

**Escenario:** Persona requiere acceso mapping table (ej: derecho al olvido, exoneración, etc.)

**Requisitos Procedimiento:**

1. **Solicitud Formal:**
   - Presentada ante tribunal competente
   - Justificación específica (ej: "Necesario para anular condenación errata")
   - Certificación abogado/procurador

2. **Autorización Judicial:**
   - Auto del Juez ordenando re-identificación
   - Limitación alcance (ej: "solo para [PERSONA_X]", no búsqueda masiva)
   - Confidencialidad: resultado acceso solo partes autorizadas

3. **Ejecución Técnica:**
   ```
   a) DPO Tribunal verifica orden judicial genuina
   b) HSM desbloquea master key bajo parámetros orden
   c) Perito autorizado decrypta solo entrada solicitada
   d) Resultado reportado al Juez (no a solicitante directo)
   e) Re-confirmación Juez antes entrega a partes
   f) Audit log CRÍTICO: timestamp, usuario, orden ref, resultado
   ```

4. **Documentación:**
   - Acta de re-identificación firmada por HSM custodian + Juez
   - Nada destruido (reversibilidad mantenida)
   - Notification procurador (si aplica)

---

## References

- AEPD: Técnicas de anonimización de datos (2023)
- ENFSI: Guidelines for digital evidence handling
- ISO/IEC 27001: Information security management
- WP29/EDPB Opinion 05/2014: Anonymisation Techniques
- NIST SP 800-188: De-Identification of Personal Information
- GDPR Art. 4(5), Art. 5(1)(e), Art. 17, Art. 32, Art. 33
