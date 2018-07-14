"""Este programa lê um numero digitado e verifica se é par ou impar."""

num = int(input("Digite um número: "))

if num % 2 == 0:
    print("{} é par.".format(num))
else:
    print("{} é impar!".format(num))