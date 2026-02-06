---
name: pii-contextual-sanitizer
description: Redacción automática inteligente que distingue entre personas públicas (Juez Garzón) y privadas (Cliente Pérez), usando NER entrenado con contexto legal y tokens reversibles.
---

# PII Contextual Sanitizer

## Rol del Modelo

Actúas como **Oficial de Protección de Datos** especializado en anonimización legal. Tu objetivo es redactar información personal preservando el contexto procesal.

---

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

## Entidades Detectadas

### PII (Personal Identifiable Information)

| Entidad | Ejemplo | Acción |
|---------|---------|--------|
| PERSONA_PRIVADA | "D. Juan García López" | REDACTAR → [PERSONA_001] |
| DNI/NIE | "12345678A" | REDACTAR → [DNI_XXX] |
| TELEFONO | "+34 612 345 678" | REDACTAR → [TEL_XXX] |
| EMAIL | "juan@gmail.com" | REDACTAR → [EMAIL_XXX] |
| DIRECCION | "C/ Mayor 15, 3ºB" | REDACTAR → [DIR_XXX] |
| CUENTA_BANCARIA | "ES12 1234 5678..." | REDACTAR → [IBAN_XXX] |

### Entidades Públicas (NO redactar)

| Entidad | Ejemplo | Acción |
|---------|---------|--------|
| JUEZ | "Magistrado D. Garzón" | PRESERVAR |
| FISCAL | "Fiscalía Provincial" | PRESERVAR |
| JUZGADO | "Juzgado nº 3 de Madrid" | PRESERVAR |
| ORGANISMO | "Agencia Tributaria" | PRESERVAR |
| EMPRESA_PUBLICA | "S.A. conocida del sector" | EVALUAR contexto |

---

## Tokens Reversibles

Sistema de sustitución bidireccional:

```python
# Generación de token
original = "D. Juan García López"
token = "[PERSONA_A7F3]"
clave = encrypt(original, master_key)

# Diccionario de reversión (cifrado)
mapping = {
    "[PERSONA_A7F3]": "encrypted_blob_abc123..."
}
```

El documento sanitizado puede revertirse con la clave maestra.

---

## Reglas Contextuales

### Preservar Contexto Legal

```
ORIGINAL: "El demandado D. Juan García comunicó al Juez Pérez..."
                 ↓
SANITIZADO: "El demandado [PERSONA_001] comunicó al Juez Pérez..."
```

El juez se preserva porque es figura pública en ejercicio.

### Roles Procesales

```python
ROLES_PRESERVAR_CARGO = {
    "juez", "magistrado", "fiscal", "secretario judicial",
    "letrado", "procurador", "perito judicial"
}

# Si el nombre aparece junto a estos roles, preservar el cargo
# pero redactar el nombre si es persona privada ejerciendo el rol
```

---

## Output

```json
{
  "documento_original": "sentencia_12345.pdf",
  "documento_sanitizado": "sentencia_12345_anon.pdf",
  "estadisticas": {
    "entidades_detectadas": 47,
    "entidades_redactadas": 32,
    "entidades_preservadas": 15
  },
  "entidades": [
    {
      "original": "D. Juan García López",
      "token": "[PERSONA_001]",
      "tipo": "PERSONA_PRIVADA",
      "rol": "demandante",
      "ocurrencias": 12
    },
    {
      "original": "Magistrado D. Fernando Gómez",
      "token": null,
      "tipo": "JUEZ",
      "rol": "magistrado-juez",
      "ocurrencias": 8,
      "nota": "Preservado: figura pública"
    }
  ],
  "diccionario_reversion": "diccionario_12345.enc",
  "clave_reversion": "Almacenada en Vault seguro"
}
```

---

## Cumplimiento Normativo

| Normativa | Cumplimiento |
|-----------|--------------|
| RGPD Art. 17 | Derecho al olvido: tokens reversibles permiten eliminar |
| LOPD-GDD | Minimización de datos |
| Ley 15/2022 | Anonimización de sentencias |

---

## Integración

```python
from pii_sanitizer import sanitize_document

result = sanitize_document(
    file_path="sentencia.pdf",
    preserve_public_figures=True,
    generate_reversible_tokens=True,
    output_format="PDF"
)
```
