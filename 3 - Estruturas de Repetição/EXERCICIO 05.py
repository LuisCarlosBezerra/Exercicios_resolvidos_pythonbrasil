"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.
"""
pop_A = int(input('Digite o número da população A: '))
cresc_A = float(input('Agora entre com a taxa de crecimento anual da população A: '))

pop_B = int(input('Digite o número da população B: '))
cresc_B = float(input('Agora entre com a taxa de crecimento anual da população B: '))

contador = 0

while pop_A < pop_B:
    contador = contador + 1
    pop_A = (pop_A * (1 + (cresc_A / 100)))
    pop_B = (pop_B * (1 + (cresc_B / 100)))

print(f'Após {contador} anos, a população A terá {round(pop_A, 0)} e a população B será de {round(pop_B, 0)}. '
      f'Esse é o período necessário para que A ultrapasse B em número de habitantes. ')
