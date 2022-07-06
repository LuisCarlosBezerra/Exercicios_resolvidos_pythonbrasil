"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
inicio = int(input('Digite o valor inicial do intervalo: '))
fim = int(input('Digite o valor final do intervalo: '))
soma = 0

for x in range(inicio, fim + 1, 1):
    print(x)
    soma += x

print(f'A soma do intervalo de números entre {inicio} e {fim} é igual a {soma}')
