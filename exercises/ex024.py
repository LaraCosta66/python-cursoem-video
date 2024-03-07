#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
city = input('Qual o nome da cidade em que nasceu:').strip().upper()
print('O nome da sua cidade e {}'.format(city))
print('SANTO' in city)