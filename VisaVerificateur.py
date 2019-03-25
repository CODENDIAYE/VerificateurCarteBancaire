from Verificateur import Verificateur
from Vluhn import is_luhn_valid


class VisaVerificateur(Verificateur):

    def __init__(self):
        ''
    def VerifierCarte(self, num):
        if(len(num) == 15 & (num.startwhith('14') | num.startwhith('15')) & is_luhn_valid(num)):
            print("La carte est correcte et c\'est une carte visa")

        print("La carte est incorrecte")

            



