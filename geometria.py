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