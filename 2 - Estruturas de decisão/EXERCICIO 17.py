"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
é ou não bissexto.
"""
ano = int(input('Digite o ano: '))
resultado = divmod(ano, 4)
if resultado[1] == 0:
    print('O ano é BISEXTO!')
else:
    print('O ano não é BISEXTO!')
