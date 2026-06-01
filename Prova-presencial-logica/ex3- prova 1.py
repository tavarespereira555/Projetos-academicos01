cont= 0
m= 0
soma= 0
cont10= 0
final= int(input('Digite o valor final da sequencia: '))
for i in range (0, final +1, 1):
    print(i)
    cont= cont + 1
    soma= soma + i
    if i > 10:
        cont10= cont10 + 1
m= soma / cont
print('total', cont)
print('Soma', soma )
print('Media', m)
print('Maior que 10', cont10)
