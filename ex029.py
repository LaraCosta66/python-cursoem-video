"""
 Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
  A multa vai custar R$7,00 por cada Km acima do limite.
"""
speed = int(input('Qual a velocidade atual do carro?'))
limit = 80
ticket = (speed - limit) * 7
if speed > limit:
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h')
    print('Voce deve pagar uma multa de R${:.2f}!'.format(ticket))

print('Tenha um bom dia! Dirija com segurança!')