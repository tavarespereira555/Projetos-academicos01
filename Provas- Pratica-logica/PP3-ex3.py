cont1= 0
cont2= 0
cont3= 0
contnulo= 0
contbran= 0
while True:
    print("=================")
    print("|     U R N A - E L E T R O N I C A  |")
    print("=================")
    print('[1] Zezo dos teclados')
    print('[2] Cleiton Rasta')
    print('[3] Gustavo Lima')
    print('[4] Nulo')
    print('[5] Branco')
    print('[7] Sair')
    print("=================")
    escolha= int(input('Sua opcao: '))
    if escolha == 1:
        cont1 = cont1 + 1
    elif escolha == 2:
        cont2= cont2 + 1
    elif escolha == 3:
        cont3= cont3 + 1
    elif escolha == 5:
        contnulo= contnulo + 1
    elif escolha == 6:
        contbran= contbran +1
    elif escolha == 7:
         break
total_votos= cont1 + cont2 + cont3 + contnulo + contbran
print('O total de votos dos candidato 1 sera de:', cont1)
print('O total de votos dos candidato 2 sera de:', cont2)
print('O total de votos dos candidato 3 sera de:', cont3)
print('O porcentual de votos nulos sera:', (contnulo / total_votos) * 100, '%')
print('O porcentual de votos brancos sera:', (contbran / total_votos) * 100, '%')
