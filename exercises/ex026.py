"""
Faça um programa que leia uma frase pelo teclado e
mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""
frase = input('Digite uma frase:').upper()
cont = frase.count('A')
enco = frase.find('A')
ult = frase.rfind('A')
print('Na sua frase existe {} letras A'.format(cont))
print('A primeira letra A aparece na posicao {}'.format(enco))
print('A ultima letra A aparece na posicao {}'.format(ult))