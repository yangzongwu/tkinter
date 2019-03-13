#Auther:YZW
print('hello word')
'''
文件操作流程：
    打开，得到的文件句柄并赋值给一个变量
    操作
    关闭
'''
data=open('yesterday',encoding='utf-8').read()
print(data)

f=open('yesterday','r',encoding='utf-8')#内存对象，文件句柄#r是只读
data=f.read()#读完之后关标在最后
print('data',data)
data2=f.read() #会从第一次结束点读，所以是空的
print('data2',data2)
f.close()

f=open('yesterday','w',encoding='utf-8')#内存对象，文件句柄
f.write('1 wo ai bei jing tian an men\n')
f.write('2 wo ai bei jing tian an men\n')
f.write('3 wo ai bei jing tian an men\n')
f.write('4 wo ai bei jing tian an men\n')
f.write('5 wo ai bei jing tian an men\n')
f.write('6 wo ai bei jing tian an men\n')
f.write('7 wo ai bei jing tian an men\n')
#w是创建一个文件，覆盖之前的，之前数据会丢失
f.close()

f=open('yesterday','a',encoding='utf-8')#a追加 不能读取
f.write('last line')
#data=f.read()
#print('--read',data)
f.close()

#打印前5行
print('--------#打印前5行-----------')
f=open('yesterday','r',encoding='utf-8')
print(f.readlines())
f.close()

#只能读取一次，第二次使用f就是空的，需要重新读取
print('--------#打印前5行02-----------')
f=open('yesterday','r',encoding='utf-8')
for i in range(5):
    print('---',f.readline())
f.close()

print('--------#打印前5行03-----------')
#只能读取一次，第二次使用f就是空的，需要重新读取
f=open('yesterday','r',encoding='utf-8')
for line in f.readlines():
    print('---',line)
f.close()

#如果文件特别大，比如几个G，怎么办？ f.readlines只适合读取小文件，每次读取释放一行
print('--------#打印大文件-----------')
f=open('yesterday','r',encoding='utf-8')
count=0
for line in f:
    count += 1
    if count==3:
        print('-----------------------')
        continue
    print(line,'---')
f.close()


#tell打印当前位置，seek回到指定位置
f=open('yesterday','r',encoding='utf-8')
print('打印句柄指针地址',f.tell())
print(f.read(3))
print(f.readline())
print(f.readline())
print('打印句柄指针地址',f.tell())
f.seek(0)
print('打印句柄指针地址',f.tell())
print(f.readline())
f.close()


f=open('yesterday','r',encoding='utf-8')
print(f.encoding) #utf-8
print(f.fileno()) #3，操作系统一个编号文件
print(f.name)#yesterday 打印名字
print(f.seekable())#True,有的文件指针是无法移动回去
print(f.readable())#是否可读
print(f.writable())#是否可写
f.close()


f=open('yesterday','r',encoding='utf-8')
print(f.flush())#刷新 数据到达一定大小一次性刷
f.close()
#要求数据实时一致性 flush
import sys,time
for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.05)


f=open('yesterday','a',encoding='utf-8')
f.seek(10)#移动没用，都是从头开始截断
f.truncate(100)#文件保存
f.close()

#读写
f=open('yesterday','r+',encoding='utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write('-----------------') #写在了文档最后面
print(f.readline())
f.close()

'''
1 wo ai bei jing tian an men
2 wo ai bei jing tian an men
3 wo ai bei jing tian an men
4 wo ai be-----------------
'''

#写读
f=open('yesterday','w+',encoding='utf-8')
f.write('first line\n')
f.write('second line\n')
f.write('third line\n')
f.write('fourth line\n')
print(f.tell())
f.seek(10)
print(f.tell())
print(f.readline())
print(f.tell())
f.write('new arrive\n')#写在了文档最后面
f.close()

'''
f=open('yesterday','r+',encoding='utf-8')#读写
f=open('yesterday','w+',encoding='utf-8')#写读
f=open('yesterday','a+',encoding='utf-8')#文件句柄，追加读写
f=open('yesterday','rb',encoding='utf-8')#文件句柄，二进制
    f=open('yesterday','rb')
    f.write('hello\n'.encode())
    f.close()
'''



f=open('old_file','r',encoding='utf-8')
f_new=open('new_file','w',encoding='utf-8')

for line in f:
    if 'fourth line' in line:
        line=line.replace('fourth line','replace line')
    f_new.write(line)
f.close()
f_new.close()


#with自动关闭,可以同时打开多个文件
with open('yesterday','r') as f:
    print(f.readline())
#python 官方规范一行代码不超过80字符
with open('old_file','r',encoding='utf-8') as old, \
        open('new_file','r',encoding='utf-8') as new:
    pass
