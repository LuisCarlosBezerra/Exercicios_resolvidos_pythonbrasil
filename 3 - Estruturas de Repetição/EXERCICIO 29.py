"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que
o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens
o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta
tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços

1 - RS 1.99
2 - RS 3.98
...
50 - RS 99.50
"""
print('TABELA DE PREÇOS POR NÚMERO DE PRODUTOS')

for i in range(1, 51, 1):
    preco = i * 1.99
    print(f'{i} - RS {preco:.2f}')
