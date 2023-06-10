from time import sleep
diario = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2])/2)
    diario.append(aluno[:])
    aluno.clear()
    cont = str(input('Quer continuar: (999 para encerrar) '))
    if cont == '999':
        break
print('-='*30)
print(f'{"No.":^4}{"NOME":<10}{"MÉDIA":<5}')
print('-'*19)
for i in range(0, len(diario)):
    print(f'{i:<4}{diario[i][0]:<10}{diario[i][3]:>5}')
while True:
    print('-' * 30)
    ind_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if ind_aluno == 999:
        break
    else:
        print(f'As notas de {diario[ind_aluno][0]} são {diario[ind_aluno][1:3]}')
sleep(1)
print('Finalizando...')
sleep(1)
print('<<<VOLTE SEMPRE>>')
