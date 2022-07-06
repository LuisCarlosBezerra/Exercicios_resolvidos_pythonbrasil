"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro
Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
é RS 2,50 o preço do litro do álcool é RS 1,90.
"""
litros = float(input('Insira a quantidade de litros vendidos.'))

tipo = str(input('"G" para GASOLINA ou "A" para ALCOOL. '))
tipo = tipo.upper()

if tipo == 'G':
    if litros < 20:
        valor = (litros * 2.50) * 0.96
    else:
        valor = (litros * 2.50) * 0.94

if tipo == 'A':
    if litros < 20:
        valor = (litros * 2.50) * 0.97
    else:
        valor = (litros * 2.50) * 0.95

print(f'O valor a ser pago é de {"%.2f" % valor} RS.')
