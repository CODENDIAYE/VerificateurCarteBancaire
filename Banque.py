from Verificateur import Verificateur
class Banque:


    def __init__(self, iverificateur):
        self.iverificateur = iverificateur

    def getVerificateur(self):
        return self.iverificateur

    def setNumero(self,iverificateur):
        self.iverificateur=iverificateur

    def Verification(self, num):
        self.iverificateur.VerifierCarte(num)