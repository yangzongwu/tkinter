#Auther:YZW

#list
print('hello word')
name=['yzw','cyy','zh','zy','gx']
print(name)             #['yzw', 'cyy', 'zh', 'zy', 'gx']
print(name[0],name[1])  #yzw,cyy
print(name[1:3])        #切片['cyy', 'zh']
print(name[-1])         #gx
print(name[-2])         #zy
print(name[-2:])        #['zy', 'gx']

#add
name.append('LY') # add to last
print(name) #['yzw', 'cyy', 'zh', 'zy', 'gx', 'LY']
name.insert(0,'HH') #
print(name) #['HH', 'yzw', 'cyy', 'zh', 'zy', 'gx', 'LY']

#change
name[3]='XD'

#delete
name.remove('gx')
del name[1]
name.pop(0)

#loc
print(name.index('cyy'))
print(name[name.index('cyy')])

#stat.
print(name.count('cyy')) #1

#reverse
print(name)
name.reverse()
print(name) #['LY', 'zy', 'XD', 'cyy']

#sort
name.sort()#特殊符号，数字，大写，小写， ASCII排序
print(name)#['LY', 'XD', 'cyy', 'zy']
name1=['qq','ww']
name.extend(name1)
print(name) #['LY', 'XD', 'cyy', 'zy', 'qq', 'ww']

#delete
del name1

#clear
name.clear()
print(name) #[]


#copy 浅copy，只copy一层
name=['yzw','cyy']
print(name)
name2=name.copy()
print(name2,name) #['yzw', 'cyy'] ['yzw', 'cyy']
name[0]='张'
print(name2,name) #['yzw', 'cyy'] ['张', 'cyy']

name=['yzw','cyy',['ww','ee']]  #['ww','ee']在name中只是存内存地址而不是实际内容
print(name)
name2=name.copy()
print(name2,name) #['yzw', 'cyy', ['ww', 'ee']] ['yzw', 'cyy', ['ww', 'ee']]
name[2][0]='张'
print(name2,name) #['yzw', 'cyy', ['张', 'ee']] ['yzw', 'cyy', ['张', 'ee']]

#
name=['yzw','cyy']
print(name)
name2=name
print(name2,name) #['yzw', 'cyy'] ['yzw', 'cyy']
name[0]='张'
print(name2,name) #['张', 'cyy'] ['张', 'cyy']

import copy
name=['yzw','cyy',['ww','ee']]
name2=name.copy().copy()
name[2][0]='张'
name[0]='李'
print(name)  #['李', 'cyy', ['张', 'ee']]
print(name2) #['yzw', 'cyy', ['张', 'ee']]

import copy
name=['yzw','cyy',['ww','ee']]
name3=copy.deepcopy(name)
name[2][0]='张'
name[0]='李'
print(name)  #['李', 'cyy', ['张', 'ee']]
print(name3) #['yzw', 'cyy', ['ww', 'ee']]


#浅copy实现方式
person=['name',['saving',100]]
p11=copy.copy(person)
p21=person[:]
p31=list(person)

#案例,共同银行存款,一般用来创建联合账号
p1=person[:]
p1[0]='alex'  #['alex', ['saving', 100]]
p2=person[:]
p2[0]='lili'
print(p1,p2)  #['lili', ['saving', 100]]

p1[1][1]=50
print(p2)  #['lili', ['saving', 50]]

#tuple
#不可改，只能查，也叫只读列表,只有count, index方法
name=('yzw','cyy','yzw')
print(name.count('yze'))#0
print(name.index('yzw'))#0
print(name.index('cyy'))#1
