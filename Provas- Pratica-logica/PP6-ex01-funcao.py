def calculadora(num1, num2, sinal):
    match sinal:
        case 1:
            soma= num1 + num2
            print(f'A soma entre {num1} e {num2} sera de: {soma}')
        case 2:
            subtra= num1 - num2
            print(f'A subtracao entre {num1} e {num2} sera de: {subtra}')
        case 3:
            multipli= num1 * num2
            print(f'A multiplicacao entre {num1} e {num2} sera de: {multipli}')
        case 4:
            divi= num1 / num2
            print(f'A divisao entre {num1} e {num2} sera de: {divi}')
        case _:
            print('\033[31mOpção invalida\033[m')
if __name__ == '__main__':
    while True:
        print('===============================================')
        print('                  CALCULADORA')
        print('===============================================')
        n1= float(input('Digite o numero: '))
        n2 = float(input('Digite o numero: '))
        print("=================")
        print("|    M E N U    |")
        print("=================")
        print('[1] +')
        print('[2] -')
        print('[3] *')
        print('[4] /')
        print("=================")
        entrada = (input('Sua opcao: '))
        if not entrada:
            print("Entrada vazia! Por favor, escolha uma operação.")
            continue
        escolha = int(entrada)
        calculadora(n1, n2, escolha)
        continu= str(input('Deseja continuar?? [S/N]: ')).strip().upper()
        if continu == 'N':
            break
        if not continu:
            print("Entrada vazia! Por favor, escolha uma operação.")
            continue