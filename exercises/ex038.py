#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem
firstNum = int(input('Digite um numero: '))
secNum = int(input('Digite segundo numero: '))

if firstNum > secNum:
    print('{} é maior que o {}'.format(firstNum, secNum))
elif secNum > firstNum:
    print('{} é maior que o {}'.format(secNum, firstNum))
else:
    print('Não existe valor maior, os dois são iguais')
