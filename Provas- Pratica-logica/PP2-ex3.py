cont= 0
contapro= 0
contrepro= 0
soma_notas= 0
m= 0
num= 0
while True:
    entrada= (input('Digite a nota dos alunos (ou tecle enter para sair): '))
    if entrada == '':
        break
    cont= cont + 1
    num= float(entrada)
    if num >= 5:
        contapro= contapro + 1
    else:
        contrepro= contrepro + 1
    soma_notas= soma_notas + num
if cont > 0:
    m= soma_notas / cont
    print('A media da turma foi de:', m)

else:
    print('Nenhuma nota foi digitada, logo não ha media')
print('A quantidade de alunos que fizeram prova foi de:',cont)
print('A quantidade de alunos \033[32maprovados\033[m foi de:',contapro)
print('A quantidade de alunos \033[31mreprovados\033[m foi de:',contrepro)
#Aluno: Pedro Pereira Tavares
#Turma: Engenharia de Software


