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

for item in len(range(test_sudoku_empty)):
    print(item)


gok = 9
rij = 6
colom = 8
# def grid(rij,colom,gok):
#     if rij <= 2:
#         if colom <= 2:
#             for item in range(3):
#                 for x in range(3):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#         elif colom <= 5:
#             for item in range(3):
#                 for x in range(3, 6):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#         elif colom <= 8:
#             for item in range(3):
#                 for x in range(6, 9):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#     elif rij <= 5:
#         if colom <= 2:
#             for item in range(3,6):
#                 for x in range(3):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#
#         elif colom <= 5:
#             for item in range(3, 6):
#                 for x in range(3, 6):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#
#         elif colom <= 8:
#             for item in range(3,6):
#                 for x in range(6, 9):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#     elif rij <= 8:
#         if colom<=2:
#             for item in range(6,9):
#                 for x in range(3):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#         elif colom <=5:
#             for item in range(6,9):
#                 for x in range(3,6):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#         elif colom <=8:
#             for item in range(6,9):
#                 for x in range(6,9):
#                     if (test_sudoku_empty[item][x]) == gok:
#                         return False
#
#
#
# x=grid(rij,colom,gok)
# print(x)
# if x != False:
#     print('is valid')

x= None
y=None
z= None

if x ==False or y == False or z == False:
    print('false')
else:
    print("true")