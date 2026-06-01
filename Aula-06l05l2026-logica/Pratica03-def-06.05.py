def absoluto(num):
    if num < 0:
        valor_absoluto= num * -1
    else:
        valor_absoluto= num
    return valor_absoluto
if __name__ == '__main__':
    numero= int(input('Digite o numero: '))
    valor_retornado= absoluto(numero)
    print(f'Valor Absoluto: {valor_retornado}')