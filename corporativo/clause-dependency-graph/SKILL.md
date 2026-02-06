---
name: clause-dependency-graph
description: Mapea interdependencias entre cláusulas en contratos complejos (SPA, SHA, TSA, escrow agreements) mediante grafo dirigido con análisis de centralidad (PageRank, betweenness), detección de ciclos y propagación de cambios. Validar contra LSC (RDL 1/2010) y marcos ABA/IBA para M&A. Incluye verificador de colisiones entre cláusulas y compatibilidad con disposiciones imperativas LSC (Art. 23, 29, 97-98, 160, 173, 236-237, 348bis). Contextos: análisis de definiciones en SPAs, impacto de cambios en TAC, auditoría de garantías post-signing, validación cruzada de anexos, compliance con autonomía de la voluntad (CC 1255–1258).
---

# Clause Dependency Graph

## Mapeo de Interdependencias Clausulares

Analizar cambios contractuales en operaciones M&A requiere trazar cómo una modificación en una definición (ej: "Conocimiento", "Material Adverse Change") propaga a través de garantías, representaciones y obligaciones en el acuerdo principal y documentos ancilares (SHA, TSA, escrow).

---

## Topología de Procesamiento

```
┌──────────────┐ ┌──────────┐ ┌──────────┐
│ SPA + SHA +  │→│ Extraer  │→│ Grafo    │
│ TSA + Escrow │ │ términos │ │ dirigido │
└──────────────┘ └──────────┘ └────┬─────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
   PageRank          Betweenness Centrality      Detección de ciclos
   (importancia)     (puentes críticos)         (dependencias circulares)
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   ▼
                    Análisis de propagación de cambios
                    (si TAC → ¿qué garantías afectar?)
                                   │
                                   ▼
                        Visualización PyVis (HTML)
                        Métricas JSON
```

---

## Aplicar cuando

- **Diligencia en SPA post-signing**: mapear si modificación en "Material Adverse Change" afecta a condiciones, garantías y anexos de escrow
- **Auditoría de coherencia**: validar que definiciones de LSC art. 4.2 (Sociedades de Capital) se apliquen consistentemente
- **Análisis de riesgo de cambio**: Si cliente negocia "Conocimiento" más restrictivo, ¿cuántas garantías cambian probabilidad de incumplimiento?
- **Documentación de M&A**: identificar nodos críticos para term sheet negociación (ej: MAC aparece en 47 cláusulas → priorizar definición)
- **Validación cruzada SHA/SPA**: asegurar que excepciones en SHA (Shareholders Agreement) se reflejan correctamente en SPA

---

## Estructura del Grafo

### Tipos de Nodos

- **DEFINICION**: Términos definidos ("Material Adverse Change", "Periodo Garantía")
- **CLAUSULA**: Secciones del acuerdo principal y documentos ancilares (3.2.1 SPA, 2.4 SHA, 5.1 TSA)
- **ANEXO**: Referencias a anexos legales (Anexo A - Definiciones, Anexo B - Escrow Agreement)
- **GARANTIA**: Representaciones y garantías (8.1, 8.15 en SPA)
- **CONDICION**: Condiciones precedentes (art. 1257 CC - condiciones suspensivas; LSC 53 para modificación estatutaria)
- **DOCUMENTO**: Acuerdos conectados (SPA, SHA, TSA, Escrow)

### Tipos de Aristas y Métricas

| Arista | Significado | Peso |
|--------|------------|------|
| USA | Cláusula → Definición | Alta |
| REFERENCIA | Cláusula → Cláusula | Media |
| MODIFICA | Anexo → Cláusula principal | Alta |
| CONDICIONA | Condición → Obligación | Alta |
| INTERCONECTA | SPA → SHA (misma definición) | Crítica |

### Métricas de Importancia

- **PageRank**: Nodos más influyentes (ej: MAC score alto)
- **Betweenness Centrality**: Nodos puente entre subsecciones (ej: "Conocimiento" conecta garantías con condiciones)
- **In-Degree/Out-Degree**: Dependencias de entrada/salida (ej: "Precio" tiene alto out-degree → muchas cláusulas dependen)

---

## Ejemplo Concreto: M&A SPA (TechCorp Acquisition)

**Documentos**: SPA 45 págs + Definitions Annex + SHA + TSA 30 ptes + Escrow Agreement
**Métricas iniciales**: 15 definiciones, 30 cláusulas, 8 anexos, 234 aristas

