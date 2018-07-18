"""Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.O programa
será interrompido quando o número solicitado for negativo."""

count = 0
i = 0


while count < 10:
    i = int(input("Quer ver a tabuada de que valor?"))
    n = 0
    if i < 0:
        break
    while n < 11:
        print(f"{i} vezes {n} = {i * n}")
        n +=1
    count +=1
print("Tabuada encerrada. Volte sempre!")
