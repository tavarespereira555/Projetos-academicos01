lista= []
def update():
    num_novo= int(input('Digite o novo numero: '))
    posi= int(input('Digite a posicao: '))
    lista[posi]= num_novo
def crescente():
    nova_lista= []
    for i in range(5):
        numero= int(input('Digite o numero: '))
        lista.append(numero)
        nova_lista= sorted(lista, reverse=True)
    print(nova_lista)

if __name__ == '__main__':
    crescente()