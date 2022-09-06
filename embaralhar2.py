import random

escolha = input("Escolha o tema: ")

def Temas(escolha):
    cidade = ["joinville", "araquari", "natal"]
    cores = ["vermelho", "amarelo", "azul"]
    paises = ["brasil", "japão", "chile"]

    

    if escolha == 'cidade':
        novo = random.choice(cidade)
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido)
        return novo

    elif escolha == 'paises':
        novo = random.choice(paises)
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido) 
        return novo

    elif escolha == 'cores':
        novo = random.choice(cores)
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido) 
        return novo

palavra = Temas(escolha)

def Ajuda():
    lista = ["Você consegue", "Tente novamente", "A maior prova de coragem é suportar as derrotas sem perder o ânimo.", "Acredite que você pode, assim você já está no meio do caminho."]
    random.shuffle(lista)
    return lista[0]

for i in range(5):
    resposta = input("Digite a resposta: ")
    if resposta == palavra:
        print("Acertou! Você utilizou " + str(i) + " tentivas")
        break
    elif resposta != palavra:
        print(Ajuda())
    if i == 4:
        print("A resposta certa era " + palavra)





