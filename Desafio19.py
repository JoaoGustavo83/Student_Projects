"""Programa lê o nome de 4 alunos, e escolhe 1 aluno
 aleatoriamente e imprime."""
import random

aluno1 = input("Diga seu nome: ")
aluno2 = input("Diga seu nome: ")
aluno3 = input("Diga seu nome: ")
aluno4 = input("Diga seu nome: ")
alunos = [aluno1,aluno2,aluno3,aluno4]

print(random.choice(alunos))