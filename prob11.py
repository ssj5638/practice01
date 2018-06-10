'''
함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.
'''
def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

result1 = sum(80,85,90,95,100)
result2 = sum(55,1,23,36,75,92)

print(result1)
print(result2)