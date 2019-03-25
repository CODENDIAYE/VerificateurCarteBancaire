from Banque import Banque
from Verificateur import Verificateur


def main():
    pass

num = input("Veiller le numero de la carte : ")

ver = Verificateur()
bank = Banque(ver)
bank.Verification(num)