**Nodo crítico identificado: "Material Adverse Change" (MAC)**
- PageRank: 8.7/10 (más importante que "Precio")
- Betweenness Centrality: 0.34 (puente entre condiciones precedentes, garantías y TSA termination)
- Apariciones: 47 referencias (vs. 12 para "Precio")
- Usuarios:
  - Cond. Precedente (3.1.2 SPA)
  - Garantía relativa a tax (8.15 SPA)
  - Excepciones de garantía (Anexo A)
  - Trigger resolución (5.2 TSA)

**Análisis de propagación** (si cliente negocia MAC más restrictivo):
```
MAC (def) → Cond.Precedente.MAC → Fee reduction (art. 9.1) → Escrow release timing
         → Garantía.Tax → Indemnification cap (10.3)
         → TSA.Terminate → Earn-out reduction
```

**Ciclo potencial detectado** (riesgo):
```
Def.MAC → Cond.MAC (3.1.2) → Escrow (Anexo E)
Anexo E (escrow terms) → Cond.MAC (modifica requisito para release)
→ CICLO: cambio en MAC afecta escrow, que vuelve a afectar MAC
```

### Análisis de Impacto: Cambio Management

Metodología para estimar "blast radius" de cambios:

**Scenario: Expandir "Material Adverse Change" para excluir "Regulatory changes"**
1. Nodo impactado: MAC
2. Descendientes (forward impact): Cond.Precedente, Tax Warranty, TSA Termination
3. Ascendientes (backward impact): Definiciones padre, contexto legal (LSC 1258 CC)
4. Métricas:
   - Cláusulas directamente afectadas: 12
   - Indirectas (2 grados): 28
   - Documentos: 4/5 (falta TSA)
   - Riesgo: MEDIO (no afecta obligaciones núcleo, solo condiciones)

---

## Output: Reporte de Análisis

```json
{
  "operacion": "TechCorp_SPA_2024",
  "documentos": ["SPA.docx", "Definitions_Annex.xlsx", "SHA.docx", "TSA.docx", "Escrow.docx"],
  "metricas_globales": {
    "definiciones": 15,
    "clausulas": 30,
    "anexos": 8,
    "aristas_totales": 234,
    "densidad_grafo": 0.24,
    "numero_componentes": 1
  },
  "nodos_criticos_ranking": [
    {
      "rango": 1,
      "nodo": "DEF_MAC",
      "pagerank": 8.7,
      "betweenness": 0.34,
      "in_degree": 47,
      "out_degree": 5,
      "apariciones": ["CL_3.1.2", "CL_8.15", "ANEXO_A", "TSA_5.2"],
      "riesgo": "CRITICA - cualquier cambio de definición requiere auditoría cruzada"
    },
    {
      "rango": 2,
      "nodo": "DEF_Precio_Compra",
      "pagerank": 7.2,
      "betweenness": 0.18,
      "in_degree": 28,
      "out_degree": 12
    }
  ],
  "ciclos_detectados": [
    {
      "ciclo_id": "C-001",
      "nodos": ["DEF_MAC", "CL_3.1.2_Condicion", "ANEXO_E_Escrow", "CL_3.1.2_Condicion"],
      "largo": 3,
      "riesgo": "MEDIO - escrow termination términos refieren a MAC definition",
      "recomendacion": "Segregar definición escrow de MAC principal"
    }
  ],
  "nodos_huerfanos": [
    {
      "id": "DEF_Precio_Ajustado",
      "tipo": "DEFINICION",
      "estado": "Dead code",
      "accion": "Eliminar o conectar"
    }
  ],
  "impacto_cambios": {
    "escenario": "MAC - ampliación para excluir cambios regulatorios",
    "nodos_afectados_directos": 12,
    "nodos_afectados_indirectos": 28,
    "documentos_impactados": 4,
    "probabilidad_inconsistencia": 0.62,
    "acciones": [
      "Revisar Cond.Precedente (3.1.2)",
      "Auditar TSA termination triggers",
      "Validar escrow release terms vs nueva MAC def"
    ]
  }
}
```

---

## Visualización Interactiva (PyVis)

Exportar grafo como HTML interactivo con:
- Nodos redimensionados por PageRank (tamaño = importancia)
- Colores por tipo (DEF=azul, CLAUSULA=gris, ANEXO=naranja)
- Aristas ponderadas por betweenness
- Hover → información completa
- Click → navegar a definición/cláusula en documento

**Archivo output**: `graph_SPA_2024.html` (abrir en navegador)

---

## Marcos de Referencia Legal

