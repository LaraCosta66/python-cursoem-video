#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
n1 = int(input('Digite sua nota: '))
n2 = int(input('Digite sua segunda nota: '))
n3 = int(input('Digite sua terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 5:
    print('Sua media é {:.1f}, Voce foi REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua media é {:.1f}, Voce está de RECUPERAÇÃO'.format(media))
else:
    print('Sua media é {:.1f}, Voce foi APROVADO'.format(media))
