def nasci(ano, num_nas):
    idade= ano - num_nas
    return idade
if __name__ == '__main__':
    AnoAtual= int(input('Digite o ano que nos estamos: '))
    NumAno= int(input('Digite o ano em que vc nasceu: '))
    conta= nasci(AnoAtual, NumAno)
    print(f'Com base no ano {AnoAtual} vc tem {conta} anos')
