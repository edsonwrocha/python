valores = []
for i in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {i}: ')))
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for c, i in enumerate(valores):
    if i == max(valores):
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for c, i in enumerate(valores):
    if i == min(valores):
        print(f'{c}...', end='')
