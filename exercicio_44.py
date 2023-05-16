num   = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num<num_2 and num<num_3:
    menor = num
if num_2<num_3 and num_2<num:
    menor = num_2
if num_3<num and num_3<num_2:
    menor = num_3
    
if num>num_2 and num>num_3:
    maior = num
if num_2>num_3 and num_2>num:
    maior = num_2
if num_3>num and num_3>num_2:
    maior = num_3

print(f"Maior número: {maior} e menor número {menor}")
    

