n1= float(input('Digite o primeiro numero: '))
n2= float(input('Digite o segundo numero: '))
escolha= 0
while True:
    print("=================")
    print("|    M E N U    |")
    print("=================")
    print('[1] +')
    print('[2] -')
    print('[3] *')
    print('[4] /')
    print('[5] Sair')
    print('[6] Novos valores')
    print("=================")
    escolha = int(input('Sua opcao: '))
    if escolha == 1:
        s = n1 + n2
        print('A soma entre os numeros {} e {} sera de: {}'.format(n1, n2, s))
    elif escolha == 2:
        Sub= n1 - n2
        print('A subtracao entre os numeros {} e {} sera de: {}'.format(n1, n2, Sub))
    elif escolha == 3:
        mul= n1 * n2
        print('A multiplicacao entre os numeros {} e {} sera: {}'.format(n1, n2, mul))
    elif escolha == 4:
        if n2 != 0:
            divi = n1 / n2
            print('A divisao entre {} e {} e: {}'.format(n1, n2, divi))
        else:
            print('Erro: Não e possivel dividir por 0')
    elif escolha == 6:
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
    elif escolha == 5:
         break

    else:
        print('Opçao invalida')

#Aluno: Pedro Pereira Tavares
#Turma: Engenharia de Software