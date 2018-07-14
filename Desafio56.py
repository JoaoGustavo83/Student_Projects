"""Programa lê nome,idade e sexo de 4 pessoas- No final do
programa mostra: A media de idade do grupo, qual é o nome do
mais velho e quantas mulheres com menos de 20 anos."""
somaIdade = 0
maiorIdade = 0
nomeVelho = ""
totMulher20 = 0

for p in range(1,5):
    print("==== {} PESSOA ====".format(p))
    nome = str(input("Nome:")).strip()
    idade = int(input("Idade:"))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaIdade = somaIdade + idade
    if p == 1 and sexo in "Mm":
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in "Mm" and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in "Ff" and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade/4
print("A média de idade do grupo é de {}".format(mediaIdade))
print("O homem mais velho tem {} e se chama {}".format(maioridadeHomem,nomeVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totMulher20))