num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O número {} é maior que {}.".format(num1,num2))
elif num1 < num2:
    print("O número {} é maior que {}.".format(num2,num1))
else:
    print("Não existe valor maior.Os dois são iguais!")