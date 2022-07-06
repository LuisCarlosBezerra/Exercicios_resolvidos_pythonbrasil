"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um
levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo:

um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza;
necessita troca do cabo ou conector;
quebrado ou inutilizado
Uma identificação igual a zero encerra o programa.

Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100
Situação Quantidade Percentual
1- necessita da esfera 40 40%
2- necessita de limpeza 30 30%
3- necessita troca do cabo ou conector 15 15%
4- quebrado ou inutilizado 15 15%
"""
from tabulate import tabulate as tb
lista_mouses = []
lista_defeitos = []
defeitos = ['\nNecessita da esfera','Necessita de limpeza','Necessita troca do cabo ou conector','Quebrado ou inutilizado']
mouse_dados = []
while True:
  try:
    defeito = int(input('\nDigite o código do defeito:\n1 - Necessita da esfera\n2 - Necessita de limpeza\n3 - Necessita troca do cabo ou conector\n4 - Quebrado ou inutilizado '))
    if 0 < defeito <= 4:
      lista_defeitos.append(defeito)
    elif defeito == 0:
      break
    else:
      print('Você digitou um valor fora do intervalo válido, tente novamente.')
  except ValueError:
    print('Você digitou um valor inválido, tente novamente.')
  id += 1
total_defeitos = len(lista_defeitos)
#print("ID\tDEFEITO\t\t\tQUANTIDADE\t\t\tPERCENTUAL")


for i in range(1, 5, 1):
  mouse_dados.append([i, defeitos[i-1], lista_defeitos.count(i), ((lista_defeitos.count(i)) * 100)/total_defeitos])

print(tb(mouse_dados, headers=["ID","SITUAÇÃO","QUANTIDADE","PERCENTUAL"]))
  #print(f'\n{i}\t{defeitos[i-1]}\t\t\t{lista_defeitos.count(i)}\t\t\t{((lista_defeitos.count(i)) * 100)/total_mouses}')
