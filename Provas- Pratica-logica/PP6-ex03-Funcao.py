def analisador(numero):
    if numero > 1:
        resultado= 'Positivo'
    elif numero < 1:
        resultado= 'Negativo'
    else:
        resultado= 'Nulo'
    if numero % 2 == 0:
        par_impar= 'Par'
    else:
        par_impar= 'Impar'
    return f'O numero {numero} é {resultado} e {par_impar}.'
if __name__ == '__main__':
    cont= 0
    somaNum= 0
    while True:
        entra= (input('Digite o numero (ou 999 para sair): '))

        if not entra:
            print("Entrada vazia! Por favor, escolha uma operação.")
            continue
        num = int(entra )
        cont =+ 1
        somaNum =+ num
        if num == 999:
            break
        resultado_funcao= analisador(num)
        print(resultado_funcao)
        print(f'A quantidade de numeros digitados foi: {cont}')
        print('A soma dos numeros digitados sera de:', somaNum)
