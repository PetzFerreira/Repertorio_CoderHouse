from os import system as sy 
sy('cls') #Limpa a tela
from datetime import datetime

dia = input('Digite o dia da data que deseja (2 digitos): \n')
mes = input('\nDigite o mês (2 dígitos): \n')
ano = input('\nDigite o ano (4 dígitos): \n')

datadigitada = dia+'/'+mes+'/'+ano #concatena as datas digitadas pelo usuário

def formatardata(data): #função que recebe uma variável como parâmetro, converte em objeto de data utilizando a variável como base, depois formata para apresentar somente o dia da semana
    data_obj = datetime.strptime(data, '%d/%m/%Y')
    
    datareformada = data_obj.strftime('%A')
    
    return datareformada
    
    
print(f'\n{formatardata(datadigitada)}')