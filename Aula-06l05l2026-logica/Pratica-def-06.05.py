def minutos(hr, min):
    v_minutos= hr * 60 + min
    return v_minutos
if __name__ == '__main__':
    resultados= []
    for i in range(2):
        hr= int(input('Digite a hora: '))
        m = int(input('Digite os minutos: '))
        v_retornado1= minutos(hr, m)
        resultados.append(v_retornado1)
    diferenca= resultados[0] - resultados[1]
    print('A diferenca dos minutos sera de:', diferenca)
    if diferenca > 0:
        print('O primero numero e maior')
    elif diferenca < 0:
        print('O segundo numero e maior')
    else:
        print('Os numeros sao iguais')
