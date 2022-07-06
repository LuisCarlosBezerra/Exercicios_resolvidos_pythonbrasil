"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
teste = False
while teste is False:
    try:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        numero3 = float(input('Digite o terceiro número: '))
        teste = True
    except ValueError:
        print('Você digitou um valor inválido! Tente novamente.')

lista_ordem = [numero1, numero2, numero3]
lista_ordem.sort()

print(f'Os números em ordem DECRESCENTE são:\n{lista_ordem[2]}\n{lista_ordem[1]}\n{lista_ordem[0]}')
