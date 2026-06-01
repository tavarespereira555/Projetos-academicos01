contmenos= 0
contmeio= 0
contmais= 0
soma= 0
salariomin= 0
total= 0
print('======================================================================================================')
print('\033[31mVale salientar que esse progama e referente ao valor do salario minimo do  mes de marco no ano de 2026\033[m ')
print('======================================================================================================')
while True:
    ano= str(input('Deseja alterar o ano??? [S/N] ')).strip().upper()
    if ano == 'S':
        mudano= float(input('Qual ano que vc deseja??? '))
        if mudano == 2020:
            salario_min = 1045.00
        elif mudano == 2021:
            salario_min = 1100.00
        elif mudano == 2022:
            salario_min = 1212.00
        elif mudano == 2023:
            salario_min = 1320.00
        elif mudano == 2024:
            salario_min = 1412.00
        elif mudano == 2025:
            salario_min = 1518.00
        elif mudano == 2026:
            salario_min = 1621.00
        else:
            print('Ano nao disponivel!')
            salario_min = 0