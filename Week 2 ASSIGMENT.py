#!/usr/bin/env python
# coding: utf-8

# In[1]:


number =int(input("Enter a number: "))
if number >  0:
    print('The number is positive')
elif number < 0:
    print('The number is negative')
else:
    print('The number is zero')
          


# In[2]:


age = int(input('Enter a age: '))
if age <= 12:
    print('you are a minor')
elif age <= 19:
    print('you are a teenager')
elif age <= 59:
    print('you are an adult')
else:
    print('you are a senior')


# In[3]:


grade =int(input('Enter your grade: '))
if grade >= 90:
    print('grade A')
elif grade > 80 and grade < 89:
    print('grade B')
elif grade > 70 and grade < 79:
    print('grade c')
elif grade > 60 and grade < 69:
    print('grade D')
else:
     print('fail')


# In[4]:


for i in range(1, 11):
    print(i)


# In[5]:


num=int(input('Enter you number: '))
while num >=0:
    print(num)
    num -=1


# ## Intermediate Questions

# In[6]:


num=0
for i in range(1, 51):
    if i % 2 ==0:
        num +=i
        print(num)


# In[7]:


import random
correct_num=(random.randint(1, 20))

counter= 0
print("Guess a number between 1 and 20. You have 5 attempt!")
while counter <5:
    counter +=1
    Guess =int(input('Enter your guess'))
    if Guess == correct_num:
        print('congratulations! You guessed it!')
        break
    elif Guess < correct_num:
        print('Too low! Try again.')
    elif Guess > correct_num:
        print('Too high! Too low')
    else:
        print('Game over')


# In[8]:


correct_password = 'kemi 120'
print('Welcome! Enter your password!')
while True:
    password=input('Enter your password ')
    if password ==correct_password:
        print('Access Granted')
        break
    else:
        print('let us try again')


# In[12]:


rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end= '')
    print()


# In[17]:


rows =5
for i in range(1, rows + 1):
    for j in range(1, i+ 1):
        print(j, end="")
    print()


# ## Advanced Questions

# In[7]:


score=int(input("Enter your score: "))
if  0 <= score <=100:
    if score >=90:
        print('Grade A')
    elif score >=80:
        print('Grade B')
    elif score >=70:
        print('Grade C')
    elif score >=60:
        print('Grade D')
    elif score >=50:
        print('Grade E')
    elif score <0 and score >49:
        print('Grade F')
else:
    print('invalid score')


# In[1]:


import random
correct_number =(random.randint(1, 20 ))
attempt=0
print("Guess a number between 1 and 20. You have 5 attempt!")
while True: 
    guess=int(input('Enter your guess: '))
    if guess < 1 or guess > 100:
        print('Enter your guess' )
        break
        
        attempt+=1
else:
    print('invild score')


# In[10]:


num=input('Enter your num: ')
digit_sum = 0
for digit in num:
    if digit.isdigit():
        digit_sum += int(digit)
print(f'The sum of digits is {digit_sum}.')


# In[16]:


for i in range(1, 101, 2):
    for i in range(2,int(num** 0.5)+1):
        if i % 2==0:
            print(num, end='')


# In[1]:


import time
countdown_time =int(input('Enter the countdowm time: '))
while countdown_time > 0:
    print(countdown_time)
    time.sleep(1)
    countdown_time-=1
print('time_up')


# In[ ]:




