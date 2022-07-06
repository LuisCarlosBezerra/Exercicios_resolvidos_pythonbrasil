"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
fatorial = int(input('Digite um número para calcular o seu fatorial (!) '))
contador = fatorial
acumulado = 1

while contador >= 1:
    acumulado = acumulado * contador
    contador -= 1

print(f'O resultado é igual a {acumulado}')
