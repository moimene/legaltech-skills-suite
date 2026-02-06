"""
BATNA Calculator - Game Theory para decisiones de litigación

Topología: Inputs → Árbol Decisión → EV → Comparación → Recomendación
"""

import json
from dataclasses import dataclass
from typing import Optional


@dataclass
class LitigationParams:
    """Parámetros del caso."""
    cantidad_reclamada: float
    prob_victoria_total: float
    prob_victoria_parcial: float
    cantidad_parcial: float
    costes_juicio: float
    costes_contraparte: float
    duracion_años: float
    tasa_descuento: float
    oferta_acuerdo: Optional[float] = None


@dataclass
class AnalisisResult:
    """Resultado del análisis."""
    ev_litigio_bruto: float
    ev_litigio_neto: float
    ev_litigio_vpn: float
    batna: float
    oferta: Optional[float]
    diferencia: Optional[float]
    recomendacion: str
    razon: str
    confianza: float


def calcular_ev_litigio(params: LitigationParams) -> tuple[float, float, float]:
    """
    Calcula el Valor Esperado del litigio.
    
    Returns:
        (ev_bruto, ev_neto, valor_presente)
    """
    # Probabilidad de derrota
    prob_derrota = 1 - params.prob_victoria_total - params.prob_victoria_parcial
    
    # Resultados de cada escenario
    resultado_victoria = params.cantidad_reclamada - params.costes_juicio
    resultado_parcial = params.cantidad_parcial - params.costes_juicio
    resultado_derrota = -params.costes_juicio - params.costes_contraparte
    
    # Valor Esperado
    ev_bruto = (
        params.prob_victoria_total * params.cantidad_reclamada +
        params.prob_victoria_parcial * params.cantidad_parcial +
        prob_derrota * 0  # En derrota no recuperamos nada
    )
    
    ev_neto = (
        params.prob_victoria_total * resultado_victoria +
        params.prob_victoria_parcial * resultado_parcial +
        prob_derrota * resultado_derrota
    )
    
    # Valor Presente Neto (descontando por tiempo)
    factor_descuento = (1 + params.tasa_descuento) ** params.duracion_años
    ev_vpn = ev_neto / factor_descuento
    
    return ev_bruto, ev_neto, ev_vpn


def calcular_sensibilidad(params: LitigationParams, ev_vpn: float) -> list[dict]:
    """Calcula umbrales de sensibilidad."""
    sensibilidad = []
    
    # Si hay oferta, calcular probabilidad umbral
    if params.oferta_acuerdo:
        # ¿Con qué P(victoria) el EV iguala la oferta?
        # Simplificado: P * (cantidad - costes) = oferta
        cantidad_neta = params.cantidad_reclamada - params.costes_juicio
        if cantidad_neta > 0:
            prob_umbral = params.oferta_acuerdo / cantidad_neta
            sensibilidad.append({
                "variable": "prob_victoria_total",
                "umbral_indiferencia": round(min(1, prob_umbral), 2),
                "interpretacion": f"Necesitas {prob_umbral:.0%} de confianza para que litigar sea mejor"
            })
        
        # ¿Qué costes máximos harían preferir el acuerdo?
        # EV_neto - costes_extra = oferta → costes_extra = EV_neto - oferta
        coste_max = ev_vpn - params.oferta_acuerdo + params.costes_juicio
        if coste_max > 0:
            sensibilidad.append({
                "variable": "costes_juicio",
                "umbral_maximo": round(coste_max, 2),
                "interpretacion": f"Si los costes superan {coste_max:,.0f}€, mejor pactar"
            })
    
    return sensibilidad


def generar_arbol(params: LitigationParams) -> dict:
    """Genera representación del árbol de decisión."""
    prob_derrota = 1 - params.prob_victoria_total - params.prob_victoria_parcial
    
    return {
        "nodos": [
            {
                "id": 1,
                "tipo": "decision",
                "label": "DECISIÓN",
                "opciones": ["LITIGAR", "ACORDAR"]
            },
            {
                "id": 2,
                "tipo": "azar",
                "label": "Resultado Juicio",
                "probabilidades": {
                    "victoria_total": params.prob_victoria_total,
                    "victoria_parcial": params.prob_victoria_parcial,
                    "derrota": round(prob_derrota, 2)
                }
            },
            {
                "id": 3,
                "tipo": "resultado",
                "escenario": "Victoria Total",
                "valor": params.cantidad_reclamada - params.costes_juicio
            },
            {
                "id": 4,
                "tipo": "resultado",
                "escenario": "Victoria Parcial",
                "valor": params.cantidad_parcial - params.costes_juicio
            },
            {
                "id": 5,
                "tipo": "resultado",
                "escenario": "Derrota",
                "valor": -(params.costes_juicio + params.costes_contraparte)
            }
        ],
        "conexiones": [
            {"from": 1, "to": 2, "label": "LITIGAR"},
            {"from": 1, "to": "acuerdo", "label": "ACORDAR"},
            {"from": 2, "to": 3, "prob": params.prob_victoria_total},
            {"from": 2, "to": 4, "prob": params.prob_victoria_parcial},
            {"from": 2, "to": 5, "prob": prob_derrota}
        ]
    }


