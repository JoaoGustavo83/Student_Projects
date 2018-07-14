"""Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo."""

num = int(input("Digite um número: "))

for n in range(1, 10):
    if num % n == 0:
        if n != 1:
            if n != num:
                print("O número não é primo!")
            else:
                print("Não é primo")





