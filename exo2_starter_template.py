from Exo1 import Robot

#class Robot():
#    """ Robot class content here"""


class Human:
    def __init__(self, sexe):
        self.sexe = sexe
        self.estomac = []

    def miam(self, manger):
        if isinstance(manger, list):
            self.estomac.extend(manger)
        else:
            self.estomac.append(manger)

    def digest(self):
        print('Digérer...')

class Cyborg(Robot, Human):
    def __init__(self, nom, sexe):
        Robot.__init__(self, nom)
        Human.__init__(self, sexe)
    
    # Méthode fun au Cyborg
    def faire_la_danse_du_robot(self):
        print(f'{self.nom} est en train de danser la danse du robot !')


if __name__ == "__main__":

    cyborg1 = Cyborg('Patrick', 'Homme')

    print(cyborg1.nom, 'sexe', cyborg1.sexe)
    print('Charging battery...')
    cyborg1.allumer()
    cyborg1.miam('banana')
    cyborg1.miam(['coca', 'chips'])
    print(cyborg1.estomac)
    cyborg1.digest()

    cyborg1.faire_la_danse_du_robot()