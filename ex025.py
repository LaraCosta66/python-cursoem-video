#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
name = input('Digite seu nome completo:').strip().upper()
validate = 'SILVA' in name
print('Seu nome tem Silva? {}'.format(validate))