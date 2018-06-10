menu = input('메뉴: ')

md = {'오뎅':300, '순대':400, '만두':500}

if md.get(menu) != None:
    price = md[menu]

else:
    price = 0

print('가격: {0}'.format(price))
