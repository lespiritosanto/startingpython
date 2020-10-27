# ler nome de pessoa e dizer se ela tem "SILVA" no nome

nome_pessoa = str(input('Digite o seu nome completo: ')).strip()

if 'SILVA' in nome_pessoa.upper():
    print('O seu nome contém SILVA')
else:
    print('O seu nome não contém SILVA')
