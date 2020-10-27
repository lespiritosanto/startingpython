# perguntar salario e calcular aumento.
# salarios superiores a R$1250 - 10%
# salarios inferiores ou iguais - 15%

salario = float(input('Digite o salário: '))

if salario > 1250:
    print('O novo salário do funcionário é de R$ {:.2f}.'
          .format(salario * 1.1))
else:
    print('O novo salário do funcionário é de R$ {:.2f}.'
          .format(salario * 1.15))
