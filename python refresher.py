#!/usr/bin/env python
# coding: utf-8

# In[1]:


mystring = 'hello'


# In[4]:


mylist = []

for letter in mystring:
    mylist.append(letter)


# In[5]:


mylist


# In[6]:


mylist = [letter for letter in mystring]


# In[7]:


mylist


# In[8]:


mylist = [x for x in 'word']


# In[9]:


mylist


# In[10]:


mylist = [num for num in range(0,11)]


# In[11]:


mylist


# In[13]:


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# ###  Assesment Test Solutions

# ### Use for, .split(), and if to create a Statement that will print out words that start with 's':

# In[1]:


st = ('Print only words that start with s in this sentence')


# In[2]:


for word in st.split():
    if word [0] == 's':
        print(word)


# In[3]:


st


# In[4]:


st.split()


# ###  Use range() to print all all the even numbers from 0 to 10

# In[6]:


list(range(0,11,2))


# In[7]:


for num in range(0,11,2):
    print(num)


# ### Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

# In[8]:


[x for x in range(1,51) if x%3 == 0]


# ### Go through the string below and if the length of a word is even print "even!"

# In[9]:


st = 'Print every word in this sentence that has an even number of letters'


# In[11]:


for word in st.split():
    if len(word) % 2 == 0:
        print(word+ ' is even!')


# ###  Write a program that prints the integers from 1 to 100. But for mulitples of three print "fizz" instead of the number, and for the mulitples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# In[14]:


for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)


# In[15]:


# trick is to check for 3 and 5 first 


# ### Use List Comprehension to create a list of the first letters of every word in the string below:  

# In[16]:


st = 'Create a list of the first letters of every word in this string'


# In[17]:


[word for word in st.split()]


# In[18]:


[word[0] for word in st.split()]


# In[ ]:




