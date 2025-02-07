#ler um angulo qualquer e mostrar o valor de seno, cosseno e tangente
import math
n = float(input('Digite um angulo: '))
s = math.sin(math.radians(n))
print('O angulo de {} tem o seno de {:.2f}'.format(n,s))
c = math.cos(math.radians(n))
print('O angulo de {} tem o cosseno de {:.2f}'.format(n,c))
t = math.tan(math.radians(n))
print('O angulo de {} tem a tangente de {:.2f}'.format(n,t))