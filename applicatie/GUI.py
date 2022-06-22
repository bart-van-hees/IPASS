import tkinter as tk
from algoritme.sudoku_algoritme import *

empty_user_grid = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
]

empty_user_grid_use = [
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
def generate_grid():
    for rij in range(len(empty_user_grid)):
        for getal in range(len(empty_user_grid[rij])):
            if rij <= 2:
                if getal <= 2:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="sunken",
                                          bg="#14213D", fg="white")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                elif getal <= 5:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="raised",
                                          bg="#fca311", fg="black")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                elif getal <= 8:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="sunken",
                                          bg="#14213D", fg="white")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")

            elif rij <= 5:
                if getal <= 2:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="raised",
                                          bg="#fca311", fg="black")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                elif getal <= 5:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="sunken",
                                          bg="#14213D", fg="white")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                elif getal <= 8:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="raised",
                                          bg="#fca311", fg="black")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")

            elif rij <= 8:
                if getal <= 2:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="sunken",
                                          bg="#14213D", fg="white")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                elif getal <= 5:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="raised",
                                          bg="#fca311", fg="black")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                elif getal <= 8:
                    temp_getal = tk.Label(master=window, text=str(empty_user_grid[rij][getal]), relief="sunken",
                                          bg="#14213D", fg="white")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")


def add_number():
    number = int(get_add_number.get())
    x = int(get_x.get())
    y = int(get_y.get())
    get_add_number.delete(0,tk.END)
    get_x.delete(0, tk.END)
    get_y.delete(0, tk.END)

    empty_user_grid[y-1][x-1] = number
    empty_user_grid_use[y-1][x-1] = number
    generate_grid()

def show_number():
    number = int(get_show_number.get())
    x = int(get_x_show.get())
    y = int(get_y_show.get())
    get_show_number.delete(0,tk.END)
    get_x_show.delete(0,tk.END)
    get_y_show.delete(0,tk.END)

def generate_answers():
    answer = recusive_backtracking(empty_user_grid_use)
    answer.solv_sudoku()
    answer.get_sudoku()






window = tk.Tk(className="sudoku test raam")
window.geometry("500x800")
window.columnconfigure([0,1,2,3,4,5,6,7,8,9], minsize=50, weight=1)
window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],minsize=50, weight=1)

#labels 1-9
XY = tk.Label(master=window, text="X →\nY\n↓")
XY.grid(row=0, column=0, sticky="nsew")


for item in range(len(empty_user_grid)):
    temp = tk.Label(master=window,text=str(item+1), relief="ridge", bg="#e5e5e5")
    temp.grid(row=0,column=item+1, sticky="nsew")

for item in range(len(empty_user_grid)):
    temp = tk.Label(master=window, text=str(item + 1),relief= "ridge", bg="#e5e5e5")
    temp.grid(row=item+1, column=0, sticky="nsew")


#9x9 grid
#functie van gemaakt waardoor ik hem kan aanroepen als er iets veranderd
generate_grid()


#buttons
btn_add_number = tk.Button(master=window, text="add\nnumber", command=add_number, relief= "raised")
btn_add_number.grid(row = 11, column= 1,sticky="nsew")

btn_show_number = tk.Button(master=window, text="show\nnumber", relief="raised")
btn_show_number.grid(row= 13, column=1, sticky="nsew")

btn_generate_answer = tk.Button(master=window, text="solve\nsudoku", relief= "raised")
btn_generate_answer.grid(row=15, column=4, sticky="nsew")

btn_show_answer = tk.Button(master=window, text="show\nsudoku", relief= "raised")
btn_show_answer.grid(row= 15, column= 6, sticky="nsew")


#labels
label_x = tk.Label(master=window, text="grid-x", fg="black", width=10, height=10, relief="groove")
label_x.grid(row=11, column=4, sticky="nsew")

label_y = tk.Label(master=window, text="grid-y", fg="black", width=10, height=10, relief="groove")
label_y.grid(row=11, column=7, sticky="nsew")

label_x_show = tk.Label(master=window, text= "grid-x", fg="black", width=10, height=10, relief="groove")
label_x_show.grid(row=13, column= 4, sticky="nsew")

label_y_show = tk.Label(master=window, text="grid-y", fg="black", width=10, height=10, relief="groove")
label_y_show.grid(row=13, column= 7 , sticky="nsew")


#entrys
get_add_number = tk.Entry(master= window,width= 2)
get_add_number.grid(row = 11, column= 2, sticky="nsew")

get_x = tk.Entry(master=window, width=2)
get_x.grid(row = 11, column= 5, sticky="nsew")

get_y = tk.Entry(master=window, width=2 )
get_y.grid(row = 11, column= 8, sticky="nsew")

get_show_number = tk.Entry(master=window, width=2)
get_show_number.grid(row= 13, column= 2, sticky="nsew")

get_x_show = tk.Entry(master=window, width=2)
get_x_show.grid(row=13, column=5, sticky="nsew")

get_y_show = tk.Entry(master=window, width=2)
get_y_show.grid(row=13, column= 8, sticky="nsew")




window.mainloop()