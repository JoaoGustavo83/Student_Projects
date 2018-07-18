# coding=utf-8
# 1 - Selecionar o nivel de dificuldade(facil, medio ou dificil):
# 2 - Mediante o nivel selecionado, o programa deve apresentar a frase e as
#  lacunas a serem preenchidas
# 3 - O jogo deve abrir espaço para o jogador preencher as lacunas e checar
#  se as respostas estão de acordo com as respostas e se errar deve pedir
#  para que tente novamente.

frase_facil = ["O principal tipo de documento da WEB: ___1___ .",
               "O principal protocolo da WEB: ___2___ .",
               "Os computadores que hospedam os arquivos: ___3___ .",
               "Um programa que executa em seu computador e exibe arquivos da WEB: chamado ___4___."]

frase_medio = ["O que significa HTML? ___1___ .",
               "A tag utilizada para incluir um link em um programa: ___2___ .",
               "A tag que utilizamos para separar frases em 2 linhas no lugar de uma linha contínua: ___3___ .",
               "Qual dos seguintes elementos não representa um elemento 'alinhado'(a,br,p,img)? ___4___."]

frase_dificil = ["Que linha inicial define o tipo de documento HTML? ___1___ .",
                 "Como se chamam os erros de programacao? ___2___ . ",
                 "O método utilizado para substituir uma string em uma variável é o ___3___ .",
                 "Que método é usado para encontrar uma string em uma lista? ___4___."]

resposta_facil =   ["html",                      "tcp/ip",      "servidores", "navegador"]
resposta_medio =   ["hypertext markup language", "<a href=''>", "</br>",      "p"]
resposta_dificil = ["<!doctype html>",           "bugs",        "replace",    "find"]

respostas = [resposta_facil, resposta_medio, resposta_dificil]
frases = [frase_facil, frase_medio, frase_dificil]
chances = [3, 2, 1]
niveis = ["facil", "medio", "dificil"]


def boas_vindas():
    """" Esta função lê o nome do jogador e imprime uma mensagem de boas-vindas. """
    name = raw_input("Olá jogador(a) qual é o seu nome?")
    print "Seja bem vindo {}. As regras são as seguintes: escolha o nível em que deseja jogar e tente acertar " \
          "as respostas das perguntas!".format(name)


def escolhe_nivel():
    """ método para usuário escolher o nível de dificuldade do jogo e retorna o nível e caso não digite ou digite
    algo fora das opções imprime erro e pergunta pelo nível novamente"""
    boas_vindas()
    while True:
        nivel = raw_input("Escolha em que nível quer jogar:facil,medio ou dificil?").lower()
        if nivel in niveis:
            return nivel
        else:
            print("Nível inválido!Tente de novo.")


def exibe_fase():
    """ este método exibe as frases correspondentes ao nível escolhido e retorna a frase , as respostas
     e as chances """
    nivel = escolhe_nivel()
    index = niveis.index(nivel)
    print("Você escolheu o nivel: " + nivel)
    # return frases[index], respostas[index], chances[index]
    jogo(frases[index], respostas[index], chances[index])


def jogo(frase, resposta, num_chances):
    '''agora sim imprimimos o numero de chances do usuário,imprimimos a frase que o usuario deve completar de acordo
    com o nível escolhido anteriormente, lemos as respostas do usuario. Se o usuario acerta a resposta passa para a
    proxima, se errar recebe mensagem de erro e tem nova chance se ainda houver chances.'''
    print("Você tem {} chances de acertar!".format(num_chances))
    indice = 0
    while num_chances > -1 and indice < len(frase):
        print frase[indice]
        palavra = raw_input("A resposta da lacuna ___{}___ é ? ".format(indice + 1)).lower()
        if palavra == resposta[indice]:
            frase[indice] = frase[indice].replace("___" + str(indice + 1) + "___", palavra)
            print("Você acertou! Veja como ficou a frase: ")
            print(frase[indice])
            indice += 1
        else:
            print("Resposta incorreta! Tente de novo!")
            print("Você tem {} chances de errar!".format(num_chances))
            num_chances -= 1


exibe_fase()