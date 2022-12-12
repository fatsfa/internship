#!/usr/bin/env python
# coding: utf-8

# # len of string

# In[1]:


s='hello world'
l=0
for i in s:
    l=l+1;
print(l)


# In[2]:


s==
print(s)
l=0
for i in s:
    l=l+1;
print(l)


# In[3]:


s='helllo'
s1={}
for i in s:
    if i in s1:
        s1[i]=s1[i]+1
    else:
        s1[i]=1
print(s1)


# In[4]:


s=input("enter the string")
print(s)
if len(s)<0:
    print('empty string')
else:
    print(s[0:2]+s[-2:])


# In[5]:


s=input("enter the string")
print(s)
s1=s.replace(s[0],'$').replace('$',s[0],1)
print(s1)   


# In[ ]:


s1=input("enter the string")
s2=input("enter the string")
new1=s1[0:2]+s2[2:] +' '+s2[0:2]+s1[2:]
print(new1)


# In[ ]:


s=input("enter the string")
print(s)
if len(s)<3:
    print(s)
else:
    if s[-3:]=='ing':
        print(s[0:]+'ly')
    else:
        print(s[0:]+'ing')


# In[ ]:


s=input("enter the string")
print(s)
s1=s.replace('not poor','good',1)
print(s1)
        


# In[ ]:


def largestword(s):
    max=len(s[0])
    temp=s[0]
    for i in s:
        if (len(i)>max):
            max=len(i)
            temp=i
    print(temp)
s=['one','two','three','four']
largestword(s)


# In[21]:


n1=1500
n2=2700
for i in range (n1,n2+1):
    if(i%7==0 and i%5==0):
        print(i,'is divisible by 7 and multiple of 5')


# In[14]:


for i in range(7):
    if(i==3 or i==6):
        continue
    print(i)


# In[ ]:





# In[18]:


for i in range (51):
    if(i%3==0 and i%5==0):
        print('FIZZBUZZ')
    elif(i%3==0):
        print('FIZZ')
    elif(i%5==0):
        print('BUZZ')
    else:
        print(i)
    count+=1


# In[20]:



  


# In[ ]:




