"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
 "Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser
aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser
armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de
cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional         Votos           %

Windows Server              1500            17%
Unix                        3500            40%
Linux                       3000            34%
Netware                     500             5%
Mac OS                      150             2%
Outro                       150             2%

Total                       8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
import operator

sistemas = {'Windows Server': 0, 'Unix      ': 0, 'Linux      ': 0, 'Netware      ': 0, 'Mac OS      ': 0,
            'Outro      ': 0}
lista_votos = []
maior_percentual = 0

while True:
    try:
        print('PESQUISA DE OPINIAO PARA O MELHOR SISTEMA OPERACIONAL')
        voto = int(input(
            'Digite o melhor sistema operacional para servidores:\n(Digite 0 para encerrar a votação)\n\n1 - Windows '
            'Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\n'))
        if 0 < voto <= 6:
            lista_votos.append(voto)
        elif voto == 0:
            print('\nVOTAÇÃO ENCERRADA!\n')
            break
        else:
            print('Você digitou um valor fora do intervalo válido, tente novamente.\n')
    except ValueError:
        print('Você digitou um valor inválido, tente novamente.\n')

total_votos = len(lista_votos)

print('SISTEMA OPERACIONAL\t\t', end='')
print('VOTOS\t\t\tPERCENTUAL')
print('-------------------\t\t', end='')
print('-----\t\t\t---------')

indice_sistema = 1
for valor in sistemas.keys():
    sistemas[valor] = lista_votos.count(indice_sistema)
    percentual = ((lista_votos.count(indice_sistema)) * 100) / total_votos
    print(f'{valor}', end=' ')
    print(f'\t\t\t{sistemas.get(valor)}', end=' ')
    print(f'\t\t\t{"%.2f" % percentual}')
    if percentual >= maior_percentual:
        maior_percentual = percentual

    indice_sistema += 1

print('-------------------\t\t', end='')
print('-----\t\t\t---------')

print('TOTAL               \t\t', end='')
print(f'{total_votos}\t\t\t100%     ')

# max(sistemas, key = sistemas.get)  #FUNCÃO PARA PEGAR A CHAVE QUE TEM O MAIOR VALOR

print(
    f'\nO Sistema Operacional mais votado foi o {max(sistemas, key=sistemas.get)}, com '
    f'{sistemas[max(sistemas, key=sistemas.get)]} voto(s), correspondendo a {"%.2f" % maior_percentual}% dos votos.')
