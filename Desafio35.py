"""Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem formar um triângulo."""

a = int(input("Digite o comprimento do lado A:"))
b = int(input("Digite o comprimento do lado B:"))
c = int(input("Digite o comprimento do lado C:"))

if (b - c) < a and a < (b + c):
    if (a - c) < b and b < (a + c):
        if (a - b) < c and c < (a + b):
            print("Com estas 3 retas podemos fazer um triângulo!")
        else:
            print("Não é possível fazer um triângulo com estas retas!")
    else:
        print("Não é possível fazer um triângulo com estas retas!")
else:
    print("Não é possível fazer um triângulo com estas retas!")

