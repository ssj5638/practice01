lst = []
sum = 0
for a in range(5):
    num = input('> ')
    num = int(num)
    lst.append(num)
    sum += num

print('평균 : ', sum/5)