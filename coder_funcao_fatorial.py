import os
os.system('cls') #limpa a tela

numerofornecido = int(input('\nDigite um número qualquer para calcular seu fatorial:\n\n ')) 

def calcularFatorial(n): #função que recebe um número inteiro, caso esse número seja 0, retorna 1 pois 0! é 1; se não, entra em um looping For que para cada vez que passar pelo laço,
                         #soma o fatorial em +1 e multipla esse valor pelo resultado anterior, até chegar no valor digitado pelo usuário 
    if n == 0:
        return 1
    fatorial = 1
    for i in range(1, n+1):
        fatorial =  fatorial * i
    return fatorial
 
numerofatorial = calcularFatorial(numerofornecido) #variável que guarda o resultado do cálculo do fatorial pela função
print(f'\nO número {numerofornecido} equivale à {numerofatorial} após ter seu fatorial calculado.\n') #imprime o valor calculado
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 