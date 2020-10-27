name = str(input('Digite o seu nome completo: ')).strip()

print(name.upper())
print(name.lower())

name = name.split()
print(name)

nova = ''.join(name)
print(nova)

print(len(nova))

# print(len(name) - name.count(' '))
