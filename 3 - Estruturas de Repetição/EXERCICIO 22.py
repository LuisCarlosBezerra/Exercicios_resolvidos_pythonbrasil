"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número
ele é divisível.
"""
# PRIMEIRA SOLUÇÃO PROGRAMA EXECUTA A DIVISÃO DE TODOS OS NUMEROS QUE ESTÃO ENTRE 1 E O NÚMERO A TESTAR,
# INCREMENTANDO SEMPRE QUE ENCONTRAR UM DIVISOR

numero_a_testar = int(input('Digite um numero natural para verificar se ele é ou não PRIMO: '))
limite = numero_a_testar
contador_divisor = 0
lista_divisores = []

for divisor in range(1, numero_a_testar + 1, 1):
    divisor_str = divmod(numero_a_testar, divisor)
    if divisor_str[1] == 0:
        contador_divisor += 1
        lista_divisores.append(divisor)

if contador_divisor == 2:
    print('É PRIMO!')

else:
    print('NÃO É PRIMO!')
    print(f'Os divisores deste número são: {lista_divisores}')
