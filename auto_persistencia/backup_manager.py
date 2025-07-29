# Script de backup automático simbólico
import os
from datetime import datetime
import shutil

def crear_backup(origen, destino_base):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    destino = os.path.join(destino_base, f"backup_{timestamp}")
    shutil.copytree(origen, destino)
    return destino
