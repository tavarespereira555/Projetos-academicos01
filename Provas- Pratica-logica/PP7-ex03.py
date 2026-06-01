altura= []
genero= []
while True:
    Alt= float(input('Digite a altura (ou [-1] para sair): '))
    if Alt == -1:
        break
    altura.append(Alt)
    gen= str(input('Digite o genero [M/F]: ')).strip().upper()
    genero.append(gen)
MaiorAltura= max(altura)
MenorAltura= min(altura)
QntF= genero.count('F')
QntM= genero.count('M')
print(f'Quantidade Feminino: {QntF}')
print(f'Quantidade Masculino: {QntM}')