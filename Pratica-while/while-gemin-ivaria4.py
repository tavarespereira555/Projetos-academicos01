while True:
    nota= float(input('Digite a sua nota entre 1 e 10: '))
    if nota > 0 and nota < 10:
        break
    print('ERRO, digite sua nota novamente')
    nota= float(input('Digite sua nota entre 1 e 10: '))