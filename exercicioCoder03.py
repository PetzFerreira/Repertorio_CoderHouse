'''3. Faça um programa que peça ao usuário para digitar uma frase e substitua todas as vogais por asteriscos(*)'''

import os
os.system('cls')


def trocarPorVogais(string):
    
    vogais = ['a', 'e', 'i', 'o', 'u']
    for vogal in vogais:
        string = string.replace(vogal, '*')
    return string

textodousuario = input('\nDigite uma frase qualquer: \n')
textodousuario = trocarPorVogais(textodousuario)

print (f'\n{textodousuario}\n')