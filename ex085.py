numeros = [[], []]
dados = 0
for i in range(1, 8):
    dados = (int(input(f'Digite o {i}° número: ')))
    if dados % 2 == 0:
        numeros[0].append(dados)
    else:
        numeros[1].append(dados)
print(f'Os valores pares digitados foram {sorted(numeros[0])}')
print(f'Os valores impares digitados foram {sorted(numeros[1])}')
