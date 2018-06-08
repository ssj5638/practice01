money = input('금액 : ')

def count (some):
    if some > 0:
        return some//5, some%5

for a in money:
    a = int(a)
    print(count(a))