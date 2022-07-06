"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
é divisível somente por ele mesmo e por 1.
"""
# SEGUNDA SOLUÇÃO ENCERRAR OS TESTES QUANDO O NÚMERO DE DIVISORES PASSAR DE 2, JÁ SATISFAZENDO A CONDIÇÃO DE QUE NÃO
# É PAR E EVITANDO OS OUTROS TESTES DESNECESSÁRIOS

numero_a_testar = int(input('Digite um numero natural para verificar se ele é ou não PRIMO: '))
limite = numero_a_testar
contador_divisor = 0
divisor = 1

while (contador_divisor <= 2) and (divisor <= numero_a_testar):
    divisor_str = divmod(numero_a_testar, divisor)
    if divisor_str[1] == 0:
        contador_divisor += 1
    divisor += 1

if contador_divisor == 2:
    print('É PRIMO!')

else:
    print('NÃO É PRIMO!')
