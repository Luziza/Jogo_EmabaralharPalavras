import random


def Embaralhar(palavra):
    novo = list(palavra)
    random.shuffle(novo)
    novo = "".join(novo)
    print(novo.lower())

    
palavra = "maluca"
Embaralhar(palavra)

resposta = print(input("Digite a resposta: "))

if resposta == Embaralhar(palavra):
    print("Acertou!")
elif resposta != Embaralhar(palavra):
    print("Tente novamente!")


