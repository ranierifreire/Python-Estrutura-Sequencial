nome = str(input('Digite seu nome completo: ')).strip()
print(f"Seu nome em maiuscula é {nome.upper()}") 
print(f"Seu nome em minuscula é {nome.lower()}") 
print(f"Seu nome tem ao todo {len(nome)-nome.count(' ')}")  
#Contar o número de letras que possuí no nome cortando todos os espaços, inclusive o existente no meio entre nome e sobrenome 
#(Len) para contagem  (-nomeeeeeeeeeeee.count(' ')) para eliminar os espaços  .strip() no começo da linha para cortar os espaços iniciais e finais
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])}")
#Quantas letras tem o primeiro nome, foi utilizado o split para transformar em lista com uma nova variavel [0] para pegar o primeiro nome 
#e len(separa[0]) para contar as letras do primeiro nome 
