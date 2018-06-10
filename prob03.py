s ="/usr/local/bin/python"

s1 = s.strip('/')
s1 = s1.split('/')
print(s1)

index = s.rindex('/')
s2 = []
s2.append(s[:index])
s2.append(s[index+1:])
print(s2)