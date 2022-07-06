"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
print('PROGRAMA PARA VERIFICAÇÃO DE MÉDIA DE "N" NOTAS')
n_notas = int(input('Digite a quantidade de notas a serem verificadas: '))
acumulador_media = 0

for _ in range(1, n_notas + 1, 1):
    nota = int(input('Digite a nota do aluno: '))
    acumulador_media += nota

media_aritimetica = acumulador_media / n_notas
print(f'A média aritimética para as notas informadas é: {media_aritimetica}')
