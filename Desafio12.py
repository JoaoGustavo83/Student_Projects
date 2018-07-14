"""Programa lê o preço do produto, calcula desconto e o novo
preço e imprime os valores"""

preco = float(input("Digite o preço do produto: "))
desconto = preco * (5/100)
novoPreco = preco - desconto
print("Já que o preço do produto é de {} e concedemos um desconto de {}, o novo preço a ser cobrado é de {}".format(preco,desconto,novoPreco))
