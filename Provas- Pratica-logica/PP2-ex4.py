cont= 0
s= 0
mpar= 0
mimpar= 0
som_par= 0
som_impar= 0
contpar= 0
contimpar= 0
maior= 0
menor= 0
while True:
    num= float(input('Digite o valor (ou digite zero para cancelar): '))
    s= s + num
    if num == 0:
        break
    cont = cont + 1
    if num > maior:
        num= maior
    if num % 2 == 0:
        contpar= contpar + 1
        som_par= som_par + num
    else:
        contimpar = contimpar + 1
        som_impar= som_impar + num
print('A quantidade de numeros digitados sera de:',cont)
print('A soma de \033[36mTODOS\033[m os numeros digitados sera: {}'.format(s))
if contpar > 0:
    mpar = som_par / contpar
    print('A media de apenas os numeros pares e: {}'.format(mpar))

else:
    print('Nao foram digitados numeros PARES para poder calcular a media')
if contimpar > 0:
    mimpar = som_impar / contimpar
    print('A media de apenas os numeros impar e: {}'.format(mimpar))
else:
    print('N foram digitados numeros IMPARES para poder calcular a media')
# Aluno: Pedro Pereira Tavares
# Turma: Engenharia de Software

