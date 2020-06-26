

'''
count = 1
while count < 101:
    print(count)
    count += 1
'''

# 打印 1+2+3......100 的结果：
'''
count = 1
sum = 0
while count < 101:
    sum = sum + count
    count += 1
print(sum)
'''

# break:循环中遇到 break 直接退出循环。
'''
while True:
    print('狼的诱惑')
    print('我们不一样')
    break
    print('人间')
print(111)
'''

# 打印 1-100 所有的偶数的和：
'''
count = 1
s = 0

while True:
    if count % 2 == 0:
        s = s + count
    count += 1
    if count == 101:
        break
print(s)
'''

# 另一种方法：
'''
count = 2
s = 0
while True:
    s = s + count
    count = count + 2
    if count == 102:
        break
print(s)
'''

# continue 退出本次循环，继续下一次循环
'''
flag = True
while flag:
    print(111)
    print(222)
    flag = False
    continue
    print(333)
'''

# while else:   while 循环如果被 break 打断，则不执行 else 语句。
'''
count = 1
while count < 5:
    print(count)
    if count == 2:
        break
    count = count + 1
else:
    print(666)
'''

