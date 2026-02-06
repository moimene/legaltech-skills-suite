# 🏛️ LegalTech Skills Suite

[![TEE Secure](https://img.shields.io/badge/TEE-Secure%20Enclave-green?style=flat-square&logo=shield)](.)
[![Skills](https://img.shields.io/badge/Skills-27-blue?style=flat-square)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square&logo=python)](.)
[![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)](LICENSE)

> **Suite de 27 skills especializadas para análisis legal en entornos TEE (Trusted Execution Environment)**

Diseñada para firmas legales, departamentos jurídicos y consultoras que requieren análisis confidencial de alta precisión sin exposición de datos sensibles.

---

## 🔐 Arquitectura de Seguridad

Todas las skills ejecutan en **modo TEE aislado** siguiendo el perfil de seguridad estricto:

```yaml
security_profile:
  network_access: DENIED          # Sin acceso a red
  file_system: READ_ONLY_INPUT    # Solo lectura de inputs
  memory_protection: ENCLAVE_ISOLATED
  data_retention: NONE            # Datos en RAM únicamente
  audit_logging: LOCAL_ONLY
```

**Modelos LLM Recomendados (locales):**
- `llama-3-70b-instruct`
- `mixtral-8x22b-instruct`  
- `qwen2-72b-instruct`

---

## 📊 Catálogo de Skills

### ⚖️ Litigios (3 skills)

| Skill | Descripción | Topología |
|-------|-------------|-----------|
| **[judicial-profiler](litigios/judicial-profiler/)** | Predice inclinación del juez mediante NLP Sentiment Analysis sobre sentencias previas | `Sentencias PDF → OCR → NLP → Perfil JSON` |
| **[batna-calculator](litigios/batna-calculator/)** | Calcula BATNA usando Game Theory para optimizar negociación | `Posiciones → Nash Equilibrium → Estrategia` |
| **[discovery-gap-hunter](litigios/discovery-gap-hunter/)** | Detecta documentos faltantes en discovery mediante análisis de referencias | `Corpus → Ref Extraction → Gap Detection` |

---

### 🔬 Forensia Digital (4 skills)

| Skill | Descripción | Topología |
|-------|-------------|-----------|
| **[timeline-reconstruction](forensia/timeline-reconstruction/)** | Cronología unificada desde emails/PDFs con normalización UTC y detección de gaps anómalos | `Docs → Metadata → UTC → Timeline + Anomalías` |
| **[metadata-archaeologist](forensia/metadata-archaeologist/)** | Recupera versiones ocultas y metadatos eliminados | `Archivos → EXIF/OLE → Historial` |
| **[audio-tamper-alert](forensia/audio-tamper-alert/)** | Detecta manipulación en grabaciones mediante análisis espectral | `Audio → Spectral Analysis → Tampering Report` |
| **[pii-contextual-sanitizer](forensia/pii-contextual-sanitizer/)** | Redacción inteligente que preserva contexto legal | `Documento → NER → Redacción Selectiva` |

---

### 🏢 Corporativo / M&A (4 skills)

| Skill | Descripción | Topología |
|-------|-------------|-----------|
| **[clause-dependency-graph](corporativo/clause-dependency-graph/)** | Visualiza impacto de cambios en definiciones usando NetworkX | `Contrato → Grafo → Ciclos/Huérfanos/Impacto` |
| **[cap-table-simulator](corporativo/cap-table-simulator/)** | Simulador de dilución para rondas de financiación | `Cap Table → Escenarios → Dilution Model` |
| **[risk-heatmap-gen](corporativo/risk-heatmap-gen/)** | Genera heatmaps de riesgo para Due Diligence | `DD Findings → Risk Matrix → Heatmap` |
| **[force-majeure-trigger](corporativo/force-majeure-trigger/)** | Análisis de activación de cláusulas de fuerza mayor | `Eventos → Matching → Trigger Assessment` |

---

### 💰 Fiscal (6 skills)

| Skill | Descripción | Topología |
|-------|-------------|-----------|
| **[transfer-pricing-bot](fiscal/transfer-pricing-bot/)** | Análisis de precios de transferencia | `Transacciones → Arm's Length → Informe` |
| **[transfer-pricing-benchmarker](fiscal/transfer-pricing-benchmarker/)** | Benchmark de márgenes contra comparables | `Financials → DB Comparables → Ranking` |
| **[vat-carousel-flag](fiscal/vat-carousel-flag/)** | Detección de fraude IVA carrusel | `Facturas → Pattern Matching → Red Flags` |
| **[financial-stress-test](fiscal/financial-stress-test/)** | Z-Score Altman para predicción de quiebra | `Estados Financieros → Z-Score → Risk Level` |
| **[pe-exposure-scanner](fiscal/pe-exposure-scanner/)** | Escaneo de exposición a Establecimiento Permanente | `Actividades → PE Rules → Exposure Report` |
| **[r+d-claim-extractor](fiscal/r+d-claim-extractor/)** | Extracción de gastos elegibles para I+D | `Contabilidad → Matching → Claim Export` |

---

### 👥 Laboral (6 skills)

| Skill | Descripción | Topología |
|-------|-------------|-----------|
| **[bias-auditor](laboral/bias-auditor/)** | Detección de sesgos en procesos HR | `Datos HR → Statistical Analysis → Bias Report` |
| **[flight-risk-detector](laboral/flight-risk-detector/)** | Predicción de riesgo de fuga de empleados | `Señales → ML Model → Risk Score` |
| **[salary-equity-calc](laboral/salary-equity-calc/)** | Cálculo de brecha salarial por género/categoría | `Nóminas → Regression → Gap Analysis` |
| **[non-compete-validator](laboral/non-compete-validator/)** | Validación de cláusulas de no competencia | `Cláusula → Jurisdicción → Validity Check` |
| **[severance-optimizer](laboral/severance-optimizer/)** | Optimización de indemnizaciones por despido | `Perfil → Cálculo Legal → Escenarios` |
| **[whistleblower-risk-scorer](laboral/whistleblower-risk-scorer/)** | Evaluación de riesgo de denuncias internas | `Denuncias → NLP → Risk Assessment` |

---

### 🛡️ Compliance (4 skills)

| Skill | Descripción | Topología |
|-------|-------------|-----------|
| **[shell-co-detector](compliance/shell-co-detector/)** | Detección de empresas pantalla | `Corporate Data → Heuristics → Shell Score` |
| **[ip-overlap-scanner](compliance/ip-overlap-scanner/)** | Detección de plagio de código/IP | `Codebase → Similarity → Overlap Report` |
| **[gdpr-consent-tracker](compliance/gdpr-consent-tracker/)** | Tracking de consentimientos GDPR | `Consents → Timeline → Compliance Status` |
| **[ai-ethics-auditor](compliance/ai-ethics-auditor/)** | Auditoría ética de sistemas de IA | `AI System → Ethics Checklist → Audit Report` |

---

## 🛠️ Instalación

```bash
# Clonar repositorio
git clone https://github.com/your-org/legaltech-skills-suite.git
cd legaltech-skills-suite

# Instalar dependencias comunes
pip install pymupdf python-docx pandas numpy networkx scipy librosa pyvis matplotlib
```

### Requisitos del Sistema

| Componente | Requisito |
|------------|-----------|
| Python | 3.10+ |
| RAM | 16GB+ (para LLM local) |
| GPU | Recomendado para inferencia rápida |
| TEE | Intel SGX / AMD SEV (opcional pero recomendado) |

---

## 📁 Estructura del Proyecto

```
legaltech-skills-suite/
├── README.md
├── _shared/
│   ├── document_loader.py    # Carga segura de PDF/DOCX
│   ├── llm_wrapper.py        # Wrapper para LLM local
│   └── security_profile.yaml # Perfil TEE común
├── litigios/
│   ├── judicial-profiler/
│   ├── batna-calculator/
│   └── discovery-gap-hunter/
├── forensia/
│   ├── timeline-reconstruction/
│   ├── metadata-archaeologist/
│   ├── audio-tamper-alert/
│   └── pii-contextual-sanitizer/
├── corporativo/
│   ├── clause-dependency-graph/
│   ├── cap-table-simulator/
│   ├── risk-heatmap-gen/
│   └── force-majeure-trigger/
├── fiscal/
│   ├── transfer-pricing-bot/
│   ├── transfer-pricing-benchmarker/
│   ├── vat-carousel-flag/
│   ├── financial-stress-test/
│   ├── pe-exposure-scanner/
│   └── r+d-claim-extractor/
├── laboral/
│   ├── bias-auditor/
│   ├── flight-risk-detector/
│   ├── salary-equity-calc/
│   ├── non-compete-validator/
│   ├── severance-optimizer/
│   └── whistleblower-risk-scorer/
└── compliance/
    ├── shell-co-detector/
    ├── ip-overlap-scanner/
    ├── gdpr-consent-tracker/
    └── ai-ethics-auditor/
```

---

## 🚀 Uso Rápido

Cada skill sigue el patrón estándar:

```python
from legaltech_skills_suite.litigios.judicial_profiler import JudicialProfiler
from _shared.document_loader import SecureDocumentLoader
from _shared.llm_wrapper import LocalLLMWrapper

# Inicializar con modelo local
llm = LocalLLMWrapper(model="llama-3-70b-instruct")
loader = SecureDocumentLoader()

# Ejecutar skill
profiler = JudicialProfiler(llm=llm, loader=loader)
resultado = profiler.analyze(
    juez_id="12345",
    sentencias_dir="./data/sentencias/"
)

print(resultado.perfil)
print(resultado.argumentos_favorables)
```

---

## 🔍 Ejemplo: Judicial Profiler

```
┌─────────────────┐    ┌──────────────┐    ┌───────────────────┐
│ Sentencias PDF  │───▶│ OCR/Parser   │───▶│ Extractor de      │
│ (Histórico)     │    │              │    │ Fallo + Argumentos│
└─────────────────┘    └──────────────┘    └─────────┬─────────┘
                                                     │
                                                     ▼
┌─────────────────┐    ┌──────────────┐    ┌───────────────────┐
│ Perfil JSON     │◀───│ Correlación  │◀───│ NLP Sentiment     │
│ del Juez        │    │ Estadística  │    │ Analysis          │
└─────────────────┘    └──────────────┘    └───────────────────┘
```

**Output:**
```json
{
  "juez": {
    "nombre": "D. Juan García López",
    "juzgado": "Juzgado Mercantil 3 de Madrid"
  },
  "perfil": {
    "tasa_estimacion_global": 0.62,
    "tiempo_medio_dias": 145,
    "tendencia_sentiment": "NEUTRAL_SEVERO"
  },
  "argumentos_favorables": [
    {"tipo": "Enriquecimiento Injusto", "ratio": 0.80}
  ],
  "recomendaciones": [
    "Enfatizar carácter objetivo del incumplimiento",
    "Aportar abundante prueba documental"
  ]
}
```

---

## 📜 Consideraciones Éticas

> ⚠️ **Uso Responsable**

- Las skills proporcionan análisis estadístico basado en datos públicos
- No predicen decisiones individuales, sino tendencias históricas
- El secreto de deliberaciones judiciales permanece intacto
- Cumplimiento estricto con GDPR y normativa de protección de datos
- Auditoría local únicamente, sin envío de datos a terceros

---

## 🤝 Contribuir

1. Fork del proyecto
2. Crear branch (`git checkout -b feature/nueva-skill`)
3. Commit cambios (`git commit -m 'Add: nueva-skill'`)
4. Push al branch (`git push origin feature/nueva-skill`)
5. Abrir Pull Request

---

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles.

---

## 🏢 Créditos

Desarrollado para entornos LegalTech de alta seguridad.

**Contacto:** [tu-email@ejemplo.com](mailto:tu-email@ejemplo.com)
