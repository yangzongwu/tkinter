#Auther:YZW
print('hello word')

'''
编程的方法或者规范：
    1.面向对象   产品---->类--->class
    2.面向过程   产品---->过程--->def
    3.函数式编程 产品---->函数--->def
    
    
数学定义：y=2x
python定义：逻辑结构化和过程化的一种编程方法
def test(x):
    'The function definitions'
    x+=1
    return x
'''

def func1(): # 定义一个函数
    '''testing1'''
    print('in the func1')
    return 0

def func2(): #定义一个过程
    '''testing2'''
    print('in the func2')

#调用,过程和函数都可以调用，过程是没有返回值的函数
#在python中把过程也变为函数，没有特殊区别
x=func1()
y=func2()
print('From func1 return is %s' %x)
print('From func2 return is %s' %y)

#函数作用？
import time
def logger():
    time_format='%Y-%m-%d %X'
    time_current=time.strftime(time_format)
    with open('new_file','a+') as f:
        f.write('%s end action\n' %time_current)
def test2():
    print('in the test2')
    logger()
def test1():
    print('in the test1')
    logger()
def test3():
    print('in the test3')
    logger()
test1()
test2()
test3()



def test1():
    print('in the test1')
def test2():
    print('in the test2')
    return 0
def test3():
    print('in the test3')
    return 1,2,'hello',{'1':'a'},1 #以元组方式返回
x=test1()
y=test2()
z=test3()
print(x) #返回值=0 返回None
print(y) #返回值=1：返回object
print(z) #返回值>1:返回tuple

#参数函数  x,y 形参，1，2 实参
def test(x,y):
    print(x)
    print(y)
test(1,2) #与形参一一对应
test(y=2,x=1) #与形参顺序无关
#test(x=2,3) 报错
test(3,y=2)  #混合调用，关键字参数必须放在最后

'''
默认参数特点：调用函数的时候，默认参数非必需传递:
'''
def test(x,y=3):
    print(x)
    print(y)
test(1)

'''
可变参数
'''
def test(*args):
    print(args)
test(1,2,3,4,5)
test(*[1,2,3,4,5,6]) #*args=*[1,2,3,4,5,6] ,tuple

def test(x,*args):
    print(x)
    print(args) #(2, 3, 4, 5)
test(1,2,3,4,5)

#把N个关键字参数变为字典形式
def test(**args):#接受字典
    print(args)
test(name='alex',age=22) #{'name': 'alex', 'age': 22}
test(**{'name':'alex','age':22})  #{'name': 'alex', 'age': 22}

def test(name,**args):
    print(name)
    print(args)
test('alex')
#alex
# {}

def test(name,age=18,**args):
    print(name)
    print(age)
    print(args)
test('alex',sex='m',hobby='testla',age=20)
#alex
#20
#{'sex': 'm', 'hobby': 'testla'}


#*args:接收N个位置参数，转换为tuple
#**args:接收N个关键字参数，转换为dict


#高阶函数
def add(a,b,f):
    return f(a)+f(b)
res=add(3,-6,abs)
print(res)
