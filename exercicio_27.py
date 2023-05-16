""" import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f"O Ângulo de {angulo} tem o Seno de {seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print(f"O Ângulo de {angulo} tem o Cosseno de {cosseno:.2f}")
tangente = math.tan(math.radians(angulo))
print(f"O Ângulo de {angulo} tem a Tangente de {tangente:.2f}") """

# outra forma de fazer aplicando somente os módulos utilizados da biblioteca 

from math import sin, radians, cos, tan # ao definir os módulos inicialmente 
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))#não é necessário utilizar o (math.) antes da função utilizada como por exemplo math.sin(math.radians) 
print(f"O Ângulo de {angulo} tem o Seno de {seno:.2f}")
cosseno = cos(radians(angulo))
print(f"O Ângulo de {angulo} tem o Cosseno de {cosseno:.2f}")
tangente = tan(radians(angulo))
print(f"O Ângulo de {angulo} tem a Tangente de {tangente:.2f}")