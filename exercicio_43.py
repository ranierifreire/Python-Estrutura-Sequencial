from datetime import date
ano = int(input("Digite um ano: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O Ano digitado {ano} é Bissexto\nChama-se ano bissexto o ano ao qual é acrescentado um dia extra,\nficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos.")
else: 
    print(f"O Ano digitado {ano} não é Bissexto")