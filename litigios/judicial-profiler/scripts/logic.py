"""
Judicial Profiler - Análisis predictivo de jueces

Topología: Sentencias PDF → OCR → NLP Sentiment → Correlación → Perfil
"""

import json
from dataclasses import dataclass, field
from collections import defaultdict
from pathlib import Path
from typing import Optional
import sys
sys.path.append(str(Path(__file__).parent.parent.parent / "_shared"))

from document_loader import DocumentLoader


@dataclass
class Sentencia:
    """Sentencia analizada."""
    id: str
    fecha: str
    materia: str
    fallo: str  # ESTIMATORIA, DESESTIMATORIA, PARCIAL
    argumentos: list[str]
    sentiment_demandante: float  # -1 a 1
    sentiment_demandado: float
    dias_resolucion: int


@dataclass
class PerfilJuez:
    """Perfil predictivo del juez."""
    nombre: str
    juzgado: str
    sentencias_analizadas: int
    tasa_estimacion: float
    tiempo_medio_dias: float
    tendencia_sentiment: str
    argumentos_favorables: list[dict]
    argumentos_desfavorables: list[dict]
    recomendaciones: list[str]


def extraer_fallo(texto: str) -> str:
    """Extrae el sentido del fallo."""
    texto_lower = texto.lower()
    
    if "estimo íntegramente" in texto_lower or "con lugar" in texto_lower:
        return "ESTIMATORIA"
    elif "desestimo" in texto_lower or "sin lugar" in texto_lower:
        return "DESESTIMATORIA"
    elif "estimo parcialmente" in texto_lower:
        return "PARCIAL"
    
    return "INDETERMINADO"


def extraer_argumentos(texto: str) -> list[str]:
    """Extrae tipos de argumentos usados."""
    argumentos = []
    
    patrones = {
        "Enriquecimiento Injusto": ["enriquecimiento injusto", "enriquecimiento sin causa"],
        "Incumplimiento Contractual": ["incumplimiento", "resolución contractual"],
        "Daño Moral": ["daño moral", "daños morales", "pretium doloris"],
        "Lucro Cesante": ["lucro cesante", "ganancias dejadas"],
        "Responsabilidad Extracontractual": ["1902", "culpa extracontractual"],
        "Vicios Ocultos": ["vicios ocultos", "saneamiento"],
    }
    
    texto_lower = texto.lower()
    for arg_tipo, keywords in patrones.items():
        if any(kw in texto_lower for kw in keywords):
            argumentos.append(arg_tipo)
    
    return argumentos


def analizar_sentiment(texto: str, objetivo: str) -> float:
    """
    Analiza sentiment hacia demandante/demandado.
    En producción usar modelo NLP real.
    
    Returns: -1 (negativo) a 1 (positivo)
    """
    # Stub - en producción usar transformers/spacy
    palabras_positivas = ["acredita", "prueba suficiente", "correctamente"]
    palabras_negativas = ["no acredita", "carece", "insuficiente", "mala fe"]
    
    texto_lower = texto.lower()
    
    score = 0
    for word in palabras_positivas:
        if word in texto_lower:
            score += 0.1
    for word in palabras_negativas:
        if word in texto_lower:
            score -= 0.1
    
    return max(-1, min(1, score))


def calcular_correlacion(sentencias: list[Sentencia]) -> dict:
    """Calcula correlación argumento → éxito."""
    stats = defaultdict(lambda: {"total": 0, "exito": 0})
    
    for s in sentencias:
        exito = s.fallo in ["ESTIMATORIA", "PARCIAL"]
        for arg in s.argumentos:
            stats[arg]["total"] += 1
            if exito:
                stats[arg]["exito"] += 1
    
    return {
        arg: {"total": v["total"], "ratio": v["exito"] / v["total"] if v["total"] > 0 else 0}
        for arg, v in stats.items()
    }


