N = int(input("2. Введите число: "))
multi = []
i = 2
# for i in range(2,N+1):
while i<=N:
    if N%i==0:
        N/=i
        multi.append(i)
        i=2
    else:
        i+=1
        # if N%i==0:
        #     multi.append(i)
        #     # i=0
print('множители данного числа:', multi)