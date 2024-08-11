# Documentación del Proyecto de Combinación de Archivos

Este proyecto es una aplicación de escritorio desarrollada en Python que permite combinar múltiples archivos en un solo archivo de salida. La interfaz de usuario está construida utilizando la librería Tkinter junto con ttkbootstrap para un diseño moderno, y soporta la funcionalidad de arrastrar y soltar archivos (Drag and Drop) utilizando tkinterdnd2.

## Archivos del Proyecto

### controlador.py

Este archivo contiene la clase `Controlador`, que maneja la lógica de la aplicación y actúa como intermediario entre la vista (interfaz de usuario) y el modelo (gestión de archivos y datos).

#### Clase `Controlador`

- \***\*init**(self, modelo, vista)\*\*: Inicializa el controlador, enlaza los botones de la vista con sus correspondientes métodos y configura el gestor de archivos y diálogos.

- **seleccionar_directorio(self)**: Permite al usuario seleccionar un directorio y agrega los archivos que cumplan con los tipos especificados a la lista de archivos del modelo.

- **anadir_archivo(self)**: Permite al usuario seleccionar uno o más archivos para añadirlos a la lista gestionada por el modelo.

- **modificar_cabecera(self, archivo)**: Permite al usuario modificar el texto de la cabecera de un archivo específico.

- **agregar_texto(self)**: Agrega un texto de cabecera general que se aplicará a todos los archivos combinados.

- **mostrar_texto_cabecera(self)**: Muestra los primeros 100 caracteres del texto de la cabecera en la interfaz de usuario.

- **eliminar_archivo(self, archivo)**: Elimina un archivo de la lista gestionada por el modelo.

- **mostrar_ruta_completa(self, archivo)**: Alterna entre mostrar el nombre del archivo y su ruta completa en la interfaz de usuario.

- **actualizar_listbox(self)**: Actualiza la lista de archivos mostrada en la interfaz de usuario.

- **archivos_arrastrados(self, event)**: Maneja los archivos arrastrados y soltados en la ventana, agregándolos a la lista del modelo.

- **combinar_archivos(self)**: Combina todos los archivos en la lista en un solo archivo de salida.

- **copiar_portapapeles(self)**: Copia el contenido combinado de los archivos al portapapeles.

### gestor_archivos.py

Este archivo contiene la clase `GestorArchivos`, responsable de gestionar la obtención de archivos desde un directorio.

#### Clase `GestorArchivos`

- **obtener_archivos_directorio(self, directorio, tipos_archivo)**: Devuelve una lista de archivos en un directorio que cumplen con los tipos de archivo especificados.

### gestor_dialogos.py

Este archivo contiene la clase `GestorDialogos`, responsable de manejar los diálogos y las interacciones con el usuario.

#### Clase `GestorDialogos`

- **seleccionar_directorio(self)**: Muestra un diálogo para que el usuario seleccione un directorio.

- **seleccionar_archivos(self, tipos_archivo)**: Muestra un diálogo para que el usuario seleccione uno o más archivos.

- **obtener_texto_cabecera(self)**: Permite al usuario introducir manualmente un texto de cabecera o seleccionarlo desde un archivo de texto.

- **obtener_nombre_archivo_salida(self)**: Solicita al usuario un nombre para el archivo de salida.

- **obtener_texto_cabecera_inicial(self, texto_actual="")**: Permite al usuario modificar el texto de cabecera de un archivo específico.

### main.py

El punto de entrada de la aplicación. Configura la ventana principal, inicializa el modelo, la vista y el controlador, y ejecuta el bucle principal de la aplicación.

### modelo.py

Este archivo contiene la clase `Modelo`, que maneja la lógica de datos, incluyendo la lista de archivos y los textos de cabecera.

#### Clase `Modelo`

- \***\*init**(self)\*\*: Inicializa las estructuras de datos para gestionar archivos y textos de cabecera.

- **agregar_archivo(self, archivo)**: Añade un archivo a la lista de archivos.

- **obtener_texto_cabecera_archivo(self, archivo)**: Devuelve el texto de cabecera asociado a un archivo específico.

- **establecer_texto_cabecera_archivo(self, archivo, texto)**: Establece el texto de cabecera para un archivo específico.

- **eliminar_archivo(self, archivo)**: Elimina un archivo de la lista de archivos.

- **obtener_archivos(self)**: Devuelve la lista de archivos gestionados.

- **agregar_texto_cabecera(self, texto)**: Establece el texto de cabecera general.

- **obtener_texto_cabecera(self)**: Devuelve el texto de cabecera general.

- **combinar_archivos(self, nombre_archivo_salida)**: Combina los archivos y sus cabeceras en un archivo de salida.

- **copiar_portapapeles(self)**: Copia el contenido combinado al portapapeles.

### vista.py

Este archivo contiene la clase `Vista`, que maneja la interfaz gráfica del usuario (GUI) utilizando Tkinter y ttkbootstrap.

#### Clase `Vista`

- \***\*init**(self, ventana)\*\*: Inicializa la ventana principal, los componentes gráficos y configura la estética de la interfaz.

- **get_tipos_archivo(self)**: Devuelve una lista de tipos de archivo seleccionados por el usuario.

- **mostrar_texto_cabecera(self, texto_mostrado)**: Muestra el texto de cabecera en el área designada de la interfaz.

- **crear_widget_archivo(self, archivo, eliminar_func, mostrar_ruta_func, modificar_cabecera_func)**: Crea y configura un widget para cada archivo en la lista de archivos.

- **limpiar_listbox(self)**: Elimina todos los widgets actuales de la lista de archivos en la interfaz.

## Requisitos

- Python 3.x
- Tkinter
- ttkbootstrap
- tkinterdnd2

## Ejecución

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias necesarias.
3. Ejecuta `main.py` para iniciar la aplicación.
