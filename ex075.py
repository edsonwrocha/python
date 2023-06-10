num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1, num2, num3, num4)
pares = 0
print('Você digitou os valores: ', tupla)
print('O número 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O número 3 foi digitado na posição {}'.format(tupla.index(3)+1))
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
        pares += 1
if pares == 0:
     print('Nenhum número par foi digitado')