#!/usr/bin/env python
# coding: utf-8

# In[11]:


dic={'a':21,'b':7,'c':19,'d':300,'e':5}
sortedd=sorted(dic.items(),key=lambda x:x[1])
sortedd


# In[3]:


dic={'a':21,'b':7,'c':19,'d':300,'e':5}
del dic['b']
dic


# In[7]:


dic={'z':21,'b':7,'c':19,'d':300,'e':5}
sortd=sorted(dic.items())
sortd


# In[28]:


dic={'z':21,'b':7,'c':19,'d':300,'e':5}
maxim=max(dic.items(),key=lambda x:x[1])
minim=min(dic.items(),key=lambda x:x[1])
print('maximum' ,maxim)
print('minimum' ,minim)


# In[1]:


di={'a':2,'b':67}
c=input('enter the key to be added')
a=input('enter the value')
if c not in di.keys():
    di[c]=a
print(di)


# In[2]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


# In[3]:


d={'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}
k=input('enter key to be searched')
found=False
for i in d:
    if k in d:
        found=True
if(found==True):
    print('key exist')
else:
    print('key does not exist')


# In[4]:


d={'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}
for i in d:
    print(i,d[i]) 


# In[5]:


n=int(input('enter value of n'))
d={}
for i in range(1,n+1):
    d[i]=(i*i)
print(d)


# In[6]:


d1={'a': 10, 'b': 20, 'c': 30, 'd': 40 }
d2={'e': 50, 'f': 60}
d1.update(d2)
print(d1)


# In[32]:


dic={'z':21,'b':7,'b':7,'c':19,'d':300,'e':5,'b':7,'z':21}
ndic={}
for i in dic:
    if i not in ndic:
        ndic[i]=dic[i]
ndic


# In[7]:


d={'a': 10, 'b': 20, 'c': 30, 'd': 40 }
print(sum(d.values()))


# In[30]:


dic={'z':21,'b':7,'b':7,'c':19,'d':300,'e':5,'b':7,'z':21}
if(dic== {}):
    print('dic is  empty')
else:
    print('dic is not empty')


# In[8]:


d={'a': 1, 'b': 2, 'c': 3, 'd': 4 }
mul=1
for i in d:
    mul= mul*d[i]
print(mul)


# In[54]:


dic={'a':21,'b':7,'c':19,'d':300,'e':5}
dic1={'a':21,'b':7,'c':1,'d':300,'e':6}
ndic={}
for k,v in dic.items():
    for ke,va in dic1.items():
        if(k==ke and v==va):
            c=v+v
            ndic[k]=c 
            break
        else:
            ndic[k]=v
ndic


# In[70]:


dic={'a':21,'b':7,'c':19,'d':300,'e':5}
lst=list(dic.values())
lst.sort(reverse=True)
lst=lst[:3]
for i in lst:
    for k,j in dic.items():
        if(i==j):
            print('{',k,':',j,'}')


# In[71]:


dic={'a':21,'b':7,'c':19,'d':300,'e':5}
dic1={'a':21,'b':7,'c':1,'d':300,'e':6}

for k,v in dic.items():
    for ke,va in dic1.items():
        if(k==ke and v==va):
            print(k,':',v, 'is present in both dictionaries')


# In[76]:


lst1=[{},{},{}]
lst2=[{'a':21},{},{}]
for i in lst1:
    if (i=={}):
        print('True')
        break
    else:
        print('false')
        break
for j in lst2:
    if (j=={}):
        print('True')
        break
    else:
        print('false')
        break


# In[83]:


lst=[[40,1],[90],[40,1],[80],[80],[90],[1]]
ts=[]
for i in lst:
    if (i not in ts):
        ts.append(i)
ts


# In[85]:


lst1=[10,20,30]
lst2=[40,50]
lst=lst1+lst2
lst


# In[ ]:




