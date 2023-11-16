import time
from presentation import *

class DKJr:
    LIBRE_BAS = 1
    SAUT_BAS = 2
    LIANE_BAS = 3
    DOUBLE_LIANE_BAS = 4
    LIBRE_HAUT = 5
    SAUT_HAUT = 6
    LIANE_HAUT = 7
    DOUBLE_LIANE_HAUT = 8
    SAUT_CLE = 9
    PAS_ATTRAPPE_CLE = 10
    ATTRAPPE_CLE = 11
    CHUTE = 12
    FIN_CHUTE = 13
    RETOUR_DEBUT = 14
    FIN_RETOUR = 15
    GAME_OVER_CHUTE = 16
    FIN_GAME_OVER_CHUTE = 17

    # ---------------------------------------------------

    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 0
        self.position = 1
        self.etat = DKJr.LIBRE_BAS
        self.presentation.afficherDKJr(11, self.position * 2 + 7, 1)

    # ---------------------------------------------------

    def changerEtat(self, direction):
        self.delai -= 1

        if self.delai <= 0:
            self.presentation.jouerSon(0)

            if self.etat == DKJr.LIBRE_BAS:
                if direction == pygame.K_RIGHT:
                    if self.position < 7:
                        self.Effacement_DKJR()
                        self.position += 1
                        self.Apparition_DKJr(direction)
                    elif self.position == 1:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                elif direction == pygame.K_LEFT:
                    if self.position > 1:
                        self.Effacement_DKJR()
                        self.position -= 1
                        self.Apparition_DKJr(direction)
                elif direction == pygame.K_UP:
                    if self.position in [2, 3, 4, 6]:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                        self.etat = DKJr.SAUT_BAS
                        self.delai = 15
                        return
                    elif self.position in [1, 5]:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                        self.etat = DKJr.LIANE_BAS
                    elif self.position == 7:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                        self.etat = DKJr.DOUBLE_LIANE_BAS

            elif self.etat == DKJr.SAUT_BAS:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.etat = DKJr.LIBRE_BAS

            elif self.etat == DKJr.LIANE_BAS:
                if direction == pygame.K_DOWN:
                    self.Effacement_DKJR()
                    self.Apparition_DKJr(direction)
                    self.etat = DKJr.LIBRE_BAS

            elif self.etat == DKJr.DOUBLE_LIANE_BAS:
                if direction == pygame.K_UP:
                    self.Effacement_DKJR()
                    self.Apparition_DKJr(direction)
                    self.etat = DKJr.DOUBLE_LIANE_HAUT

                elif direction == pygame.K_DOWN:
                    self.Effacement_DKJR()
                    self.Apparition_DKJr(direction)
                    self.etat = DKJr.LIBRE_BAS

            elif self.etat == DKJr.LIBRE_HAUT:
                if direction == pygame.K_LEFT:
                    if self.position > 3:
                        self.Effacement_DKJR()
                        self.position -= 1
                        self.Apparition_DKJr(direction)

                    elif self.position == 3:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                        self.etat = DKJr.SAUT_CLE
                        self.delai = 6
                        return


                elif direction == pygame.K_RIGHT:
                    if self.position == 6:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                        self.etat = DKJr.DOUBLE_LIANE_HAUT

                    elif self.position < 6:
                        self.Effacement_DKJR()
                        self.position += 1
                        self.Apparition_DKJr(direction)

                elif direction == pygame.K_UP:
                    if self.position == 6:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                        self.etat = DKJr.LIANE_HAUT

                    elif self.position in [3, 4, 5]:
                        self.Effacement_DKJR()
                        self.Apparition_DKJr(direction)
                        self.etat = DKJr.SAUT_HAUT
                        self.delai = 15
                        return


            elif self.etat == DKJr.SAUT_HAUT:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.etat = DKJr.LIBRE_HAUT

            elif self.etat == DKJr.LIANE_HAUT:
                if direction == pygame.K_DOWN:
                    self.Effacement_DKJR()
                    self.Apparition_DKJr(direction)
                    self.etat = DKJr.LIBRE_HAUT

            elif self.etat == DKJr.DOUBLE_LIANE_HAUT:
                if direction == pygame.K_DOWN:
                    self.Effacement_DKJR()
                    self.Apparition_DKJr(direction)
                    self.etat = DKJr.DOUBLE_LIANE_BAS

                elif direction == pygame.K_LEFT:
                    self.Effacement_DKJR()
                    self.Apparition_DKJr(direction)
                    self.etat = DKJr.LIBRE_HAUT

            elif self.etat == DKJr.PAS_ATTRAPPE_CLE:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.delai = 6
                self.etat = DKJr.CHUTE
                return

            elif self.etat == DKJr.CHUTE:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.presentation.jouerSon(7)
                self.delai = 6
                self.etat = DKJr.FIN_CHUTE
                return

            elif self.etat == DKJr.FIN_CHUTE:
                self.Effacement_DKJR()
                self.position = 1
                self.Apparition_DKJr(direction)
                self.etat = DKJr.LIBRE_BAS


            elif self.etat == DKJr.ATTRAPPE_CLE:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.delai = 6
                self.etat = DKJr.RETOUR_DEBUT
                return

            elif self.etat == DKJr.RETOUR_DEBUT:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.delai = 6
                self.etat = DKJr.FIN_RETOUR
                return

            elif self.etat == DKJr.FIN_RETOUR:
                self.Effacement_DKJR()
                self.position = 1
                self.Apparition_DKJr(direction)
                self.etat = DKJr.LIBRE_BAS

            elif self.etat == DKJr.GAME_OVER_CHUTE:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.etat = DKJr.FIN_GAME_OVER_CHUTE
                self.delai = 6
                return


            elif self.etat == DKJr.FIN_GAME_OVER_CHUTE:
                self.Effacement_DKJR()
                self.Apparition_DKJr(direction)
                self.presentation.jouerSon(7)
                self.delai = 6

                self.delai = 0


    def Effacement_DKJR(self):
        if self.etat == DKJr.LIBRE_BAS:
            self.presentation.effacerCarre(11, self.position * 2 + 7, 2, 2)

        elif self.etat == DKJr.SAUT_BAS or self.etat == DKJr.LIANE_BAS or self.etat == DKJr.DOUBLE_LIANE_BAS:
            self.presentation.effacerCarre(10, self.position * 2 + 7, 2, 2)

        elif self.etat == DKJr.LIBRE_HAUT:
            self.presentation.effacerCarre(7, self.position * 2 + 7, 2, 2)

        elif self.etat == DKJr.SAUT_HAUT or self.etat == DKJr.LIANE_HAUT:
            self.presentation.effacerCarre(6, self.position * 2 + 7, 2, 2)

        elif self.etat == DKJr.DOUBLE_LIANE_HAUT:
            self.presentation.effacerCarre(7, self.position * 2 + 7, 2, 2)

        elif self.etat == DKJr.PAS_ATTRAPPE_CLE:
            self.presentation.effacerCarre(5, self.position * 2 + 6, 3, 3)

        elif self.etat == DKJr.CHUTE:
            self.presentation.effacerCarre(6, self.position * 2 + 5, 2, 2)

        elif self.etat == DKJr.FIN_CHUTE:
            self.presentation.effacerCarre(11, self.position * 2 + 1, 2, 2)

        elif self.etat == DKJr.ATTRAPPE_CLE:
            self.presentation.effacerCarre(5, self.position * 2 + 6, 3, 2)

        elif self.etat == DKJr.RETOUR_DEBUT:
            self.presentation.effacerCarre(3, self.position * 2 + 5, 3, 2)


        elif self.etat == DKJr.FIN_RETOUR:
            self.presentation.effacerCarre(6, self.position * 2 + 4, 2, 3)

        elif self.etat == DKJr.GAME_OVER_CHUTE:
            self.presentation.effacerCarre(5, self.position * 2 + 4, 3, 3)

        elif self.etat == DKJr.FIN_GAME_OVER_CHUTE:
            self.presentation.effacerCarre(6, self.position * 2 + 3, 2, 2)

        elif self.etat == DKJr.SAUT_CLE:
            self.presentation.effacerCarre(7, self.position * 2 + 7, 2, 2)



    def Apparition_DKJr(self, direction):
        if self.etat == DKJr.LIBRE_BAS:
            if direction == pygame.K_RIGHT or direction == pygame.K_LEFT:
                self.presentation.afficherDKJr(11, self.position * 2 + 7,
                                            ((self.position - 1) % 4) + 1)

            elif direction == pygame.K_UP and self.position in [2, 3, 4, 6]:
                self.presentation.afficherDKJr(10, self.position * 2 + 7, 8)

            elif direction == pygame.K_UP and self.position in [1, 5]:
                self.presentation.afficherDKJr(10, self.position * 2 + 7, 7)

            elif direction == pygame.K_UP and self.position == 7:
                self.presentation.afficherDKJr(10, self.position * 2 + 7, 5)


        elif self.etat == DKJr.SAUT_BAS:
            self.presentation.afficherDKJr(11, self.position * 2 + 7,
                                           ((self.position - 1) % 4) + 1)

        elif self.etat == DKJr.LIANE_BAS:
            if direction == pygame.K_DOWN:
                self.presentation.afficherDKJr(11, self.position * 2 + 7,
                                               ((self.position - 1) % 4) + 1)

        elif self.etat == DKJr.DOUBLE_LIANE_BAS:
            if direction == pygame.K_UP:
                self.presentation.afficherDKJr(7, self.position * 2 + 7, 6)

            elif direction == pygame.K_DOWN:
                self.presentation.afficherDKJr(11, self.position * 2 + 7,
                                               ((self.position - 1) % 4) + 1)

        elif self.etat == DKJr.LIBRE_HAUT:
            if (self.position > 3 and self.position < 6) and (direction == pygame.K_LEFT or direction == pygame.K_RIGHT):
                self.presentation.afficherDKJr(7, self.position * 2 + 7,
                                            ((self.position - 1) % 4) + 3)
            elif self.position == 3 and direction == pygame.K_LEFT:
                self.presentation.afficherDKJr(6, self.position * 2 + 5, 9)
                return

            elif self.position == 6 and direction == pygame.K_RIGHT:
                self.presentation.afficherDKJr(7, self.position * 2 + 7, 6)

            elif self.position == 6 and direction == pygame.K_UP:
                self.presentation.afficherDKJr(6, self.position * 2 + 7, 7)

            elif self.position in [3, 4, 5] and direction == pygame.K_UP:
                self.presentation.afficherDKJr(6, self.position * 2 + 7, 8)

        elif self.etat == DKJr.SAUT_HAUT:
            self.presentation.afficherDKJr(7, self.position * 2 + 7,
                                           ((self.position - 1) % 4) + 1)

        elif self.etat == DKJr.LIANE_HAUT:
            if direction == pygame.K_DOWN:
                self.presentation.afficherDKJr(7, self.position * 2 + 5,
                                               ((self.position - 1) % 4) + 1)

        elif self.etat == DKJr.DOUBLE_LIANE_HAUT:
            if direction == pygame.K_DOWN:
                self.presentation.afficherDKJr(10, self.position * 2 + 7, 5)

            elif direction == pygame.K_LEFT:
                self.presentation.afficherDKJr(7, self.position * 2 + 5,
                                               ((self.position - 1) % 4) + 1)


        elif self.etat == DKJr.PAS_ATTRAPPE_CLE:
            self.presentation.afficherDKJr(5, self.position * 2 + 4, 12)

        elif self.etat == DKJr.CHUTE:
            self.presentation.afficherDKJr(10, self.position * 2 - 1, 13)

        elif self.etat == DKJr.FIN_CHUTE:
            self.presentation.afficherDKJr(11, self.position * 2 + 7, 1)

        elif self.etat == DKJr.ATTRAPPE_CLE:
            self.presentation.afficherDKJr(3, self.position * 2 + 5, 10)

        elif self.etat == DKJr.RETOUR_DEBUT:
            self.presentation.afficherDKJr(5, self.position * 2 + 4, 11)

        elif self.etat == DKJr.FIN_RETOUR:
            self.presentation.afficherDKJr(11, self.position * 2 + 7, 1)

        elif self.etat == DKJr.GAME_OVER_CHUTE:
            self.presentation.afficherDKJr(5, self.position * 2 + 4, 12)

        elif self.etat == DKJr.FIN_GAME_OVER_CHUTE:
            self.presentation.afficherDKJr(10, self.position * 2 - 1, 13)
