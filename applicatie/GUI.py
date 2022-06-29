import tkinter as tk
from tkinter.messagebox import showinfo
from algoritme.sudoku_algoritme import *
from algoritme.sudoku_generator import *
from applicatie.grids import *


def generate_grid():
    """
    :description:
        Maakt het 9x9 grid met 3x3 grids erin.
        Ik heb dit in een functie gezet waardoor ik het vaker kan aanroepen.
    """
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
    """
    :description:
        Maakt het 9x9 grid van 3x3 grids in de applicatie.
        Deze functie zorgt ook voor de entry's waardoor de gebruiker makkelijk zijn sudoku kan invullen.
        Elke entry wordt toegevoegd aan een lijst, hierdoor kan ik ook terug vinden wat er waar is ingevuld.
        Ik heb dit in een functie gezet omdat ik het makkelijker vaker kan aanroepen.
    """
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
    """
    :description:
        Split de lijst met entry's op in 9 sublijsten bestaand uit 9 entry's
        Loopt door de lijsten heen en kijkt of de entry leeg is of niet.
        Zo niet wordt dat getal toegevoegd op dezelfde index in de lijst die een visueel doeleinde heeft,
        en aan een lijst die wordt gebruikt om de oplossing te berekenen.
    """
    eind_lijst=[]
    for i in range(0, len(lst), 9):
        eind_lijst.append(lst[i:i + 9])

    for item in range(len(eind_lijst)):
        for x in range(len(eind_lijst[item])):
            y = eind_lijst[item][x]
            if y.index("end") != 0:
                empty_user_grid[item][x] = y.get()
                empty_user_grid_use[item][x]= int(y.get())


def show_number():
    """
    :description:
        Haalt de x en y coördinaten op en maakt de entry's daarna weer leeg voor hergebruik.
        Als x of y coördinaat niet klopt krijg je een pop-up.
        Als de coördinaten wel kloppen word het nummer op dat index opgevraagd en daarna in de applicatie laten zien.
    """
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
    else:
        tip = recusive_backtracking(empty_user_grid_use)
        empty_user_grid[y-1][x-1] = tip.get_tip(y-1,x-1)
        get_x_show.delete(0,tk.END)
        get_y_show.delete(0,tk.END)
        generate_grid()

def generate_answers():
    """
    :description:
        Haalt de antwoorden van de sudoku op doormiddel van het sudoku algoritme
        Ook veranderd hij de applicatie waardoor de gebruik geen nieuwe getallen meer kan invullen.
    """
    answer = recusive_backtracking(empty_user_grid_use)
    answer.solv_sudoku()
    answer.get_sudoku()
    generate_grid()

def show_sudoku():
    """
    :description:
        Loopt door de lijst met de antwoorden en vervangt de streepjes op het visuele grid.
        Roept aan het einde generate_grid aan om de volledige opgeloste sudoku te laten zien in de applicatie.
    """
    for y in range(len(empty_user_grid_use)):
        for x in range(len(empty_user_grid_use[y])):
            empty_user_grid[y][x] = empty_user_grid_use[y][x]
    generate_grid()

def new_sudoku():
    """
    :description:
        Roept de sudoku generator aan en laat een nieuwe sudoku genereren doormiddel van het ingevulde aantal nummers.
        De for loops zijn er voor om de twee lijsten te updaten na welke getallen er nu in staan.
        Hierdoor kan je vaker dan 1 keer een nieuwe sudoku genereren zonder het programma te stoppen.
        Aan het einde wordt generate_grid gebruikt om de applicatie te updaten.
    """
    total = int(get_total_numbers.get())
    get_total_numbers.delete(0,tk.END)
    new_sudoku = generate_sudoku(total)
    new_sudoku.make_sudoku()

    for rij in range(len(new_sudoku.get_sudoku())):
        for colom in range(len(new_sudoku.get_sudoku()[rij])):
            empty_user_grid_use[rij][colom] = new_sudoku.get_sudoku()[rij][colom]

    for rij in range(len(empty_user_grid_use)):
        for colom in range(len(empty_user_grid_use[rij])):
            if empty_user_grid_use[rij][colom] != 0:
                empty_user_grid[rij][colom] = empty_user_grid_use[rij][colom]
            else:
                empty_user_grid[rij][colom] = "_"
    generate_grid()

def delete_text(x):
    """
    :description:
        Als er op de entry box wordt geklikt verwijderd hij de tijdelijke tekst.
    """
    get_total_numbers.delete(0,tk.END)



"""
    Hieronder worden alle knoppen, labels en entry's aangemaakt.
    De twee for loops zijn om de x en y aan te maken inplaats van 18 labels zelf uit te schrijven.

"""


window = tk.Tk(className="sudoku applicatie")
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
btn_add_number = tk.Button(master=window, text="add\nnumbers", command=get_numbers,relief= "raised", fg="#000000", bg="#e5e5e5")
btn_add_number.grid(row = 13, column= 1,sticky="nsew")

btn_show_number = tk.Button(master=window, text="show\nnumber",command=show_number, relief="raised", fg="#000000", bg="#e5e5e5")
btn_show_number.grid(row= 11, column=1, sticky="nsew")

btn_generate_answer = tk.Button(master=window, text="solve\nsudoku", command=generate_answers,  relief= "raised", fg="#000000", bg="#e5e5e5")
btn_generate_answer.grid(row=13, column=3, sticky="nsew")

btn_show_answer = tk.Button(master=window, text="show\nanswers",command=show_sudoku, relief= "raised", fg="#000000", bg="#e5e5e5")
btn_show_answer.grid(row= 13, column= 5, sticky="nsew")

btn_get_new_sudoku = tk.Button(master=window, text="new\nsudoku",command=new_sudoku, relief= "raised", fg="#000000", bg="#e5e5e5")
btn_get_new_sudoku.grid(row= 13, column= 7, sticky="nsew")

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

get_total_numbers = tk.Entry(master=window, width=2)
get_total_numbers.grid(row=13, column=8,sticky="nsew")
get_total_numbers.insert(0, "numbers\n")
get_total_numbers.bind("<FocusIn>", delete_text)

window.mainloop()