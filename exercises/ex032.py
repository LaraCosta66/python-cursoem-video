#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano quer analisar?Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year #Pega o ano em que sua máquina está configurada
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))