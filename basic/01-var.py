#Auther:YZW
print('hello word')
'''
变量：
如何定义变量
变量名=变量值  name='dog'
C 语言  string name='dog'; 需要什么数据类型，但是python不需要提前声明
'''

#name2直接指向name所指向的内存地址X，而不是指向name
#name改变的时候，name指向新的内存地址Y，name2仍指向内存地址X
name='dog'
name2=name
print('My name is',name,name2) #My name is dog dog
name='cat'
print('My name is',name,name2) #My name is cat dog

'''
变量定义规则：
    变量名只能是字母，数字或者下划线的任意组合
    变量名的第一个字符不能是数字
    关键字符不能声明为变量
约定俗成：
    定义a,b,c,a1,b1..... 不建议
    变量名需要有含义， name, job,age
    变量名不建议用中文，可以用中文   姓名='dog'
    变量名不建议用拼音， xingming='dog'
    
    不建议：gfofoldboy 
    方式一：gf_of_oldboy 中间加下划线
    方式二：GFOfOldboy   每个单词第一个字符大写
    
变量与常量
    python 中没有常量的概念
    如果想要表示常量， PIE全部用大写写，表示你不应该该，但是实际还是可以改写的
'''

#Auther:YZW
print('hello word')

def change_name(name):
    print('before change',name)
    name='ALEX LI'
    print('after change',name)

test_name='alex' #全局变量
change_name(test_name)
print(test_name)
#before change alex
# after change ALEX LI
# alex

test_name='alex' #全局变量
def change_name(name):
    global test_name
    test_name='ALEX LI'
    print('after change',test_name)


change_name(test_name)
print(test_name)
#after change ALEX LI
#ALEX LI
