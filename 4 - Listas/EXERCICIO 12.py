"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos.
"""
lista_idade = []
lista_altura = []

for i in range(30):
    while True:
        try:
            idade = int(input('Digite a idade do aluno: '))
            if idade >= 0:
                lista_idade.append(idade)
                break
            else:
                print('Você entrou com um valor negativo para a idade, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    while True:
        try:
            altura = float(input('Digite a altura do aluno: '))
            if altura >= 0:
                lista_altura.append(altura)
                break
            else:
                print('Você entrou com um valor negativo para a altura, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

media = sum(lista_altura) / 5
contador = 0
for ida, alt, in zip(lista_idade, lista_altura):
    if (ida > 13) and (alt > media):
        contador += 1

print(f'A média de altura dos 30 alunos é igual a: {media}')
print(f'A quantidade de alunos acima de 13 anos que tem altura acima da média geral da turma é: {contador}')
