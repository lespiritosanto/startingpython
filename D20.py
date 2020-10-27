from random import shuffle

# pegar nomes de alunos e apresentar ordem de apresentação

n = int(input('Digite o numero de alunos para a apresentação: '))
alunos = []

for i in range(1, n + 1):
    nome = input('Digite o nome do {}° aluno: '.format(i)).strip()
    alunos.append(nome)

shuffle(alunos)
print('A ordem de apresentação dos alunos será: {}'.format(alunos))
