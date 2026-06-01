num1= float(input('Digite o valor do primeiro numero: '))
num2= float(input('Digite o valor do segundo numero: '))
escolha= 0
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Novos valores')
print('[4] Sair do progama')
while escolha != 4:
    escolha = int(input('Sua opção: '))
    if escolha == 1:
        soma= num1 + num2
        print('A soma dos numeros {} e {} sera de: {}'.format(num1, num2, soma))
    elif escolha == 2:
        multiplicar= num1 * num2
        print('A multiplicao entre {} e {} e igual a: {}'.format(num1, num2, multiplicar))
    elif escolha == 3:
        num1= float(input('Digite os novos valores: '))
        num2= float(input('Digite o outro valor: '))
    elif escolha == 4:
        print('Saindo...')
    else:
        print('Opçao invalida')