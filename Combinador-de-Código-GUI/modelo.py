import os

class Modelo:
    def __init__(self):
        self.lista_archivos = []
        self.texto_cabecera = ""

    def agregar_archivo(self, archivo):
        if archivo.endswith('.py'):
            self.lista_archivos.append(archivo)

    def eliminar_archivo(self, archivo):
        if archivo in self.lista_archivos:
            self.lista_archivos.remove(archivo)

    def obtener_archivos(self):
        return self.lista_archivos

    def agregar_texto_cabecera(self, texto):
        self.texto_cabecera = texto

    def obtener_texto_cabecera(self):
        return self.texto_cabecera or ""  # Devolver una cadena vacía si no hay texto de cabecera


    def combinar_archivos(self, nombre_archivo_salida):
        with open(nombre_archivo_salida, 'w') as archivo_salida:
            if self.texto_cabecera:
                archivo_salida.write(self.texto_cabecera + '\n\n')
            for archivo in self.lista_archivos:
                archivo_salida.write(f'=== {os.path.basename(archivo)} ===\n')
                with open(archivo, 'r') as archivo_py:
                    archivo_salida.write(archivo_py.read())
                    archivo_salida.write('\n\n')
    
    def copiar_portapapeles(self):
        contenido_combinado = self.texto_cabecera + '\n\n' if self.texto_cabecera else ""
        for archivo in self.lista_archivos:
            contenido_combinado += f'=== {os.path.basename(archivo)} ===\n'
            with open(archivo, 'r') as archivo_py:
                contenido_combinado += archivo_py.read() + '\n\n'
        return contenido_combinado
