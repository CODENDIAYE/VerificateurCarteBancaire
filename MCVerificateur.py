from Verificateur import Verificateur
from Vluhn import is_luhn_valid


class  MCVerificateur(Verificateur):

    def VerifierCarte(self, num):
        if(len(num) == 16 & (num.startwhith('41') | num.startwhith('40')) & is_luhn_valid(num)):
            print("La carte est correcte et c\'est une masterCard")

        print("La carte est incorrecte")