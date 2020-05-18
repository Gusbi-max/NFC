class NFC:
    def __init__(self):
        self.montant_maximum = 30
        self.cumul_maximum = 100
        self.cumul = 0
        self.serie_HA_max = 5
        self.serie_HA = 0
        self.code = 1234

    #GETTERS
    def getMontant(self): return self.montant_maximum
    def getCumul(self): return self.cumul
    def getCumulMax(self): return self.cumul_maximum
    def getSerie(self): return self.serie_HA
    def getSerieMax(self): return self.serie_HA_max
    def getCode(self): return self.code

    #SETTERS
    def setSerie(self, serie): self.serie_HA = serie
    def setCumul(self, montant): self.cumul = montant
        
    #METHODES    
    def incrementeSerie(self):
        self.setSerie(self.getSerie() + 1)
    def incrementeCumul(self, montant):
        self.setCumul(self.getCumul() + montant)

    def taperCode(self):
        entree = int(input("Veuillez entrer votre code à 4 chiffres: "))
        if entree != self.code:
            entree = int(input("Code faux ! Veuillez entrer votre code à 4 chiffres: "))
        else:
            print("Code valide")
            self.setSerie(0)
            self.setCumul(0)
   
    def controleAchat(self, montant):
        if montant > self.montant_maximum:
            self.taperCode()
        else:
            self.controleSerie()
            self.controleCumul(montant)

    def controleSerie(self):
        if self.getSerie() == self.getSerieMax():
            self.taperCode()
        else:
            self.incrementeSerie()

    def controleCumul(self, montant):
        if self.getCumul() + montant > self.getCumulMax():
            self.taperCode()
        else:
            self.incrementeCumul(montant)

if __name__ == "__main__":
    
    carteNFC = NFC()

    while(True):
        montant_achat = float(input("Veuillez entrer le montant de votre nouvel achat: "))

        carteNFC.controleAchat(montant_achat)