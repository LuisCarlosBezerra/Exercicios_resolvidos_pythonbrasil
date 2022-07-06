"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""
print('PROGRAMA PARA CÁLCULA DA MÉDIA DE ALUNOS POR TURMA')
n_turmas = int(input('\nDigite a quantidade de turmas existentes: '))
acumulador_alunos = 0
for _ in range(1, n_turmas + 1, 1):
    while True:
        try:
            quantidade_alunos = int(input('\nDigite a quantidade de alunos da turma:\nValor máximo de 40 alunos! '))
        except ValueError:
            print('Você digitou um valor inválido, tente novamente. ')
        if quantidade_alunos <= 40:
            acumulador_alunos += quantidade_alunos
            print('Turma salva!')
            break
        else:
            print('Você digitou um valor acima do limite de 40 alunos. Tente novamente. ')

media_alunos = acumulador_alunos / n_turmas

print(f'\nA média de alunos por turma é igual a: {media_alunos}')
