import tkinter as tk
from tkinter.messagebox import showinfo
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

window = tk.Tk(className="sudoku test raam")
window.geometry("500x800")
window.columnconfigure([0,1,2,3,4,5,6,7,8,9], minsize=50, weight=1)
window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],minsize=50, weight=1)

lst=[]
def generate_grid():
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
    eind_lijst=[]
    for i in range(0, len(lst), 9):
        eind_lijst.append(lst[i:i + 9])

def get_numbers():
    eind_lijst=[]
    for i in range(0, len(lst), 9):
        eind_lijst.append(lst[i:i + 9])


    x=(eind_lijst[0][0])
    print(x.get())
    # for item in lst:
    #     x = (item.get())
    #     print(x, "met item: ", item)

generate_grid()
btn_add_number = tk.Button(master=window, text="add\nnumber", command=get_numbers, relief= "raised")
btn_add_number.grid(row = 11, column= 1,sticky="nsew")



window.mainloop()