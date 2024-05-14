import os
os.system('cls') #limpa a tela

chavedemeses = {'janeiro':232, 'feveiro':321, 'junho':589, 'julho':547} # dicinário com meses e seus valores de quantidade

entradausuario =input('Digite o mês que deseja saber a quantidade ou 0 para finalizar o programa:\n ')

while (entradausuario != 0): #enquanto a entrada do usuário não for "O", realiza a função. Ao digitar 0, o programa finaliza
    if (entradausuario.lower() in chavedemeses): #converte a string do usuario em letras pequenas para evitar erros; se a entrada se encontrar no dicionário, imprimi o mês e a quantidade
        print(f'\nNo mês de {entradausuario} a quantidade foi de {chavedemeses[entradausuario]}\n')
    else: # se não, imprimi que não há dados a serem apresentados.
        print(f'\nNão há dados para o mês solicitado.\n')
    entradausuario =input('Digite o mês que deseja saber a quantidade ou 0 para finalizar o programa: \n')