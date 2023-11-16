from presentation import *
import time

class cage:
    CAGE_ENTIERE = 0
    CAGE_HAUT_1 = 1
    CAGE_HAUT_2 = 2
    CAGE_BAS_1 = 3
    CAGE_BAS_2 = 4
    REAFFICHER_CAGE = 5


    def __init__(self, presentation):
        self.presentation = presentation
        self.etat = cage.CAGE_ENTIERE
        self.delai = 0
        self.presentation.afficherCage(1)
        self.presentation.afficherCage(2)
        self.presentation.afficherCage(3)
        self.presentation.afficherCage(4)


    def Effacer_Cage (self, etat):
        if self.etat == cage.CAGE_ENTIERE:
            self.presentation.effacerCarre(2, 7, 2, 2)
            self.etat = cage.CAGE_HAUT_1

        elif self.etat == cage.CAGE_HAUT_1:
            self.presentation.effacerCarre(2, 9, 2, 2)
            self.etat = cage.CAGE_HAUT_2

        elif self.etat == cage.CAGE_HAUT_2:
            self.presentation.effacerCarre(4, 7, 2, 2)
            self.etat = cage.CAGE_BAS_1

        elif self.etat == cage.CAGE_BAS_1:
            self.presentation.effacerCarre(4, 9, 2, 2)
            self.presentation.afficherRireDK()

            self.etat = cage.CAGE_BAS_2


        elif self.etat == cage.CAGE_BAS_2:

            self.etat = cage.REAFFICHER_CAGE

        elif self.etat == cage.REAFFICHER_CAGE:
            self.presentation.afficherCage(1)
            self.presentation.afficherCage(2)
            self.presentation.afficherCage(3)
            self.presentation.afficherCage(4)
            self.presentation.effacerCarre(3, 8, 2, 2)
            self.etat = cage.CAGE_ENTIERE
            self.delai = 15



        self.delai = 0


