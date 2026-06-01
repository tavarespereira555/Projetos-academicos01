soma= 0
for i in range(1, 500 + 1,1):
    if i % 3 == 0 and i % 2 == 1:
        soma= soma + i
print('A soma dos valores impares e multiplos de 3 entre 1 e 500 sera de:', soma)