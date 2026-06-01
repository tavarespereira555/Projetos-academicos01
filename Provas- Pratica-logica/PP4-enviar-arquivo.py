while True:
    print("=================")
    print("|    M E N U    |")
    print("=================")
    print('[1] Exercicio 1')
    print('[2] Exercicio 2')
    print('[3] Exercicio 3')
    print('[4] Exercicio 4')
    print('[5] Exercicio 5')
    print('[6] Exercicio 6')
    print('[7] Sair')
    print("=================")
    try:
        escolha= int(input('Qual opcao vc deseja??? '))
    except ValueError:
        escolha= -1
    match escolha:
        case 1:
            cont = 0
            num = int(input('Qual o valor final da sequencia??? '))
            for i in range(0, num + 1, 1):
                print(i)
                cont += 1
            print('A quantidade de numeros sera de:', cont)
        case 2:
            cont = 0
            num = int(input('Digite o valor inicial da sequencia: '))
            for i in range(num, 0 - 1, -1):
                print(i)
                cont += 1
            print('A quantidade de valores da sequencia sera de:', cont)
        case 3:
            soma = 0
            for i in range(1, 500 + 1, 1):
                soma = soma + i
            print('A soma dos valores entre 1 e 500 sera de:', soma)
        case 4:
            soma = 0
            for i in range(1, 500 + 1, 1):
                if i % 3 == 0 and i % 2 == 1:
                    soma = soma + i
            print('A soma dos valores impares e multiplos de 3 entre 1 e 500 sera de:', soma)
        case 5:
            for i in range(0, 6 + 1, 1):
                for segnum in range(0, 6 + 1, 1):
                    print(i, segnum)
        case 6:
            for i in range(0, 6 + 1, 1):
                for SegNum in range(0, 6 + 1, 1):
                    if SegNum >= i:
                        print(i, SegNum)
        case 7:
            break
        case _:
            print('\033[31mOpcao invalida\033[m')