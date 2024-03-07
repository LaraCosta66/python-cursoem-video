# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n =str(input('Digite seu nome completo:')).strip()
name = n.split()
print('Seu primeiro nome e {}'.format(name[0]))
print('Seu ultimo nome e {}'.format(name[len(name)-1]))

