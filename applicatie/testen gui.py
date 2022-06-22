empty_user_grid = [
    [1, 0, 1, 4, 0, 4, 7, 0, 7],
    [2, 0, 2, 5, 0, 5, 8, 0, 8],
    [3, 0, 3, 6, 0, 6, 9, 0, 9],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

for rij in range(len(empty_user_grid)):
    for getal in range(len(empty_user_grid[rij])):
        print(rij, "is rij")
        print(getal, "is getal")
        print(empty_user_grid[rij][getal])
        if rij <= 2 :
            print('kleiner dan 2')
            if getal <= 2:
