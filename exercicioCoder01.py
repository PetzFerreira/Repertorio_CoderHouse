''' 1. Crie uma variável chama saldo e atribua o valor de 950,60. Em seguida, pergunte ao usuário quanto dinheiro ele deseja sacar e armazene a resposta em uma variável
chamada saque. Subtraia o valor de saque do valor de saldo e imprima a mensagem "Seu novo saldo é {saldo}"'''

import os
os.system('cls')

saldo = 956.60
saque = 0

saque = float(input('Olá,\nQual o valor deseja sacar?:\n\n'))

saldo = saldo - saque

print(f'\nSeu novo saldo é {saldo:.2f}.\n')