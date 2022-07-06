"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
escolha = int(input('Escolha o dia da semana pelo número: '))
if 1 <= escolha <= 7:
    if escolha == 1:
        print('1 - DOMINGO')
    if escolha == 2:
        print('2 - SEGUNDA-FEIRA')
    if escolha == 3:
        print('3 - TERÇA-FEIRA')
    if escolha == 4:
        print('4 - QUARTA-FEIRA')
    if escolha == 5:
        print('5 - QUINTA-FEIRA')
    if escolha == 6:
        print('6 - SEXTA-FEIRA')
    if escolha == 7:
        print('7 - SÁBADO')

else:
    print('Valor inválido!')
