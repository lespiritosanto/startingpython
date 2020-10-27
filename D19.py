from random import randint, choice

# sortear alunos para apagar quadro

alunos = []
for i in range(1, 5):
    temp = input('Digite o nome do {}° aluno: '.format(i))
    alunos.append(temp)

print('Nome dos alunos a serem sorteados: {}'.format(alunos))
print()
sorteado = choice(alunos)
# sorteado = randint(1, 4)
print('O aluno sorteado para apagar o quadro foi {}.'
      .format(sorteado))
# print('O aluno sorteado para apagar o quadro foi {}.'
#      .format(alunos[sorteado]))
