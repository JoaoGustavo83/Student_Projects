nota1 = float(input("Digite aqui a sua nota:"))
nota2 = float(input("Digite aqui a sua outra nota:"))

media = (nota1 + nota2) / 2

if media < 5.0:
    print("\033[1;31mREPROVADO\033[m")
elif media > 5.0 and media < 6.9:
    print("\033[1;32mRECUPERAÇÃO\033[m")
else:
    print("\033[1;34mAPROVADO!\033[m")
