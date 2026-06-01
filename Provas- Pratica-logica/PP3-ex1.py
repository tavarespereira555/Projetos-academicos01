mpar= 0
mimpar= 0
contpar= 0
contimpar= 0
sompar= 0
somimpar= 0
cont= 0
soma= 0
while True:
    num= float(input('Digite o valor (ou digite [0] para sair do progama): '))
    if num == 0:
        break
    if num % 2 == 0:
        cont= cont + 1
        contpar= contpar + 1
        sompar=  sompar + num
        mpar= sompar / contpar
    else:
        cont= cont + 1
        contimpar= contimpar + 1
        somimpar= somimpar + num
        mimpar= somimpar / contimpar
    soma= soma + num
print('A media dos numeros pares sera de:', mpar)
print('A media dos numeros impares sera:', mimpar)
print('A quantidade total de numeros sera igual a:', cont)
print('A soma total de todos os numeros digitados sera:', soma)
