"""Melhore o jogo desafio 28 onde o computador vai "pensar
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites
forem necessários para vencer."""
import random

count = 0
palpite = 1
while palpite < 11:
    numero = random.randint(0, 10)
    palpite = int(input("Digite um número de 0 a 10:"))
    if palpite == numero:
        print("\033[32mParabéns! Você venceu!\033[m")
        print("O número era: {} ".format(numero))
        palpite = 11
    else:
        print("\033[30mVocê perdeu!\033[m")
        print("O número era: {} ".format(numero))
        count = count + 1
print("Você precisou de {} tentativas!".format(count + 1))