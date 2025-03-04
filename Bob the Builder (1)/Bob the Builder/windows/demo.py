import tkinter as tk

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Demo")
        self.label = tk.Label(self.window, text = "Work in progress")
        self.label.grid()
        self.window.mainloop()