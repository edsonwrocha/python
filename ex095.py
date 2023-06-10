lista_jogadores = []
jogador = dict()
while True:
    print('_'*30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    jogador['gols'] = []
    total_gols = 0
    for i in range(0, jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i}? ')))
    for i in jogador['gols']:
        total_gols += i
    jogador['total'] = total_gols
    lista_jogadores.append(jogador.copy())
    cont = input('Quer continuar? [S/N]').upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'{"cod":>3} {"nome":<15}{"gols":<15}{"total":<5}')
print('_'*38)
for i, v in enumerate(lista_jogadores):
    print(f'{i:>3} {v["nome"]:<15}{str(v["gols"]):<15}{v["total"]:<5}')
print('_'*38)
while True:
    while True:
        show = int(input('Mostrar dados de qual jogador? '))
        if show >= len(lista_jogadores) and show != 999:
            print(f'ERRO! Não existe jogador com código {show}! Tente novamente.')
        else:
            break
    if show == 999:
        print('<< VOLTE SEMPRE >>')
        break
    print(f'LEVANTAMENTO DO JOGADOR {lista_jogadores[show]["nome"]}:')
    for i in range(0, len(lista_jogadores[show]['gols'])):
        print(f'No jogo {i} fez {lista_jogadores[show]["gols"][i]} gols.')
    print('_'*30)
