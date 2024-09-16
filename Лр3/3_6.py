#Сидоров Александр ИНС-б-о-20-2
M = 3
K = 2
P = 6
x = [1,2,3,4,5,6,7,8,9,0]
buffbegin = x[min(K,P):min(K,P)+M]
buffend = x[max(K,P):max(K,P)+M]
x[min(K,P):min(K,P)+M] = buffend
x[max(K,P):max(K,P)+M] = buffbegin
print(x)

