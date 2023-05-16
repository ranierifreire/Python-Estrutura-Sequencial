n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print(f"A sua média é {m:.1f}")
if m >= 6.0:
    print("Sua média é boa, Parabéns!")
else: 
    print("Sua média está negativa, estude mais.")
    