"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
"""
letra = str(input('Digite M para MASCULINO ou F para FEMININO '))
letra = letra.upper()

if letra == 'M':
    print('M - MASCULINO!')

elif letra == 'F':
    print('F - FEMININO')

else:
    print('SEXO INVÁLIDO!')
