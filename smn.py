N = int(input("Введите число: "))
multi = []
while N%2==0:
    N/=2
    multi.append(N)
# multi.append(N)
print(multi)