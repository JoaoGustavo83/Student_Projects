"""Programa lê um número e mostra o dobro,triplo e
raiz quadrada dele."""

n1 = int(input("Digite um número:"))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
print("O número {} tem o dobro de {}, o triplo {} e \n a raiz quadrada {}".format(n1,dobro,triplo,raiz))