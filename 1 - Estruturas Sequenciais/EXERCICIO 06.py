"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
teste = False
while teste is False:
    try:
        raio = float(input('Digite o raio do círculo (em centímetros): '))
        teste = True
    except ValueError:
        print("Digite um raio válido!")

area = (raio * raio) * 3.14
print(f'A área do círculo é igual a {area:.2f} centímetros quadrados')
