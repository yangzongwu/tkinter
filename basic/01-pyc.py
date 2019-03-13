#Auther:YZW
print('hello word')
'''
什么是.pyc
c compiled 缩写

计算机不能识别高级语言，需要一个翻译机，翻译成机器码
编译语言，C++在程序执行之前对程序执行一个编译过程，把程序编程机器语言
解释语言，逐行编译，然后直接运行，ruby
java:首先通过编译器编译成字节码文件，然后在运行时通过解释器给解释成机器文件，所以Java是一种先编译后解释语言

python？
当输入 python hello.py，激活了解释器，但其实在‘解释’之前，python已经编译了

PyCodeObject和pyc文件
PyCodeObject是python编译器真正编译成的结果，当python结束运行时，python解释器则将PyCodeObject写回到pyc文件中
下次调用则不需要再次编译，直接调用pyc
如何更新源代码，怎么办？pyc更新时间和源代码更新时间，决定是否需要再次编译
'''
