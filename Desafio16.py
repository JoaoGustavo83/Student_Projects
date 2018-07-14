"""Programa importa a função math,lê um número e imprime o
 número sem as casas decimais"""

import math
num = float(input("Digite um número: "))
print(math.trunc(num))