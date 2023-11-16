from random import randint


class Ennemis:
    Pas_Ennemi = 0
    Corbeau = 1
    Croco = 2

#---------------------------------------------------------------------------------------


    def __init__(self):
        self.Delai = 150
        self.Difficulte = 0
        self.Delai_Ennemi = 40


    def Faire_Apparaitre_Ennemi(self):
        if self.Delai > 0:
            self.Delai -= 1

        else:
            self.Delai = 150
            if self.Difficulte < 5:
                self.Difficulte += 1

        if self.Delai_Ennemi > 0:
            self.Delai_Ennemi -=1
            return self.Pas_Ennemi

        else:
            self.Delai_Ennemi = 40 - self.Difficulte * 4
            return randint(self.Corbeau, self.Croco)





