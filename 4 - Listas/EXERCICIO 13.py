"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
lista_meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO",
               "NOVEMBRO", "DEZEMBRO"]
media_mes = []

for i, j in zip(range(0, 12, 1), lista_meses):
    while True:
        try:
            print('Digite a média de temperatura do mês de ', end="")
            print(j)
            temperatura = float(input(''))
            if (temperatura > -30) and (temperatura <= 50):
                media_mes.append(temperatura)
                break
            else:
                print('Você digitou um valor fora do intervalo padrão ( -30 à 50 ºC), tente novamente')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

media = sum(media_mes) / 12
print(media)

print('AS TEMPERATURAS ACIMA DA MÉDIA DO ANO SÃO:')
for indice, med in enumerate(media_mes):
    if med >= media:
        print(f'{indice + 1} - {lista_meses[indice]} , {med} ºC')
