vel = float(input("Digite a velocidade do carro: "))
valor = vel - 80
valor_2 = valor * 7 
if vel > 80:
    print(f"O limite de velocidade é 80KM/h você atingiu {vel}KM/h será multado em {valor_2} Reais. ")
else: 
    print(f"Você está abaixo do limite de velocidade {vel}KM/h.")
