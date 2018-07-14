"""Crie um programa que leia uma frase qualquer e diga se ela é
um palíndromo desconsiderando os espaços."""

frase = str(input("Digite uma frase: ")).lower()#linha para ler frase e transformar caracteres em minúsculos.
frasesEspacos = frase.replace(" ","")#linha para remover os espaços entre as palavras da string
print(frase)
print(frasesEspacos)

if frasesEspacos == frasesEspacos[::-1]:
    print("Sua frase é um palíndromo")
else:
    print("Sua frase não é um palíndromo.")
print(frase[::-1])