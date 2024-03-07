#estrutura condicional
"""time = int(input('Quanto anos tem seu carro?'))
if time <= 3:
    print('Seu carro é relativamente novo')
else:
    print('Seu carro é velhoo')"""
#condicional simplificada
"""time = int(input('Quanto anos tem seu carro?'))
print('Carro novo'if time <=3 else 'Carro velho')
print('--FIM--')"""

n1= float(input('QUal a sua primeira nota:'))
n2= float(input('QUal a sua segunda nota:'))
m = (n1+n2)/2
print('A media é {:.1f}'.format(m))
if m <= 5.5:
    print('Voce precisa estudar mais')
else:
    print('Parabéns voce está na média')