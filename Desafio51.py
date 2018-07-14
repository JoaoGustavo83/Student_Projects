"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final,mostre os 10 primeiros termos desta progressão."""

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

n = 0
for n in range(0,11):
    termo = termo + razao
    print(termo)
