def mensa(m, n):
    print(f'{m}\n{n}')
def soma(v1, v2, v3):
    SomaNum= v1 + v2 + v3
    return SomaNum
def nasci(ano, num_nas):
    idade= ano - num_nas
    return idade
def calcula_combus(v_dista, v_consumo):
    calculo= v_dista / v_consumo
    return  calculo
if __name__ == '__main__':
    while True:
        print("=================")
        print("|    M E N U    |")
        print("=================")
        print('[1] Exercicio 1')
        print('[2] Exercicio 2')
        print('[3] Exercicio 3')
        print('[4] Exercicio 4')
        print('[5] Sair')
        print("=================")
        escolha = int(input('Qual opcao vc deseja??? '))
        match escolha:
            case 1:
                mensagem = str(input('Digite uma mensagem: '))
                num = float(input('Digite um numero: '))
                mensa(mensagem, num )
            case 2:
                num1 = int(input('Digite o primeiro numero: '))
                num2 = int(input('Digite o segundo numero: '))
                num3 = int(input('Digite o terceiro numero: '))
                VSoma = soma(num1, num2, num3)
                print(f'A soma entre {num1}, {num2} e {num3} sera de: {VSoma} ')
            case 3:
                AnoAtual = int(input('Digite o ano que nos estamos: '))
                NumAno = int(input('Digite o ano em que vc nasceu: '))
                conta = nasci(AnoAtual, NumAno)
                print(f'Com base no ano {AnoAtual} vc tem {conta} anos')
            case 4:
                distancia = float(input('Digite o valor da distancia do percusso: Em Km '))
                consumo = float(input('Digite o consumo do carro (km por litro): '))
                v_caculo = calcula_combus(distancia, consumo)
                print(f'Para essa viagem, vc precisará de {v_caculo:.3f} litros de combustivel')
            case 5:
                break
            case _:
                print('\033[31mOpcao invalida\033[m')