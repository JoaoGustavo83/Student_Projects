"""programa lê o nome do usuário, lê duas notas
calcula a média e a imprime."""

aluno = input("Digite seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
mediaArit = (n1 + n2) / 2
print("A média do aluno {} é {:.2f}".format(aluno,mediaArit))