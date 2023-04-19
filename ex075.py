num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
pares = []
tupla = (num1, num2, num3, num4)

print('Você digitou os valores: ', tupla)
print('O número 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O número 3 foi digitado na posição {}'.format(tupla.index(3)))
else:
    print('O número 3 não foi digitado')
for i in tupla:
    if i % 2 == 0:
        pares.append(i)
if len(pares) > 0:
    print('Os números {} foram pares'.format(pares))
else:
    print('Você não digitou nenhum número par')