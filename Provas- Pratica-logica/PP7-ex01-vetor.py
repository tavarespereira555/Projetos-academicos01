lista= []
while True:
    entrada= (input('Digite o numero (ou [0] para sair:) '))
    if not entrada:
        print("Entrada vazia! Por favor, escolha um numero.")
        continue
    num= int(entrada)
    if num == 0:
        break
    qnt= len(lista)
    print(f'A quantidade de numeros sera de {qnt}')