"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
print("Digite as 4 notas bimestrais para saber a média do aluno")

# BLOCO COM TESTE PARA SABER SE AS VARIÁVEIS SÃO NÚMEROS.
teste = False
while teste is False:
    try:
        nota1, nota2, nota3, nota4 = float(input('insira a primeira nota: ')), float(
            input('insira a segunda nota: ')), float(input('insira a terceira nota: ')), float(
            input('insira a quarta nota: '))
        teste = True
    except ValueError:
        print("Valor inválido. Digite apenas números!")

# PROCESSAMENTO DAS INFORMAÇÕES
media = (nota1 + nota2 + nota3 + nota4) / 4

# SAÍDA DE DADOS
print(f'a média para as quatro notas informadas é {media}')
