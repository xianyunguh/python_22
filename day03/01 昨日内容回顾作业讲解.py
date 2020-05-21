# 7.使用 while 循环输出 1 2 3 4 5 6 8 9 10 （注意少一个7）
'''
count = 1
while count < 11:
    if count == 7:
        print('')
    else:
        print(count)
    count += 1
'''

'''
count = 1
while count < 11:
    if count == 7:
        pass
    else:
        print(count)
    count += 1
'''
'''
count = 1
while count < 11:
    if count == 7:
        count += 1
    print(count)
    count += 1
'''

'''
count = 0
while count < 10:
    count += 1
    if count == 7:
        continue
    print(count)
'''