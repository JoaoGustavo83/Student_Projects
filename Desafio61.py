"""Refaça o desadio 51, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while"""

"""termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

n = 0
for n in range(0,11):
    termo = termo + razao
    print(termo)"""

termo = int(input("Digite o primeiro termo da PA: "))

razao = int(input("Digite a razão da PA: "))
print(termo)
n = 1
while n < 10:
    termo = termo * razao
    print (termo)
    n += 1
