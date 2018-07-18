"""Melhore o desafio 61 perguntando se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que
quer mostrar 0 termos"""

termo1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = termo1
print(termo)
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo = termo + razao
        print(termo)
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais?"))
print("PA finalizada com {} termos mostrados".format(total))
