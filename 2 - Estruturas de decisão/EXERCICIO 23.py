"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
"""
numero = float(input('Digite um número: '))

if int(numero) == numero:
  print('O numero digitado é INTEIRO!')
else:
  print('O numero digitado é DECIMAL!')
