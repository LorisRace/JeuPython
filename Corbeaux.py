class Corbeau:
    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 7
        self.position = 0
        self.presentation.afficherCorbeau(self.position * 2 + 8, 2)

    def Deplacement(self):
        if self.delai > 0:
            self.delai -= 1
        else:
            self.Effacement_Corbeau()
            self.position += 1

            if self.position == 1:

                self.presentation.afficherCorbeau(self.position * 2 + 8,
                                                  ((self.position - 1) % 2) + 1)
                self.delai = 7

            elif self.position == 2:
                self.presentation.afficherCorbeau(self.position * 2 + 8,
                                                  ((self.position - 1) % 2) + 1)
                self.delai = 7

            elif self.position == 3:
                self.presentation.afficherCorbeau(self.position * 2 + 8,
                                                  ((self.position - 1) % 2) + 1)
                self.delai = 7

            elif self.position == 4:
                self.presentation.afficherCorbeau(self.position * 2 + 8,
                                                  ((self.position - 1) % 2) + 1)
                self.delai = 7

            elif self.position == 5:
                self.presentation.afficherCorbeau(self.position * 2 + 8,
                                                  ((self.position - 1) % 2) + 1)
                self.delai = 7

            elif self.position == 6:
                self.presentation.afficherCorbeau(self.position * 2 + 8,
                                                  ((self.position - 1) % 2) + 1)
                self.delai = 7

            elif self.position == 7:
                self.presentation.afficherCorbeau(self.position * 2 + 8,
                                                  ((self.position - 1) % 2) + 1)
                self.delai = 7

            elif self.position == 8:
                return 1

        return 0

    def Effacement_Corbeau(self):
        self.presentation.effacerCarre(9, self.position * 2 + 8, 2, 1)