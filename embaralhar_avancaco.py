import random

def Temas():
    cidade = ["joinville", "araquari", "natal"]
    cores = ["vermelho", "amarelo", "azul"]
    paises = ["brasil", "japão", "chile"]

    escolha = input("Escolha o tema: ")

    if escolha == cidade:
        escolhido = list(cidade[0])
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido)
    elif escolha == cores:
        escolhido = list(cores[0])
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido.lower())
    elif escolha == paises:
        escolhido = list(paises[0])
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido.lower())


def Ajuda():
    lista = ["Você consegue", "Tente novamente", "A maior prova de coragem é suportar as derrotas sem perder o ânimo.", "Acredite que você pode, assim você já está no meio do caminho."]
    random.shuffle(lista)
    return lista[0]

Temas()


for i in range(5):
    resposta =(input("Digite a resposta: "))
    if resposta == Temas():
        print("Acertou! Você utilizou " + str(i) + " tentivas")
        break
    elif resposta != Temas():
        print(Ajuda())
    if i == 4:
        print("A resposta certa era " + Temas())

