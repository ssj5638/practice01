'''
반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
출력해보세요. 1부터 99까지만 실행하세요.
'''

for a in range(1, 100):
    b = str(a)
    if len(b)==1:
        if str(3) in b or str(6) in b or str(9) in b:
            print(b, ' 짝')
    elif len(b)==2:
        c, d = b[0],b[1]
        if str(3) in c or str(6) in c or str(9) in c:
            if str(3) in d or str(6) in d or str(9) in d:
                print(b, ' 짝짝')
            else:
                print(b, ' 짝')
        elif str(3) in d or str(6) in d or str(9) in d:
            print(b, ' 짝')