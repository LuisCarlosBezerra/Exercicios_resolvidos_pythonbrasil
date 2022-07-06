"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
enesimo = int(input('Digite o n-esimo número da sequência de Fibonacci: '))
numero_A = 0
numero_B = 1
contador = 1

print(numero_A)

while contador < enesimo:
    print(numero_B)
    num = numero_B + numero_A;
    numero_A = numero_B
    numero_B = num
    contador += 1
