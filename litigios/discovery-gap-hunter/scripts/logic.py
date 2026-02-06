"""
Discovery Gap Hunter - Detección de documentos faltantes en discovery

Topología: Docs → Extracción Referencias → Cotejo Inventario → Gaps
"""

import json
import re
import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
import sys
sys.path.append(str(Path(__file__).parent.parent.parent / "_shared"))

from document_loader import DocumentLoader


@dataclass
class Referencia:
    """Referencia a documento encontrada."""
    texto: str
    ubicacion: str  # "Hecho 3, línea 45"
    tipo: str  # ANEXO, EMAIL, CONTRATO, etc.
    fecha: str = None


@dataclass
class DocumentoEntregado:
    """Documento en el inventario."""
    nombre: str
    path: str
    hash_md5: str
    tipo_inferido: str
    fecha_inferida: str = None


@dataclass
class Gap:
    """Gap documental detectado."""
    referencia: str
    ubicacion: str
    criticidad: str  # ALTA, MEDIA, BAJA
    razon: str
    posibles_matches: list = field(default_factory=list)
    accion: str = ""


# Patrones de referencias documentales
PATRONES_REFERENCIA = [
    (r"(?:ver|véase|cfr\.?|vid\.?)\s+(?:anexo|documento|doc\.?)\s+(\w+)", "ANEXO"),
    (r"(?:según|conforme)\s+(?:el|la)\s+(\w+)\s+(?:de\s+)?fecha\s+(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", "DOCUMENTO_FECHA"),
    (r"(?:adjunto|acompaño)\s+(?:copia|original)\s+de\s+(.+?)(?:\.|,)", "ADJUNTO"),
    (r"(?:exhibit|anexo)\s+([A-Z]|\d+)", "EXHIBIT"),
    (r"doc(?:umento)?\.?\s*(?:nº|núm\.?|n°|#)?\s*(\d+)", "DOC_NUM"),
    (r"email\s+(?:de|del|de\s+fecha)\s+(.+?)(?:\.|,|$)", "EMAIL"),
    (r"contrato\s+(?:de|del|de\s+fecha)\s+(.+?)(?:\.|,|$)", "CONTRATO"),
    (r"acta\s+(?:de|del|de\s+fecha)\s+(.+?)(?:\.|,|$)", "ACTA"),
    (r"factura\s+(?:nº|núm\.?|n°|#)?\s*(\w+)", "FACTURA"),
]


