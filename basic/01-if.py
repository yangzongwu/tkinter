#Auther:YZW
print('hello word')

import getpass
_username='alex'
_password='abc123'
username=input('username:')
password=input('password:')
#password=getpass.getpass('password') pycharm 不好用
if _username==username and _password==password:
    print("Welcome User{name} login...".format(name=username))#python 需要缩进4个空格
else:
    print('Invalid username or password')

'''
guess year old game
'''
age_of_oldboy=56
guess_age=int(input('guess oldboy_age:'))
if guess_age==age_of_oldboy:
    print('yes, you got it')
elif guess_age>age_of_oldboy:
    print('think smaller..')
else:
    print('think older...')
