import random


def Embaralhar(palavra):
    novo = list(palavra)
    random.shuffle(novo)
    novo = "".join(novo)
    print(novo.lower())

    
palavra = "atumalaca"
Embaralhar(palavra)




for i in range(5):
    resposta =(input("Digite a resposta: "))
    if resposta == palavra:
        print("Acertou!")
        break
    elif resposta != palavra:
        print("Tente novamente!")
    if i == 4:
        print("A resposta certa era " + palavra)



