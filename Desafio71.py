"""Crie um prog. que simule um caixa eletronico. No início pergunte
ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de 50,20,10 e 1."""

print("**** BEM VINDO AO BANCO CASH ****")
valor = int(input("Prezado cliente, favor insira o valor desejado: "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        print(f"Total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("Volte sempre ao BANCO CASH")






