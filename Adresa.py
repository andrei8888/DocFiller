class Adresa:
    def __init__(self):
        self.strada = None
        self.nr = None
        
    def set_adresa(self, strada, nr):
        self.strada = strada
        self.nr = nr

    def __str__(self):
        return "Sos. "+self.strada+" nr."+str(self.nr)
