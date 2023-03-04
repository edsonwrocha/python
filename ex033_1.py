num1 = float(input('Digite um número: '))
num2 = float(input('Digite um segundo número: '))
num3 = float(input('Digite um terceiro número: '))

menor = num1
maior = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3

if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3

print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))