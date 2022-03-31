import pickle

from Domiciliu import Domiciliu
from Localitate import Localitate


class Persoana:
    def __init__(self):
        self.nume = None
        self.prenume = None
        self.cetatenie = None
        self.loc_nastere = Localitate()
        self.domiciliu = Domiciliu()
        self.emis = None
        self.data_nastere = None

    def af(self):
        print(self.nume, '\n', self.prenume, '\n', self.cetatenie, '\n', self.loc_nastere, '\n', self.domiciliu, '\n', self.emis, '\n', self.data_nastere.strftime("%d.%m.%y"), '\n')

    def salveaza_informatii(self):
        file = open("resources/informations", "wb")
        pickle.dump(self, file)
        file.close()

    def preia_informatii(self):
        file = open("resources/informations", "rb")
        self = pickle.load(file)
        file.close()
