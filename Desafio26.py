"""O programa identifica quantas vezes a string "a" aparece na frase escrita pelo usuário e localiza a
 primeira posição em que aparece"""
frase = input("Digite alguma coisa: ").lower()

print(frase.count("a"))
print(frase.find("a"))