
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

# multik = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
si = len(multi)
x = 0
y = 0
total = 1
temp = multi[0]
mega = []
while x<si:
    # if x==temp:
    # else:
    #     temp = i
    # if multi[i]==temp:
    #     i2=0
    #     total+=1
    #     temp=multi[i]
    #     while i2<len(multi):
    #         if i2==temp:
    #             multi.remove(multi[i2])
    #         i2+=1
    while y<si:
        if multi[x]!=multi[y]:
            temp=multi[x]
        else:
            total+=1
        y+=1
                # print(temp)
                # multi.pop(2)
    if total==1:
        mega.append(temp)
    total=1
    x+=1
    y=0
    # temp = multi[i]
print('3.', mega, "\n ")