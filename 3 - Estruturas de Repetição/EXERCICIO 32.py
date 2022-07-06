"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5 5! = 5 . 4 . 3 . 2 . 1 = 120
"""
print('PROGRAMA PARA IMPRESSÃO DO FATORIAL DE UM NÚMERO')

n_fatorial = int(input('Digite um número para saber o seu fatorial: '))
acumulador_fatorial = 1
print(f'FATORIAL DE {n_fatorial}:')
for i in range(n_fatorial, 0, -1):
    acumulador_fatorial *= i
    if i == n_fatorial:
        print(f'{i}! = {i} . ', end="")
    if (i > 1) and (i < n_fatorial):
        print(f'{i} . ', end="")
    if i == 1:
        print(f'{i} = {acumulador_fatorial}')
