"""
 Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
distance = int(input('Qual a distancia da sua viagem?'))
print('Voce vai embarcar em uma viagem de {:.1f}Km'.format(distance))
if distance <= 200:
    price = distance * 0.5
    print('O preço da sua passagem será de R${:.2f}'.format(price))
else:
    price = distance * 0.45
    print('O preço da sua passagem será de R${:.2f}'.format(price))