lista= []
while True:
    num= int(input('Digite o numero (ou [0] para sair:)  '))
    if num == 0:
        break
    lista.append(num)
print(lista)
print('-----------------------------')
for item in lista:
    print(item)
print('-----------------------------')
qnt= len(lista)
print('Quantidade numeros: ', qnt)
maior= max(lista)
print(f'Maior {maior}')
menor= min(lista)
print(f'Menor {menor}')
soma= sum(lista)
print(f'Soma {soma}')
print('-----------------------------')
pesquisa= int(input('Digite o valor para verificar se existe: '))
if pesquisa in lista:
    print('Esse valor esta na lista')
    print(f'Indice do numero: {lista.index(pesquisa)}')
else:
    print('Esse valor n esta na litsa')
print('-----------------------------')
print('ORDENACAO DOS NUMEROS DA LISTA')
lista.sort()
print(lista)
#nova_lista= sorted()lista
#print(nova_lista)
print('-----------------------------')
lista.insert(1, 33)
print(lista)