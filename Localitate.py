class Localitate:
    def __init__(self):
        self.oras = None
        self.judet = None

    def set_localitate(self, oras, judet):
        self.oras = oras
        self.judet = judet

    def __str__(self):
        return "Ors. "+self.oras+" Jud. "+self.judet
