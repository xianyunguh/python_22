# msg = '''-------- info of 太白金星 --------
# name : 太白金星
# age  : 18
# job  : Teacher
# Hobbie: girl
# -------- end --------'''
# print(msg)

# 制作一个公共的模板
# 让一个字符串的某些位置变成动态可传入的。
# 格式化输出
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
job = input('请输入你的工作：')
hobby = input('请输入你的爱好：')
# % 占位符 s --> str d i r
msg = '''
-------- %s --------
姓名： %s
年龄： %s
工作： %s
爱好： %s
-------- end --------''' %(name,name,age,job,hobby)
print(msg)