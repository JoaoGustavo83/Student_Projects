"""Faça um programa que leia um número qualquer e mostre o seu
fatorial"""

"""from math import factorial

numero = int(input("Digite um número:"))
f = factorial(numero)
print("O fatorial de {}".format(f))"""
from math import factorial

n = int(input("Digite o numero para calcular fatorial:"))
c = n
f = 1
while c > 0:
    print("{} ".format(c),end="")
    print("x " if c > 1 else "=",end="")
    f = f * c
    c = c - 1
print(" {}".format(f))








