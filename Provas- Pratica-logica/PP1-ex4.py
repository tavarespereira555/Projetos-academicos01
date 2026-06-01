n1= int(input('Digite o valor do numero: '))
n2= int(input('Digite outro numero: '))
if n1 > n2:
    maior= n1
    menor= n2
else:
    maior= n2
    menor= n1
print('Colocando os numeros {} e {} em ordem crescente ficaria: {} e {}'.format(n2,n1,menor, maior))
#Pedro Pereira Tavares