money = input('금액 : ')

money = int(money)

result = money // 50000
print('50000원 : {0}개'.format(result))
money -= result*50000
result = money // 10000
print('10000원 : {0}개'.format(result))
money -= result*10000
result = money // 5000
print('5000원 : {0}개'.format(result))
money -= result*5000
result = money // 1000
print('1000원 : {0}개'.format(result))
money -= result*1000
result = money // 500
print('500원 : {0}개'.format(result))
money -= result*500
result = money // 100
print('100원 : {0}개'.format(result))
money -= result*100
result = money // 50
print('50원 : {0}개'.format(result))
money -= result*50
result = money // 10
print('10원 : {0}개'.format(result))
money -= result*10
result = money // 5
print('5원 : {0}개'.format(result))
money -= result*5
result = money // 1
print('1원 : {0}개'.format(result))
money -= result*1