#!/usr/bin/env python
# coding: utf-8

# ### Functions

# In[51]:


# functions allow us to create blocks of code that can be easily executed many times


# In[52]:


# functions syntax
#  def name_of_function():
#  ""
#  Docstring explains function


# In[53]:


def add_function(num1,num2):
    return num1+num2


# In[54]:


result = add_function(1,2)


# In[55]:


print(result)


# In[56]:


def name_function():
    print('Hello')


# In[57]:


name_function


# In[58]:


name_function()


# In[59]:


help(name_function)


# In[60]:


def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: name
    OUTPUT: Hellooo...
    '''
    
    print('Hello')


# In[61]:


help(name_function)


# In[62]:


def say_hello(name):
    print('hello '+name)


# In[63]:


say_hello('Tony')


# In[64]:


say_hello('Jordan')


# In[65]:


say_hello('Brandon')


# In[66]:


def say_hello(name='NAME'):
    print('hello '+name)


# In[67]:


say_hello()


# In[68]:


say_hello('Jack')


# In[69]:


result


# In[70]:


type(result)


# In[71]:


def say_hello(name='NAME'):
    return 'hello '+name


# In[72]:


result = say_hello('Jordan')


# In[73]:


result


# In[74]:


def say_hello(name='NAME'):
    return 'Hi '+name


# In[75]:


result = say_hello('Robo')


# In[76]:


result


# In[77]:


say_hello()


# In[78]:


def add(n1,n2):
    return n1+n2


# In[79]:


result = add(20,30)


# In[80]:


result


# ###### Functions allow you to solve problems

# In[81]:


# ex. problems


# In[82]:


# Find out if the word dog is in a string?


# In[83]:


def dog_check(s):
    if 'dog' in s:
        return True
    else:
        return False


# In[84]:


dog_check('My dog is very hungry')


# In[85]:


dog_check('No this human is tired')


# In[86]:


def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False


# In[87]:


dog_check('Dog ran away')


# In[88]:


'dog' in 'dog ran away'


# In[89]:


def dog_check(mysting):
    return 'dog' in mystring.lower()
       


# In[90]:


# pig latin exercise


# ### Pig Latin 
# 

# In[91]:


#  if word starts with a vowel add 'ay' to end
#  if word does not start with a vowel, put first letter at the end, then add 'ay'
# word --> ordaway
#  apple --> appleay


# In[92]:


def pig_latin(word):
    
    first_letter = word[0]
    
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
        
        return pig_word


# In[101]:


pig_latin('Jordan')


# In[103]:


pig_latin('hi')


# ### Python Exercises
# 

# In[104]:


# triangle


# In[105]:


for i in range(5):
    print(i)


# In[108]:


for i in range(1,6):
    print(i)


# In[110]:


n = 5
for i in range(1, n+1):
    print(i)


# In[111]:


n = 7
for i in range(1, n+1):
    print(i)


# In[112]:


for i in range(1, n+1):
    print('*')


# In[115]:


for i in range(1, n+1):
    print(i * "*")


# In[127]:


n = 33
for i in range(1, n+1):
    print(i * '*')


# In[140]:


n = 2
for i in range(1, n+1):
    print(i * '*')


# In[149]:


count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")


# In[ ]:




