""" import random
nome_1 = str(input("Digite o nome do primeiro aluno: "))
nome_2 = str(input("Digite o nome do segundo aluno: "))
nome_3 = str(input("Digite o nome do terceiro aluno: "))
nome_4 = str(input("Digite o nome do quarto aluno: "))
lista = [nome_1, nome_2, nome_3, nome_4]

sorteado = random.choice(lista)
print(f"O Aluno sorteado foi {sorteado}")
 """

from random import choice
nome_1 = str(input("Digite o nome do primeiro aluno: "))
nome_2 = str(input("Digite o nome do segundo aluno: "))
nome_3 = str(input("Digite o nome do terceiro aluno: "))
nome_4 = str(input("Digite o nome do quarto aluno: "))
lista = [nome_1, nome_2, nome_3, nome_4]

sorteado = choice(lista)
print(f"O Aluno sorteado foi {sorteado}")