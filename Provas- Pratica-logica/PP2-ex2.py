s= 0
cont= 0
m= 0
contg= 0
while True:
    num= float(input('Digite o valor desejado: '))
    continuar= str(input('Deseja continuar?? [S/N] ')).strip().upper()
    if num > 20:
        contg= contg + 1
    cont= cont + 1
    s= s + num
    if continuar == 'N':
        break
    if cont > 0:
        m = s / cont
    else:
        print('Nenhum numero foi digitado para calculcar a media')
print('A quantidade de valores digitados sera de:',cont)
print('A soma de todos os numeros sera: {}'.format(s))
print('A media dos numeros digitados sera de: {:.4f}'.format(m))
print('A quantidade de valores maior que 20 e:', contg)
"""eu sei q impossivel n digitar numero nenhum pois c der enter o progama vai travar kkk, mais eu estou
pensando em uma visao de longo alcance ou n faz sentido???"""
#Aluno: Pedro Pereira Tavares
#Turma: Engenharia de Software