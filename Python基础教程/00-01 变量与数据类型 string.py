#  字符串 就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号，


str1 = "This is a string."
str2 = 'This is also a string.'
str3 = 'I told my friend, "Python is my favorite language!"'
str4 = "The language 'Python' is named after Monty Python, not the snake."
str5 = "One of Python's strengths is its diverse and supportive community."

#  使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title())  # Ada Lovelace
print(name.upper())  # ADA LOVELACE
print(name.lower())  # ada lovelace

#  合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)  # ada lovelace
print("Hello, " + full_name.title() + "!")  # Hello, Ada Lovelace!

#  使用制表符或换行符来添加空白
print("Python")
# Python
print("\tPython")
#  Python
# 要在字符串中添加制表符，可使用字符组合\t
# 要在字符串中添加换行符，可使用字符组合\n
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Languages:
#   Python
#   C
#   JavaScript


#  删除空白
favorite_language = 'python '
print(favorite_language)    # 'python '
favorite_language.rstrip()  # 'python'
print(favorite_language)    # 'python '
# 要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)    # 'python'
# 你还可以剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法lstrip() 和strip()

