from os import system as sy 
sy('cls') #Limpa a tela

numerofornecido = int(input('\nDigite um número qualquer para calcular seu fatorial:\n\n ')) #Solicita um número inteiro como entrada
fatorial = 1
resultadofatorial = 1
while fatorial <= numerofornecido: #Até o fatorial ser o mesmo número que o fornecido, ficará no lopping 
    resultadofatorial = fatorial*(resultadofatorial) # fotorial vezes o resultado da multiplicação anterior, após acrescentar 1 ao fatorial na linha seguinte (1*2, 2*3, 6*4...)
    fatorial = fatorial +1

print (resultadofatorial)
    