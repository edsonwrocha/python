peso = []
maior = 0
menor = 0
for i in range(0, 5):
    peso.append(float(input('Digite um peso: ')))
maior = menor = peso[0]
for i in peso:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
