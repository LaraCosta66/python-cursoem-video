"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
num = int(input('Digite um numero:'))
result = num % 2
if result == 0:
    print('o numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))