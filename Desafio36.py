valorCasa = float(input("Qual é o valor da casa?"))

salario = float(input("Digite o seu \033[1;33msalário mensal\033[m: "))

prazo = float(input("Em quantos meses será o pagamento?"))

prestacaoMaxima = salario * (30/100)
prestacaoEmprestimo = valorCasa / prazo

if prestacaoEmprestimo < prestacaoMaxima:
    print("Seu empréstimo será \033[1;34maprovado\033[m!")
    print("A prestação mensal será de:{:.2f}".format(prestacaoEmprestimo))
else:
    print("Seu empréstimo será \033[1;31mrejeitado!\033[m")
    print("A prestação mensal seria de:{:.2f}".format(prestacaoEmprestimo))
