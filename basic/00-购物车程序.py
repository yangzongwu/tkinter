#Auther:YZW
print('hello word')
'''
程序：购物车程序
需求：
    启动程序后，让用户输入工资，然后打印商品列表
    允许用户根据商品编码购买商品
    用户选择商品后，检测余额是否够，够直接扣款，不够就提醒
    可随时推出，退出时，打印已购买商品和余额
'''
nums=[[1,'iphone',5000],[2,'bike',500],[3,'Mac Pro',1200],[4,'starbuck',30]]

while True:
    customer_salary=input('your salary or "q" to exist:')
    if customer_salary == 'q':
        exit()
    if customer_salary.isdigit():
        customer_salary=int(customer_salary)
        break
    else:
        print('please re-inter your salary')

for num in nums:
    if num[2]<=customer_salary:
        print(num)
while True:
    while True:
        customer_buy_id = input('please enter which ID you want to buy or "q" to exist:')
        if customer_buy_id=='q':
            exit()
        if customer_buy_id.isdigit():
            customer_buy_id = int(customer_buy_id)
            break
        else:
            print('please re-enter which ID you want to buy:')

    if customer_salary<nums[customer_buy_id-1][2]:
        print('you have not enough money to buy this one')
        rebuy=input('do you want to re-choose or quit Y/N')
        if rebuy=='Y':
            continue
        else:
            print('your balance:', customer_salary)
            break
    else:
        print('you bought:',nums[customer_buy_id-1][1])
        customer_salary=customer_salary-nums[customer_buy_id-1][2]
        print('your balance:',customer_salary)

