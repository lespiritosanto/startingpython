# ler nome e mostrar separadamente primeiro e ultimo nome

nome = str(input('Digite o seu nome completo: ')).strip().split()

print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu último nome é: {}'.format(nome[-1]))

# poderia ser também
# print('O seu ultimo nome é: {}'.format(nome[len(nome) - 1]))
