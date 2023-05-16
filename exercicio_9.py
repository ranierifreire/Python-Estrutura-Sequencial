""" 9.Crie um script python que leia um número e mostre os seus tipos"""

coisa = input('Digite qualquer coisa:')
print(coisa, 'É do tipo primitivo', type(coisa))
print(coisa, 'Possui apenas números?', coisa.isnumeric(), '!')
print(coisa, 'Possui apenas letras?',  coisa.isalpha(), '!')
print(coisa, 'Possui letra ou número?', coisa.isalnum())
print(coisa, 'Possuia apenas letras maiúsculas?', coisa.isupper())
print(coisa, 'Possui apenas letras minúsculas?', coisa.islower())