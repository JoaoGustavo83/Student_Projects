"""Programa lê largura, altura, calcula área e calcula o
quanto de tinta será necessária para pintar a área"""

larg = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
areaParede = larg * altura
tinta = int(areaParede / 2)

print("Já que sua parede tem a largura de {}, a altura de {}, sua área é de {} e serão necessárias {} latas de tintas".format(larg,altura,areaParede,tinta))