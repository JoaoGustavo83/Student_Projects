"""Este programa deve ler um ano digitado e dizer se ele é bissexto ou não."""

ano = int(input("Digite um ano qualquer com 4 digitos: "))

if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print("O ano {} é bissexto.".format(ano))
        else:
            print("O ano {} não é bissexto.".format(ano))
    else:
        print("O ano {} é bissexto.".format(ano))
else:
    print("O ano {} não é bissexto.".format(ano))