import random

numero = random.randint(0,5)

palpite = int(input("Digite um número de 0 a 5:"))

if palpite == numero:
    print("Você venceu!")
else:
    print("\033[30mVocê perdeu!\033[m")
print("O número era: {} ".format(numero))