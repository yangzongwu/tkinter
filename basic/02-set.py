#Auther:YZW
print('hello word')
'''
集合
1：去重
2：关系测试，如何取同时在两个列表中的交集，并集等关系
集合是无序的
'''
list_1=[1,4,5,7,8,7,9]

list_1=set(list_1)
print(list_1,type(list_1))
#{1, 4, 5, 7, 8, 9} <class 'set'>

list_2=set([2,6,7,33,66,8])
print(list_1,list_2)
#{1, 4, 5, 7, 8, 9} <class 'set'>

#intersection
print(list_1.intersection(list_2))
print(list_1&list_2)
#{8, 7}
#union
print(list_1.union(list_2))
print(list_1|list_2)
#{1, 33, 2, 4, 5, 66, 7, 8, 9, 6}
#differenct
print(list_1.difference(list_2))
print(list_1-list_2)
#{1, 4, 5, 9}
#subset
print(list_1.issubset(list_2))#False
#supperset
print(list_1.issuperset(list_2))#False
#symmetric_difference
print(list_1.symmetric_difference(list_2))
print(list_1^list_2)
#{1, 2, 66, 4, 5, 6, 9, 33}


##################################################
list_1=[1,4,5,7,8,7,9]
list_1=set(list_1)

list_1.add(10)
print(list_1) #{1, 4, 5, 7, 8, 9, 10}
list_1.update([1,2,3,9])
print(list_1)#{1, 2, 3, 4, 5, 7, 8, 9, 10}

list_1.remove(8)
print(list_1) #{1, 2, 3, 4, 5, 7, 9, 10}

print(len(list_1))

print(9 in list_1)

list_1.pop()
print(list_1)# 随机删除一个{2, 3, 4, 5, 7, 9, 10}

list_1.discard('sss')#不报错，没有返回值
