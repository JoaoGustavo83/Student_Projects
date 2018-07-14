"""Faça um programa que leia o peso de cinco pessoas.No final
mostre qual foi o maior e menor peso lidos."""
pesos = []

for n in range(0,5):
    peso = float(input("Digite seu peso: "))
    pesos.append(peso)
print("O maior peso digitado foi {} kg".format(max(pesos)))
print("O menor peso digitado foi {} kg".format(min(pesos)))