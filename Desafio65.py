r = ""
soma = 0
lista = []
while r != "Não":
    n = int(input("Digite número inteiro:"))
    soma = soma + n
    lista.append(n)
    r = input("Deseja continuar inserindo valores?[Sim/Não]")
media = soma / len(lista)
print("A média de todos os valores digitados é {} !".format(media))
print("O maior valor digitado foi:{}{}{}".format("\033[1;33m",max(lista),"\033[m"))
print("O menor valor digitado foi: {}".format(min(lista)))
