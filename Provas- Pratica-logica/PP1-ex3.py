import math
p1x= float(input('Digite o valor de x do ponto 1: '))
p1y= float(input('Agora o valor de y do ponto 1: '))
p2x= float(input('Digite o valor de x do ponto 2: '))
p2y= float(input('Agora o valor de y do ponto 2: '))
d= math.sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
print('O valor da distancia de 2 pontos é: {:.4f}'.format(d))
#Pedro Pereira Tavares