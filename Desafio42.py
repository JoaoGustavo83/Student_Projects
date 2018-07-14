a = int(input("Digite o comprimento do lado A:"))
b = int(input("Digite o comprimento do lado B:"))
c = int(input("Digite o comprimento do lado C:"))

if (b - c) < a and a < (b + c):
    if (a - c) < b and b < (a + c):
        if (a - b) < c and c < (a + b):
            print("Com estas 3 retas podemos fazer um triângulo!")
            if a == b and b == c:
                print("O triângulo será EQUILÁTERO")
            elif a == b or b == c or a == c:
                print("O triângulo será ISÓSCELES")
            else:
                print("O triângulo será ESCALENO")
        else:
            print("Não é possível fazer um triângulo com estas retas!")
    else:
        print("Não é possível fazer um triângulo com estas retas!")
else:
    print("Não é possível fazer um triângulo com estas retas!")