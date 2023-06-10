aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif aluno['media'] < 7 and aluno['media'] >=5:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média do aluno é {aluno["media"]}')
print(f'A situação do aluno é {aluno["situacao"]}')
