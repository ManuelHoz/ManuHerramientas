import os
from gestor_pdf import GestorPDF

class Modelo:
    def __init__(self):
        self.lista_archivos = []
        self.textos_cabecera = {}

    def agregar_archivo(self, archivo):
        if archivo.endswith(".pdf"):
            gestor_pdf = GestorPDF(archivo)
            texto_pdf = gestor_pdf.extraer_texto()
            self.textos_cabecera[archivo] = texto_pdf
        else:
            self.lista_archivos.append(archivo)
            self.textos_cabecera[archivo] = ""

    def obtener_texto_cabecera_archivo(self, archivo):
        return self.textos_cabecera.get(archivo, "")

    def establecer_texto_cabecera_archivo(self, archivo, texto):
        self.textos_cabecera[archivo] = texto

    def eliminar_archivo(self, archivo):
        if archivo in self.lista_archivos:
            self.lista_archivos.remove(archivo)

    def obtener_archivos(self):
        return self.lista_archivos

    def agregar_texto_cabecera(self, texto):
        self.texto_cabecera = texto

    def obtener_texto_cabecera(self):
        return self.texto_cabecera or ""

    def combinar_archivos(self, nombre_archivo_salida):
        with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            if self.texto_cabecera:
                archivo_salida.write(self.texto_cabecera + '\n\n')
                print(f"Escribiendo cabecera general: {self.texto_cabecera}")  # Depuración

            for archivo in self.lista_archivos:
                archivo_salida.write(f'=== {os.path.basename(archivo)} ===\n')
                cabecera_individual = self.textos_cabecera.get(archivo, "")
                if (cabecera_individual):
                    archivo_salida.write(cabecera_individual + '\n')
                    print(f"Escribiendo cabecera individual para {archivo}: {cabecera_individual}")  # Depuración

                with open(archivo, 'r', encoding='utf-8') as archivo_file:
                    contenido = archivo_file.read()
                    archivo_salida.write(contenido)
                    archivo_salida.write('\n\n')
                print(f"Escribiendo contenido del archivo {archivo}")  # Depuración

    def copiar_portapapeles(self):
        contenido_combinado = self.texto_cabecera + '\n\n' if self.texto_cabecera else ""
        for archivo in self.lista_archivos:
            contenido_combinado += f'=== {os.path.basename(archivo)} ===\n'
            with open(archivo, 'r', encoding='utf-8') as archivo_file:
                contenido_combinado += archivo_file.read() + '\n\n'
        return contenido_combinado
