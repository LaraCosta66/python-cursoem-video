"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas e minusculas
- quantas letras ao todo
- Quantas letras tem o primeiro nome
"""
name = input('Digite seu Nome completo:').strip()
#maiusculas
print('Seu nome em maiusculas {}'.format(name.upper()))
#minusculas
print('Seu nome em minusculas {}'.format(name.lower()))
#cumprimento
print('Seu nome tem ao todo {} letras'.format(len(name)-name.count(' ')))
div = name.split()
print('Seu primeiro nome tem {} letras'.format(len(div[0])))