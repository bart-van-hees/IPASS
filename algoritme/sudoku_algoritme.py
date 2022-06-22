import time
start_time = time.time()

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

# test_sudoku_empty = [ #medium
#     [0, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]

test_sudoku_empty = [ #expert
    [0, 2, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 7],
    [0, 8, 3, 0, 9, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 6, 4, 0, 0],
    [0, 4, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 3, 0, 0, 0, 2],
    [1, 0, 0, 0, 8, 0, 7, 0, 9],
]

empty_user_grid = [
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


class recusive_backtracking:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solv_sudoku(self):
        rij, colom = self.find_zero()
        if rij == False and colom == False and self.sudoku[0][0] != 0:          # 0 == false als index 0,0 == 0 denk het programma dat hij al klaar is daarom die laatste and
            print("de puzzle is solved")
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

    def get_sudoku(self):
        x = self.sudoku
        return x






# test1 = recusive_backtracking(test_sudoku_empty)
# test1.solv_sudoku()
# for item in test1.get_sudoku():
#     print(item)

# c = int(input("vul hier in hoeveel cijfers je al in je sudoku hebt: "))
# print("links boven is vakje 0.0\nrechts onder is vakje 9.9\n")
# count = 0
# while count <= c:
#     getal = int(input("vul hier een cijfer in"))
#     horizontaal = int(input("vul hier je horizontale coordinaat in: "))
#     verticaal = int(input("vul hier je verticale coordinaat in: "))
#     empty_user_grid[horizontaal][verticaal] = getal
#     count+=1
#     for item in empty_user_grid:
#         print(item)
#
#
#
# print("links boven is vakje 0.0\nrechts onder is vakje 9.9\n")
# h = int(input("vul hier je horizontale coordinaat in: "))
# v = int(input("vul hier je verticale coordinaat in: "))
#
# print("het cijfer van vakje",h,".",v,"is:",test1.get_sudoku()[h][v])
print("--- %s seconds ---" % (time.time() - start_time))