- **España - LSC (RDL 1/2010, de 2 de julio)**: Art. 4.2 (definiciones en acuerdos), Art. 53 (modificación estatutaria requiere definiciones claras)
- **ABA Model SPA**: Estructura estándar de definiciones y cross-references
- **IBA Guidelines (2020)**: Mejores prácticas para operaciones M&A transfronterizas
- **Spanish CC (Código Civil)**: Art. 1255 (autonomía de la voluntad), Art. 1256 (interpretación de contratos), Art. 1257 (condiciones suspensivas), Art. 1258 (rebus sic stantibus)

---

## Verificador de Colisiones con Disposiciones Imperativas LSC

### Disposiciones Imperativas LSC con Impacto Contractual

Ciertas normas de la LSC son de aplicación obligatoria y no pueden ser derogadas por acuerdos entre socios. El verificador de colisiones detecta intentos de vulnerar estas disposiciones:

| Artículo LSC | Norma Imperativa | Conflicto Típico | Severidad |
|--------------|------------------|------------------|-----------|
| Art. 23 | Prohibición de pactos leoninos | Asignación desigual de dividendos sin contrapartida | NULA |
| Art. 29 | Derechos mínimos de minoría (impugnación, información, voto) | Cláusulas que anulen derecho a voto de minoría | NULA |
| Art. 97-98 | Derechos de tanteo y retracto | Restricción contractual que impida ejercer tanteo/retracto | NULA |
| Art. 160 | Competencias exclusivas JGA | Delegar a administradores acuerdos de JGA | ANULABLE |
| Art. 173 | Impugnación de acuerdos | Cláusula que impida acciones de impugnación | NULA |
| Art. 236-237 | Responsabilidad de administradores | Exención total de responsabilidad de órganos de administración | NULA |
| Art. 348bis | Derecho de separación | Limitación de derecho a separarse por falta de dividendos | ANULABLE |

### Algoritmo de Detección de Colisiones

```
ENTRADA: Cláusula contractual extraída del grafo
PROCESO:
  1. EXTRAER_OBLIGACIÓN(cláusula)
     └─ Identificar sujeto, acción, objeto (ej: "Socios no pueden ejercer voto")

  2. NORMALIZAR_OBLIGACIÓN(obligación)
     └─ Mapear a categoría legal (derechos, obligaciones, restricciones)

  3. REGISTRAR_LSC = obtener_disposiciones_imperativas_LSC()
     └─ Tablas hash: Art.23→prohibición_leonino, Art.29→derechos_minoría, etc.

  4. MATCH_CONTRA_REGISTRO(obligación, REGISTRAR_LSC)
     ├─ SI match = "prohibición de X" Y cláusula = "X no permitido"
     │  └─ FLAG: INTENTO_VULNERACIÓN
     ├─ SI match = "derecho Y" Y cláusula = "Y revocable/limitado"
     │  └─ FLAG: RESTRICCIÓN_DERECHO_IMPERATIVO
     └─ SINO → permitido por autonomía de la voluntad (CC 1255)

  5. ASIGNAR_SEVERIDAD(flag)
     ├─ NULA: Vulneración de prohibición absoluta (Art. 23, 29, 173, 236-237)
     ├─ ANULABLE: Vicio susceptible de confirmación (Art. 160, 348bis)
     └─ VÁLIDA_CON_LÍMITES: Compatible con CC 1255 sujeta a interpretación

SALIDA: {
  colisión_detectada: BOOL,
  artículos_implicados: [lista],
  descripción_conflicto: STRING,
  severidad: ENUM(NULA, ANULABLE, VÁLIDA_CON_LÍMITES),
  recomendación: STRING
}
```

### Ejemplo de Detección: Cláusula de Drag-Along vs Art. 29 LSC

**Cláusula contractual analizada:**
```
"En caso de oferta de adquisición de la empresa por tercero, los socios mayoritarios
podrán obligar a los minoritarios a vender sus participaciones en las mismas condiciones
(drag-along), sin posibilidad de ejercer derecho a tanteo previo."
```

**Análisis de colisión:**
```
1. OBLIGACIÓN EXTRAÍDA: "Minoría obligada a vender sin derecho tanteo"
2. MATCH CONTRA LSC:
   ✗ Art. 97-98 LSC: "Socios tienen derecho de tanteo y retracto"
   ✗ Art. 29 LSC: "Derechos mínimos de minoría no pueden ser limitados"
3. FLAG: RESTRICCIÓN_DERECHO_IMPERATIVO
4. SEVERIDAD: NULA (intento de anular derechos imperativos)
5. RECOMENDACIÓN: "Redactar drag-along respetando Art. 97-98:
   ofrecer tanteo a minoritarios antes de forzar venta a terceros"
```

