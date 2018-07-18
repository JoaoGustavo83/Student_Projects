"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos"""

countIdade = 0
countSexo = 0
countMabaixo20 = 0

while True:
    idade = int(input("Qual é a sua idade?"))
    #Para limitar a digitacao do usuario em M/F vamos escrever
    #as 2 linhas abaixo:"""
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual é o seu sexo [M/F]:")).strip().upper()[0]
    if idade >= 18:
        countIdade += 1
    if sexo == "M":
        countSexo += 1
    if sexo == "F" and idade < 20:
        countMabaixo20 +=1
    #Para limitar a digitacao do usuario em S/N vamos escrever
    #as 2 linhas abaixo:"""
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Deseja continuar o cadastramento [S/N]:")).strip().upper()[0]
    if opcao == "N":
        break
print(f"Os maiores de 18 anos cadastrados são {countIdade}.")
print(f"Dos cadastrados {countSexo} são homens.")
print(f"Dos cadastrados {countMabaixo20} são mulheres com menos de 20 anos")
