# Módulo de consultas simbólicas en lenguaje natural
def consultar_memoria(pregunta):
    if "última solución técnica" in pregunta.lower():
        return "La última solución técnica aplicada fue: Reiniciar el servicio con memoria preservada."
    return "Consulta simbólica procesada: " + pregunta
