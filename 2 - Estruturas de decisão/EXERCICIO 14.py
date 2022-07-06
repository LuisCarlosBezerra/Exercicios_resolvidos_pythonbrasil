"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento Conceito

Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se
o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
while True:
    try:
        nota1 = float(input('Digite a primeira nota: '))
        if 0 <= nota1 <= 10:
            break
        else:
            print('Você digitou um valor inválido! Digite um valor entre 0 e 10.')
    except ValueError:
        print('Digite um valor válido!')

while True:
    try:
        nota2 = float(input('Digite a segunda nota: '))
        if 0 <= nota2 <= 10:
            break
        else:
            print('Você digitou um valor inválido! Digite um valor entre 0 e 10.')
    except ValueError:
        print('Digite um valor válido!')

media_notas = (nota1 + nota2) / 2
conteito = ''

if 0 <= media_notas < 4:
    conceito = 'E'
elif 4 <= media_notas < 6:
    conceito = 'D'
elif 6 <= media_notas < 7.5:
    conceito = 'C'
elif 7.5 <= media_notas < 9:
    conceito = 'B'
elif 9 <= media_notas <= 10:
    conceito = 'A'

if media_notas >= 6:
    print(
        f'\nNota 1 = {nota1}\nNota 2 = {nota2}\nMédia = {media_notas}\nO aluno obteve conceito {conceito} e está '
        f'APROVADO!')
else:
    print(
        f'\nNota 1 = {nota1}\nNota 2 = {nota2}\nMédia = {media_notas}\nO aluno obteve conceito {conceito} e está '
        f'REPROVADO!')
