libry = []
maior = 0
soma = 0
f_20 = 0
nome_maior = 0
for i in range(0, 4):
    user = [str(input('Digite o nome: ')), int(input('Digite a idade: ')), str(input('Digite o sexo: '))]
    libry.append(user)

for i in range(0, 4):
    soma += libry[i][1]
print('A média das idades cadastradas é {:.0f}'.format(soma / 4))

for i in range(0, 4):
    if libry[i][2] == 'm' and libry[i][1] > maior:
        maior = libry[i][1]
        nome_maior = libry[i][0]
print('O homem de maior idade cadastrado é {} e tem {} ano(s)'.format(nome_maior, maior))

for i in range(0, 4):
    if libry[i][2] == 'f' and libry[i][1] < 20:
        f_20 += 1
print('O total de mulheres cadastradas com menos de 20 anos é {}'.format(f_20))



