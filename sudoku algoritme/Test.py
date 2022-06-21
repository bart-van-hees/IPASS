# import tkinter as tk
#
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

# window = tk.Tk()
#
# for i in range(9):
#     for j in range(9):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=empty_user_grid[i][j])
#         label.pack(padx = 10, pady = 5)
#
# window.mainloop()






# import tkinter as tk
#
# def increase():
#     value = float(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
# def decrease():
#     value = float(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"
#
# def divide():
#     value = float(lbl_value["text"])
#     lbl_value["text"] = f"{value/2}"
#
# window = tk.Tk()
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=50, weight=1)
# # window.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1, minsize=50)
#
# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")
#
# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)
#
# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")
#
# btn_divide = tk.Button(master=window, text="/", command=divide)
# btn_divide.grid(row=0, column=3, sticky="nsew")
#
# window.mainloop()


import tkinter as tk

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






























