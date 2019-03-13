#Auther:YZW
print('hello word')
'''
数字：
    int   
        在32位机器：-2**31--2**31-1
        在64位机器：-2**63--2**63-1
        在python中如果超了，会自动编程长整型
        注意python3没有长整形，所有输出都是整形，python2.7有长整形概念，其他语言有，超出报错
    long 长整形
    float 浮点数
    complex 复数
'''
print(type(2))#<class 'int'>
print(type(2**32))#<class 'int'>
print(type(2**99))#<class 'int'>
'''
布尔值：
    只有两个值：0  1（True False）
    三元运算
        a,b,c=1,3,5
        d= a if a<b else c 1
        d= a if a>b else c 5

进制：
    二进制   01
    八进制   01234567
    十进制   0123456789
    十六进制 0123456789ABCDEF（四位二进制表示） H后缀表示，或者0X前缀表示  BH,0X53
    二进制转十六进制，每四位表示一个数来转换，如果前后位数不够，补0
    十六进制转二进制，每位转成对于的4位二进制

byte：
    Python 3最重要的新特性之一是对字符串和二进制数据流做了明确的区分。
    文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示。
    Python 3不会以任意隐式的方式混用str和bytes，
    你不能拼接字符串和字节流，也无法在字节流里搜索字符串（反之亦然），
    也不能将字符串传入参数为字节流的函数（反之亦然）
    'adf'.encode('utf-8')
'''
ms='我们'
print(ms.encode()) #python3默认utf-8
print(ms.encode('utf-8')) #b'\xe6\x88\x91\xe4\xbb\xac'
mss=b'\xe6\x88\x91\xe4\xbb\xac'
print(mss.decode('utf-8'))
