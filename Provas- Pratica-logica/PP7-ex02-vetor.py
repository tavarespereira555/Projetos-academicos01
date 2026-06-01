NotasAlun= []
Qnt_alun= 0
Soma_Nota= 0
while True:
    nota= int(input('Digite a nota do aluno (ou [-1] para sair do programa: ) '))
    if nota == -1:
        break
    NotasAlun.append(nota)
    Soma_Nota= sum(NotasAlun)
    Qnt_alun= len(NotasAlun)
print(f'A quantidade de alunos da turma sera de: {Qnt_alun}')
m= Soma_Nota / Qnt_alun
print(f'A media da turma sera de: {m}')


