import tkinter as tk

empty_user_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def add_number():
    number = int(get_add_number.get())
    x = int(get_x.get())
    y = int(get_y.get())
    get_add_number.delete(0,tk.END)
    get_x.delete(0, tk.END)
    get_y.delete(0, tk.END)

    empty_user_grid[x-1][y-1] = number
    for item in empty_user_grid:
        print(item)



window = tk.Tk(className="sudoku test raam")
window.geometry("500x700")
window.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=50, weight=1)
window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],minsize=50, weight=1)

btn_add_number = tk.Button(master=window, text="add number", command=add_number)
btn_add_number.grid(row = 11, column= 2,sticky="nsew")

label_x = tk.Label(master=window, text="grid-x", fg="black", width=10, height=10)
label_x.grid(row=10, column=4, sticky="nsew")

label_x = tk.Label(master=window, text="grid-y", fg="black", width=10, height=10)
label_x.grid(row=11, column=4, sticky="nsew")

get_add_number = tk.Entry(master= window,width= 2, )
get_add_number.grid(row = 10, column= 2, sticky="nsew")

get_x = tk.Entry(master=window, width=2, )
get_x.grid(row = 10, column= 5, sticky="nsew")

get_y = tk.Entry(master=window, width=2, )
get_y.grid(row = 11, column= 5, sticky="nsew")





window.mainloop()
