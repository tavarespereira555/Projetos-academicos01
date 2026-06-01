def fatorial(numero1):
    f= 1
    for i in range(numero1, 0, -1):
        f *= i
    return f
if __name__ == '__main__':
    print('=================================================')
    print('                  FATORIAL')
    print('=================================================')
    numero_entrada= int(input('Digite o numero para poder ver ser fatorial: '))
    v_retornado= fatorial(numero_entrada)
    print(f'O fatorial de {numero_entrada}! sera: {v_retornado}')
