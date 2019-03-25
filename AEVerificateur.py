from Verificateur import Verificateur
from Vluhn import is_luhn_valid


class AEVerificateur(Verificateur):

    def VerifierCarte(self, num):
        if (len(num) == 17 & (num.startwhith('39') | num.startwhith('30')) & is_luhn_valid(num)):
            print("La carte est correcte et c\'est une americainExpress")

        print("La carte est incorrecte")
