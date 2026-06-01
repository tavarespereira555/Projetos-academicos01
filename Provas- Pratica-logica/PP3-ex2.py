soma= 0
cont= 0
m= 0
contmaior= 0
while True:
    num= float(input('Digite qualquer valor: '))
    continuar= str(input('Deseja continuar?? [S/N] ')).strip().upper()
    if num >= 50:
        contmaior= contmaior + 1
    cont= cont + 1
    soma= soma + num
    if continuar == 'N':
        break
    if cont > 0:
        m = soma / cont
    else:
        print('Nenhum numero foi digitado para calculcar a media')
print('A quantidade de valores digitados sera de:',cont)
print('A soma de todos os numeros sera: {}'.format(soma))
print('A media dos numeros digitados sera de: {:.4f}'.format(m))
print('A quantidade de valores maior que 50 e:', contmaior)

