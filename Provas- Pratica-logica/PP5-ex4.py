def calcula_combus(v_dista, v_consumo):
    calculo= v_dista / v_consumo
    return  calculo
if __name__ == '__main__':
    distancia= float(input('Digite o valor da distancia do percusso: Em Km '))
    consumo= float(input('Digite o consumo do carro (km por litro): '))
    v_caculo= calcula_combus(distancia, consumo)
    print(f'Para essa viagem, vc precisará de {v_caculo:.3f} litros de combustivel')