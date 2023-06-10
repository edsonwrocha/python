matriz = [[], [], []], [[], [], []], [[], [], []]
for line in range(0, 3):
    for columm in range(0, 3):
        matriz[line][columm] = int(input(f'Digite um valor para [{line}, {columm}]: '))
for i in range(0, 3):
    print(f'[ {matriz[i][0]} ][ {matriz[i][1]} ][ {matriz[i][2]} ]')
