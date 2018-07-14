"""Programa lê o nome e imprime o primeiro e ultimo nomes."""

nome = str(input("Digite seu nome completo: ")).strip()
nomeSplit = nome.split()

print("Seu primeiro nome é {}{}{}".format("\033[4;36m",nomeSplit[0],"\033[m"))
print("Seu ultimo nome é: {}{}{}".format("\033[1;33m",nomeSplit[len(nomeSplit)-1],"\033[m"))



