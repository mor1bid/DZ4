
N = int(input("2. Введите число: "))
multi = []
i = 2
while i<=N:
    if N%i==0:
        N/=i
        multi.append(i)
        i=2
    else:
        i+=1
print('множители данного числа:', multi)

# multi = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
si = len(multi)
x = 0
y = 0
total = 1
temp = multi[0]
mega = []
while x<si:
    while y<si:
        if multi[x]!=multi[y]:
            temp=multi[x]
        else:
            total+=1
        y+=1
    if total==2:
        mega.append(temp)
    total=1
    x+=1
    y=0
print('3. Неповторяющиеся элементы:', mega)

# import math
import random
k = int(input('4. Введите значение степени: '))
x = []
si = round(random.uniform(0,101))
for i in range(int(si)):
    xnum = round(random.uniform(0,101))
    x.append(xnum)
ix = x[si-1]
form = round(2*pow(ix, k)+4*ix+5)
data = open('DZ4.txt', 'a')
data.write('k=')
data.write(str(k))
data.write(' => ')
data.write('2*x^')
data.write(str(k))
data.write('+4*x+5=0 \n')
data.writelines('with x=')
data.write(str(ix))
data.write(' => ')
data.write(str(form))
data.close()


