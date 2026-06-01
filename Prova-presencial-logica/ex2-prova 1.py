cont= 0
soma= 0
m= 0
menor= 99999999
print('Digite -1 para sair do programa')
while True:
    nota= float(input('Digite o valor da nota: '))
    if nota == -1:
        break
    cont= cont + 1
    soma= soma + nota
    if nota < menor:
        menor= nota
m= soma / cont
print('A quantidade total de alunos sera:', cont)
print('A soma das notas das turma sera:', soma)
print('A media sera de:', m)
print('O menor valor sera:', menor)