"""
copyright@yinwuhui
version:1.0
date:2021.05.13
modify infor: first create
"""
sum = 0
for i in range(100):
    sum += i
    print(sum)
print(sum)

for i in range(2, 101, 2):
    sum += i
    print(sum)
print(sum)

for i in range(100, 1, -1):
    sum += i
    print(i)
print(sum)