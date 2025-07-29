# Módulo de diagnóstico basado en errores simbióticos
errores = []

def registrar_error(descripcion):
    errores.append(descripcion)

def analizar_errores():
    return {"total": len(errores), "último": errores[-1] if errores else "Ninguno"}
