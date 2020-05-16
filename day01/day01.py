# 1、打印 'hello world 老铁'
# print('hello world 老铁')

# 2、打印 1+2+3+4+5 的和。
# print(1+2+3+4+5)

# 3、用变量打印 1+2+3+4+5 ，（1+2+3+4+5)*3/2， (((1+2+3+4+5)*3/2）+100）/24

"""
num = 1+2+3+4+5
num2 = num*3/2
num3 = (num2+100)/24
print(num,num2,num3)
"""

# 4、下列变量定义，哪些是合法的，哪些是不合法的。
"""
x8 = 100
b__ = 12
4g = 32  # False
_ = 11
*r = 12   # False
r3t4 = 10
t_ = 66
"""

# 5、下面的程序输出结果是什么？
'''
age1 = 18
age2 = age1
age3 = age2
age2 = 12
print(age1,age2,age3) 
'''

# 6、定义并打印一个常量
'''
NAME = 'taibai'
print(NAME)
'''

# 7、下面的程序输出结果是什么？
'''
i = 100
i1 = 2
i2 = i*i1
print(i2)
'''

# 8、分别用3个符号定义3个字符变量
"""
str1 = '你好'
str2 = "你好"
str3 = '''你好'''
"""

# 9、定义字符变量，变量的值是：I'am taibai, 18 years old.
'''
str = "I'am taibai, 18 years old."
print(str)
'''

# 10、用一首诗做为一个变量的值，并打印这个变量。
"""
msg ='''
白日依山尽，
黄河入海流。
欲穷千里目，
更上一层楼。
'''
print(msg)
"""

# 11、定义2个字符变量，验证字符串的 +，* 两种运算。
'''
str1 = 'aaa'
str2 = 'bbb'
print(str1+str2)
print(str1*8)
'''

# 12、说出下面的打印结果：
'''
print(2 > 1)
print(3 < 1)
print(True)
print('True')
'''

# 13、验证： input: 出来的全部都是字符串类型。
'''
str1 = input('请输入：')
print(str1,type(str1))
'''

# 14、让用户输入姓名、年龄、性别，然后打印一句话‘我叫：  ，今年： ，性别： ’
'''
name = input('姓名：')
age = input('年龄：')
sex = input('性别：')

print('我叫：' + name + ', 今年' + age + ', 性别' + sex)
'''

# 15、输入年龄，如果大于18岁，打印'你已成年'，如果小于18岁，打印'小屁孩儿'
'''
age = input('请输入你的年龄：')

if int(age) > 18:
    print('你已成年')
else:
    print('小屁孩儿')
'''

# 16、猜数：如果是1，打印'晚上请吃饭'；如果是2，打印'请你大宝剑'；如果是3，打印'一起溜达'；如果都不是，则打印'你太笨了'
'''
num = int(input('请输入一个数字：'))

if num == 1:
    print('晚上请吃饭')
elif num == 2:
    print('请你大宝剑')
elif num == 3:
    print('一起溜达')
else:
    print('太笨了！')
'''

# 17、输入用户名、密码、验证码，判断条件，分别打印'用户名或密码错误'、'验证码错误'、'登陆成功'
'''
name = input('请输入用户名：')
password = input('请输入密码：')
code = input('请输入验证码：')

if code == 'aaa':
    if name == 'lhx' and password == '123456':
        print('登陆成功')
    else:
        print('用户名或密码错误。')
else:
    print('验证码错误')
'''

# 18、输入分数判断等级：A、B、C、D、太笨了...E,（90、80、70、60、60以下）
'''
num = int(input('请输入分数：'))
if num >= 90:
    print('A')
elif num >= 80:
    print('B')
elif num >= 70:
    print('C')
elif num >= 60:
    print('D')
else:
    print('E')
'''


# ---------------------------------
# Day1作业及默写

# 1.简述变量命名规范

# 2.name = input(“>>>”) name变量是什么数据类型？ 字符型

# 3.if条件语句的基本结构？
'''
单独if
if else 二选一
if elif elif .... 多选一
if elif elif .... else 多选一
嵌套的if
'''

# 4.用print打印出下面内容：
"""
msg = '''
文能提笔安天下, 
武能上马定乾坤. 
心存谋略何人胜, 
古今英雄唯是君.
'''
print(msg)
"""

# 5.利用if语句写出猜大小的游戏：
'''
设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
'''
'''
bingo = 66
num = int(input('请输入一个数：'))
if num > bingo:
    print('太大了')
elif num < bingo:
    print('太小了')
elif num == bingo:
    print('猜对啦')
'''

# 6.提示户输入他的年龄, 程序进行判断：
'''
如果小于10, 提示小屁孩, 
如果大于10, 小于20, 提示青春期叛逆的小屁孩. 
如果大于20, 小于30. 提示开始定性, 开始混社会的小屁孩儿, 
如果大于30, 小于40. 提示看老大不小了, 赶紧结婚小屁孩儿. 
如果大于40, 小于50. 提示家里有个不听话的小屁孩儿. 
如果大于50, 小于60. 提示自己马上变成不听话的老屁孩儿.
如果大于60, 小于70. 提示活着还不错的老屁孩儿. 
如果大于70, 小于90. 提示人生就快结束了的一个个老屁孩儿.
如果大于90以上.提示.再见了这个世界.
'''
'''
age = int(input('请输入你的年龄：'))

if age < 10:
    print('小屁孩')
elif 10 < age < 20:
    print('青春期叛逆的小屁孩儿')
elif 20 < age < 30:
    print('开始混社会的小屁孩儿')
elif 30 < age < 40:
    print('老大不小了，赶紧结婚小屁孩儿')
elif 40 < age < 50:
    print('家里有个不听话的小屁孩儿')
elif 50 < age < 60:
    print('马上变成不听话的老屁孩儿')
elif 60 < age < 70:
    print('活着还不错的老屁孩儿')
elif 70 < age < 90:
    print('人生就快结束了的一个老屁孩儿')
elif age > 90:
    print('再见了这个世界')
'''

# 7.单行注释以及多行注释？

# 8.简述你所知道的Python3x和Python2x的区别？
'''
在Python3x中，无论用户通过input功能输入什么内容，均视为字符串；
而在Python2x中，则视为表达式，若要在Python2x中也要将input输入的内容视为字符串，
则应该使用raw_input。
'''

# 9.提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对，提示输入有误
'''
test = input("请输入'麻花藤'这三个字：")
if test == '麻花藤':
    print('真聪明')
else:
    print('输入有误')
'''

# 10.用户输入一个月份，然后判断月份是多少月，根据不同的月份，打印出不同的饮食（根据个人习惯和老家习惯随意编写）
'''
str1 = input('请输入一个月份：')

if int(str1) == 1:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃aaa')
elif int(str1) == 2:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃bbb')
elif int(str1) == 3:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃ccc')
elif int(str1) == 4:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃ddd')
elif int(str1) == 5:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃eee')
elif int(str1) == 6:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃fff')
elif int(str1) == 7:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃ggg')
elif int(str1) == 8:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃hhh')
elif int(str1) == 9:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃iii')
elif int(str1) == 10:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃jjj')
elif int(str1) == 11:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃kkk')
elif int(str1) == 12:
    print('你输入的月份是' + str1 + '月,' + '这个月我们老家喜欢吃lll')
else:
    print('你输入的月份是不存在')
'''

# 11.用户输入一个分数，根据分数来判断用户考试成绩的档次
'''
num = int(input('请输入分数：'))

if num >= 90:
    print('A')
elif 90 >= num >= 80:
    print('B')
else:
    print('C')
'''

