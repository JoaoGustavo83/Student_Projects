"""programa pede que o usuário digite algo, imprime,
 diz se é alfabético, numérico,decimal ou minúsculo."""
algo =input("Digite algo:")
print(type(algo))
print(algo.isalpha())
print(algo.isnumeric())
print(algo.isdecimal())
print(algo.islower())
