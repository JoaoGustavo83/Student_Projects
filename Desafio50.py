"""Desenvolva programa que leia 6 números inteiros e mostre a soma apenas
daqueles que forem pares.Se o valor digitado for ímpar, desconsidere-o."""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))
numero6 = int(input("Digite o sexto número: "))
maior = max(numero1, numero2, numero3, numero4, numero5, numero6)
menor = min(numero1, numero2, numero3, numero4, numero5, numero6)

s = 0
for n in range(menor, maior+1):
    if n % 2 == 0:
        s = s + n
print(s)
