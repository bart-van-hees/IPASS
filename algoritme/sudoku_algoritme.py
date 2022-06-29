class recusive_backtracking:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solv_sudoku(self):
        """
        :param sudoku: is de input sudoku die moet worden opgelost
        :returns:dat de sudoku is opgelost

        :discription:
            Doormiddel van recursie wordt de sudoku opgelost.
            De index van de eerst volgende 0 wordt opgehaald.
            Als die er niet meer is eindigd het programma.
            Als die er wel is gaat hij gokken binnen met de getallen 1 t/m 9,
            Per gok wordt gekeken of die mag als hij mag wordt die gok ingevuld op de index,
            Als de gok niet mag verhoogd hij de gok met 1 tot hij de max range heeft behaald

            Als alle getallen binnen de range niet kunnen gaat hij een stap terug
        """
        rij, colom = self.find_zero()
        if rij == False and colom == False and self.sudoku[0][0] != 0:          # 0 == false als index 0,0 == 0 denk het programma dat hij al klaar is daarom die laatste and
            return True
        else:
            for gok in range(1,10):
                if (self.good_guess(rij, colom, gok)) == True:
                    self.sudoku[rij][colom] = gok
                    if self.solv_sudoku() == True:
                        return True
                self.sudoku[rij][colom] = 0

    def find_zero(self):
        """
        :return: Index van de eerst volgende 0 of false en false als er geen nullen meer zijn
        """
        for rij in range(9):
            for colom in range(9):
                if self.sudoku[rij][colom] == 0:
                    return rij, colom
        if (self.sudoku[rij][colom]) != 0:
            return False, False

    def good_guess(self, rij, colom, gok):
        """
        :param rij: Index van de rij binnen de sudoku
        :param colom: Index van de colom binnen de sudoku
        :param gok:  Getal dat momenteel de gok is bijvoorbeeld: 9

        :discription:
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

    def get_tip(self, rij, colom):
        """
        :param rij: index van de rij.
        :param colom: index van de colom.
        :return: geeft het getal terug dat wordt opgevraagd.
        """
        self.solv_sudoku()
        return self.sudoku[rij][colom]

    def get_sudoku(self):
        """
        :return: geeft de opgeloste sudoku terug.
        """
        opgeloste_sudoku = self.sudoku
        return opgeloste_sudoku
