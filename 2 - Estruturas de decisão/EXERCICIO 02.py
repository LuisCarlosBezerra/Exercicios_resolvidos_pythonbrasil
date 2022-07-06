"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
teste = False
while teste is False:
    try:
        numero = float(input('Digite um número! '))
        teste = True
    except ValueError:
        print("Digite um valor válido!")

if numero != 0:
    if numero < 0:
        print(f'O número {numero} é negativo!')
    if numero > 0:
        print(f'O número {numero} é positivo!')

else:
    print(f'O número zero não tem sinal.')
