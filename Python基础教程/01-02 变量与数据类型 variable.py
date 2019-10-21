message = "Hello Python world!"
print(message)
'''
-----------output------------
Hello Python world!
Hello Python Crash Course world!
'''


message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
'''
-----------output------------
Hello Python world!
Hello Python Crash Course world!
'''

# 在程序中可随时修改变量的值，而Python将始终记录变量的最新值。

'''
变量的命名和使用
在Python中使用变量时，需要遵守一些规则和指南:
1.变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，
    例如，可将变量命名为message_1，但不能将其命名为1_message。
2.变量名不能包含空格，但可使用下划线来分隔其中的单词。
    例如，变量名greeting_message可行，但变量名greetingmessage会引发错误。
3.不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，
    如print。
4.变量名应既简短又具有描述性。
    例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
5.慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0
'''
