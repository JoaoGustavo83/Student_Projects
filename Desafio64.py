count = 0
soma = 0
inteiro = ""
while inteiro != 999:
    inteiro = int(input("Digite um número inteiro:"))
    soma = soma + inteiro
    count = count + 1
print("Você digitou {} números.".format(count - 1))
print(" A soma dos números digitados {}".format(soma - inteiro))

