def maior_num(num1, num2):
    if num1 > num2:
        maior= num1
    else:
        maior= num2
    return maior
if __name__ == '__main__':
    numero1= int(input('Digite o numero: '))
    numero2 = int(input('Digite o numero: '))
    v_retornado= maior_num(numero1, numero2)
    print(f'O maior valor sera: {v_retornado}')