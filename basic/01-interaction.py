#Auther:YZW
print('hello word')
'''
用户输入

'''
name=input("username:")
password=input("password:")
print(name,password)
info='''
-------info of $--------
Name:
Age:
Job:
Salary:
'''
#格式化输出，如何打印
name=input('name:')
age=input('age:')
job=input('job')
salary=input('salary')
print(info)

#方法一
info='''
-------info of'''+name+'''--------
Name:'''+name+'''
Age:'''+age+'''
Job:'''+job+'''
Salary:'''+salary+'''
'''
print(info)

#方法二：格式化输入，%s s表示string， %d d表示数字
info='''
-------info of %s--------
Name:%s
Age:%s
Job:%s
Salary:%s
'''% (name,name,age,job,salary)
print(info)

#方法二：格式化输入，%s s表示string， %d
#上述也没有报错，%d 可以用于检验
info='''
-------info of %s--------
Name:%s
Age:%f
Job:%s
Salary:%s
'''% (name,name,age,job,salary)
print(info)
#注意上述age报错，因为input默认输入是字符串
age=int(input('age:')) #integer
info='''
-------info of %s--------
Name:%s
Age:%f
Job:%s
Salary:%s
'''% (name,name,age,job,salary)
print(info)

#格式化方法三
name=input('name:')
age=input('age:')
job=input('job')
salary=input('salary')
info='''
-------info of {_name}--------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)
print(info)

#格式化方法四 不建议使用
name=input('name:')
age=input('age:')
job=input('job')
salary=input('salary')
info='''
-------info of {0}--------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
print(info)

#password
username=input('username:')
password=input('password:')
print(username,password)
#有专门的库，需要导入
import getpass
password=getpass.getpass('password')
print(username,password)
