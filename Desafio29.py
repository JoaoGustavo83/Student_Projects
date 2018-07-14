"""Este programa lê a velocidade de um veículo e calcula a multa sobre os km se o veiculo ultrapassar os 80 km"""

velocidade = int(input("Qual a velocidade do veículo: "))
multa = int(velocidade - 80) * 7.00

if velocidade > 80:
    print("Você foi multado em {:.2f}".format(multa))
else:
    print("Parabéns! Você respeitou a velocidade!")