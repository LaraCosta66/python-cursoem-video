"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('Para Aprovarmos o emprestimo preciso saber de algumas informações')
priceHouse = float(input('Qual o Valor da Casa? R$'))
sal = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar?'))
parcela = priceHouse / (anos * 12)
min = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${}'.format(priceHouse, anos, parcela))
if parcela <= min:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')