import time

import pygame.display

from presentation import *
from dkjr import *
from Cle import *
from Corbeaux import *
from Crocos import *
from Ennemis import *
from DK import *

class Jeu:
    def __init__(self, presentation):
        self.presentation = presentation
        self.dkjr = DKJr(self.presentation)
        self.Cle = Cle(self.presentation)
        self.cage = cage(self.presentation)
        self.Ennemi = Ennemis()
        self.listeCorbeaux =[]
        self.listeCrocos=[]
        self.nbEchecs = 0  # nombre de vies perdues
        self.score = 0   # le score

 #----------------------------------------------------------------------------
    # méthode contenant la boucle principale du jeu

    def demarrer(self):
        self.presentation.afficherScore(self.score)

        self.presentation.jouerSon(8)
        time.sleep(3)
        self.presentation.jouerSon(5)

        while self.nbEchecs < 3:
            while True:
                # lire l'événement au clavier lorsque DK Jr est prêt à bouger
                self.Cle.Changer_ETAT()
                self.Deplacement_Ennemis()

                if self.nbEchecs == 3:
                    break

                if self.dkjr.delai <= 0:
                    evenement = self.presentation.lireEvenement()

                if evenement in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                    # changer l'état/la position de DK Jr selon l'événement du joueur

                    self.dkjr.changerEtat(evenement)

                    if self.Ennemi_Touche():
                        self.Collision()

                    if self.dkjr.etat == self.dkjr.LIBRE_HAUT:
                        if evenement == pygame.K_LEFT and self.dkjr.position == 3:
                                self.dkjr.etat = self.dkjr.SAUT_CLE
                                time.sleep(0.5)
                                if self.Cle.etat == 1:
                                    self.dkjr.etat = self.dkjr.ATTRAPPE_CLE
                                    self.Cle.etat = self.Cle.CLE_ATTRAPPEE
                                    self.dkjr.changerEtat(evenement)
                                    self.cage.Effacer_Cage(evenement)
                                    self.score = self.score + 10
                                    self.presentation.afficherScore(self.score)
                                    self.presentation.jouerSon(3)
                                    self.presentation.jouerSon(4)

                                elif self.Cle.etat != 1:
                                    self.dkjr.etat = self.dkjr.PAS_ATTRAPPE_CLE
                                    self.dkjr.changerEtat(evenement)
                                    self.nbEchecs += 1

                                    if self.nbEchecs == 1:
                                        self.presentation.afficherEchec(0)
                                        self.presentation.jouerSon(1)

                                    elif self.nbEchecs == 2:
                                        self.presentation.afficherEchec(1)
                                        self.presentation.jouerSon(1)

                                    elif self.nbEchecs == 3:
                                        self.presentation.afficherEchec(2)
                                        self.presentation.jouerSon(1)
                                        self.dkjr.etat = 16
                                        self.dkjr.changerEtat(evenement)
                                        break

                    if self.cage.etat == 4:
                        self.cage.etat = 5
                        time.sleep(0.6)
                        self.score = self.score + 10
                        self.presentation.afficherScore(self.score)
                        self.presentation.jouerSon(3)
                        self.cage.Effacer_Cage(evenement)
                        time.sleep (0.6)
                        self.presentation.jouerSon(6)



                # attendre 100 millisecondes (délai de référence)

                time.sleep(0.1)



        # la partie est terminée. Attendre le clic sur la croix dans la fenêtre
        # pour fermer l'application

        self.presentation.attendreFermetureFenetre()

    def Deplacement_Ennemis(self):
        Ennemis = self.Ennemi.Faire_Apparaitre_Ennemi()
        if Ennemis == self.Ennemi.Corbeau:
            self.listeCorbeaux.append(Corbeau(self.presentation))
            print(self.Ennemi.Corbeau)
        elif Ennemis == self.Ennemi.Croco:
            self.listeCrocos.append(Croco(self.presentation))
            print(self.Ennemi.Croco)
        for corbeau in self.listeCorbeaux:
            if corbeau.Deplacement() == 1:
                self.listeCorbeaux.pop(0)
        for croco in self.listeCrocos:
            if croco.Deplacement() == 1:
                self.listeCrocos.pop(0)


    def Collision(self):
        if self.dkjr.etat == DKJr.LIBRE_BAS:
            for croco in self.listeCrocos:
                if croco.position == self.dkjr.position and croco.Position_Augmente is False:
                    croco.Effacement_Croco()
                    self.listeCrocos.pop(0)
                    return True
        elif self.dkjr.etat in [DKJr.LIANE_BAS, DKJr.SAUT_BAS, DKJr.DOUBLE_LIANE_BAS]:
            for corbeau in self.listeCorbeaux:
                if corbeau.position == self.dkjr.position:
                    corbeau.Effacement_Corbeau()
                    self.listeCorbeaux.pop(0)
                    return True
        elif self.dkjr.etat == DKJr.LIBRE_HAUT and self.dkjr.position != 2:
            for croco in self.listeCrocos:
                if croco.position == self.dkjr.position and croco.Position_Augmente is True:
                    croco.Effacement_Croco()
                    self.listeCrocos.pop(0)
                    return True
                elif self.dkjr.etat == self.dkjr.SAUT_HAUT and croco.position == self.dkjr.position:
                    self.score = self.score + 1
                    self.presentation.afficherScore(self.score)

        else:
            return False

    def Ennemi_Touche(self):
        if self.Collision() == True:
            self.presentation.jouerSon(1)
            for i in range(3):
                self.dkjr.Effacement_DKJR()
                time.sleep(0.05)
                self.dkjr.Apparition_DKJr(self)
                time.sleep(0.05)
            while self.nbEchecs <= 3:
                self.nbEchecs += 1
                if self.nbEchecs == 1:
                    self.presentation.afficherEchec(0)

                elif self.nbEchecs == 2:
                    self.presentation.afficherEchec(1)

                elif self.nbEchecs == 3:
                    self.presentation.afficherEchec(2)
                return True
        else:
            return False

    def Supprimer_Ennemis(self):
        for corbeau in self.listeCorbeaux:
            if corbeau.position in [0, 1, 2]:
                corbeau.Effacer_Corbeau(0)
                self.listeCorbeaux.pop(corbeau)
        for croco in self.listeCrocos:
            if croco.position in [1, 2, 3]:
                croco.effacer_croco()
                self.listeCrocos.pop(0)