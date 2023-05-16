#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Quantidade de dias alugado: "))
km = float(input("Quantos KMs percorridos: "))

valor_dias = dias * 60
valor_km = km * 0.15

total = valor_dias + valor_km

print(f"Você alugo o carro por {dias} dias e percorreu {km} KMs")
print(f"O preço a pagar é R$ {total:.2f}")