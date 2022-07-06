"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada.
"""
print('PROGRAMA PARA MÉDIA DE IDADE DE "N" PESSOAS: ')
n_pessoas = int(input('Digite a quantidade de idades a serem verificadas: '))
acumulador_idade = 0

for _ in range(1, n_pessoas + 1, 1):
    idade = int(input('Digite a sua idade: '))
    acumulador_idade += idade

media_idade = acumulador_idade / n_pessoas
print(f'A média de idade dessas pessoas é de {media_idade}.')

if (0 < media_idade) and (media_idade < 25.26):
    print('Essa é uma turma JOVEM.')

if (25.26 <= media_idade) and (media_idade < 60):
    print('Essa é uma turma ADULTA.')

if media_idade >= 60:
    print('Essa é uma turma IDOSA.')
