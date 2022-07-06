"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento.
"""
pop_A = 80_000
pop_B = 200_000

contador_anos = 0

while pop_A < pop_B:
    pop_A = (pop_A * 1.03)
    pop_B = (pop_B * 1.015)
    contador_anos = contador_anos + 1

print(f'Após {contador_anos} anos, a população A terá {round(pop_A, 0)} e a população B será de {round(pop_B, 0)}. '
      f'Esse é o período necessário para que A ultrapasse B em número de habitantes. ')
