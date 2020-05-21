# 1、用while循环写用户登陆（用户名、密码、验证码），3次不成功则退出。
"""
count = 0
namex = 'liu'
passwordx = '123456'
codex = 'aaa'
while count < 3:
    name = input('请输入用户名：')
    password = input('请输入密码：')
    code = input('请输入验证码：')
    if code == codex:
        if name == namex and password == passwordx:
            print('登陆成功')
        else:
            print('用户名或密码错误')
    else:
        print('验证码错误')

    count += 1
"""

# 2、打印 1-100 所有的数字
'''
count = 1
while count < 101:
    print(count)
    count += 1
'''

# 3、打印 1+2+3......100 的结果：
'''
count = 1
sum = 0
while count < 101:
    sum = sum + count
    count += 1
print(sum)
'''

# 4、打印 1-100 所有偶数的和：
'''
count = 2
sum = 0
while count < 102:
    sum = sum + count
    count = count + 2
print(sum)
'''

# 5、continue 退出本次循环，继续下一次循环
'''
count = 0
sum = 0
while count < 101:
    count = count + 1
    if count % 2:
        continue
    sum = sum + count
print(sum)
'''

# 6、while else:   while 循环如果被 break 打断，则不执行 else 语句。

# 7、制作一个公共的模板，让一个字符串的某些位置变成动态可传入的。
"""
-------- info of 太白金星 --------
name : 太白金星
age  : 18
job  : Teacher
Hobbie: girl
-------- end --------
"""
"""
name = input('请输入姓名：')
age = input('请输入年龄：')
job = input('请输入工作：')
hobbie = input('请输入爱好：')
msg = '''
-------- info of %s --------
name : %s
age  : %s
job  : %s
Hobbie: %s
-------- end --------
''' %(name,name,age,job,hobbie)

print(msg)
"""

# 8、用占位符 % 输出 ”我叫 太白金星, 今年 18, 学习进度 1%" ,其中 1%不用占位符
'''
name = input('请输入姓名：')
age = input('请输入年龄：')
msg = "我叫 %s，今年 %s，学习进度 1%%。" %(name,age)
print(msg)
'''

# 9、判断下面的打印结果：
"""
i1 = 2
i2 = 3
print(2 ** 3)
print(10//3)
print(10 % 3)

print(3 != 4)

count = 1
count = count + 1
count += 1
print(count)
"""

# 10、 判断下面的打印结果：
'''
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
print(True or False)
'''

# 11、判断打印结果：
'''
print(1 or 2)
print(3 or 2)
print(4 or 2)
print(-1 or 2)
print(0 or 2)
print(1 and 2)
'''

# 12、判断结果：
'''
s1 = '00100'
print(int(s1))

i1 = 100
print(str(i1),type(str(i1)))

i = 0
print(bool(i))
print(int(True)) 
print(int(False)) 
'''

# 13、判断结果：
'''
print(3 and 9)
print(1 and 2 or 3 and 4)
'''

# 14、判断结果：
'''
print(1 > 2 and 3 or 6)
print(2**32)
print(7.6 * 1024 * 1024 * 8)
'''

# Day2作业

# 1.判断下列逻辑语句的True, False.
'''
1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
= False or  True or False and True and True or True
= False or True or False and True or True 
= False or True or False or True
= True or False or True
= True or True
= True
'''

'''
2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
= not True and True or False and True and True or False
= False and True or False and True and True or False
= False or False and True and True or False
= False or False and True or False
= False or False or False
= False or False
= False
'''

# 2.求出下列逻辑语句的值。
'''
1), 8 or 3 and 4 or 2 and 0 or 9 and 7
= 8 or 4 or 0 or 7
= 8 or 0 or 7
= 8 or 7
= 8
'''

'''
2), 0 or 2 and 3 and 4 or 6 and 0 or 3
= 0 or 3 and 4 or 0 or 3
= 0 or 4 or 0 or 3
= 4 or 0 or 3
= 4 or 3
= 4
'''

# 3.下列结果是什么？
# 1)、6 or 2 > 1   # 6
# 2)、3 or 2 > 1   # 3
# 3)、0 or 5 < 4   # False
# 4)、5 < 4 or 3   # 3
# 5)、2 > 1 or 6   # Ture
# 6)、3 and 2 > 1  # Ture
# 7)、0 and 3 > 1  # 0
# 8)、2 > 1 and 3  # 3
# 9)、3 > 1 and 0  # 0

# 10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2  #
# = 1 and 2 or 1 and 4 or 1
# = 2 or 4 or 1
# = 2 or 1
# = 2

# 4.while循环语句基本结构？
# while 条件：
#     循环体

# 5.利用while语句写出猜大小的游戏：
'''
设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
如果比66小，则显示猜测的结果小了;
只有等于66，显示猜测结果正确，然后退出循环。
'''

'''
s = 66

while True:
    t = int(input('请输入一个数：'))
    if t > 66:
        print('太大了')
    elif t < 66:
        print('太小了')
    else:
        print('恭喜你，猜对了！')
        break
'''

# 6.在5题的基础上进行升级：
'''
给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，
如果三次之内没有猜测正确，则自动退出循环，并显示‘太笨了你....’。
'''

'''
s = 66
count = 0
while True:
    count += 1
    t = int(input('请输入一个数：'))

    if count == 3 and t != 66:
        print('太笨了...')
        break
    elif t > 66:
        print('太大了')
    elif t < 66:
        print('太小了')
    else:
        print('恭喜你，猜对了！')
        break
'''


# 7.使用while循环输出
'''
1
2
3
4
5
6
8
9
10
'''

'''
count = 1
while count < 11:
    print(count)
    count += 1
'''

# 8.求1 - 100的所有数的和
'''
s = 1
sum = 0
while s < 101:
    sum = sum + s
    s += 1
print(sum)
'''

# 9.输出1 - 100内的所有奇数
'''
s = 1
sum = 0
while s < 101:
    sum = sum + s
    s = s + 2
print(sum)
'''

# 10.输出1 - 100内的所有偶数
'''
s = 2
sum = 0
while s < 101:
    sum = sum + s
    s = s + 2
print(sum)
'''

# 11.求 1 - 2 + 3 - 4 + 5...99 的所有数的和
'''
count = 1
s = 0
while count < 100:
    if count % 2:
        s = s + count
    else:
        s = s - count
    count += 1
print(s)
'''

# 12.用户登录（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
'''
count = 1
x = 3
while count <= 3:
    name = input('请输入用户名：')
    password = input('请输入密码：')
    code = input('请输入验证码：')
    if code == 'aaa':
        if name == 'liu' and password == '123':
            print('登陆成功')
            break
        else:
            print('用户名或密码错误')
    else:
        print('验证码错误')

    count += 1
    x = x - 1
    print('你还有 %d 次机会。' %(x))
'''

# 13.简述ASCII、Unicode、utf - 8编码
'''
ASCII：只包含英文字母，数字，特殊字符。均占8位（1字节）
Unicode：万国码，包括世界上所有的文字，不论中文、英文或符号，每个字符均占32位（4字节）。
        浪费空间，浪费资源。
utf - 8：万国码升级版，英文占8位（1字节）、欧洲字符占16位（2字节）、中文字符站24位（3字节）
'''

# 14.简述位和字节的关系？
# 8位 = 1字节


