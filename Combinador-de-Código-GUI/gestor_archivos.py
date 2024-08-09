import os

class GestorArchivos:
    def obtener_archivos_directorio(self, directorio, tipos_archivo):
        archivos = []
        for tipo in tipos_archivo:
            archivos.extend([os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith(tipo)])
        return archivos
