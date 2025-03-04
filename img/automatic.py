import parameters as p
import numpy as np
import random

tam=14
orden=(0,1,2,0,1,2,5,4,5,4,5,4,5,4,5,4,5,4,3,4,5,6,4,3,3,2,1)
class Game:
    def __init__(self):
        self.turno=0
        
        self.tablero = self.empty_list(9,9, fill = False)
        self.up2date = True
        self.score = 0
        self.shape = random.randint(0,tam)
        
    
    
    def empty_list(self, rows, columns, fill=False):
        return [[fill for _ in range(columns)] for _ in range(rows)]

    def check_list(self, lst):
        return all(lst)

    def delete_full(self, filled_shapes):
        rows_to_check = set()
        cols_to_check = set()
        squares_to_check = set()

        points = 0
        value=500
        # Collect unique rows, columns, and squares to check based on filled_shapes
        for shape in filled_shapes:
            r, c = shape
            rows_to_check.add(r)
            cols_to_check.add(c)
            squares_to_check.add((r // 3, c // 3))  # Get the square index (3x3 grid)

        rows = []
        for r in rows_to_check:
            if self.check_list(self.tablero[r]):  # Check only rows in filled_shapes
                points += value
                rows.append(r)

        columns = []
        for c in cols_to_check:
            col = [self.tablero[i][c] for i in range(9)]  # Extract the specific column
            if self.check_list(col):
                points += value
                columns.append(c)

        squares = []
        for sq in squares_to_check:
            n1, n2 = sq
            cels = [self.tablero[n1 * 3 + i][n2 * 3 + j] for i in range(3) for j in range(3)]
            if self.check_list(cels):
                points += value
                for i in range(3):
                    for j in range(3):
                        squares.append([n1 * 3 + i, n2 * 3 + j])

            # Clear columns
        for column in columns:
            for i in range(9):
                self.tablero[i][column] = False

        # Clear rows
        for row in rows:
            for i in range(9):
                self.tablero[row][i] = False

        # Clear squares
        for square in squares:
            self.tablero[square[0]][square[1]] = False
        if points> 2:
            print(points,"Y")
        return points
        
    
    def fill_shape(self, row, column, fill):
        filled_shapes = []
        able = True
        for elem in p.shape_dict[self.shape]:
            r = row + elem[0]
            c = column + elem[1]
            if r >= 0 and r <= 8 and c >= 0 and c <= 8:   ## check celda inside the map
                if self.tablero[r][c]:
                    able = False
            else:
                able = False
        
        if able:
            if not fill: ## only check for able
                return True, filled_shapes
            for elem in p.shape_dict[self.shape]:
                self.tablero[row + elem[0]][column + elem[1]] = True
                filled_shapes.append([row + elem[0], column + elem[1]])
            return True, filled_shapes
        return False, filled_shapes

    def get_shape(self):
        # The 5 lists directly correspond to the rows in the output
        lista = [
            [False],                       # Row 0
            [False, False, False],         # Row 1
            [False, False, False, False, False],  # Row 2 (middle row)
            [False, False, False],         # Row 3
            [False]                        # Row 4
        ]
        
        coordinate_map = {
            (-2, 0): (0, 0),  #
            (-1, -1): (1, 0),  
            (-1, 0): (1, 1), 
            (-1, 1): (1, 2),  
            (0, -2): (2, 0),  
            (0, -1): (2, 1),  
            (0, 0): (2, 2),   
            (0, 1): (2, 3),   
            (0, 2): (2, 4),   
            (1, -1): (3, 0),  
            (1, 0): (3, 1),   
            (1, 1): (3, 2),   
            (2, 0): (4, 0),   
        }
        

        shape = p.shape_dict[self.shape]
        

        for coord in shape:
            if coord in coordinate_map:
                row, col = coordinate_map[coord]
                lista[row][col] = True
    
        return lista
        
    def number2rc(self, number):
        row = number//9
        column = number-row*9
        return row, column
    
    def rc2number(self, row, column):
        number = 9*row+column
        return number

    def play_number(self, number):
        row, column = self.number2rc(number) 
        i, filled_shapes = self.fill_shape(row, column, True)
        self.score += self.delete_full(filled_shapes)
        self.turno +=1
        self.shape = random.randint(0,tam)
        if i:
            self.score+=len(filled_shapes)
            #print(self.score,"S")
            return True
        else:
            #print(self.score,"N")
            return self.score

        
    def join_input(self):
        flat_list1 = [item for sublist in self.get_shape() for item in sublist]
        flat_list2 = [item for sublist in self.tablero for item in sublist]
        self.joined_list = flat_list1 + flat_list2
        return self.joined_list
    
    def reset_game(self):
        self.__init__()

            




