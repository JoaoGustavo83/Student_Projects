from datetime import date

hj = date.today()
print(hj)
ano = hj.year

contaMenores = 0
contaMaiores = 0

for n in range(0,7):
    nascimento = int(input("Digite seu ano de nascimento:"))
    if ano - nascimento < 18:
        print("Você é menor de idade!")
        contaMenores = contaMenores + 1
    else:
        print("Você é maior de idade!")
        contaMaiores = contaMaiores + 1
print("Os menores de idade são: {}".format(contaMenores))
print("Os maiores de idade são: {}".format(contaMaiores))



#contaMenores = 0
#contaMaiores = 0

#for n in range(0,6):
