import tkinter as tk
from tkinter.messagebox import showinfo
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

global generated
generated = 0
lst=[]

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

def generate_input_grid():
    for rij in range(len(empty_user_grid)):
        for getal in range(len(empty_user_grid[rij])):
            if rij <= 2:
                if getal <= 2:
                    temp_getal = tk.Entry(master=window, relief="sunken",bg="#14213D", fg="white", justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
                elif getal <= 5:
                    temp_getal = tk.Entry(master=window, relief="raised",bg="#fca311", fg="black",justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
                elif getal <= 8:
                    temp_getal = tk.Entry(master=window, relief="sunken",bg="#14213D", fg="white",justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
            elif rij <= 5:
                if getal <= 2:
                    temp_getal = tk.Entry(master=window, relief="raised", bg="#fca311", fg="black", justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
                elif getal <= 5:
                    temp_getal = tk.Entry(master=window, relief="sunken", bg="#14213D", fg="white", justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
                elif getal <= 8:
                    temp_getal = tk.Entry(master=window, relief="raised", bg="#fca311", fg="black", justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
            elif rij <= 8:
                if getal <= 2:
                    temp_getal = tk.Entry(master=window, relief="sunken", bg="#14213D", fg="white", justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
                elif getal <= 5:
                    temp_getal = tk.Entry(master=window, relief="raised", bg="#fca311", fg="black", justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)
                elif getal <= 8:
                    temp_getal = tk.Entry(master=window, relief="sunken", bg="#14213D", fg="white", justify="center")
                    temp_getal.grid(row=rij + 1, column=getal + 1, sticky="nsew")
                    lst.append(temp_getal)

def get_numbers():
    eind_lijst=[]
    for i in range(0, len(lst), 9):
        eind_lijst.append(lst[i:i + 9])

    for item in range(len(eind_lijst)):
        for x in range(len(eind_lijst[item])):
            y = eind_lijst[item][x]
            if y.index("end") != 0:
                #add failsafe voor _ zodat laagstreepje niet in 0 ding komt
                empty_user_grid[item][x] = y.get()
                empty_user_grid_use[item][x]= int(y.get())




def show_number():
    x = int(get_x_show.get())
    y = int(get_y_show.get())
    if x < 1 or x > 9:
        showinfo(title='error', message="je x bestaat niet")
        get_x_show.delete(0, tk.END)
        get_y_show.delete(0, tk.END)
    elif y < 1 or y > 9:
        showinfo(title='error', message="je y bestaat niet")
        get_x_show.delete(0, tk.END)
        get_y_show.delete(0, tk.END)
    # elif generated == 0:
    #     showinfo(title='error', message="je hebt de antwoorden nog niet gegenereerd")
    #     get_x_show.delete(0, tk.END)
    #     get_y_show.delete(0, tk.END)
    else:
        tip = recusive_backtracking(empty_user_grid_use)
        empty_user_grid[y-1][x-1] = tip.get_tip(y-1,x-1)
        get_x_show.delete(0,tk.END)
        get_y_show.delete(0,tk.END)
        generate_grid()

def generate_answers():
    answer = recusive_backtracking(empty_user_grid_use)
    answer.solv_sudoku()
    answer.get_sudoku()
    generate_grid()


def show_sudoku():
    for y in range(len(empty_user_grid_use)):
        for x in range(len(empty_user_grid_use[y])):
            empty_user_grid[y][x] = empty_user_grid_use[y][x]
    generate_grid()



window = tk.Tk(className="sudoku test raam")
window.geometry("500x750")
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
generate_input_grid()


#buttons
btn_add_number = tk.Button(master=window, text="add\nnumbers", command=get_numbers,relief= "raised")
btn_add_number.grid(row = 13, column= 1,sticky="nsew")

btn_show_number = tk.Button(master=window, text="show\nnumber",command=show_number, relief="raised")
btn_show_number.grid(row= 11, column=1, sticky="nsew")

btn_generate_answer = tk.Button(master=window, text="solve\nsudoku", command=generate_answers,  relief= "raised")
btn_generate_answer.grid(row=13, column=4, sticky="nsew")

btn_show_answer = tk.Button(master=window, text="show\nanswers",command=show_sudoku, relief= "raised")
btn_show_answer.grid(row= 13, column= 6, sticky="nsew")


#labels
label_x_show = tk.Label(master=window, text= "grid-x", fg="black", width=10, height=10, relief="groove")
label_x_show.grid(row=11, column= 4, sticky="nsew")

label_y_show = tk.Label(master=window, text="grid-y", fg="black", width=10, height=10, relief="groove")
label_y_show.grid(row=11, column= 7 , sticky="nsew")


#entrys
get_x_show = tk.Entry(master=window, width=2)
get_x_show.grid(row=11, column=5, sticky="nsew")

get_y_show = tk.Entry(master=window, width=2)
get_y_show.grid(row=11, column= 8, sticky="nsew")


window.mainloop()