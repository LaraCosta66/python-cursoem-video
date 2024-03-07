#Ajuste salarial
sal = float(input('qual o salario do funcionario? R$'))
novo = sal + (sal * 15 / 100)
print('Um funcionario que ganhava R${:.2f} com 15% de aumento, passa a receber R${:.2f}'.format(sal, novo))