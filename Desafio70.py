"""Crie um prog. que leia o nome e o preço de vários produtos
.O prog. deverá perguntar se o usuário vai continuar. No final mostra:
a)Total gasto na compra
b)Quantos produtos custam mais de R$1000
c)Qual é o nome do produto mais barato"""

total = 0
maisMil = 0
menor = 0
cont = 0
barato = 0
print("$$$ LOJA SUPER BARATÃO $$$")

while True:
    produto = str(input("Digite qual produto deseja comprar: "))
    preco = float(input("Digite o preço do produto: "))
    cont +=1
    total += preco
    if preco > 1000:
        maisMil = maisMil + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Deseja continuar suas compras [S/N]:")).strip().upper()[0]
    if opcao == "N":
        break
print("FIM DO PROGRAMA")
print(f"O total gasto em suas compras foi de {total}")
print(f"Nas suas compras,{maisMil} produtos custam mais de R$1000")
print(f"O produto mais barato em sua lista é o {barato}")
