'''
주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
주어진 리스트에서 3의 배수의 개수=> 6
주어진 리스트에서 3의 배수의 합=> 150
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0
sum = 0

for a in lst:
    if a%3 == 0:
        cnt = cnt +1
        sum += a

print('주어진 리스트에서 3의 배수의 개수 => ', cnt)
print('주어진 리스트에서 3의 배수의 함 => ', sum)