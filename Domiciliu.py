from Adresa import Adresa
from Localitate import Localitate


class Domiciliu:
    def __init__(self):
        self.localitate = Localitate()
        self.adresa = Adresa()

    def set_domiciliu(self, localitate, adresa):
        self.localitate.set_localitate(localitate[0], localitate[1])
        self.adresa.set_adresa(adresa[0], adresa[1])

    def __str__(self):
        return self.localitate.__str__()+"\n"+self.adresa.__str__()
