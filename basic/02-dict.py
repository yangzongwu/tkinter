#Auther:YZW
print('hello word')
#key-value
info={
    'student01':'yzw',
    'student02':'cyy',
    'student03':'zh'
}
print(info) #字典无序

#search
print(info['student02']) #通过key取值
#info['student04'] 会报错
print(info.get('student04')) #None 建议使用
print('student04' in info)

#modify
info['student02']='zd'
print(info['student02']) #通过key取值

#add
info['student04']='adf'
print(info)

#del
del info['student02']
print(info)
#del info 全部删除
info.pop('student03')
print(info)


#多级字典嵌套
info={
    'student01':'yzw',
    'student02':'cyy',
    'student03':'zh'
}
b={
    'student01':'sdf',
    'student05':'sedf',
    1:3,
    2:5
}
info.update(b)
print(info)
#{'student01': 'sdf', 'student02': 'cyy', 'student03': 'zh', 'student05': 'sedf', 1: 3, 2: 5}
print(info.items())
#dict_items([('student01', 'sdf'), ('student02', 'cyy'), ('student03', 'zh'), ('student05', 'sedf'), (1, 3), (2, 5)])
c=dict.fromkeys([6,7,8],'test')
print(c)
#{6: 'test', 7: 'test', 8: 'test'}
c=dict.fromkeys([6,7,8],[1,{'name':'alex'},23]) #多个key共享一个地址
print(c)
#{6: [1, {'name': 'alex'}, 23], 7: [1, {'name': 'alex'}, 23], 8: [1, {'name': 'alex'}, 23]}
c[7][1]['name']='jack' #全部改了
print(c)
#{6: [1, {'name': 'jack'}, 23], 7: [1, {'name': 'jack'}, 23], 8: [1, {'name': 'jack'}, 23]}

#循环
info={
    'student01':'yzw',
    'student02':'cyy',
    'student03':'zh'
}
for i in info:
    print(i,info[i])
'''
student01 yzw
student02 cyy
student03 zh
'''
for k,v in info.items():  #速度很慢，不建议用
    print(k,v)
