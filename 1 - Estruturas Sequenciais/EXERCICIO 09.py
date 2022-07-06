"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
print('Corversor de temperatura\n')

teste = False
while teste is False:
    try:
        Fahrenheit = float(input('Digite a temperatura em °F Fahrenheit: '))
        teste = True
    except ValueError:
        print("Digite um valor válido")

Celsius = (5 * (Fahrenheit - 32)) / 9
print(f'Essa temperatura equivale à {"%.2f" % Celsius}° Celsius')
