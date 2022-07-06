"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
o número de alunos com média maior ou igual a 7.0.
"""
lista_medias = []
contador_media = 0
for alunos in range(3):
    notas = []

    for i in range(4):
        while True:
            try:
                nota = float(input('Digite a nota do aluno: '))

                if (nota >= 0) and (nota <= 10):
                    notas.append(nota)
                    break
                else:
                    print('Você digitou um valor fora do intervalo de 1 à 10, tente novamente. ')
            except ValueError:
                print('Você digitou um valor inválido!')

    if alunos < 3:
        media_aluno = sum(notas) / 4
        lista_medias.append(media_aluno)
        print(media_aluno)
        print('\nDIGITE A NOTA DO PROXIMO ALUNO')

for _ in lista_medias:
    if _ >= 7:
        contador_media += 1

print(f'\nO número de alunos acima da média é: {contador_media}. ')
