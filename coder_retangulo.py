import os
os.system('cls') #Limpa a tela

class Retangulo: #Cria classe Retangulo, que cria um objeto que recebe base e altura
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura
        
    def area(self): #Método para calcular a area do objeto
        area = self.base*self.altura
        return area
        
    def perimetro(self): #Método que calcula o perímetro do objeto
        perimetro = (self.base*2)+(self.altura*2)
        return perimetro
        
basedigita = float(input ('Dite o valor da base:\n')) #Recebe valor da base
ladodigitado = float(input ('Digite o valor referente à altura:\n')) #Recebe valor da altura

retangulo = Retangulo(basedigita,ladodigitado) #cria um Objeto Retangulo e o nomeia de retangulo; os parâmetros são os digitados na Entrada do Usuário
areadoretangulo = retangulo.area() #Aplica função area no objeto criado
perimetroretangulo = retangulo.perimetro() #Aplica função perímetro no objeto criado

print(f'\nArea: {areadoretangulo}')
print(f'Perímetro: {perimetroretangulo}\n')