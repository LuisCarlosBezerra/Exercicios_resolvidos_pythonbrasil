"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

  Até 5 Kg                  Acima de 5 Kg
Morango RS 2,50     por     Kg RS 2,20 por Kg
Maçã RS 1,80        por     Kg RS 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
escreva o valor a ser pago pelo cliente.
"""
peso_macas = float(input('Digite o peso das maçãs. '))
peso_morangos = float(input('Digite o peso dos morangos. '))

# PREÇO DAS MAÇAS
if peso_macas < 5:
    preço_macas = 1.80 * peso_macas

if peso_macas >= 5:
    preço_macas = 1.50 * peso_macas

# PREÇO DOS MORANGOS
if peso_morangos < 5:
    preço_morangos = 2.50 * peso_morangos

if peso_morangos >= 5:
    preço_morangos = 2.20 * peso_morangos

peso_total = peso_morangos + peso_macas
preço_total = preço_morangos + preço_macas

if peso_total >= 8 or preço_total >= 25:
    pagar = preço_total * 0.90

else:
    pagar = preço_total

print(f'O cliente deverá pagar {"%.2f" % pagar} RS')
