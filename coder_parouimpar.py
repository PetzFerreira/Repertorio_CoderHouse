import os
os.system('cls') #limpa a tela

numerodigitado = input('\nDigite um número inteiro qualquer para saber se ele é par ou ímpar: \n\n')

try: #tenta realizar a linha abaixo, conferindo se o valor digitado é inteiro, se não for, cai no except; caso seja, continua e entra no If
    numerodigitado = int(numerodigitado) #converte o valor digitado para um número inteiro caso seja possível
    if (numerodigitado %2 == 0): #divie o valor digitado por 2; se for par, qualquer número digitado por 2 terá, após a vírgula, apenas zeros. Se ímpar, terá "sobra" após a vírgula
        print(f'\nO número {numerodigitado} é um número par!\n')
    else:
        print(f'\nO número {numerodigitado} é um número ímpar!\n')
except:
    print(f'\n {numerodigitado} não é um número inteiro! Digite apenas números inteiros!\n')