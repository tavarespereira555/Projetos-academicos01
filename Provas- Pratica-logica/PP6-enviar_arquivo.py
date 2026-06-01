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
def fatorial(numero1):
    f= 1
    for i in range(numero1, 0, -1):
        f *= i
    return f
def analisador(numero):
    if numero > 0:
        resultado= 'Positivo'
    elif numero < 0:
        resultado= 'Negativo'
    else:
        resultado= 'Nulo'
    if numero % 2 == 0:
        par_impar= 'Par'
    else:
        par_impar= 'Impar'
    return f'O numero {numero} é {resultado} e {par_impar}.'
if __name__ == '__main__':
    while True:
        print("=================")
        print("|    M E N U    |")
        print("=================")
        print('[1] Exercicio 1')
        print('[2] Exercicio 2')
        print('[3] Exercicio 3')
        print('[4] Sair')
        print("=================")
        opcao_inicio = (input('Qual opcao vc deseja??? '))
        if not opcao_inicio:
            print("Entrada vazia! Por favor, escolha uma opção.")
            continue
        opcao_comecar = int(opcao_inicio)
        match opcao_comecar:
            case 1:
                while True:
                    print('===============================================')
                    print('                  CALCULADORA')
                    print('===============================================')
                    n1 = float(input('Digite o numero: '))
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
                    continu = str(input('Deseja continuar?? [S/N]: ')).strip().upper()
                    if continu == 'N':
                        break
                    if not continu:
                        print("Entrada vazia! Por favor, escolha uma operação.")
                        continue
            case 2:
                print('=================================================')
                print('                  FATORIAL')
                print('=================================================')
                numero_entrada = int(input('Digite o numero para poder ver ser fatorial: '))
                v_retornado = fatorial(numero_entrada)
                print(f'O fatorial de {numero_entrada}! sera: {v_retornado}')
            case 3:
                cont = 0
                somaNum = 0
                while True:
                    entra = (input('Digite o numero (ou 999 para sair): '))

                    if not entra:
                        print("Entrada vazia! Por favor, escolha uma operação.")
                        continue
                    num = int(entra)
                    cont +=  1
                    somaNum +=  num
                    if num == 999:
                        break
                    resultado_funcao = analisador(num)
                    print(resultado_funcao)
                    print(f'A quantidade de numeros digitados foi: {cont}')
                    print('A soma dos numeros digitados sera de:', somaNum)
            case 4:
                break
            case _:
                print('\033[31mOpcao invalida\033[m')