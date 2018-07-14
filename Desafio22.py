"""Programa lê o nome, e imprime o nome em maiuscula
,minúscula, conta o número de caracteres diferentes
de espaço e digita o primeiro nome"""

nome = input("Digite seu nome: ")

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(" "))

nomeDiv = nome.split()
print(nomeDiv[0])
