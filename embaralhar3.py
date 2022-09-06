import random

escolha = input("Escolha o tema: ")
dificuldade = input("Escolha dificuldade facil, intermediario ou dificil: ")



def Temas(escolha, dificuldade):
    cidade = ["Natal", "Joinville", "São José do Vale do Rio Preto"]
    cores = ["vermelho", "amarelo", "azul"]
    paises = ["brasil", "japão", "chile"]

    

    if escolha == 'cidade' and dificuldade == 'facil':
        novo = cidade[0]
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido)
        return novo

    elif escolha == 'cidade' and dificuldade == 'intermediario':
        novo = cidade[1]
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido)
        return novo

    elif escolha == 'paises' and dificuldade == 'facil':
        novo = paises[0]
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido) 
        return novo
    
    elif escolha == 'paises' and dificuldade == 'facil':
        novo = paises[1]
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido) 
        return novo

    elif escolha == 'cores' and dificuldade == 'fácil':
        novo = cores[0]
        escolhido = list(novo)
        random.shuffle(escolhido)
        escolhido = "".join(escolhido)
        print(escolhido) 
        return novo

palavra = Temas(escolha, dificuldade)

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