def execute_skill(
    cantidad_reclamada: float,
    prob_victoria_total: float,
    prob_victoria_parcial: float,
    costes_juicio: float,
    duracion_años: float = 2.0,
    cantidad_parcial: Optional[float] = None,
    costes_contraparte: float = 0,
    tasa_descuento: float = 0.05,
    oferta_acuerdo: Optional[float] = None
) -> dict:
    """
    Ejecuta el cálculo BATNA.
    
    Returns:
        Análisis completo con recomendación
    """
    # Si no se especifica cantidad parcial, asumir 50%
    if cantidad_parcial is None:
        cantidad_parcial = cantidad_reclamada * 0.5
    
    # Validar probabilidades
    if prob_victoria_total + prob_victoria_parcial > 1:
        return {"error": "Las probabilidades suman más de 1"}
    
    params = LitigationParams(
        cantidad_reclamada=cantidad_reclamada,
        prob_victoria_total=prob_victoria_total,
        prob_victoria_parcial=prob_victoria_parcial,
        cantidad_parcial=cantidad_parcial,
        costes_juicio=costes_juicio,
        costes_contraparte=costes_contraparte,
        duracion_años=duracion_años,
        tasa_descuento=tasa_descuento,
        oferta_acuerdo=oferta_acuerdo
    )
    
    # Calcular EV
    ev_bruto, ev_neto, ev_vpn = calcular_ev_litigio(params)
    batna = ev_vpn
    
    # Determinar recomendación
    if oferta_acuerdo is not None:
        diferencia = oferta_acuerdo - batna
        if diferencia > 0:
            recomendacion = "ACEPTAR_ACUERDO"
            razon = f"La oferta ({oferta_acuerdo:,.0f}€) supera el BATNA ({batna:,.0f}€) en {diferencia:,.0f}€"
            confianza = min(0.95, 0.5 + (diferencia / oferta_acuerdo) * 0.5)
        else:
            recomendacion = "RECHAZAR_Y_LITIGAR"
            razon = f"El BATNA ({batna:,.0f}€) supera la oferta ({oferta_acuerdo:,.0f}€) en {-diferencia:,.0f}€"
            confianza = min(0.95, 0.5 + (-diferencia / batna) * 0.5)
    else:
        diferencia = None
        recomendacion = "SIN_OFERTA_EVALUAR"
        razon = f"BATNA calculado: {batna:,.0f}€. Cualquier oferta superior es aceptable."
        confianza = 0.7
    
    # Análisis de sensibilidad
    sensibilidad = calcular_sensibilidad(params, ev_vpn)
    
    # Árbol de decisión
    arbol = generar_arbol(params)
    
    return {
        "escenario": f"Reclamación de {cantidad_reclamada:,.0f}€",
        "parametros": {
            "cantidad_reclamada": cantidad_reclamada,
            "prob_victoria_total": prob_victoria_total,
            "prob_victoria_parcial": prob_victoria_parcial,
            "costes_juicio": costes_juicio,
            "duracion_años": duracion_años
        },
        "analisis": {
            "ev_litigio_bruto": round(ev_bruto, 2),
            "ev_litigio_neto": round(ev_neto, 2),
            "ev_litigio_valor_presente": round(ev_vpn, 2),
            "batna": round(batna, 2),
            "oferta_acuerdo": oferta_acuerdo,
            "diferencia": round(diferencia, 2) if diferencia else None
        },
        "decision": {
            "recomendacion": recomendacion,
            "razon": razon,
            "confianza": round(confianza, 2)
        },
        "sensibilidad": sensibilidad,
        "arbol_decision": arbol
    }


if __name__ == "__main__":
    # Ejemplo de uso
    result = execute_skill(
        cantidad_reclamada=100000,
        prob_victoria_total=0.40,
        prob_victoria_parcial=0.30,
        costes_juicio=15000,
        costes_contraparte=12000,
        duracion_años=2.5,
        oferta_acuerdo=45000
    )
    
    print(json.dumps(result, indent=2, ensure_ascii=False))
