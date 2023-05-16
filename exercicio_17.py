altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area = altura * largura
tinta = area/2
print(f"Sua parede tem {area} m² é necessário {tinta:.2f} litros de tinta para pintar a parede")
