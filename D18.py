from math import sin, cos, tan, radians

# calcular sen, cos e tan de dado ângulo

angulo = float(input('Digite o angulo para obter em resposta o seu seno, coseno e tangente: '))
print('O seno de {} é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'
      .format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
