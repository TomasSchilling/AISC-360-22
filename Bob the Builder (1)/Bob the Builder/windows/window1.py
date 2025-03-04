import tkinter as tk
from . import Widgets

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("I Armado - Secciones Nacionales y Extranjeras. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005")
        self.table_1 = Widgets.Table(self.window, [2,6])
        self.table_1.grid()
        self.boton = tk.Button(self.window, text="Print", command=self.print_table)
        self.boton.grid()
        self.window.mainloop()

    def print_table(self):
        print(self.table_1.table_to_list())