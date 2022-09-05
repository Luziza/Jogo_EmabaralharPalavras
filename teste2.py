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

def Temas1():
    cores = ["vermelho", "amarelo", "azul"]

    if escolha == 'cores':
        novo1 = random.choice(cores)
        escolhido1 = list(novo1)
        random.shuffle(escolhido1)
        escolhido1 = "".join(escolhido1)
        print(escolhido1) 

def Temas2():
    paises = ["brasil", "japão", "chile"]

    if escolha == 'paises':
        novo = random.choice(paises)
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido)

    

    
    

    



Temas1()

Temas2()

Temas()



