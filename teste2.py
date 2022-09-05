import random

escolha = input("Escolha o tema: ")

def Temas():
    cidade = ["joinville", "araquari", "natal"]
    if escolha == 'cidade':
        novo = random.choice(cidade)
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido)


    for i in range(5):
        resposta =(input("Digite a resposta: "))
        if resposta == novo:
            print("Acertou")
            break

def Temas1():
    cores = ["vermelho", "amarelo", "azul"]

    if escolha == 'cores':
        novo1 = random.choice(cores)
        escolhido1 = list(novo1)
        random.shuffle(escolhido1)
        escolhido1 = "".join(escolhido1)
        print(escolhido1) 

    for i in range(5):
        resposta1 =(input("Digite a resposta: "))
        if resposta1 == novo1:
            print("Acertou")
            break

def Temas2():
    paises = ["brasil", "japão", "chile"]

    if escolha == 'paises':
        novo2 = random.choice(paises)
        escolhido2 = list(novo2)
        random.shuffle(escolhido2)
        escolhido2 = "".join(escolhido2)
        print(escolhido2)

    


Temas1()

Temas2()

Temas()



