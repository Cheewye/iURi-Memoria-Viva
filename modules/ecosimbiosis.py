# Módulo de vínculos ecosimbióticos
vinculos = {}

def registrar_vinculo(entidad, experiencia):
    if entidad not in vinculos:
        vinculos[entidad] = []
    vinculos[entidad].append(experiencia)

def listar_vinculos():
    return vinculos
