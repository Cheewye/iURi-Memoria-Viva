# Módulo de bitácora encriptada
import base64

bitacora = []

def registrar_evento(evento):
    encriptado = base64.b64encode(evento.encode()).decode()
    bitacora.append(encriptado)

def leer_bitacora():
    return [base64.b64decode(e).decode() for e in bitacora]
