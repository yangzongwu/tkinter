#Auther:YZW
print('hello word')

count=0
while True:
    print('count:',count)
    count+=1
    if count==1000:
        break


age_of_oldboy=56
while True:
    guess_age = int(input('guess oldboy_age:'))
    if guess_age==age_of_oldboy:
        print('yes, you got it')
        break
    elif guess_age>age_of_oldboy:
        print('think smaller..')
    else:
        print('think older...')



age_of_oldboy=56
count=0
while True:
    if count==3:
        break
    guess_age = int(input('guess oldboy_age:'))
    if guess_age==age_of_oldboy:
        print('yes, you got it')
        break
    elif guess_age>age_of_oldboy:
        print('think smaller..')
    else:
        print('think older...')
    count+=1


age_of_oldboy=56
count=0
while count<3:
    guess_age = int(input('guess oldboy_age:'))
    if guess_age==age_of_oldboy:
        print('yes, you got it')
        break
    elif guess_age>age_of_oldboy:
        print('think smaller..')
    else:
        print('think older...')
    count+=1
else:
    print('you have tried too many times')

############################################################
for i in range(10):
    print('loop:',i)
for i in range(0,10,2):
    print('loop:',i)

age_of_oldboy=56
for i in range(3):
    guess_age = int(input('guess oldboy_age:'))
    if guess_age==age_of_oldboy:
        print('yes, you got it')
        break
    elif guess_age>age_of_oldboy:
        print('think smaller..')
    else:
        print('think older...')
else:
    print('you have tried too many times')


############################################################
age_of_oldboy=56
count=0
while count<3:
    guess_age = int(input('guess oldboy_age:'))
    if guess_age==age_of_oldboy:
        print('yes, you got it')
        break
    elif guess_age>age_of_oldboy:
        print('think smaller..')
    else:
        print('think older...')
    count+=1
    if count==3:
        countinue_confirm=input('do you want to keep guess..?')
        if countinue_confirm!='n':
            count=0
else:
    print('you have tried too many times')

#########################################################################
for i in range(10):
    print('hello')
    if i<5:
        print('loop:',i)
    else:
        continue

