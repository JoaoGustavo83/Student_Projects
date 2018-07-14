"""Faça um programa que leia o salário e diga o aumento que o funcionário terá. Se o salário for maior que 1250
o aumento será de 10%, caso seja menor será de 15%"""

salario = int(input("Digite seu salário: "))

if salario > 1250:
    aumento = salario * 10 / 100
    print("Seu aumento será de: {}".format(aumento))
else:
    aumento = salario * 15 / 100
    print("Seu aumento será de:{}".format(aumento))