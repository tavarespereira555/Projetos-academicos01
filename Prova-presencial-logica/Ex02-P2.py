def area(b, altu):
    return (b + altu) / 2
def area_c(r):
    a = 3.14 * r ** 2
    return a
if __name__ == '__main__':
    base= float(input('Digite o valor da base: '))
    altura = float(input('Digite o valor da altura: '))
    print('-' * 40)
    print('CALCULO DE AREA DO TRIANGULO'.center(40))
    print('-' * 40)
    print(f'A area do triangulo sera de {area(base, altura)}')
    raio= float(input('Digite o valor do raio: '))
    v_retornado= area_c(raio)
    print('-' * 40)
    print('CALCULO DE AREA DO CIRCULO'.center(40))
    print('-' * 40)
    print(f'A area do circulo sera de {v_retornado}')
    print('-' * 40)