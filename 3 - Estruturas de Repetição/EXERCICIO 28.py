"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
n_cds = int(input('Digite a quantidade de CDs da sua coleção: '))
acumulador_preco = 0
preco = 0

for _ in range(1, n_cds + 1, 1):
    while True:
        try:
            preco = float(input('\nEntre com o preço pago por este CD: '))
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')
        if preco >= 0:
            acumulador_preco += preco
            break
        else:
            print('Você digitou um valor inválido (negativo), tente novamente.')

print(f'\nO total investido em sua coleção é de {acumulador_preco:.2f}\nO valor médio por CD é igual a '
      f'{acumulador_preco / n_cds}')
