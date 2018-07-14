import random

lanceJog = str(input("pedra,papel ou tesoura? "))
lancePc = ["pedra","papel","tesoura"]

sorteio = random.choice(lancePc)
print (sorteio)

if sorteio == "pedra" and lanceJog == "tesoura":
    print ("O PC venceu pois a pedra destrói a tesoura!")
elif sorteio == "pedra" and lanceJog == "papel":
    print("Você venceu o PC pois o papel enrola a pedra!")
elif sorteio == "papel" and lanceJog == "tesoura":
    print("Você venceu o PC pois a tesoura destrói o papel!")
elif sorteio == "papel" and lanceJog == "pedra":
    print("O PC venceu pois o papel enrola a pedra!")
elif sorteio == "tesoura" and lanceJog == "papel":
    print("O PC venceu pois a tesoura destrói o papel!")
elif sorteio == "tesoura" and lanceJog == "pedra":
    print("Você venceu pois a pedra destrói a tesoura!")
else:
    print("Vocês empataram!")