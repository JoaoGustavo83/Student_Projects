"""Programa lê um valor e converte para dolar e imprime."""

valor = float(input("Digite o quanto você tem: "))
convDolar = valor / 4.27
print("Seu valor de {} convertido em dólar é {:.2f}".format(valor,convDolar))