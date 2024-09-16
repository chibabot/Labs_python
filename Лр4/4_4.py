#Сидоров Александр ИНС-б-о-20-2
m=int(input("Введите значение M = "))
n=int(input("Введите значение N = "))
a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        t=int(input("Введите значение a["+str(i)+","+str(j)+"] = "))
        a[i].append(t)
b=[]
for i in range(m):
    for j in range(n):
        k=min(a[i])
    b.append(k)
print("Минимальные значения каждой строки")
print(b)
