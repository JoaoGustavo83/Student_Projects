"""A Confederação Brasileira de Natação precisa
"""

from datetime import date

anoNascimento = int(input("Digite o ano de nascimento: "))

anoHoje = date.today()

idade = anoHoje.year - anoNascimento

if idade < 9:
    print("\033[1;34mMIRIM\033[m")
elif 9 <= idade < 14:
    print("\033[1;34mINFANTIL\033[m")
elif 14 <= idade < 19:
    print("\033[1;34mJUNIOR\033[m")
elif 19 <= idade < 20:
    print("\033[1;34mSENIOR\033[m")
else:
    print("\033[1;34mMASTER\033[m")
