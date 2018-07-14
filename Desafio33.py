"""Faça um programa que leia 3 numeros e mostre o maior e o menor número"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print("O maior número é {}.".format(int(max(num1,num2,num3))))
print("O menor número é {}.".format(int(min(num1,num2,num3))))