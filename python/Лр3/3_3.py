#Сидоров Александр ИНС-б-о-20-2
n=int(input("Введите кол-во элементов: "))
a=[]
for i in range(n):
    b=int(input("a["+str(i)+"] = "))
    a.append(b)
k=0
for i in range(n-1):
    if (a[i]%2==1) and (a[i+1]%2==0):
        k=a[i]
        a[i]=a[i+1]
        a[i+1]=k
print("Результат обработки массива")
print(a)
