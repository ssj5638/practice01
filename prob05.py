s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
result= {}
cnt = 1
s = s.upper().replace('\n',' ').replace(',','').replace('.','')
lst = s.split(' ')
result = sorted(set(lst))
for a in range(len(result)):
    print(result[a])

print('--------------')
result = list(result)
lst_dict = {}
for keys in result:
    lst_dict[keys] = 0
for values in lst:
    lst_dict[values] += 1
for key, value in lst_dict.items():
    print(key, ":", value)