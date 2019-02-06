print('Bem vindo ao 53')

print('Crie um programa que leia uma frase qualquer e diga se ela é um palindromo')

# Palavra que é lida tanto na frente quanto atrás e dá igual

frase = str(input('Informe uma frase')).strip().upper()
palavras = frase.split() # Aqui ela divide todas as palavras
juntas = ''.join(palavras)
inverso = ''
for letra in range(len(juntas)-1,-1,-1):
    inverso = inverso + juntas[letra]
print(juntas, inverso)
if inverso == juntas:
    print('Temos um palindromo')
else:
    print('Não é palindromo')


