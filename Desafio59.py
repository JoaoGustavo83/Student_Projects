"""Crie um programa que leia 2 valores e mostre um menu na tela: [1]somar,[2]multiplicar,[3]maior,[4]novos números,
[5]sair do programa. Seu programa deverá realizar a operação solicitada em cada caso."""

n = 1
print("==== MENU ====")
print("[1]Somar")
print("[2]Multiplicar")
print("[3]Maior")
print("[4]Novos Números")
print("[5]Sair do Programa")

while n != 0:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número:"))
    opcao = int(input("Escolha uma opção: "))
    soma = numero1 + numero2
    multi = numero1 * numero2
    if opcao == 1:
        print(" A soma é : {}".format(soma))
    elif opcao == 2:
        print("A multiplicação é: {}".format(multi))
    elif opcao == 3:
        print("O maior número digitado é {}".format(max(numero1,numero2)))
    elif opcao == 4:
        print("Você poderá digitar novos números. ")
    elif opcao == 5:
        print("O programa será encerrado!")
        n = 0


