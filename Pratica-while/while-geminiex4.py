nota= float(input('Qual e o valor da nota: '))
while nota < 0 or nota > 10:
    print('ERRO, por favor digite sua nota novamente')
    nota= float(input('Digite sua nota novamente: '))