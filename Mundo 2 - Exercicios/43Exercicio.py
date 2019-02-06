print('Bem vindo ao exercicio 43')

print('Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo\n'
      'Abaixo de 18.5: Abaixo do peso'
      'Entre 18.5 e 25: Peso ideal'
      '25 até 30: Sobrepeso'
      '30 até 40: Obesidade'
      'Acima de 40: Obesidade mórbida')

print('\033[33m *** Resolução do Exercicio ***\033[m')

peso = float(input('Informe seu peso'))

altura = float(input('Informe sua altura'))

IMC = peso / (altura **2)

print('Seu IMC é de: {:.1f}' .format(IMC))


if IMC < 18.5:
      print('Você está abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
      print('Parabéns! Seu peso está ideal')
elif IMC >= 25 and IMC < 30:
      print('Você está com Sobrepeso')
elif IMC >= 30 and IMC < 40:
      print('Obesidade')
else:
      print('Obesidade mórbida')