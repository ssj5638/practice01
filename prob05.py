s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
result= {}
cnt = 1
s = s.upper().replace('\n',' ').replace(',','').replace('.','')
lst = s.split(' ')
result = set(lst)
result = sorted(result)

for a in result:
    print(a)