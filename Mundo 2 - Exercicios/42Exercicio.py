print('Peça o desafio 35 dos triangulos, acrescentando o recurso de mostrear que tipo de triangulo será formado\n'
      'Equilátero: Todos os lados iguais'
      'Isósceles: dois lados iguais'
      'Escaleno: todos os lados diferentes')

print('\033[33m *** Resolução do Exercicio ***\033[m')

p1 = float(input('Informe o lado do triangulo'))

p2 = float(input('Informe o segundo lado do triangulo'))

p3 = float(input('Informe o terceiro lado do triangulo'))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
      print('Com essas medidas é possivel fazer um triangulo')
      if p1 == p2 and p2 == p3:
            print('Esse é um triangulo Equilátero')
      elif p1 != p2 and p1 != p3 and p2 != p3:
            print('Esse é um triangulo Escaleno')
      else:
            print('Isósceles')
else:
      print('Não é possivel realizar um triangulo com essas medidas')
print('Espero ter ajudado!')
