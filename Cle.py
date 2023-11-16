import time
from presentation import*

class Cle:
    ETAT_1 = 1
    ETAT_2 = 2
    ETAT_3 = 3
    ETAT_4 = 4
    ETAT_5 = 5
    ETAT_6 = 6
    CLE_ATTRAPPEE = 7


    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 0.1
        self.etat = Cle.ETAT_1
        self.presentation.afficherCle(1)

    def Changer_ETAT(self):
        self.delai -= 1
        if self.delai <= 0:
            self.presentation.jouerSon(4)
            if self.etat == Cle.ETAT_1:
                self.presentation.effacerCarre(3, 12, 2, 1)
                self.presentation.afficherCle(2)
                self.etat = Cle.ETAT_2
                self.delai = 7
                return


            elif self.etat == Cle.ETAT_2:
                self.presentation.effacerCarre(3, 13, 2, 1)
                self.presentation.afficherCle(3)
                self.etat = Cle.ETAT_3
                self.delai = 7
                return


            elif self.etat == Cle.ETAT_3:
                self.presentation.effacerCarre(3, 13, 2, 2)
                self.presentation.afficherCle(4)
                self.etat = Cle.ETAT_4
                self.delai = 7
                return

            elif self.etat == Cle.ETAT_4:
                self.presentation.effacerCarre(3, 13, 2, 2)
                self.presentation.afficherCle(3)
                self.etat = Cle.ETAT_5
                self.delai = 7
                return


            elif self.etat == Cle.ETAT_5:
                self.presentation.effacerCarre(3, 13, 2, 2)
                self.presentation.afficherCle(2)
                self.etat = Cle.ETAT_6
                self.delai = 7
                return


            elif self.etat == Cle.ETAT_6:
                self.presentation.effacerCarre(3, 13, 2, 1)
                self.presentation.afficherCle(1)
                self.etat = Cle.ETAT_1
                self.delai = 7
                return

            elif self.etat == Cle.CLE_ATTRAPPEE:
                self.presentation.effacerCarre(3, 12, 2, 1)
                self.presentation.effacerCarre(3, 13, 2, 1)
                self.presentation.effacerCarre(3, 13, 2, 2)
                self.presentation.effacerCarre(3, 13, 2, 2)
                self.delai = 20
                self.etat = Cle.ETAT_2







