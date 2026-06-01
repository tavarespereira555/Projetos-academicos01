def soma(v1, v2, v3):
    SomaNum= v1 + v2 + v3
    return SomaNum
if __name__ == '__main__':
    num1=int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    num3 = int(input('Digite o terceiro numero: '))
    VSoma= soma(num1, num2, num3)
    print(f'A soma entre {num1} {num2} {num3} sera de: {VSoma} ')