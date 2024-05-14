import os
os.system('cls')
from geometria import Retangulo as rtg

base = float(input('\nDigite o valor referente à base do retângulo:\n'))
altura = float(input('\nDigite o valor referente à altura do retângulo:\n'))

retangulocriado = rtg(base, altura)
areadoretangulo = retangulocriado.area()
perimetroretangulo = retangulocriado.perimetro()

print(f'\nA área do retângulo de base {base} e altura {altura} é: {areadoretangulo}')
print(f'\nO perimetro do retângulo de base {base} e altura {altura} é: {perimetroretangulo}\n')