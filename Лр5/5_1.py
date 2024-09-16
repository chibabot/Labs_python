#Сидоров Александр ИНС-б-о-20-2
k=input("Количество предприятий: ")
name=[]
plan=[]
fact=[]
for i in range(int(k)):
    n=input("Название: ")
    name.append(n)
    p1=input("План: ")
    plan.append(p1)
    p2=input("Факт: ")
    fact.append(p2)
procent=map(lambda x, y:x*100/y, fact, plan)
fakty=zip(name, procent)
plany=zip(plan, name)
plany.sort()
print (16* "=")
print ("Процент выполнения плана каждым предприятием:")
nedo=0
for i in range(int(k)):
    s1=fakty[i][0]
    s2=fakty[i][1]
    if s2 < 100:
        nedo=nedo+1
        print(str(s1)+": "+str(s2))
print("Количество предприятий, недовыполнивших план: ", nedo)
print("Наибольший плановый товарооборот: ", max(plan))
print("Предприятия по возрастанию плана:")
for i in range(int(k)):
    s1=plany[i][1]
    s2=plany[i][0]
    print (str(s1)+": "+str(s2))
