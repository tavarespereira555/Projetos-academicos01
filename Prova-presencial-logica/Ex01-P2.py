cont= 0
menor= 999999999999
m= 0
somaP= 0
cont50 = 0
maiorP= -9999999999999
m50 = 0
soma50 = 0
for i in range(5):
    num= float(input('Digite o peso: '))
    somaP += num
    if menor < num:
        menor = num
    if maiorP > num:
        num= maiorP
    if num >= 50:
        cont50 += 1
        soma50 += num
    cont += 1
m= m / cont
print(f'Media: {m}')
print(f'Pessoa mais magra: {menor}')
print(f'Pessoa mais gorda: {maiorP}')
print(f'Pessoa com mais de 50kg: {cont50}')
print(f'Media pessoa mais de 50kg: {soma50 / cont50}')





