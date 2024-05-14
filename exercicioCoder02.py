'''2. Faça um programa que crie uma lista com 5 frutas e permita que o usuário digite o nome de uma fruta. Se for uma fruta repetida deverá ser desconsiderada.'''

import os
os.system('cls')

listaDeFrutas = ['pera','banana', 'uva', 'kiwi', 'goiaba']

frutaDoUsuario = input(str('\nEscolha uma fruta e digite o nome dela para conferir se ela já está no cesto: \n\n'))


if (frutaDoUsuario in listaDeFrutas):
    print(f'A fruta {frutaDoUsuario} já está no cesto!')
else:
    opcaoDoUsuario = int(input(f'A fruta {frutaDoUsuario} ainda não está no cesto! Se deseja adicioná-la no cesto, digite 1, se não, digite 2.'))
    if (opcaoDoUsuario == 1):
        listaDeFrutas.append(frutaDoUsuario)
        print('Agora a fruta escolhida agora também está no cesto!')
        print(listaDeFrutas)
    elif (opcaoDoUsuario ==2):
        print('Ok! As frutas no cesto continuam as mesmas!')
    else:
        print('Opção inválida!.Digite apenas 1 para adicionar a fruta ao cesto ou 2 para desconsiderar a ação!')   