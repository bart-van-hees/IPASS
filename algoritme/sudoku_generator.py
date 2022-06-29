import random

class generate_sudoku:
    def __init__(self, total):
        self.sudoku = [
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
        self.min_numbers = total

    def make_sudoku(self):
        """
        :description:
            while loop gebruikt zodat het programma stopt op het moment dat het aantal nummers is bereikt.
            Random gebruikt om een random x en y coordinaat te krijgen.
            Random gebruikt om een random gok te krijgen.
            Hierna controleert het programma of de gok en plaats geldig is,
            zoja wordt de gok geplaatst zo niet probeert het programma alle stappen opnieuw.

        :return: Niks, deze functie maakt alleen een nieuwe onopgeloste sudoku aan.
        """
        counter = 0
        while self.min_numbers != counter:
            x = (random.randint(0, 8))
            y = (random.randint(0, 8))
            gok = (random.randint(1, 9))
            if self.good_guess(x, y, gok) != False and self.sudoku[x][y] == 0:
                self.sudoku[x][y] = gok
                counter += 1
            else:
                continue

    def good_guess(self, rij, colom, gok):
        """
        :param rij: Index van de rij binnen de sudoku
        :param colom: Index van de colom binnen de sudoku
        :param gok:  Getal dat momenteel de gok is bijvoorbeeld: 9

        :description:
            Deze functie roept 3 andere functies aan die allemaal een boolean terug geven,
            op de basis van die booleans maakt hij een keuze.

        :return: True of false, true wanneer er geen conflict is met andere getallen.
        False wanneer er een conflict is met andere getallen.
        """
        y = self.horizontal_check(rij,gok)
        x = self.grid(rij,colom, gok)
        z = self.vertical_check(colom,gok)
        if x == False or y == False or z == False:
            return False
        else:
            return True

    def vertical_check(self, colom, gok):
        """
        :param colom: Index van de colom
        :param gok: Getal dat momenteel de gok is

        :description:
            Loopt door alle lijsten in sudoku en bekijkt het getal op de index van colom,
            dit getal vergelijkt het programma met gok. Hierdoor kan ik dus de verticale rijen vergelijken.
            Als het getal op de index van colom en gok overeen komen geeft het programma false terug anders None

        :returns: False wanneer het getal al in de colom staat,
        None wanneer het getal nog niet in de sudoku staat.
        """
        for item in self.sudoku:
            if item[colom] == gok:
                return False
            else:
                continue

    def horizontal_check(self, rij, gok):
        """
        :param rij: Geeft aan welke rij uit de sudoku nodig is.
        :param gok: Getal dat momenteel de gok is

        :description:
            Loopt door alle getallen van de rij heen en vergelijkt ze met gok.
            Als ze overeen komen geeft hij False terug anders None

        :return: False wanneer de gok al in de rij staat, anders None
        """
        for item in self.sudoku[rij]:
            if item == gok:
                return False
            else:
                continue

    def grid(self, rij, colom, gok):
        """
        :param rij: Index van de rij van de sudoku
        :param colom: Index van de colom van de sudoku
        :param gok: Het getal dat momenteel de gok is

        :description:
            Kijkt in welke rij het getal zit en dan in welke colom:
            Hierdoor bekijkt de functie altijd de juist 3x3 grid.
            De functie loopt dan door alle getallen in de 3x3 grid en vergelijkt ze met gok.
            Als ze overeen komen wordt false terug gegeven anders None.

        :return: False wanneer het getal al in de 3x3 grid zit en None er nog niet in zit.
        """
        if rij <= 2:
            if colom <= 2:
                for item in range(3):
                    for x in range(3):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 5:
                for item in range(3):
                    for x in range(3,6):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 8:
                for item in range(3):
                    for x in range(6,9):
                        if (self.sudoku[item][x]) == gok:
                            return False
        elif rij <= 5:
            if colom <= 2:
                for item in range(3, 6):
                    for x in range(3):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 5:
                for item in range(3, 6):
                    for x in range(3, 6):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 8:
                for item in range(3, 6):
                    for x in range(6, 9):
                        if (self.sudoku[item][x]) == gok:
                            return False
        elif rij <= 8:
            if colom <= 2:
                for item in range(6, 9):
                    for x in range(3):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 5:
                for item in range(6, 9):
                    for x in range(3, 6):
                        if (self.sudoku[item][x]) == gok:
                            return False
            elif colom <= 8:
                for item in range(6, 9):
                    for x in range(6, 9):
                        if (self.sudoku[item][x]) == gok:
                            return False

    def get_sudoku(self):
        """
        :return: Geeft de nieuwe onopgeloste sudoku terug.
        """
        unsolved_sudoku = self.sudoku
        return unsolved_sudoku