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
            lista = []
            qnt= 0
            while True:
                entrada = (input('Digite o numero (ou [-1] para sair:) '))
                if not entrada:
                    print("Entrada vazia! Por favor, escolha um numero.")
                    continue
                num = int(entrada)
                if num == -1:
                    break
                lista.append(num)
                qnt = len(lista)
            print(f'A quantidade de numeros sera de {qnt}')
        case 2:
            NotasAlun = []
            Qnt_alun = 0
            Soma_Nota = 0
            m= 0
            while True:
                Nota_ini = (input('Digite a nota do aluno (ou [-1] para sair do programa: ) '))
                if not Nota_ini:
                    print("Entrada vazia! Por favor, escolha um numero.")
                    continue
                nota= int(Nota_ini)
                if nota == -1:
                    break
                NotasAlun.append(nota)
            if len(NotasAlun) > 0:
                Soma_Nota = sum(NotasAlun)
                Qnt_alun = len(NotasAlun)
                print(f'A quantidade de alunos da turma sera de: {Qnt_alun}')
                m = Soma_Nota / Qnt_alun
                print(f'A media da turma sera de: {m}')
            else:
                print('Nenhuma nota foi digitada')
        case 3:
            altura = []
            genero = []
            while True:
                Alt_ini = (input('Digite a altura: '))
                if not Alt_ini:
                    print('Entrada vazia!! Por favor, digite um numero.')
                    continue
                Alt= float(Alt_ini)
                gen = str(input('Digite o genero [M/F]: ')).strip().upper()
                if not gen or gen not in ['M', 'F']:
                    print('Entrada vazia!!! Por favor, digite M ou F.')
                    continue
                genero.append(gen)
                altura.append(Alt)
                Cont_ini= str(input('Deseja continuar??? [S/N]: ')).upper().strip()
                if not Cont_ini:
                    print('Entrada vazia!!! Por favor, digite um numero')
                    continue
                if Cont_ini == 'N':
                    break
            if len(altura) > 0:
                MaiorAltura = max(altura)
                MenorAltura = min(altura)
                QntF = genero.count('F')
                QntM = genero.count('M')
                print(f'Quantidade Feminino: {QntF}')
                print(f'Quantidade Masculino: {QntM}')
                print(f'Maior altura: {MaiorAltura}')
                print(f'Menor altura: {MenorAltura}')
            else:
                print('Dados invalidos.')
        case 4:
            break
        case _:
            print('\033[31mOpcao invalida\033[m')