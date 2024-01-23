from abc import ABCMeta, abstractmethod


class UnmannedVehicle(metaclass=ABCMeta):
    @abstractmethod
    def mission(self):
        pass


class AerialVehicle(UnmannedVehicle, metaclass=ABCMeta):
    @abstractmethod
    def avion(self):
        pass


class GroundVehicle(UnmannedVehicle, metaclass=ABCMeta):
    @abstractmethod
    def voiture(self):
        pass


class UnderwaterVehicle(UnmannedVehicle, metaclass=ABCMeta):
    @abstractmethod
    def bateau(self):
        pass


class UAV(AerialVehicle):
    def mission(self):
        print("Il faut décoller")

    def avion(self):
        print("Je voooooooole !!!!")


class UGV(GroundVehicle):
    def mission(self):
        print("Il faut aller à l'aéroport")

    def voiture(self):
        print("Vroooum vroouuum")


class UUV(UnderwaterVehicle):
    def mission(self):
        print("Il faut explorer les profondeur de l'antarctique")

    def bateau(self):
        print("JE SUIS TOM ET JE SUIS SOUS L'EAU AHAHAHAHAHAHAHAH$")

if __name__ == '__main__':

    uav = UAV()
    uav.mission()
    uav.avion()


    ugv = UGV()
    ugv.mission()
    ugv.voiture()

    uuv = UUV()
    uuv.mission()
    uuv.bateau()


