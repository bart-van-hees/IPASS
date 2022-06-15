
test_sudoku_solved= [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9],
]


test_sudoku_empty = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]



# z = [1,2,3,4,5,6,7,8,9]


class recusive_backtracking():
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solv_sudoku(self):
        rij, colom = self.find_unused()



    def find_unused(self):
        for rij in range(9):
            for colom in range(9):
                if self.sudoku[colom][rij] == 0:
                    return rij, colom
                if(self.sudoku[8][8]) !=0:
                    return False, False
test1 = recusive_backtracking(test_sudoku_empty)
test1.solv_sudoku()