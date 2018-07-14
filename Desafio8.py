"""Programa lê a metragem, converte a mesma para centímetros
e milímetros e imprime."""

metragem = int(input("Digite a metragem: "))
convCent = metragem * 100
convMil = metragem * 1000
print("A metragem {} metros convertida em centimetros resulta em {} centimetros e em milímetros {} milímetros.".format(metragem,convCent,convMil))