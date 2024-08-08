import tkinter as tk
from tkinter import filedialog, messagebox
import os
from utils.file_selector import select_files
from utils.script_runner import run_script

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi Aplicación Tkinter")
        self.geometry("600x400")
        
        # Menú
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        
        # Menú de Archivo
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_files)
        
        # Área de Texto
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill='both')
        
        # Lista de Scripts
        self.scripts = self.load_scripts()
        
    def open_files(self):
        files = select_files()
        if files:
            self.text_area.insert(tk.END, "Archivos seleccionados:\n")
            for file in files:
                self.text_area.insert(tk.END, f"{file}\n")
    
    def load_scripts(self):
        script_dir = os.path.join(os.path.dirname(__file__), 'scripts')
        return [f for f in os.listdir(script_dir) if f.endswith('.py')]
    
    def run_selected_script(self, script, files):
        run_script(script, files)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
