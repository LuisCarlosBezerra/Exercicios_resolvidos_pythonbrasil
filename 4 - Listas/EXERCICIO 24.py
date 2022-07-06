"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
from random import randint
from tabulate import tabulate as tb

lista_lancamentos = []
lancamentos_dados = []

for i in range(100):
    dado = randint(1, 6)
    lista_lancamentos.append(dado)

for j in range(1, 7, 1):
    lancamentos_dados.append([j, lista_lancamentos.count(j)])

print(tb(lancamentos_dados, headers=["FACE", "QUANTIDADE"]))


