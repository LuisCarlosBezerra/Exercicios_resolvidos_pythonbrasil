"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno
mais alto e o número do aluno mais baixo, junto com suas alturas.
"""
print('CADASTRO DE ALTURA DE ALUNOS DA ESCOLA TABAJARA')
total = int(input('Digite o número total de alunos: '))
for i in range(1, total + 1, 1):
    while True:
        try:
            codigo = int(input('Digite o número do aluno: '))
            if codigo > 0:
                break
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    while True:
        try:
            altura_atual = int(input('Digite a altura do aluno em centímetros: '))
            if altura_atual > 0:
                break
        except ValueError:
            print('Você digitou um valor inválido, tente novamente')

    if i == 1:
        alto = altura_atual
        baixo = altura_atual
        cod_baixo = codigo
        cod_alto = codigo

    else:
        if altura_atual >= alto:
            alto = altura_atual
            cod_alto = codigo
        if altura_atual <= baixo:
            baixo = altura_atual
            cod_baixo = codigo

print(f'O aluno mais alto é o de código {cod_alto}, com {alto} cm.')
print(f'O aluno mais baixo é o de código {cod_baixo}, com {baixo} cm.')
