
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

multi = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
si = len(multi)
x = 0
y = 1
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
    y=1
print('3. Неповторяющиеся элементы среди элементов:', mega, "\n ")