def calcular_hash(file_path: str) -> str:
    """Calcula hash MD5 del archivo."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()[:12]


def inferir_tipo_documento(nombre: str) -> str:
    """Infiere el tipo de documento por el nombre."""
    nombre_lower = nombre.lower()
    
    if any(x in nombre_lower for x in ["email", "correo", "mail"]):
        return "EMAIL"
    elif any(x in nombre_lower for x in ["contrato", "contract"]):
        return "CONTRATO"
    elif any(x in nombre_lower for x in ["factura", "invoice"]):
        return "FACTURA"
    elif any(x in nombre_lower for x in ["acta", "minutes"]):
        return "ACTA"
    elif any(x in nombre_lower for x in ["anexo", "exhibit", "annex"]):
        return "ANEXO"
    else:
        return "DOCUMENTO"


def extraer_referencias(texto: str) -> list[Referencia]:
    """Extrae todas las referencias documentales del texto."""
    referencias = []
    lineas = texto.split('\n')
    
    for num_linea, linea in enumerate(lineas, 1):
        for patron, tipo in PATRONES_REFERENCIA:
            matches = re.finditer(patron, linea, re.IGNORECASE)
            for match in matches:
                ref = Referencia(
                    texto=match.group(0).strip(),
                    ubicacion=f"Línea {num_linea}",
                    tipo=tipo,
                    fecha=match.group(2) if match.lastindex and match.lastindex >= 2 else None
                )
                referencias.append(ref)
    
    return referencias


def construir_inventario(directorio: str) -> list[DocumentoEntregado]:
    """Construye inventario de documentos entregados."""
    inventario = []
    path = Path(directorio)
    
    extensiones = {'.pdf', '.docx', '.doc', '.eml', '.msg', '.xlsx', '.xls', '.txt'}
    
    for archivo in path.rglob('*'):
        if archivo.is_file() and archivo.suffix.lower() in extensiones:
            doc = DocumentoEntregado(
                nombre=archivo.name,
                path=str(archivo),
                hash_md5=calcular_hash(str(archivo)),
                tipo_inferido=inferir_tipo_documento(archivo.name)
            )
            inventario.append(doc)
    
    return inventario


def matching_score(referencia: str, documento: str) -> float:
    """Calcula score de similitud entre referencia y documento."""
    ref_clean = re.sub(r'[^\w\s]', '', referencia.lower())
    doc_clean = re.sub(r'[^\w\s]', '', documento.lower())
    
    return SequenceMatcher(None, ref_clean, doc_clean).ratio()


def buscar_matches(referencia: Referencia, inventario: list[DocumentoEntregado]) -> list[str]:
    """Busca posibles matches para una referencia."""
    matches = []
    
    for doc in inventario:
        score = matching_score(referencia.texto, doc.nombre)
        if score > 0.4:
            matches.append((doc.nombre, score))
    
    # Ordenar por score descendente
    matches.sort(key=lambda x: x[1], reverse=True)
    return [m[0] for m in matches[:3]]


def clasificar_criticidad(referencia: Referencia) -> str:
    """Clasifica la criticidad del gap."""
    texto_lower = referencia.texto.lower()
    
    # Crítico: contratos, actas notariales, documentos centrales
    if any(x in texto_lower for x in ["contrato", "acta notarial", "escritura", "principal"]):
        return "ALTA"
    
    # Medio: emails, facturas, documentos secundarios
    if any(x in texto_lower for x in ["email", "factura", "anexo"]):
        return "MEDIA"
    
    return "BAJA"


def generar_accion(criticidad: str) -> str:
    """Genera acción recomendada según criticidad."""
    acciones = {
        "ALTA": "Requerir expresamente bajo apercibimiento art. 329 LEC",
        "MEDIA": "Solicitar aclaración en audiencia previa",
        "BAJA": "Documentar para alegaciones finales"
    }
    return acciones.get(criticidad, "Revisar manualmente")


def execute_skill(documentos_dir: str, texto_principal: str = None, texto_principal_file: str = None) -> dict:
    """
    Ejecuta el análisis de gaps documentales.
    
    Args:
        documentos_dir: Directorio con documentos entregados
        texto_principal: Texto del documento principal (demanda, etc.)
        texto_principal_file: Ruta al archivo del documento principal
    """
    # Cargar texto principal
    if texto_principal_file:
        doc = DocumentLoader.load(texto_principal_file)
        texto_principal = doc.text
    
    if not texto_principal:
        return {"error": "Se requiere texto_principal o texto_principal_file"}
    
    # Construir inventario
    inventario = construir_inventario(documentos_dir)
    
    # Extraer referencias
    referencias = extraer_referencias(texto_principal)
    
    # Buscar gaps
    gaps = []
    matches_confirmados = 0
    
    for ref in referencias:
        posibles = buscar_matches(ref, inventario)
        
        if posibles and matching_score(ref.texto, posibles[0]) > 0.6:
            # Match confirmado
            matches_confirmados += 1
        else:
            # Gap detectado
            criticidad = clasificar_criticidad(ref)
            gap = Gap(
                referencia=ref.texto,
                ubicacion=ref.ubicacion,
                criticidad=criticidad,
                razon="Documento referenciado no encontrado en inventario",
                posibles_matches=posibles,
                accion=generar_accion(criticidad)
            )
            gaps.append(gap)
    
    # Estadísticas
    tasa_completitud = matches_confirmados / len(referencias) if referencias else 1.0
    
    return {
        "analisis": {
            "documentos_entregados": len(inventario),
            "referencias_detectadas": len(referencias),
            "matches_confirmados": matches_confirmados,
            "gaps_detectados": len(gaps),
            "posibles_matches_parciales": sum(1 for g in gaps if g.posibles_matches)
        },
        "gaps": [
            {
                "referencia": g.referencia,
                "ubicacion": g.ubicacion,
                "criticidad": g.criticidad,
                "razon": g.razon,
                "posibles_matches": g.posibles_matches,
                "accion": g.accion
            }
            for g in sorted(gaps, key=lambda x: {"ALTA": 0, "MEDIA": 1, "BAJA": 2}[x.criticidad])
        ],
        "estadisticas": {
            "tasa_completitud": round(tasa_completitud, 2),
            "gaps_criticos": sum(1 for g in gaps if g.criticidad == "ALTA"),
            "gaps_medios": sum(1 for g in gaps if g.criticidad == "MEDIA"),
            "gaps_menores": sum(1 for g in gaps if g.criticidad == "BAJA")
        },
        "inventario_resumen": [
            {"nombre": d.nombre, "tipo": d.tipo_inferido, "hash": d.hash_md5}
            for d in inventario[:20]  # Limitar output
        ]
    }


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Uso: python logic.py <directorio_docs> <archivo_principal>")
        sys.exit(1)
    
    result = execute_skill(sys.argv[1], texto_principal_file=sys.argv[2])
    print(json.dumps(result, indent=2, ensure_ascii=False))
