"""Programa importa math para ler ângulo e calcular seno,
cosseno e tangente.No final imprime."""
import math
#Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno,cosseno e tangente deste triângulo.
angulo = float(input("Digite o ângulo do triângulo: "))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print("Considerando o ângulo de {}, temos o seno de {}, o cosseno de {} e a tangente {}.".format(angulo,seno,cosseno,tangente))