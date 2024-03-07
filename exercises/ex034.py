"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
salary = float(input('Digite o seu salario? R$'))
if salary <= 1250:
    new = salary + (salary * 15 / 100) #aumento de 15% no salario
else:
    new = salary + (salary * 10 / 100) #aumento de 10% no salario
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salary, new))