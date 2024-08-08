from tkinter import filedialog

def select_files():
    files = filedialog.askopenfilenames(
        title="Selecciona archivos",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    return files
