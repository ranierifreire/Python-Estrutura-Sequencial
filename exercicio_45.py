salario  = float(input("Qual é o seu Salário? "))
aumento  = salario * 10 / 100
aumento2 = salario * 15 / 100

total  = salario + aumento
total2 = salario + aumento2

if salario > 1.250: 
    print(f"Parabéns você recebeu um aumento de 10% agora recebe R${total:.3f} no próximo mês.")
else:
    print(f"Parabéns você recebeu um aumento de 15% agora recebe R${total2:.3f} no próximo mês.")
    