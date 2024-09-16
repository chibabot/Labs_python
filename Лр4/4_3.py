#Сидоров Александр ИНС-б-о-20-2
m=int(input("Введите значение M = "))
n=int(input("Введите значение N = "))
a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        t=int(input("Введите значение a["+str(i)+","+str(j)+"] = "))
        a[i].append(t)
s=0
k=0
for i in range(m):
    for j in range(n):
        s+=a[i][j]
        k=min(map(min,a))
print("Вывод двумерного массива")
print('\n'.join(['  '.join([str(cell) for cell in row]) for row in a]))
print("Абсолютная сумма значений: "+str(s))
print("Минимальное значение массива: "+str(k))
