"""Programa lê o salário,calcula um aumento de 15% e imprime
o total."""


salario = float(input("Digite seu salário: "))
aumento = salario * (15/100)
novoSalario = salario + aumento
print("Seu novo salário após o aumento de {:.2f}, será de {:.2f}".format(aumento,novoSalario))