from datetime import date

anoNascimento = int(input("Digite o ano de seu nascimento: "))

anoAtual = date.today()

tempoFalta = 18 - (anoAtual.year - anoNascimento)
tempoPassou = (anoAtual.year - anoNascimento) - 18

if anoAtual.year - anoNascimento < 18:
    print("Você ainda vai se alistar.")
    print("Faltam {}{} anos {} para seu alistamento".format("\033[1;34m",tempoFalta,"\033[m"))
elif anoAtual.year - anoNascimento > 18:
    print("Você já passou do tempo do alistamento")
    print("Você deveria ter se alistado há {}{} anos {}.".format("\033[1;31m",tempoPassou,"\033[m"))
else:
    print("\033[1;32mEsta é a hora de se alistar!\033[m")


