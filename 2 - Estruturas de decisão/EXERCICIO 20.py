"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""
while True:
    try:
        nota1 = float(input('Digite a primeira nota parcial: '))
        if 0 <= nota1 <= 10:
            break
        else:
            print('Você digitou um valor fora do intervalo válido. Digite uma nota entre 0 e 10. ')
    except ValueError:
        print('Você digitou um caractere inválido. Tente novamente.')

while True:
    try:
        nota2 = float(input('Digite a segunda nota parcial: '))
        if 0 <= nota2 <= 10:
            break
        else:
            print('Você digitou um valor fora do intervalo válido. Digite uma nota entre 0 e 10. ')
    except ValueError:
        print('Você digitou um caractere inválido. Tente novamente.')

while True:
    try:
        nota3 = float(input('Digite a terceira nota parcial: '))
        if 0 <= nota3 <= 10:
            break
        else:
            print('Você digitou um valor fora do intervalo válido. Digite uma nota entre 0 e 10. ')
    except ValueError:
        print('Você digitou um caractere inválido. Tente novamente.')

media = (nota1 + nota2 + nota3) / 3
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    if media >= 7:
        if media == 10:
            print('O aluno foi aprovado com DISTINÇÃO, PARABÉNS!')
        else:
            print('O aluno está APROVADO!')

    else:
        print('O aluno está REPROVADO!')
else:
    print('Você digitou uma nota inválida!')
