#!/usr/bin/env python
# coding: utf-8

# In[22]:


def greet(name):
    print("Hello, "+ name +" Welcome to the world of python")

greet('olaide' )    


# In[5]:


def make_pancake(flour, eggs, milk):
    batches =min(flour, eggs, milk)
    total_pancakes = batches * 4
    return total_pancakes
flour= 5
eggs =3
milk=2
result = make_pancake(flour, eggs, milk)
print('you can make', result, 'pancake')


# In[10]:


def convert_to_fahrenheit(celsius):
    fahrenheit =(celsius*9/5)+32
    return fahrenheit

temperature_celsius =20
temperature_fahrenheit=convert_to_fahrenheit(temperature_celsius)


print(f'{temperature_celsius}°C is equal to {temperature_fahrenheit}°F.' ) 


# In[12]:


def add_two_number(num1, num2):
    return num1+num2

add_two_number(3, 7)


# In[21]:


def personal_welcome(name):
    print(f'Welcome, {name}! You are doing amazing')
    
personal_welcome('Kemi')
personal_welcome('Olaide')
personal_welcome('Ruka')


# ## Intermediate Level

# In[26]:


def math_quiz(num1, num2):
    sum_result =num1 + num2
    different_result =num1-num2
    product_result =num1*num2
    quotient_result =num1/num2
    
    return(sum_result, different_result, product_result, quotient_result)

    
math_quiz(5, 3)


# In[32]:


def magic_box(item1, item2):
    return(f'You have placed {item1} and {item2} in the magic box')
           
           
print (magic_box('A book', 'A pen'))
print (magic_box('A ruler', 'A novel')) 
print (magic_box('A notepad', 'A marker'))           


# In[3]:


def can_fly(power_level):
    if power_level>100:
        return('You can fly')
    else:
        return('Try again, keep training')
    
    
print(can_fly(150)) 
print(can_fly(80))    


# In[27]:


def calculate_area(shape, dimension1, dimension2=0 ):
    if shape =='rectangle':
        return (dimension1 * dimension2)
    elif shape == 'square':
        return (dimension1 * dimension2)
    else:
        return ('invvalid shape')
rectangle_area =calculate_area('rectangle', 5, 10)
square_area=calculate_area('square', 4)


print(f'rectangle_area: {rectangle_area}')
print(f'square_area: {square_area}')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




