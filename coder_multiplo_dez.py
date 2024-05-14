from os import system as sy 
sy('cls') #Limpa a tela

eh_multiplo_dez = lambda x: (x % 10) == 0 #Divide x por 10, se sobrar 0, é par, se não, é impar (Sobra = valor depois da vírgula)
numerodigitado = float(input('\nDigite um número qualquer para saber se ele é múltiplo de 10!: \n\n')) #solicita um número qualquer, podendo ser float, como entrada
resultado = eh_multiplo_dez(numerodigitado) #usa a função com o valor digitado
print (resultado)