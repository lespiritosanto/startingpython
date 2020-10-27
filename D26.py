# ler frase e dizer quantas vezes "A" aparece,
# sua posição da primeira vez e sua ultima posição

frase = str(input('Digite algo: ')).strip()

print('Esta frase contém {} letras "A".'.format(frase.count('A')))
print('Esta frase contém {} letras "a".'.format(frase.count('a')))

print('A primeira aparição da letra "A" se encontra na posição {} da string.'
      .format(frase.find('A')))

print('A última ocorrência da letra "A" está na posição {} da string.'
      .format(frase.rfind('A')))
