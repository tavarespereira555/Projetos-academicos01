def calculo(v1, v2):
    sub= v1 - v2
    return sub
def adicao(v1,v2):
    #soma= v1 + v2
    return v1 + v2
if __name__ == '__main__':
    num1=int(input('Digite o numero: '))
    num2 = int(input('Digite o numero: '))
    v_soma= adicao(num1, num2)
    v_sub = calculo(num1, num2)
    print('Soma', v_soma)
    print('Subtracao', v_sub)