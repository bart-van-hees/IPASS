test_sudoku_solved = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

test_sudoku_empty = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


# z = [1,2,3,4,5,6,7,8,9]




#taken voor vrijdag
# split good_guess 2 keer op in horizontal en vertical
#finish het algoritme

class recusive_backtracking():
    def __init__(self, sudoku):
        self.sudoku = sudoku
        # self.rij = rij
        # self.colom = colom

    def solv_sudoku(self):
        rij, colom = self.find_zero()
        print(rij, colom)
        if rij == False and colom == False:
            print("de puzzle is solved")
        else:
            for gok in range(1,10):
                if (self.good_guess(self.sudoku, rij, colom, gok)) != False:
                    print(gok, "kan op deze plek")


    def find_zero(self):
        for rij in range(9):
            for colom in range(9):
                if self.sudoku[colom][rij] == 0:
                    # self.rij = rij
                    # self.colom = colom
                    return rij, colom
        if (self.sudoku[rij][colom]) != 0:
            return False, False




    def good_guess(self, sudoku, rij, colom, gok):
        #verticale check
        print("ik ben gok", gok)
        for item in sudoku:
            if item[colom] == gok:
                print("ik breek")
                return False
            else:
                continue

        #horizontale check
        for item in sudoku[rij]:
            if item == gok:
                print("ik breek horzontaal")
                return False
            else:
                continue

        #3x3 check
        #haal de index van de 3x3 grid op
        x = self.grid(rij,colom, gok)


    def grid(self, rij,colom, gok):
        if rij <= 2:
            if colom <= 2:
                for item in range(3):
                    for x in range(3):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 5:
                for item in range(3):
                    for x in range(3,6):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 8:
                for item in range(3):
                    for x in range(6,9):
                        if (self.sudoku[item][x]) == gok:
                            return False

        elif rij <= 5:
            if colom <= 2:
                for item in range(3, 6):
                    for x in range(3):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 5:
                for item in range(3, 6):
                    for x in range(3, 6):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 8:
                for item in range(3, 6):
                    for x in range(6, 9):
                        if (self.sudoku[item][x]) == gok:
                            return False

        elif rij <= 8:
            if colom <= 2:
                for item in range(6, 9):
                    for x in range(3):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 5:
                for item in range(6, 9):
                    for x in range(3, 6):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 8:
                for item in range(6, 9):
                    for x in range(6, 9):
                        if (self.sudoku[item][x]) == gok:
                            return False







test1 = recusive_backtracking(test_sudoku_empty)
test1.solv_sudoku()
