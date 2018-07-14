"""Programa lê um número de 0 a 9999, e mostra a unidade
,dezena,centena e milhar"""

numero = input("Digite um numero de 0 a 9999: ")

print("unidade: " + numero[3])
print("dezena: " + numero[2])
print("centena: " + numero[1])
print("milhar: " + numero[0])