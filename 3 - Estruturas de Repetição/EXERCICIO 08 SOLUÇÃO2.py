"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
# RESOLUÇÃO 2

lista = []

for _ in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

print(lista)

soma = sum(lista)
media = soma / 5

print(f'A soma dos 5 número é {soma}')
print(f'A média dos 5 número é {media}')
