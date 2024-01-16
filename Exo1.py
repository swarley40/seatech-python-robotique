import time

class Robot:
    def __init__(self, nom):
        self.nom = nom
        self.allume = False
        self.batterie = 0
        self.vitesse = 0
        self.en_deplacement = False

    def allumer(self):
        if not self.allume:
            print(f"{self.nom} s'allume.")
            self.allume = True
        else:
            print(f"{self.nom} est déjà allumé.")

    def eteindre(self):
        if self.allume:
            print(f"{self.nom} s'éteint.")
            self.allume = False
            self.en_deplacement = False  # Arrête le déplacement lorsque le robot s'éteint
        else:
            print(f"{self.nom} est déjà éteint.")

    def charger_batterie(self, pourcentage_cible):
        if 0 <= pourcentage_cible <= 100:
            print(f"{self.nom} commence à charger sa batterie.")
            temps_max_charge = 10  # 10 secondes max pour la charge
            temps_attente = temps_max_charge / 100  # temps d'attente par pourcentage
            while self.batterie < pourcentage_cible:
                self.batterie += 1
                print(f"{self.nom} charge à {self.batterie}%.")
                time.sleep(temps_attente)
            print(f"{self.nom} a terminé la charge à {self.batterie}%.")
        else:
            print("Le pourcentage de charge doit être compris entre 0 et 100.")

    def enregistrer_vitesse(self, vitesse):
        self.vitesse = vitesse
        print(f"{self.nom} enregistre une vitesse de déplacement de {self.vitesse}.")

    def obtenir_vitesse(self):
        return self.vitesse

    def arreter_deplacement(self):
        if self.en_deplacement:
            print(f"{self.nom} arrête son déplacement.")
            self.en_deplacement = False
        else:
            print(f"{self.nom} n'est pas en déplacement.")

    def etat_global(self):
        etat = f"{self.nom} - État global:\n"
        etat += f"   Allumé: {self.allume}\n"
        etat += f"   Batterie: {self.batterie}%\n"
        etat += f"   Vitesse de déplacement: {self.vitesse}\n"
        etat += f"   En déplacement: {self.en_deplacement}\n"
        return etat

# Exemple d'utilisation



if __name__ == "__main__":
    def main():
        mon_robot = Robot("ROB")

        mon_robot.allumer()

        mon_robot.enregistrer_vitesse(5)  # Enregistre une vitesse de déplacement de 5

        mon_robot.charger_batterie(100)

        mon_robot.arreter_deplacement()

        print(mon_robot.etat_global())

        mon_robot.eteindre()

    main()

    