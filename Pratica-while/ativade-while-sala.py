contm= 0
contf= 0
soma= 0
m= 0
maior= -9999999
menor= 99999999
cont= 0
while True:
    altura= float(input('Digite o valor da altura (ou digite [0] para poder cancelar: '))
    if altura == 0:
        break
    if altura > maior:
        maior= altura
    if altura < menor:
        menor= altura
    gene= str(input('Qual seu genero [M/F]: ')).strip().upper()
    if gene == 'M':
        contm= contm + 1
    elif gene == 'F':
        contf= contf + 1
    else:
        print('Genero invalido, tente novamente')
    soma= soma + altura
    cont= cont + 1
    m= soma / cont
if contm > 0 or contf > 0:
    print('A maior altura e de:',maior)
    print('A menor altura e de:',menor)
    print('A quantidade total de mulheres sera de:', contf)
    print('A quantidade total de homens sera:', contm)
    print('A media das alturas sera de:', m)
else:
    print('Nao foi digitado nenhum valor')