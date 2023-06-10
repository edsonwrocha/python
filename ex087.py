matriz = [[], [], []], [[], [], []], [[], [], []]
pares = coluna3 = maiorlinha2 = 0
for line in range(0, 3):
    for columm in range(0, 3):
        matriz[line][columm] = int(input(f'Digite um valor para [{line}, {columm}]: '))
        if matriz[line][columm] % 2 == 0:
            pares += matriz[line][columm]
        if columm == 2:
            coluna3 += matriz[line][columm]
        if line == 1:
            if matriz[line][columm] > maiorlinha2:
                maiorlinha2 = matriz[line][columm]
print('-='*30)
for i in range(0, 3):
    print(f'[ {matriz[i][0]} ][ {matriz[i][1]} ][ {matriz[i][2]} ]')
print('-='*30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior valor da segunda linha é {maiorlinha2}.')
