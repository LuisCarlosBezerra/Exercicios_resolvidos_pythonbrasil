"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

    Até 5 Kg                      Acima de 5 Kg
File Duplo RS 4,90      por      Kg RS 5,80 por Kg
Alcatra RS 5,90         por      Kg RS 6,80 por Kg
Picanha RS 6,90         por      Kg RS 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
escolha = str(input('Escolha o tipo de carne para comprar: "F" para FILE DUPLO, "A" para ALCATRA, "P" para PICANHA '))
escolha = escolha.upper()
peso = float(input('Digite o peso total da compra da carne: '))

if escolha == 'F':
    carne = "FILE DUPLO"
    if peso < 5:
        preço = peso * 5.80
    else:
        preço = peso * 4.90

if escolha == 'A':
    carne = "ALCATRA"
    if peso < 5:
        preço = peso * 6.80
    else:
        preço = peso * 5.90

if escolha == 'P':
    carne = "PICANHA"
    if peso < 5:
        preço = peso * 7.80
    else:
        preço = peso * 6.90

pagamento = str(input('Escolha o tipo de pagamento: "V" para A VISTA ou "C" para CARTÃO TABAJARA ')).upper()
if pagamento == 'V':
    tipo_pagamento = "A VISTA"
    desconto = 0.0

if pagamento == 'C':
    tipo_pagamento = "CARTÃO TABAJARA"
    desconto = 5.0

preço_descontado = preço * ((100 - desconto) / 100)

print(
    f'Carne: {carne} peso: {peso} Kg\nValor total da compra: {"%.2f" % preço} RS\nModo de pagamento escolhido: '
    f'{tipo_pagamento} com desconto de {desconto}%\nValor total a pagar, com desconto: {"%.2f" % preço_descontado} RS')
