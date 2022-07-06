"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
teste = False
while teste is False:
    try:
        nota1, nota2 = float(input('Digite a primeira nota parcial: ')), float(input('Digite a segunda nota parcial: '))
        if (nota1 < 0) or (nota2 < 0):
            print("Você digitou um valor negativo! Tente novamente.")
        elif (nota1 > 10) or (nota2 > 10):
            print("Você digitou um valor maior que maior que 10! Tente novamente.")
        else:
            teste = True
    except ValueError:
        print("Você digitou um valor não numérico! Tente novamente.")

media = (nota1 + nota2) / 2
print(f"A média do aluno foi {media}")

if media >= 7:
    if media == 10:
        print('O aluno foi aprovado com DISTINÇÃO, PARABÉNS!')
    else:
        print('O aluno está APROVADO!')

else:
    print('O aluno está REPROVADO!')
