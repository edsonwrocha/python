nome = []
idade = []
sexo = []
soma = 0
maior = 0
for i in range(0, 4):
    nome.append(str(input('Digite o nome: ')))
    idade.append(int(input('Digite a idade: ')))
    sexo.append(str(input('Digite o sexo: ')))

for i in idade:
    soma += i
    media = soma / 4

for i in idade:
    if i > maior:
        maior = i

for i in range(0, 4):
    if maior == idade[i]:
        ind_maior = i

