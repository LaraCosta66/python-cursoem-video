"""
 Escreva um programa que faça o computador “pensar” em um número inteiro
 entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
compute = randint(0,5) #Faz o computador "pensar"
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
player = int(input('Em que numero eu pensei?')) #Player tenta adivinhar
print('PROCESSANDO...')
sleep(2)# faz o computador 'dormir'
if player == compute:
    print('Parabéns!! voce adivinhou, o numero pensado foi {}'.format(compute))
else:
    print('Voce errou, o numero pensado foi {}'.format(compute))

