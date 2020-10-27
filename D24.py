# ler um nome de cidade e dizer se ela começa ou não com "SANTO"

cidade = str(input('Digite o nome da sua cidade: ')).strip()

print('A sua cidade contem "SANTO"? {}'
      .format('SANTO' in cidade.upper()))

print('A sua cidade começa com "SANTO"? {}'.format("SANTO" in cidade[:5].upper()))

# print(cidade[:5].upper() == 'SANTO')

# solução melhor
# cidade = cidade.strip().split()
# print('SANTO' == cidade[0])
