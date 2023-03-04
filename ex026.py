frase = str(input('Digite uma frase: ')).upper().strip()
#fraseup = frase.upper()
#azes = fraseup.count('A')
#listasema = fraseup.split('A', azes)
#del listasema[azes]
#listacoma = 'a'.join(listasema)
#tamanho = len(listacoma) + 1
#print(listacoma)
#print('A ultima ocorrência de "A" é na pos {}'.format(tamanho))
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))
print('A última ocorrência de "A" é na posição {}'.format(frase.rfind('A')+1))
