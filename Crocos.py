class Croco:
    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 7
        self.position = 2
        self.Position_Augmente = True
        self.presentation.afficherCroco(self.position * 2 + 5, 2)

    def Deplacement(self):
        if self.delai > 0:
            self.delai -= 1
        else:
            self.Effacement_Croco()
            if self.Position_Augmente == True:
                self.position += 1
                if self.position == 2:
                    self.presentation.afficherCroco(self.position * 2 + 5,
                                                    ((self.position - 1) % 2) + 1)
                    self.delai = 7

                if self.position == 3:
                    self.presentation.afficherCroco(self.position * 2 + 5,
                                                    ((self.position - 1) % 2) + 1)
                    self.delai = 7

                if self.position == 4:
                    self.presentation.afficherCroco(self.position * 2 + 5,
                                                    ((self.position - 1) % 2) + 1)
                    self.delai = 7

                if self.position == 5:
                    self.presentation.afficherCroco(self.position * 2 + 5,
                                                    ((self.position - 1) % 2) + 1)
                    self.delai = 7

                if self.position == 6:
                    self.presentation.afficherCroco(self.position * 2 + 5,
                                                    ((self.position - 1) % 2) + 1)
                    self.delai = 7

                if self.position == 7:
                    self.presentation.afficherCroco(self.position * 2 + 5,
                                                    ((self.position - 1) % 2) + 1)
                    self.delai = 7
                    
            elif self.Position_Augmente == False:
                self.position -= 1
                if self.position == 7:
                    self.presentation.afficherCroco(self.position * 2 + 7,
                                                    ((self.position - 1) % 2) + 4)
                    self.delai = 7

                if self.position == 6:
                    self.presentation.afficherCroco(self.position * 2 + 7,
                                                    ((self.position - 1) % 2) + 4)
                    self.delai = 7

                if self.position == 5:
                    self.presentation.afficherCroco(self.position * 2 + 7,
                                                    ((self.position - 1) % 2) + 4)
                    self.delai = 7

                if self.position == 4:
                    self.presentation.afficherCroco(self.position * 2 + 7,
                                                    ((self.position - 1) % 2) + 4)
                    self.delai = 7

                if self.position == 3:
                    self.presentation.afficherCroco(self.position * 2 + 7,
                                                    ((self.position - 1) % 2) + 4)
                    self.delai = 7

                if self.position == 2:
                    self.presentation.afficherCroco(self.position * 2 + 7,
                                                    ((self.position - 1) % 2) + 4)
                    self.delai = 7

                if self.position == 1:
                    self.presentation.afficherCroco(self.position * 2 + 7,
                                                    ((self.position - 1) % 2) + 4)
                    self.delai = 7

            if self.position == 0:
                return 1

            elif self.position == 8:
                self.Position_Augmente = False
                self.presentation.afficherCroco(23, 3)


            return 0

    def Effacement_Croco(self):
        if self.position != 8:
            if self.Position_Augmente:
                self.presentation.effacerCarre(8, self.position * 2 + 5, 1, 1)
            else:
                self.presentation.effacerCarre(12, self.position * 2 + 7, 1, 1)
        else:
            self.presentation.effacerCarre(9, 23, 1, 1)