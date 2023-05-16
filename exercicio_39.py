import random
num = random.randint(1,5)
num_user = int(input("Digite um número inteiro de 1 a 5: "))
if num_user == num:
    print(f"Parabéns, você ganhou! o número sorteado foi {num} e você digitou {num_user}")
else:
    print(f"Boa tentativa, o número sorteado foi {num} você digitou {num_user}")