**Salida JSON del verificador:**
```json
{
  "cláusula": "Drag-along sin tanteo",
  "colisión_detectada": true,
  "artículos_implicados": ["Art. 97-98 LSC", "Art. 29 LSC"],
  "descripción_conflicto": "Cláusula intenta anular derecho de tanteo
                           (Art. 97-98) y vulnera derechos mínimos de minoría (Art. 29)",
  "severidad": "NULA",
  "sustento_legal": "CC 1255 autonomía de la voluntad está limitada por
                    disposiciones imperativas LSC (STS 1047/2015)",
  "recomendación": "Reformular para permitir ejercicio de tanteo:
                   'Antes de vender a tercero, socios mayoritarios ofrecerán
                   participaciones a minoritarios en iguales condiciones (Art. 97-98)'"
}
```

---

## Control de Calidad Semántica

### Umbrales de Confianza en Extracción de Grafos

El análisis de dependencias clausulares depende de extracción automática de términos y relaciones. Se aplican umbrales de confianza para garantizar calidad:

| Confianza | Rango | Acción | Ejemplo |
|-----------|-------|--------|---------|
| CONFIRMADO | > 0.90 | Incluir en grafo producción | "Material Adverse Change" refiere 47 veces con contexto idéntico |
| REVISAR | 0.70–0.90 | Marcar para auditoría manual | Referencia ambigua: "como se define en el presente acuerdo" |
| BANDERA | < 0.70 | Excluir / Solicitar clarificación | Pronombre sin antecedente claro: "ello se aplicará..." |

### Limitaciones Semánticas Conocidas

El verificador y el grafo de dependencias presentan estas limitaciones inherentes:

1. **Referencias Ambiguas**
   - Frases como "as defined herein" sin antecedente explícito
   - Pronouns ("esto", "ello") sin contexto suficiente
   - Definiciones implícitas (términos asumidos en prácticas de mercado)
   - Mitigación: Pre-procesar con anotaciones manuales para términos críticos

2. **Dependencias Implícitas**
   - Cláusulas que refieren a "regímenes de derecho aplicable" sin citarlas explícitamente
   - Incorporaciones por referencia ("incluidos todos los anexos aquí mencionados")
   - Efectos colaterales no escritos (ej: cambio en MAC afecta timing de earn-out implícitamente)
   - Mitigación: Ejecutar análisis de propagación en múltiples pasadas para detectar aristas ocultas

3. **Asuntos Transfronterizos**
   - Contratos que mezclan definiciones españolas (LSC) con marcos anglosajones (ABA, IBA)
   - Términos que tienen significado distinto en diferentes jurisdicciones ("Conocimiento" más amplio en common law)
   - Conflictos entre disposiciones imperativas españolas e ley aplicable extranjera
   - Mitigación: Incluir matriz de equivalencias cross-jurisdiccional; flagear ambigüedades

4. **Semántica Temporal**
   - Condiciones suspensivas cuyo cumplimiento es incierto (MAC puede ocurrir o no)
   - Earn-outs y obligaciones contingentes con probabilidad difícil de modelar
   - Mitigation: Incluir análisis de probabilidad Bayesiana para escenarios inciertos

### Validación de Análisis Antes de Entrega

Checklist de validación semántica antes de reportar resultados:

- [ ] **Completitud**: ¿Se extrajeron todas las definiciones explícitas del acuerdo? (verificar vs. Índice del contrato)
- [ ] **No duplicación**: ¿Hay nodos con mismo significado pero denominaciones distintas? (ej: "MAC" vs. "Material Adverse Change" vs. "MAE")
- [ ] **Ciclos validados**: Para cada ciclo detectado, ¿se verificó que realmente existe lógicamente? (no es solo artefacto de NLP)
- [ ] **Severidad calibrada**: ¿Se revisó la clasificación (NULA/ANULABLE/VÁLIDA) contra jurisprudencia reciente?
- [ ] **Documentación cruzada**: ¿Las referencias inter-documentos (SPA-SHA-TSA) se validaron en documentos originales?
- [ ] **Limitaciones documentadas**: ¿Se indicó dónde confidence < 0.90 para que usuario sea consciente de incertidumbre?
- [ ] **Recomendaciones accionables**: ¿Cada finding incluye pasos concretos para resolverlo o confirmarlo manualmente?

---

## Dependencias & Instalación

```python
networkx>=2.8       # Grafo dirigido, ciclos, centralidad
pandas>=1.5         # Manejo de tablas
spacy>=3.5          # NLP para extracción de definiciones
pyvis>=0.3          # Visualización HTML interactiva
```
