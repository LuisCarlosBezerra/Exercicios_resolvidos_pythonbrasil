"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
print('Corversor de temperatura\n')

teste = False
while teste is False:
    try:
        Celsius = float(input('Digite a temperatura em °Celsius: '))
        teste = True
    except ValueError:
        print("Digite um valor válido!")

Fahrenheit = (9 * Celsius + 160) / 5
print(f'Essa temperatura equivale à {"%.2f" % Fahrenheit}°Fahrenheit')
