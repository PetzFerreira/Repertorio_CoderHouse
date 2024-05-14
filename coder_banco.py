from os import system as sy
sy('cls')

class Conta:
    def __init__ (self, titular, saldo):
        self.saldo = saldo
        self.titular = titular
    def sacar (self,valordosaque):
        self.saldo = self.saldo - valordosaque
        return self.saldo
    def depositar (self, valordedeposito):
        self.saldo = self.saldo + valordedeposito
        return self.saldo
    
usuariotitular = input('Olá,\nParabéns pela aprovação da sua nova conta!\nMe diga o seu nome completo ou como deseja ser chamado:\n')
saldotitular = 600
contadousuario = Conta(usuariotitular,saldotitular)
sy('cls')
print(f'É um prazer {usuariotitular}!\nSeu saldo inicial de R$600,00 já está disponível para uso.')


while True:
            opcaousaurio = input('Digite 1 para sacar, 2 para depositar ou 0 para finalizar a operação:\n')
            
            if opcaousaurio == '0':
                sy('cls')
                print('Operação finalizada!')
                break
                
            if (opcaousaurio == '1'):
                sy('cls')
                print(f'Saldo atual: {contadousuario.saldo} R$.')
                valordesaque = float(input("Digite o valor (R$) que deseja sacar:\n"))
                if (valordesaque >= 0.01) and (valordesaque <= contadousuario.saldo):
                    contadousuario.sacar(valordesaque)
                    sy('cls')
                    print(f'Valor sacado: {valordesaque} R$\nNovo saldo: {contadousuario.saldo} R$')
                elif valordesaque <= 0.01:
                    sy('cls')
                    print("O valor mínimo de saque é R$ 0,01 R$.\n")    
                else:
                    sy('cls')
                    print(f'Saldo insuficiente! Saldo disponível: {contadousuario.saldo} R$')
            
            if opcaousaurio == '2':
                sy('cls')
                valordedeposito = float(input("Digite o valor (R$) que deseja depositar:\n"))
                if (valordedeposito > 0.01):
                    contadousuario.depositar(valordedeposito)
                    sy('cls')
                    print(f'Valor depositado: {valordedeposito} R$\nNovo saldo: {contadousuario.saldo} R$.')
                else:
                    sy('cls')
                    print('O valor mínimo para depósito é de 0,01 R$.\n')