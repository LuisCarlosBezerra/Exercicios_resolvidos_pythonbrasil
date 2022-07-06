"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
é divisível somente por ele mesmo e por 1.
"""
# PRIMEIRA SOLUÇÃO PROGRAMA EXECUTA A DIVISÃO DE TODOS OS NUMEROS QUE ESTÃO ENTRE 1 E O NÚMERO A TESTAR,
# INCREMENTANDO SEMPRE QUE ENCONTRAR UM DIVISOR

numero_a_testar = int(input('Digite um numero natural para verificar se ele é ou não PRIMO: '))
limite = numero_a_testar
contador_divisor = 0

for divisor in range(1, numero_a_testar + 1, 1):
    divisor_str = divmod(numero_a_testar, divisor)
    if divisor_str[1] == 0:
        contador_divisor += 1

if contador_divisor == 2:
    print('É PRIMO!')

else:
    print('NÃO É PRIMO!')
