"""Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será
a base de conversão."""

numero = int(input("Digite um número:"))

print("Escolha uma base para conversão:")
print("[1] BINÁRIO")
print("[2] OCTAL")
print("[3] HEXADECIMAL")

opcao = int(input("Digite sua opção: "))

if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(numero,bin(numero)))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(numero,oct(numero)))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(numero, hex(numero)))
else:
    print("Opção inválida!")