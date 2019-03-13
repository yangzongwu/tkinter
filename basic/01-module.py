#Auther:YZW
print('hello word')
'''
模块，也叫库，有两种：
    标准库，默认
    第三方库，必须下载安装
'''
import sys
print(sys.path)
#['C:\\Users\\yzw\\Desktop\\python\\day2',
#打印一python的全局环境变量，存的路径
# 'C:\\Users\\yzw\\Desktop\\python',
# 'C:\\Users\\yzw\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip',
# 'C:\\Users\\yzw\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs',
# 'C:\\Users\\yzw\\AppData\\Local\\Programs\\Python\\Python37-32\\lib',
# 'C:\\Users\\yzw\\AppData\\Local\\Programs\\Python\\Python37-32',
# 'C:\\Users\\yzw\\Desktop\\python\\venv',
# 'C:\\Users\\yzw\\Desktop\\python\\venv\\lib\\site-packages',
# 'C:\\Users\\yzw\\Desktop\\python\\venv\\lib\\site-packages\\setuptools-39.1.0-py3.7.egg',
# 'C:\\Users\\yzw\\Desktop\\python\\venv\\lib\\site-packages\\pip-10.0.1-py3.7.egg']
print(sys.argv)
#['C:/Users/yzw/Desktop/python/day2/module.py']
#打印相对路径


import os
#与操作系统交互
os.system('dir')
#返回该目录下文档
cmd_res=os.system('dir')
print('-->',cmd_res)#输出0
#os.system执行命令，不保存结果，0是标志吗，0表示成功，1表示失败
#如何保存呢
cmd_res=os.popen('dir').read()
print('-->',cmd_res)


#第三方库

