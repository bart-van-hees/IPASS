from sudoku_algoritme import *
import random

class generate_sudoku:
    def __init__(self):
        self.sudoku = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.min_numbers = 17



    def make_sudoku(self):
        counter = 0
        while self.min_numbers != counter:
            x = (random.randint(0, 8))
            y = (random.randint(0, 8))
            gok = (random.randint(1, 9))
            if self.good_guess(x, y, gok) != False:
                self.sudoku[x][y] = gok
                counter += 1
            else:
                continue

        # valid = recusive_backtracking(self.sudoku)
        # for item in valid.get_sudoku():
        #     print(item)
        for item in self.sudoku:
            print(item)


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

    def get_sudoku(self):
        x = self.sudoku
        return x




test = generate_sudoku()
test.make_sudoku()
x = test.get_sudoku()
print("\n")
p =recusive_backtracking(x)
p.solv_sudoku()
for item in p.get_sudoku():
    print(item)

