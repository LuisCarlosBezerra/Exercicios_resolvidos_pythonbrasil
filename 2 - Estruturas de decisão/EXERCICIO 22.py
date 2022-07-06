"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""
numero = int(input('Digite um número para saber se é PAR ou IMPAR '))
par_impar = divmod(numero, 2)

if par_impar[1] == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é IMPAR!')
