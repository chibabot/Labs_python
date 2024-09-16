#Сидоров Александр ИНС-б-о-20-2
n=int(input("Введите кол-во элементов: "))
a=[]
for i in range(n):
    b=int(input("a["+str(i)+"] = "))
    a.append(b)
k=0
for i in range(int(n/2)):
     k = a[i];
     a[i] = a[n-1-i];
     a[n-1-i] = k;
print("Результат обработки массива")
print(a)
