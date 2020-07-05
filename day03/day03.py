# 1、 将 0001 1010 转换成十进制。
# =1*2**4+1*2**3+0*2**2+1*2**1+0
# =16+8+2
# =26

# 2、 将 42 转换成二进制。
# 0010 1010

# 3、 显示 4、5、42,转换成二进制后的长度。
# s1 = 4
# s2 = 5
# s3 = 42
# print(s1.bit_length())
# print(s2.bit_length())
# print(s3.bit_length())

# 4、 bool str int 三种类型互换。
# s1 = True
# s2 = '100'
# s3 = 10
# print(str(s1),int(s1))
# print(bool(s1),int(s2))
# print(bool(s3),str(s3))

# 5、 判断，用户有输入显示 “有内容”， 没输入内容，显示 “无内容” 。
# s1 = input('请输入内容：')
# if s1:
#     print('有内容')
# else:
#     print('无内容')

# 6、写出下列变量 s2、s3、s4、s5、s6、s7、s8的值
# s1 = 'python全栈22期'
# s2 = s1[0]  # p
# print(s2,type(s2))
# s3 = s1[2]  # t
# print(s3)
# s4 = s1[-1]  # 期
# print(s4)
# s5 = s1[0:6]  # python
# s5 = s1[:6]  # python
# print(s5)
# s6 = s1[6:]  # 全栈22期
# print(s6)
# s7 = s1[:5:2]  # pto
# print(s7)
# print(s1[:])    # python全栈22期
# s8 = s1[-1:-6:-1]  # 期22栈全
# print(s8)
# s11 = s[4:0:-1]
# print(s11)
# s12 = s[3::-1]
# print(s12)
# s13 = s[3::-2]
# print(s13)
# s = 'ABCDLSESRF'
# s14 = s[-1::-1]
# print(s14)
# s15 = s[::-1]
# print(s15)

# 7、倒序全部取出来： 'taiBAIfdsa'
# s = 'taiBAIfdsa'
# t = len(s) + 1
# s1 = s[-1:-t:-1]
# print(s1)

# s = 'taiBAIfdsa'
# s1 = s[-1::-1]
# print(s1)

# 8、将变量 s 转换成全部大写、全部小写
# s = 'taiBAIfdsa'
# print(s.upper())
# print(s.lower())

# 9、判断用户登陆、验证码不区分大小写。
# username = 'liu'
# password = '123456'
# code = 'Abc'
# while True:
#     usernamex = input('请输入用户名：')
#     passwordx = input('请输入密码：')
#     codex = input('请输入验证码：')
#     if codex.upper() == code.upper():
#         if usernamex == username and passwordx == password:
#             print('登陆成功')
#         else:
#             print('用户名或密码错误')
#     else:
#         print('验证码错误')

# 10、判断变量 s 是不是 t 开头，是不是 taiBAI 开头，3至6的字符是不是以 B 开头。
# s = 'taiBAIfdsa'
# print(s.startswith('t'))
# print(s.startswith('taiBAI'))
# print(s.startswith('B',3,6))

# 11、现有变量  msg = 'alex 很nb,alex是老男孩教育的创始人之一，alex长得很帅'
#  将其中的 'alex' 全部替换成 '太白' ; 将其中的前两个 'alex' 替换成 '太白'
# msg = 'alex 很nb,alex是老男孩教育的创始人之一，alex长得很帅'
# msg1 = msg.replace('alex','太白')
# msg2 = msg.replace('alex','太白',2)
# print(msg)
# print(msg1)
# print(msg2)

# 12、去掉变量  s4 = ' \n太r白\t'  的前后空白字符，只去除其中的部分字符：qrsed
# s4 = ' \n太r白\t'
# s5 = s4.strip()
# s6 = 'qr太rs白ed'
# s7 = s6.strip('qrsed')
# print(s4)
# print(s5)
# print(s6)
# print(s7)


# 13、按 ： 对变量 s6 = '太白:女神:吴超' 进行分隔
# s6 = '太白:女神:吴超'
# s7 = s6.split(':')
# print(s7)


# 14、 按 ： 对变量 s6 = ':barry:nvshen:wu:liu' 进行分隔；按 ： 对变量 s6 只分隔前两个。
# s6 = ':barry:nvshen:wu:liu'
# s7 = s6.split(':',2)
# print(s7)

# 15、用 + 连接 s1 = 'alex' 的每一个字母。
# s1 = 'alex'
# s2 = '+'.join(s1)
# print(s2)

# 16、 用 ： 连接 列表 l1 = ['太白','女神','吴超'] 的各个元素。
# l1 = ['太白','女神','吴超']
# l2 = ':'.join(l1)
# print(l2)

# 17、读懂下列语句
# s1 = '老男孩edu'
# print('老' in s1)
# print('老男' in s1)
# print('老ed' in s1)
# print('老ed' not in s1)

# 18、用while迭代打印 s1 = '老男孩教育最好的讲师：太白'
# s1 = '老男孩教育最好的讲师：太白'
# index = 0
# while index <= len(s1)-1:
#     print(s1[index])
#     index = index + 1

# 19、用for迭代打印 s1 = '老男孩教育最好的讲师：太白'
# s1 = '老男孩教育最好的讲师：太白'
# for i in s1:
#     print(i)

