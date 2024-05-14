from os import system as sy 
sy('cls') #Limpa a tela

primeiro_nome = lambda string: string.split() #cria a função lambda utilizando split() para transformar o nomecompleto em uma lista; cada index é um nome/sobrenome
nomecompleto = input('\nDigite um nome completo, separando o nome e, cada sobrenome, apenas por espaços: \n\n')
primeironome = primeiro_nome(nomecompleto) #usando a função com a String de entrada
print(f'\n{primeironome[0]}') #imprime o primeiro elemento da lista

listadestrings = ['João Carlos', 'Maria Eduarda','Ana Rute', 'Ana Clara']
listadenomes = map(primeiro_nome, listadestrings) #Aplica a função primeiro_nome a lista com nomes

for nome in listadenomes: #para cada elemento das listas criadas por map, vai imprimir a string na primeira posição
    print(nome[0])