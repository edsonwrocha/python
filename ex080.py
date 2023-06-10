lista = []
for i in range(0, 5):
    entrada = int(input('Digite um número: '))
    if i == 0:
        lista.append(entrada)
        print('Adicionado ao final da lista...')
    elif entrada > max(lista):
        lista.append(entrada)
        print('Adicionado ao final da lista...')
    elif entrada < min(lista):
        lista.insert(0, entrada)
        print('Adicionado ao inicio da lista...')
    else:
        for c, ii in enumerate(lista):
            if lista[c] < entrada < lista[c + 1]:
                lista.insert(c+1, entrada)
                print(f'Adicionado a posição {c+1} da lista...')
print('-='*30)
print(f'Os valores digitados em ordem foram : {lista}')
