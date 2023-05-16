print("-="*20)
print("Analisador de triângulos")
print("-="*20)
r1 = float (input("Primeira reta: "))
r2 = float (input("Segunda reta: "))
r3 = float (input("Terceira reta: "))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print("O Comprimento das retas acima podem forma um triângulo")
else: 
    print("O comprimento das retas acima não podem formar um trinângulo!")