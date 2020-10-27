# testando funcionalidades da aula

frase = 'Curso em Vídeo Python    '
print(len(frase))

frase = frase.strip()  # imutável se não atribuir novamente

print(frase)

print(len(frase))
print()

print(frase.split())
print()

print(frase[9:])
print()

print(frase.upper().find('O'))
print()

print(frase.replace('Curso', 'Puto'))
