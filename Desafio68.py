import random

i = 0
vitoriaJogador = 0

while i == 0:
    print("=== Vamos jogar par ou ímpar ===")
    jogador = int(input("Digite um valor:"))
    chance = str(input("Par ou ímpar [P/I]: "))
    computador = random.randint(0, 10)
    if (jogador + computador) % 2 == 0:
        if chance == "P":
            print("Você venceu!")
            vitoriaJogador += 1

        else:
            print("Você perdeu!")
            print(f"O número escolhido pelo computador foi {computador}:(")
            break

    else:
        if chance == "I":
            print("Você venceu!")
            vitoriaJogador += 1

        else:
            print("Você perdeu!")
            print(f"O número escolhido pelo computador foi {computador}:(")
            break

    print(f"O número escolhido pelo computador foi {computador}")
print(f"O seu número de vitórias foi de {vitoriaJogador} rodadas consecutivas.")
