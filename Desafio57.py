"""Faça um programa que leia o sexo de uma pessoa, mas só
aceite os valores M ou F. Caso esteja errado peça a digitação
novamente até ter um valor correto"""
sexo = 1
while sexo != 0:
    sexo = str(input("Digite seu sexo [M/F]: ")).upper()
    if sexo == "M":
        print("Você é do sexo masculino!")
        sexo = 0
    elif sexo == "F":
        print("Você é do sexo feminino!")
        sexo = 0

