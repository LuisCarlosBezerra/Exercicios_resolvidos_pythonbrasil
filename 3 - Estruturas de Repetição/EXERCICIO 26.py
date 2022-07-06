"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
"""

n_eleitores = int(input('Digite a quantidade de eleitores que irão votar: '))
print('INICIO DAS ELEIÇÕES ')
votos_A = 0
votos_B = 0
votos_C = 0

for _ in range(1, n_eleitores + 1, 1):
    while True:
        try:
            escolha = int(input(
                '\nDigite o número correspondente ao candidato escolhido:\nCANDIDATO A : 10\nCANDIDATO B : 20'
                '\nCANDIDATO C : 30\n\n'))
        except ValueError:
            print('Você digitou um valor inválido. Vote novamente.\n')
        if (escolha == 10) or (escolha == 20) or (escolha == 30):
            if escolha == 10:
                votos_A += 1
            if escolha == 20:
                votos_B += 1
            if escolha == 30:
                votos_C += 1
            print('Voto computado!')
            if _ < n_eleitores:
                print('Próximo eleitor deverá votar.\n')
            break

        else:
            print('Número inválido. Tente novamente, escolhendo o número de um dos três candidatos.\n')

print('\nFIM DA ELEIÇÃO')
print(f'Votos do candidato "A" : {votos_A}\nVotos do candidato "B" : {votos_B}\nVotos do candidato "C"   : {votos_C}\n')
