"""programa lê a cidade que o usuário digita e imprime
se há ou nao Santo na cidade digitada"""

cidade = input("Digite sua cidade: ").upper()

print(cidade.startswith("SANTO"))