# 20、用for迭代打印 s1 = '老男孩教育最好的讲师：太白' ,只打印至 '好'，余下的不打。
# s1 = '老男孩教育最好的讲师：太白'
# for i in s1:
#     if i == '的':
#         break
#     print(i)

# 21、有字符串 s = '123a4b5c'
# s = '123a4b5c'
# # 通过对 s 切片形成新的字符串 s1, s1 = '123'
# s1 = s[:3]
# print(s1)
# # 通过对 s 切片形成新的字符串 s2, s2 = 'a4b'
# s2 = s[3:6]
# print(s2)
# # 通过对 s 切片形成新的字符串 s3, s3 = '1345'
# s3 = s[:7:2]
# print(s3)
# # 通过对 s 切片形成新的字符串 s4, s4 = '2ab'
# s4 = s[1:6:2]
# print(s4)
# # 通过对 s 切片形成新的字符串 s5, s5 = 'c'
# s5 = s[-1]
# print(s5)
# # 通过对 s 切片形成新的字符串 s6, s6 = 'ba2'
# s6 = s[-3::-2]
# print(s6)

# 22、有变量name = "aleX leNb" 完成如下操作：
# name = "aleX leNb"
# # 移除 name 变量对应的值两边的空格, 并输出处理结果
# namex = name.strip()
# print(namex)
# # 判断 name 变量是否以 "al" 开头, 并输出结果
# print(name.startswith('al'))
# # 判断 name 变量是否以 "Nb" 结尾, 并输出结果
# print(namex.endswith('Nb'))
# # 将 name 变量对应的值中的所有的 "l" 替换为 "p", 并输出结果
# print(namex.replace('l','p'))
# # 将name变量对应的值中的第一个 "l" 替换成 "p", 并输出结果
# print(namex.replace('l','p',1))
# # 将 name 变量对应的值根据所有的 "l" 分割, 并输出结果。
# print(namex.split('l'))
# # 将name变量对应的值根据第一个 "l" 分割, 并输出结果。
# print(namex.split('l',1))
# # 将 name 变量对应的值变大写, 并输出结果
# print(namex.upper())
# # 将 name 变量对应的值变小写, 并输出结果
# print(namex.lower())
# # 判断 name 变量对应的值字母 "l" 出现几次，并输出结果
# print(namex.count('l'))
# # 判断 name 变量对应的值前四位 "l" 出现几次, 并输出结果
# print(namex.count('l',4))
# # 请输出 name 变量对应的值的第 2 个字符?
# print(namex[2])
# # 请输出 name 变量对应的值的前 3 个字符?
# print(namex[:3])
# # 请输出 name 变量对应的值的后 2 个字符?
# print(namex[-2:])

# 23、有字符串 s = "123a4b5c"
# s = "123a4b5c"
# # 通过对 s 切片形成新的字符串 s1, s1 = "123"
# s1 = s[:3]
# print(s1)
# # 通过对 s 切片形成新的字符串 s2, s2 = "a4b"
# s2 = s[3:6]
# print(s2)
# # 通过对 s 切片形成新的字符串 s3, s3 = "1345"
# s3 = s[::2]
# print(s3)
# # 通过对 s 切片形成字符串 s4, s4 = "2ab"
# s4 = s[1:6:2]
# print(s4)
# # 通过对 s 切片形成字符串 s5, s5 = "c"
# s5 = s[-1:]
# print(s5)
# # 通过对 s 切片形成字符串 s6, s6 = "ba2"
# s6 = s[-3:-8:-2]
# print(s6)

# 24、使用 while 和 for 循环分别打印字符串 s = "asdfer" 中每个元素。
# s = "asdfer"
# index = 0
# while index < len(s):
#     print(s[index])
#     index +=1
#
# for i in s:
#     print(i)

# 25、使用for循环对 s = "asdfer" 进行循环，但是每次打印的内容都是 "asdfer"。
# s = "asdfer"
# for i in s:
#     print(s)

# 26、使用for循环对 s = "abcdefg" 进行循环，每次打印的内容是每个字符加上 sb， 例如：asb, bsb，csb, ...gsb。
# s = "abcdefg"
# for i in s:
#     print(i+'sb')

# 27、使用for循环对 s = "321" 进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s = "321"
# for i in s:
#     print("倒计时{x}秒" .format(x=i))
# print("出发")

# 28、实现一个整数加法计算器(两个数相加)：
# while True:
#     x = int(input("请输入一个数："))
#     y = int(input("再输入一个数："))
#     xy = x + y
#     print('结果是：{s}' .format(s=xy))

# 29、如：content = input("请输入内容:")
# 用户输入：5 + 9
# 或5 + 9
# 或5 + 9，然后进行分割再进行计算。
# content = input("请输入内容:")
# l = content.split('+')
# print('{m}的计算结果：{n}' .format(m=content,5+9n=int(l[0])+int(l[1])))


# 30、** 选做题 **：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5 + 9 + 6 + 12 + 13，然后进行分割再进行计算。




# 计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：")  # 如fhdal234slfh98769fjdla


# ** 选做题 **：写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B, C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B, C选项。


# 写代码：计算 1 - 2 + 3... + 99 中除了88以外所有数的总和？



#  ** 选做题： ** 判断一句话是否是回文.回文: 正着念和反着念是一样的.例如, 上海自来水来自海上


# 3.制作趣味模板程序需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
# 如：敬爱可亲的xxx，最喜欢在xxx地方干xxx