import os
os.system('cls') #limpa a tela

frasedigitada = input('\nDigite uma frase qualquer: \n\n')

palavras = frasedigitada.split() #transforma a frase uma lista, onde cada elemento da frase dividido com espaço ocupa um index da lista

for palavra in palavras: # para cada elemento da lista, imprime o elemento e depois quantas letras possui
    print(f'\n{palavra}\b')
    print (len(f'\n{palavra}\n'))