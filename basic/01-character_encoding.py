#Auther:YZW
print('hello word')
'''
字符编码
    0，1，
    eg:烽火台怎么点烟告知有多少敌人来袭，
        1烟表示1-100， 2烟表示100-1000，3烟表示1000-10000
    增加要求准确来了多少敌人23431，如何描述
        每个位表示数值    1   2   4   8   16   32   64
        使用该位数为1     1   1   1   1   1    1    1
        最大表示数值      1   3   7   15  31   63   127
        01排列组合
    那么对于英文字符，如何用二进制表示呢？字符编码
    ASCII（美国标准信息交换码），其最多8位表示一个字符，一共127个，最初预留了128-255留给其他语言扩展
    怎么存汉字？GB2312（支持7K汉字）, GBK（支持20k+）,  CG18030（支持27k+）
    全世界各个语言，怎么办？
    Unicode， 统一码，万国码，单一码，规定字符和符号占用2个字节，16位
    UTF-8 （可变长短的Unicode）存英文的时候用ASCII，1byte,存汉字用Unicode 3byte
'''
#python2 中执行中文,需要本文开头增加如下行，python3不需要，已经支持中文
#-*- coding:utf-8 -*-
name='你好'
print(name)

'''
Unicode---encode--->utf-8
utf-8---decode--->Unicode
Unicode---encode--->GBK
GBK---decode--->Unicode
GBK 需要转位UTF-8 需要通过Unicode转
'''

#上述语句引用哪种编码
import sys
print(sys.getdefaultencoding())

#python 默认编码utf-8

#-*-coding:gbk-*-
#上述是文件编码
s='你好' #默认Unicode
print(s)
print(s.encode('gbk'))    #b'\xc4\xe3\xba\xc3'  byte 类型，bgk编码模式
print(s.encode('utf-8'))  #b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(s.encode('utf-8').decode('utf-8').encode('gb2312')) #b'\xc4\xe3\xba\xc3'
print(s.encode('utf-8').decode('utf-8').encode('gb2312').decode('gb2312'))#你好
