"""Programa lê 4 nomes e sorteia a ordem de apresentação
e imprime"""

import random

aluno1 = input("Diga seu nome: ")
aluno2 = input("Diga seu nome: ")
aluno3 = input("Diga seu nome: ")
aluno4 = input("Diga seu nome: ")
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print("A apresentação seguirá a seguinte ordem: ")
print(alunos)