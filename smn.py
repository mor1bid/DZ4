
# N = int(input("2. Введите число: "))
# multi = []
# i = 2
# while i<=N:
#     if N%i==0:
#         N/=i
#         multi.append(i)
#         i=2
#     else:
#         i+=1
# print('множители данного числа:', multi)

# # multi = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
# si = len(multi)
# x = 0
# y = 0
# total = 1
# temp = multi[0]
# mega = []
# while x<si:
#     while y<si:
#         if multi[x]!=multi[y]:
#             temp=multi[x]
#         else:
#             total+=1
#         y+=1
#     if total==2:
#         mega.append(temp)
#     total=1
#     x+=1
#     y=0
# print('3. Неповторяющиеся элементы:', mega)

# import random
# k = int(input('4. Введите значение степени: '))
# x = []
# si = round(random.uniform(0,101))
# for i in range(int(si)):
#     xnum = round(random.uniform(0,101))
#     x.append(xnum)
# ix = x[si-1]
# form = round(2*pow(ix, k)+4*ix+5)
# data = open('DZ4.txt', 'a')
# data.write('k=')
# data.write(str(k))
# data.write(' => ')
# data.write('2*x^')
# data.write(str(k))
# data.write('+4*x+5=0 ')
# data.writelines('with x=')
# data.write(str(ix))
# data.write(' => ')
# data.write(str(form))
# data.close()
# data = open('DZ4.txt', 'r')
# for li in data:
#     print(li, '\n')
# data.close()

data1 = open('DZ51.txt', 'r')
data2 = open('DZ52.txt', 'r')
res = open('DZ5.txt', 'w')
with open('DZ51.txt', 'r') as data1:
    text1 = data1.read(8)
    res.write(text1)
res.write('+ ')
with open('DZ52.txt', 'r') as data2:
    text2 = data2.read()
    res.write(text2)
# res.write(text1)
# res.write('+ ')
# res.write(text2)
data1.close()
data2.close()
res.close()
res = open('DZ5.txt', 'r')
for li in res:
    # if li != '=' or li != '0':
    print(li)
# print('\n = 0')
res.close()