def generar_recomendaciones(perfil: PerfilJuez, correlacion: dict) -> list[str]:
    """Genera recomendaciones estratégicas."""
    recs = []
    
    if perfil.tasa_estimacion < 0.4:
        recs.append("Juez conservador: priorizar acuerdos extrajudiciales")
    elif perfil.tasa_estimacion > 0.7:
        recs.append("Juez proactivo: proceder con confianza si los hechos son sólidos")
    
    for arg in perfil.argumentos_desfavorables[:2]:
        if arg["ratio"] < 0.3:
            recs.append(f"Evitar argumentos de {arg['tipo']} (ratio bajo: {arg['ratio']:.0%})")
    
    for arg in perfil.argumentos_favorables[:2]:
        if arg["ratio"] > 0.7:
            recs.append(f"Enfatizar {arg['tipo']} (ratio alto: {arg['ratio']:.0%})")
    
    return recs


def execute_skill(sentencias_dir: str, juez_nombre: str = "Juez Anónimo", juzgado: str = "N/A") -> dict:
    """
    Ejecuta el análisis del perfil judicial.
    
    Args:
        sentencias_dir: Directorio con PDFs de sentencias
        juez_nombre: Nombre del juez
        juzgado: Juzgado asignado
    """
    sentencias_path = Path(sentencias_dir)
    pdfs = list(sentencias_path.glob("*.pdf"))
    
    if not pdfs:
        return {"error": "No se encontraron sentencias PDF"}
    
    sentencias = []
    
    for i, pdf in enumerate(pdfs):
        try:
            doc = DocumentLoader.load(str(pdf))
            texto = doc.text
            
            sentencia = Sentencia(
                id=pdf.stem,
                fecha=str(doc.metadata.modified or "N/A"),
                materia="CIVIL",  # En producción, detectar automáticamente
                fallo=extraer_fallo(texto),
                argumentos=extraer_argumentos(texto),
                sentiment_demandante=analizar_sentiment(texto, "demandante"),
                sentiment_demandado=analizar_sentiment(texto, "demandado"),
                dias_resolucion=0  # En producción, calcular desde fechas
            )
            sentencias.append(sentencia)
        except Exception as e:
            print(f"Error procesando {pdf}: {e}")
    
    if not sentencias:
        return {"error": "No se pudieron procesar las sentencias"}
    
    # Calcular estadísticas
    total = len(sentencias)
    estimatorias = sum(1 for s in sentencias if s.fallo == "ESTIMATORIA")
    parciales = sum(1 for s in sentencias if s.fallo == "PARCIAL")
    
    correlacion = calcular_correlacion(sentencias)
    
    # Ordenar argumentos por ratio
    args_sorted = sorted(correlacion.items(), key=lambda x: x[1]["ratio"], reverse=True)
    
    perfil = PerfilJuez(
        nombre=juez_nombre,
        juzgado=juzgado,
        sentencias_analizadas=total,
        tasa_estimacion=(estimatorias + parciales * 0.5) / total,
        tiempo_medio_dias=sum(s.dias_resolucion for s in sentencias) / total,
        tendencia_sentiment="NEUTRAL",
        argumentos_favorables=[
            {"tipo": arg, "ratio": round(data["ratio"], 2), "casos": data["total"]}
            for arg, data in args_sorted[:5] if data["ratio"] > 0.5
        ],
        argumentos_desfavorables=[
            {"tipo": arg, "ratio": round(data["ratio"], 2), "casos": data["total"]}
            for arg, data in args_sorted[-5:] if data["ratio"] < 0.5
        ],
        recomendaciones=[]
    )
    
    perfil.recomendaciones = generar_recomendaciones(perfil, correlacion)
    
    return {
        "juez": {
            "nombre": perfil.nombre,
            "juzgado": perfil.juzgado,
            "sentencias_analizadas": perfil.sentencias_analizadas
        },
        "perfil": {
            "tasa_estimacion_global": round(perfil.tasa_estimacion, 2),
            "tiempo_medio_dias": round(perfil.tiempo_medio_dias, 0),
            "tendencia_sentiment": perfil.tendencia_sentiment
        },
        "argumentos_favorables": perfil.argumentos_favorables,
        "argumentos_desfavorables": perfil.argumentos_desfavorables,
        "recomendaciones": perfil.recomendaciones
    }


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python logic.py <directorio_sentencias>")
        sys.exit(1)
    
    result = execute_skill(sys.argv[1])
    print(json.dumps(result, indent=2, ensure_ascii=False))
