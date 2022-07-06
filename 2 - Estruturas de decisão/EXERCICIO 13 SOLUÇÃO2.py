"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
teste = False
while teste is False:
    try:
        escolha = int(input('Escolha o dia da semana pelo número: '))
        if 0 < escolha < 8:
            teste = True
        else:
            print('Você digitou um valor fora do intervalo de 1 à 7! Tente novamente.')
    except ValueError:
        print('Você digitou um valor inválido, tente novamente.')

dici_dia = {1: 'DOMINGO', 2: 'SEGUNDA-FEIRA', 3: 'TERÇA-FEIRA', 4: 'QUARTA-FEIRA', 5: 'QUINTA-FEIRA', 6: 'SEXTA-FEIRA',
            7: 'SÁBADO'}
print(dici_dia.get(escolha))
