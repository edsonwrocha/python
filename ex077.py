palavras = ('biblioteca', 'computador', 'elefante', 'filosofia',
            'guitarra', 'historiador', 'inteligente', 'jornalista',
            'montanha', 'oportunidade', 'paralelepipedo', 'qualidade',
            'revolucionario', 'sustentavel', 'tecnologia')

for palavra in palavras:
    print('\nNa palavra {} temos as vogais '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')
