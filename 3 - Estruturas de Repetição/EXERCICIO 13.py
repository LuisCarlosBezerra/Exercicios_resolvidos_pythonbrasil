"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""
base = int(input('Digite o número da base: '))
expoente = int(input('Digite o número do expoente: '))
resultado = 1

for x in range(0, expoente, 1):
    resultado = resultado * base

print(resultado)
