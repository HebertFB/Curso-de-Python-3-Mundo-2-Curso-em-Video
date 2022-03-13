"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""

notaUm = float(input('Informe a primeira nota: '))
notaDois = float(input('Informe a segunda nota: '))
media = (notaUm + notaDois) / 2

if media < 5.0:
    print(f'\nREPROVADO!! Pois sua média é {media} e está abaixo de 5.0')
elif media >= 5.0 and media < 7.0:
    print(f'\nRECUPERAÇÃO!! Pois sua média é {media} e está abaixo de 7.0')
if media >= 7.0:
    print(f'\nAPROVADO!! Pois sua média é {media} e é igual  ou superior a 7.0')
