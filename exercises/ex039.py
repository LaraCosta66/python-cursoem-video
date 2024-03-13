"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento:'))
idade =  atual - nasc

print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado há {} anos'.format(saldo))
    