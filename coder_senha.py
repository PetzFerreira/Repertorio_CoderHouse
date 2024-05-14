import os
os.system ('cls')


senhadousuario = 1234 #senha solicitada, fixa
senhasolicitada = 0000 

while (senhasolicitada != senhadousuario): #enquanto as senhas forem diferentes, permanece no laço
    senhasolicitada = int(input('Digite a senha de 4 dígitos: \n\n')) #solicita que o usuário digite um valor, sendo 4 número, apenas inteiros
    if (senhasolicitada != senhadousuario): # se a senha digitada for incorreta, avisa o usuário e solicita novamente
        print('\nSenha Incorreta!\n')
    
    else: 
        os.system ('cls')
        print('Senha correta!\nFim de Programa!\n') #se for igual, digita que é correta
        
    