# ler três números e comparar retornando qual é o maior e qual é o menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior número'.format(n1))
    if n2 > n3:
        print('{} é o menor número'.format(n3))
    else:
        print('{} é o menor número'.format(n2))
elif n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
    if n1 > n3:
        print('{} é o menor número'.format(n3))
    else:
        print('{} é o menor número'.format(n1))
else:
    print('{} é o maior número'.format(n3))
    if n2 > n1:
        print('{} é o menor número'.format(n1))
    else:
        print('{} é o menor número'.format(n2))

# outra solução

lista = [n1, n2, n3]
lista = sorted(lista)
print(lista)

# poderia ter usado os métodos min() e max() na lista também
