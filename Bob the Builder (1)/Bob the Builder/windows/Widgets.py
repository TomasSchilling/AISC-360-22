import tkinter as tk

class Table(tk.Frame):
    def __init__(self, parent, dimentions):
        super().__init__(parent)
        self.n_rows = dimentions[1]
        self.n_cols = dimentions[0]

        self.cells = []
        for i in range(self.n_rows):
            self.cells.append([])
            for j in range(self.n_cols):
                cell = tk.Entry(self)
                cell.grid(row = i, column = j)
                self.cells[i].append(cell)
    
    def table_to_list(self):
        data = []
        for i in range(self.n_rows):
            data.append([])
            for j in range(self.n_cols):
                info = self.cells[i][j].get()
                try: 
                    info = float(info)
                except:
                    pass
                data[i].append(info)
        return data
        
                