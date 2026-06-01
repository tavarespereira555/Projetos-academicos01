"""for i in range(1, 10 + 1,1):
    print(f'{i:2} X 5 =  {5 * i:2}') """
"""for i in range(1, 10 + 1,1):
    print(f'{i:2} + 5 = {i + 5:2}')"""
"""import random
print('Numeros sorteados')
for i in range(1, 12 + 1,1):
    num_sor= random.randint(1, 6)
    print(num_sor)"""
#print('Digite -1 para sair do programa')
sair= int(input('Digite a tabuada ou [-1] para sair: '))
while sair != -1:
    cont = 0
    #num = int(input('Digite o numero para ver sua tabuada: '))
    print('Tabuada de multiplicacao do numero', sair)
    for i in range(1, 10 + 1,1):
        print(f'{i:2} X {sair:2} = {i * sair:2}')
        cont += 1
    print('A quantidade de valores foi:', cont)
    sair = int(input('Digite a tabuada ou [-1] para sair: '))