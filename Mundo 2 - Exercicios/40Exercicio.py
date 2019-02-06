print('Crie um programa que leia duas notas do aluno e mostre sua média e uma mensagem de acordo com a média\n'
      'Média abaixo de 5.0: Reprovado'
      'Média entre 5.0 e 6.9: Recuperação'
      'Média 7.0 ou superior: Aprovado')

print('\033[33m *** Resolução do Exercicio *** \033[m')

nota1 = float(input('Informe a nota cabloco'))
nota2 = float(input('Informe a segunda nota'))

média = (nota1 + nota2)/2

if média < 5.0:
      print('Seu merda, foi reprovado, sua média é {:.1f} '.format(média))
elif média == 5.0 or média < 6.9:
      print('Sem condições, você foi para recuperação com média {:.1f} '.format(média))
else:
      print('Mais do que a obrigação, você passou com média {:.1f} '.format(média))
