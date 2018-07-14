"""Refaça o desafio 009 mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for."""

num = int(input("Digite um número: "))

for n in range(0,11):
    print("{} * {} = {}".format(num,n,n * num))
print("FIM")