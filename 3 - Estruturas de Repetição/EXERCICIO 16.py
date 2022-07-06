"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""
# enesimo = int(input('Digite o n-esimo número da sequência de Fibonacci: '))
numero_A = 0
numero_B = 1
contador = 1

print(numero_A)
while numero_B <= 500:
    print(numero_B)
    num = numero_B + numero_A
    numero_A = numero_B
    numero_B = num
    contador += 1
