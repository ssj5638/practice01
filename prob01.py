# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
a = input('수를 입력하세요 : ')
print(a)

if a.isdigit()==True:
    str = (int(a) % 3 == 0) and "3의 배수 입니다." or "3의 배수가 아닙니다."
    print(str)
else:
    print("정수가 아닙니다.")