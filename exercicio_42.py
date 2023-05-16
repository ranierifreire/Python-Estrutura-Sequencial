distancia = float(input("Qual foi a distância percorrida em sua viagem em KM? "))
valor = 0.50 * distancia
valor_2 = 0.45 * distancia
if distancia > 200:
    print(f"você percorreu {distancia:.0f}KM o valor a pagar pela distância percorrida é R${valor_2:.2f}")
else:
    print(f"você percorreu {distancia:.0f}KM o valor a pagar pela distância percorrida é R${valor:.2f}")