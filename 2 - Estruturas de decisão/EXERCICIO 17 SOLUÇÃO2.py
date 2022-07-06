"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
é ou não bissexto.
"""
while True:
    try:
        ano = int(input('Digite o ano para saber se é BISEXTO:'))
        break
    except ValueError:
        print('Você digitou um valor inválido! Tente novamente: ')

if ano % 4 == 0:
    print('O ano é BISEXTO!')
else:
    print('O ano digitado não é BISEXTO!')
