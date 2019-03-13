#Auther:YZW
print('hello word')
#字符串操作
name='my \tname is {name},{year} years old'
print(name.capitalize()) #My 	name is {name},{year} years old
print(name.count('a')) #4
print(name.center(50,'-'))#-------my 	name is {name},{year} years old--------
print(name.endswith('ex'))#False 字符串以什么结尾
print(name.expandtabs(tabsize=10))#my        name is {name},{year} years old
print(name.find('name'))#4
print(name[name.find('name'):9])#name
print(name.format(name='Alex',year=23))#my 	name is Alex,23 years old
print(name.format_map({'name':'alex1','year':12}))#my 	name is alex1,12 years
print(name.isalnum())#False 是否阿拉伯数字和英文字符，有特殊字符False
print(name.isalpha())#False 纯英文字符
print('233'.isdecimal())#True  是否十进制
print('2e'.isdigit()) #False
print('1A'.isidentifier())#False 判断是否一个合法的标识符/变量名

name='sdfd123'
print(name.islower()) #True
print(name.isnumeric()) #False
print(' '.isspace())#True
print('My Name Is '.istitle())#True
print(name.isupper())#False

print(''.join(['1','a','2']))#1a2
print(name.join('=='))#=sdfd123= 注意

print(name.ljust(20,'*'))#sdfd123*************长度20 用*补
print(name.rjust(20,'*'))#*************sdfd123

print(name.lower()) #sdfd123
print(name.upper()) #SDFD123
print(' sdfd123 '.lstrip()) #去左边空格
print(' sdfd123 '.rstrip()) #去右边空格
print('ss sdfd123\n'.strip())#去空格

p=str.maketrans('abcdef','123456')
print('alex li'.translate(p))#1l5x li

print('alex li'.replace('l','L'))#aLex Li
print('alex li'.replace('l','L',1))#aLex li
print('alex li'.rfind('l'))#找最右边值的下标返回
print('alex li'.split()) #['alex', 'li']
print('alex li'.split('l'))#['a', 'ex ', 'i']
print('1+2\n+3+4'.splitlines())#['1+2', '+3+4'] 按照换行分
print('alex li'.swapcase())#ALEX LI
print('alex li'.title())#Alex Li
print('Alex Li'.zfill(20))#0000000000000Alex Li 自动补位
