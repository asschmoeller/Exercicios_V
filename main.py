# j0 = Frame, j1 = Tempo de carga, j2 = Quantidade Referências
# j3 = Tempo da última referência, j4 = BR , j5 = BM

# ordem   j0  j1  j2  j3  j4 j5
tabela = [[1, 12, 10, 20, 1, 1], 
          [2, 10, 1, 12, 0, 0], 
          [3, 11, 2, 21, 1, 0]]

print('-------------------------------------------')
print('Escreva o numero do critério de seleção:')
print("1 - FIFO;")
print("2 - NRU;")
print("3 - LFU;")
print("4 - LRU;")
print('-------------------------------------------')
selecao = int(input("Resposta: "))

#----------------------------------------------/
#FIFO
if selecao == 1:
  valor = 0
  menor = 0
  final = 0
  for i in range(len(tabela)):
    valor = tabela[i][1]
    if i == 0 or valor < menor:
      menor = valor  
      final = tabela[i][0]
  print(f'O menor tempo de carga é, {menor}; Frame: {final}')
#----------------------------------------------/
#NRU
elif selecao == 2:
  BMR = 0
  menor = 0
  final = 0
  for i in range(len(tabela)):
    BMR = tabela[i][4] + tabela[i][5]
    if i == 0 or BMR < menor:
      menor = BMR  
      final = tabela[i][0]
  print(f'O menor BR e BM é, {menor}; Frame: {final}')
#----------------------------------------------/
#LFU
elif selecao == 3:
  valor = 0
  menor = 0
  final = 0
  for i in range(len(tabela)):
    valor = tabela[i][2]
    if i == 0 or valor < menor:
      menor = valor  
      final = tabela[i][0]
  print(f'A menor quantidade de referências é, {menor}; Frame: {final}')
#----------------------------------------------/
#LRU
elif selecao == 4:
  valor = 0
  maior = 0
  final = 0
  for i in range(len(tabela)):
    valor = tabela[i][3]
    if i == 0 or valor > maior:
      maior = valor  
      final = tabela[i][0]
  print(f'O maior tempo da última referência é, {maior}; Frame: {final}')
#----------------------------------------------/