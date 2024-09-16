#Сидоров Александр ИНС-б-о-20-2
m=int(input("Введите значение M = "))
n=int(input("Введите значение N = "))
a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        t=int(input("Введите значение a["+str(i)+","+str(j)+"] = "))
        a[i].append(t)
print("Вывод исходного двумерного массива")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a])+"\n")
s=0
k=0
b=a
for i in range(m):
    for j in range(n):
        s+=a[i][j]
        k+=1
    b[i].append(int(s/k))
c=[]
for i in range(m):
    for j in range(n):
        s+=a[j][i]
        k+=1
    c.append(int(s/k))
c.append('-')
b.append(c)
print("Результат обработки двумерного массива")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b]))

