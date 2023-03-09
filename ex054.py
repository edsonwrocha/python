from datetime import date
maior = 0
menor = 0
for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 21:
        menor += 1
    else:
        maior +=1
print('{} são maior(es) de idade, já {} são menor(es) de idade'.format(maior, menor))
