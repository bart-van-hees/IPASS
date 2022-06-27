import time
start_time = time.time()

# test_sudoku_expert = [
#     [0, 2, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 0, 7],
#     [0, 8, 3, 0, 9, 0, 0, 0, 0],
#     [0, 7, 0, 0, 0, 6, 4, 0, 0],
#     [0, 4, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 8, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [5, 0, 0, 0, 3, 0, 0, 0, 2],
#     [1, 0, 0, 0, 8, 0, 7, 0, 9],
# ]
test_sudoku_expert = [
    [3, 8, 0, 0, 7, 0, 0, 4, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 7, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 5, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
]



class recusive_backtracking:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solv_sudoku(self):
        rij, colom = self.find_zero()
        if rij == False and colom == False and self.sudoku[0][0] != 0:          # 0 == false als index 0,0 == 0 denk het programma dat hij al klaar is daarom die laatste and
            return True
        else:
            for gok in range(1,10):
                if (self.good_guess(rij, colom, gok)) == True:
                    self.sudoku[rij][colom] = gok
                    if self.solv_sudoku() == True:
                        return True
                self.sudoku[rij][colom] = 0
            return False

    def find_zero(self):
        for rij in range(9):
            for colom in range(9):
                if self.sudoku[rij][colom] == 0:
                    return rij, colom
        if (self.sudoku[rij][colom]) != 0:
            return False, False

    def good_guess(self, rij, colom, gok):
        y = self.horizontal_check(rij,gok)
        x = self.grid(rij,colom, gok)
        z = self.vertical_check(colom,gok)
        if x == False or y == False or z == False:
            return False
        else:
            return True

    def vertical_check(self, colom, gok):
        for item in self.sudoku:
            if item[colom] == gok:
                return False
            else:
                continue

    def horizontal_check(self, rij, gok):
        for item in self.sudoku[rij]:
            if item == gok:
                return False
            else:
                continue

    def grid(self, rij, colom, gok):
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

    def get_tip(self, rij, colom):
        self.solv_sudoku()
        return self.sudoku[rij][colom]

    def get_sudoku(self):
        x = self.sudoku
        return x


# test1 = recusive_backtracking(test_sudoku_expert)
# test1.solv_sudoku()
# for item in test1.get_sudoku():
#     print(item)

print("--- %s seconds ---" % (time.time() - start_time))