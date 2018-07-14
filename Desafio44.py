preco = float(input("Digite o valor do produto: "))
condicaoPgto=int(input("Em quantas vezes deseja parcelar: "))
modalidade = str(input("Qual a forma de pagamento (dinheiro,cheque ou cartão): "))

if condicaoPgto == 1 and modalidade == "dinheiro" or modalidade == "cheque":
    preco = preco - (preco * (10/100))
    print ("Você teve um desconto de 10% e vai pagar apenas:{}.".format(preco))
elif condicaoPgto == 1 and modalidade == "cartão":
    preco = preco - (preco * (5/100))
    print("Você teve um desconto de 5% e vai pagar apenas:{}.".format(preco))
elif condicaoPgto == 2 and modalidade == "cartão":
    print("O preço normal do produto é: {}".format(preco))
elif condicaoPgto == 3 and modalidade == "cartão":
    preco = preco + (preco * (20/100))
    print("Você teve um juros de 20% e vai pagar o total de:{}.".format(preco))
