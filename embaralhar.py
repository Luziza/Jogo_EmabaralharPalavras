import random



def Embaralhar(palavra):
    novo = list(palavra)
    random.shuffle(novo)
    novo = "".join(novo)
    print(novo.lower())

def Ajuda():
    lista = ["Você consegue", "Tente novamente", "A maior prova de coragem é suportar as derrotas sem perder o ânimo.", "Acredite que você pode, assim você já está no meio do caminho."]
    random.shuffle(lista)
    return lista[0]

    
palavra = "atumalaca"
Embaralhar(palavra)


for i in range(5):
    resposta =(input("Digite a resposta: "))
    if resposta == palavra:
        print("Acertou! Você utilizou " + str(i) + " tentivas")
        break
    elif resposta != palavra:
        print(Ajuda())
    if i == 4:
        print("A resposta certa era " + palavra)

