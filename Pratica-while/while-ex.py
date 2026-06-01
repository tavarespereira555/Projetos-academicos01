cont= 0
soma= 0
print('Digite [-1] para fechar o progama')
while True:
    num= float(input('Digite os numeros: '))
    if num == -1:
        break
    cont= cont + 1
print('A quantidade de numero e: {}'.format(cont))