from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('0s números sorteados foram: ', end='')
for i in num:
    print(i, end=' ')
maior = num[0]
menor = num[0]

for i in num:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'\nO menor valor sorteado foi: {menor}')
print(f'O maior valor sorteado foi: {maior}')
