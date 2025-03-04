import tkinter as tk
from . import window1 as w1
from . import demo

class MenuWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Structito")
        for i in range(14):
            boton = tk.Button(self.window, text = window_dict[i], command = function_dict[i])
            boton.grid()
        self.window.mainloop()

def start_window_1():
    w1.Window()

def start_demo_window():
    demo.Window()

window_dict = {0: "I Armado - Secciones Nacionales y Extranjeras. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005",
               1: "I Armado - Secciones Especiales. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005",
               2: "C Laminado - Secciones Especiales. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005",
               3: "Cajón Armado - Secciones Especiales. Flexos-Compresión Biaxial, Corte Biaxial y Torsión AISC 2005",
               4: "O - Secciones Especiales. Flexos-Compresión Biaxial, Corte Biaxial y Torsión AISC 2005",
               5: "T Armado - Secciones Nacionales, Extranjeras y Especiales. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005",
               6: "VPR Armado - Secciones Especiales. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005, Standard 13",
               7: "L Laminado - Secciones Nacionales y Especiales. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005",
               8: "TL Laminado - Secciones Nacionales y Especiales. Flexos-Compresión, Corte AISC 2005",
               9: "L Plegado - Secciones Nacionales y Especiales. Flexos-Compresión Biaxial, Corte Biaxial AISC 2005",
               10: "XL Plegado - Secciones Nacionales y Especiales. Compresión Pura AISC 2005",
               11: "TL Plegado - Secciones Nacionales y Especiales. Flexo-Compresión, Corte AISC 2005",
               12: "C Plegado - Secciones Nacionales y Especiales. Flexos-Compresión Biaxial, Corte Biaxial",
               13: "CA Plegado - Secciones Nacionales y Especiales. Flexos-Compresión Biaxial, Corte Biaxial"}

function_dict = {0: start_window_1,
                 1: start_demo_window,
                 2: start_demo_window,
                 3: start_demo_window,
                 4: start_demo_window,
                 5: start_demo_window,
                 6: start_demo_window,
                 7: start_demo_window,
                 8: start_demo_window,
                 9: start_demo_window,
                 10: start_demo_window,
                 11: start_demo_window,
                 12: start_demo_window,
                 13: start_demo_window}