d = int(input('1. Введите точность вычисления числа π: '))
pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(d))
print(round(pi, d))

N = int(input("2. Введите число: "))
multi = []
i = 2
while i <= N:
    if N % i == 0:
        N /= i
        multi.append(i)
        i = 2
    else:
        i += 1
print('множители данного числа:', multi)

# multi = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
si = len(multi)
x = 0
y = 0
total = 1
temp = multi[0]
mega = []
while x < si:
    while y < si:
        if multi[x] != multi[y]:
            temp = multi[x]
        else:
            total += 1
        y += 1
    if total == 2:
        mega.append(temp)
    total = 1
    x += 1
    y = 0
print('3. Неповторяющиеся элементы:', mega)

import random
k = int(input('4. Введите значение степени: '))
x = []
si = round(random.uniform(0,101))
for i in range(int(si)):
    xnum = round(random.uniform(0,101))
    x.append(xnum)
ix = x[si - 1]
form = round(2*pow(ix, k) + 4 * ix + 5)
data = open('DZ4.txt', 'a')
data.write('k=')
data.write(str(k))
data.write(' => ')
data.write('2*x^')
data.write(str(k))
data.write('+4*x+5=0 ')
data.writelines('with x=')
data.write(str(ix))
data.write(' => ')
data.write(str(form))
data.write(' \r\n')
data.close()
data = open('DZ4.txt', 'r')
for li in data:
    print(li)
data.close()

dataa = open('DZ51.txt', 'r')
dataa = str(*dataa)
lista = [int(i) for i in dataa if i.isdigit() and i != '2']
listaa = [i for i in dataa if i.isdigit()==False and i != 'x' and i != ' ']
datab = open('DZ52.txt', 'r')
datab = str(*datab)
listb = [int(i) for i in datab if i.isdigit() and i!='2']
listbb = [i for i in datab if i.isdigit()==False and i!='x' and i!=' ']
listf = []
for i in range(len(lista)):
    if listaa[i] == '-' and listbb[i] == '-':
        num = lista[i] * -1 + listb[i] * -1
    elif listbb[i] == '-':
        num = lista[i] + listb[i] * -1
    elif listaa[i] == '-':
        num = lista[i] * -1 + listb[i]
    else:
        num = lista[i] + listb[i]
    listf.append(num)
print('5.', listf)
with open('DZ5.txt', 'w') as res:
    for i in range(len(listf)):
        if i == 0:
            res.write(str(listf[i]))
            res.write('x^2')
        elif listf[i] >= 0 or i == 1 and listf[i] >= 0: 
            res.write(' +', str(listf[i]))
            res.write('x')
        elif i == 1:
            res.write(str(listf[i]))
            res.write('x')
        else:
            res.write(str(listf[i]))