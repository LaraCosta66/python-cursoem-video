#seno cosseno e tangente
from math import radians,sin, cos, tan

ang = float(input('digite o angulo que voce deseja:'))
seno = sin(radians(ang))
print(' o angulo de {} tem o Seno de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print(' o angulo de {} tem o Cosseno de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print(' o angulo de {} tem o tangente de {:.2f}'.format(ang, tangente))
