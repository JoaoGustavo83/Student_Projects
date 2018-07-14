"""Programa importa math, lê o cateto oposto, o cateto
adjacente e calcula a hipotenusa e imprime"""

import math

catOposto = float(input("Digite o tamanho do cateto oposto: "))
catAdjacente = float(input("Digite o tamanho do cateto adjacente: "))
hipotenusa = math.hypot(catOposto,catAdjacente)
print ("A hipotenusa tem o comprimento de: {:.3f}.".format(hipotenusa))