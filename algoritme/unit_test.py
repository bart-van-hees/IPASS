import unittest
from sudoku_algoritme import *

test_sudoku_medium = [ #medium
    [0, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

test_sudoku_medium_solved = [
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

test_sudoku_expert = [
    [4, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 7],
    [0, 8, 3, 0, 9, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 6, 4, 0, 0],
    [0, 4, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 3, 0, 0, 0, 2],
    [1, 0, 0, 0, 8, 0, 7, 0, 9],
]

test_sudoku_expert_solved=[
    [4, 2, 7, 5, 6, 8, 1, 9, 3],
    [9, 1, 5, 3, 4, 2, 8, 6, 7],
    [6, 8, 3, 1, 9, 7, 5, 2, 4],
    [8, 7, 1, 9, 2, 6, 4, 3, 5],
    [3, 4, 9, 8, 5, 1, 2, 7, 6],
    [2, 5, 6, 4, 7, 3, 9, 8, 1],
    [7, 6, 4, 2, 1, 9, 3, 5, 8],
    [5, 9, 8, 7, 3, 4, 6, 1, 2],
    [1, 3, 2, 6, 8, 5, 7, 4, 9],
]

class test_sudoku(unittest.TestCase):

    def test_get(self):
        S1 = recusive_backtracking(test_sudoku_medium)
        self.assertListEqual(S1.get_sudoku(), test_sudoku_medium)

        S2 = recusive_backtracking(test_sudoku_expert)
        self.assertListEqual(S2.get_sudoku(), test_sudoku_expert)

    def test_solv_sudoku(self):
        S1 = recusive_backtracking(test_sudoku_medium)
        S1.solv_sudoku()
        self.assertListEqual(S1.get_sudoku(), test_sudoku_medium_solved)

        S2 = recusive_backtracking(test_sudoku_expert)
        S2.solv_sudoku()
        self.assertListEqual(S2.get_sudoku(), test_sudoku_expert_solved)

    def test_find_zero(self):
        S1 = recusive_backtracking(test_sudoku_medium)
        self.assertTupleEqual(S1.find_zero(),(0,0))

        S2 = recusive_backtracking(test_sudoku_expert)
        self.assertTupleEqual(S2.find_zero(),(0,1))

    def test_good_guess(self):
        S1 = recusive_backtracking(test_sudoku_medium)
        self.assertTrue(S1.good_guess(0,0,1))
        self.assertFalse(S1.good_guess(0,0,9))

        S2 = recusive_backtracking(test_sudoku_expert)
        self.assertTrue(S2.good_guess(3,7,2))
        self.assertFalse(S2.good_guess(3,7,8))

    def test_vertical(self):
        S1 = recusive_backtracking(test_sudoku_medium)
        self.assertFalse(S1.vertical_check(0,6))

        S2 = recusive_backtracking(test_sudoku_expert)
        self.assertFalse(S2.vertical_check(5,6))

    def test_horizontal(self):
        S1 = recusive_backtracking(test_sudoku_medium)
        self.assertFalse(S1.horizontal_check(0,3))
        self.assertIsNone(S1.horizontal_check(0,1))

        S2 = recusive_backtracking(test_sudoku_expert)
        self.assertFalse(S2.horizontal_check(3,7))
        self.assertIsNone(S2.horizontal_check(3,1))

    def test_grid(self):
        S1 = recusive_backtracking(test_sudoku_medium)
        self.assertFalse(S1.grid(0,0,8))
        self.assertFalse(S1.grid(3,3,2))
        self.assertFalse(S1.grid(6,6,9))
        self.assertIsNone(S1.grid(0,0,1))
        self.assertIsNone(S1.grid(3,3,1))
        self.assertIsNone(S1.grid(6,6,1))

        S2 = recusive_backtracking(test_sudoku_expert)
        self.assertFalse(S2.grid(7,1,7))
        self.assertFalse(S2.grid(3,0,4))
        self.assertFalse(S2.grid(7,3,3))
        self.assertIsNone(S2.grid(7,1,2))
        self.assertIsNone(S2.grid(3,0,2))
        self.assertIsNone(S2.grid(7,3,2))


