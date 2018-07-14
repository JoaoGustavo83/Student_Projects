"""Este programa calcula o preço da passagem. Caso a viagem tenha mais de 200 km o valor é 0.45 por km, caso tenha
menos o valor é de 0.50 por km."""

distancia = int(input("Qual é a distância da viagem: "))

if distancia <= 200:
    passagem = distancia * 0.50
    print("O preço da passagem é {}{}{}".format("\033[1;41m",passagem,"\033[m"))
else:
    passagem = distancia * 0.45
    print("O preço da passagem é {}.".format(passagem))