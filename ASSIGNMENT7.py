#!/usr/bin/env python
# coding: utf-8

# # class
# 

# In[ ]:



    def rom(n):
        res=""
        lst=[(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        for c,r in lst:
            d,m=divmod(n,c)
            res+=r*d
            n=m
        return res
n=int(input('enter the number'))
print(MyClass.rom(n))


# In[ ]:





# In[17]:


class myclass:
    def paravalidate(s):
        o=['[','{','(']
        c=[']','}',')']
        stk=[]

        for i in s:
            if i in o:
                stk.append(i)
            elif i in c:
                p=c.index(i)
                if(len(stk)>0) and (o[p]==stk[len(stk)-1]):
                    stk.pop()
                else:
                    return False
        if(len(stk)==0):
            return True
        else:
            return False
s=input('enter the string')
print(myclass.paravalidate(s))


# In[10]:


class slist:
    def sublist(lst):
        slst=[[]]
        for i in range(len(lst)+1):
            for j in range(i):
                slst.append(lst[j:i])
        return slst
ls1=[1,2,3]
ls2=[3,4]
print(slist.sublist(ls1))
print(sublist(ls2))


# In[47]:


class myclass:
    def myf(lst,n):
        for i in lst:
            for j in lst:
                if(n==i+j):
                    k=lst.index(i)
                    s=lst.index(j)
                    return k,s
        #return a,b
lst=[10,20,30,40,50]
n=int(input('enter n'))
myclass.myf(lst,n)


# In[24]:


class myclass:
       def sumo(l1):
           for i in l1:
               for j in l1:
                   for k in l1:
                       if(i+j+k==0):
                           print(i,j,k)
   
l1=[2,20,-5,3,10]
myclass.sumo(l1)                    


# In[56]:


class myclass:
       def sumo(l1):
           ki=[]
           for i in l1:
               b=(l1.index(i)+1)
               for j in range(l1.index(i)+1,len(l1)):
                   for k in range(l1.index(i)+2,len(l1)):
                       if(i+l1[j]+l1[k]==0):
                           a=l1[j]
                           b=l1[k]
                           if(i and a not in ki):
                               print(i,a,b)
                               ki.append(i)
                               ki.append(a)
                               ki.append(b)
                               
l1=[2,20,-5,3,10,-22]
myclass.sumo(l1)


# In[16]:


class Myclass:
    def revstr(str):
        str1=list(str.split(' '))
        str2=''
        for i in range(len(str1)-1,-1,-1):  
            str2=str2+(str1[i])
            str2+=' '
        print(str2)
str='My name is fats'
Myclass.revstr(str)


# In[23]:


class Myclass:
    def get_str():
        str=input('enter the string')
        return str
    def print_str(str):
        #str1=list(str.split(' '))
        str2=''
        for i in range(len(str)-1,-1,-1):  
            str2=str2+(str[i])
        print(str2)
Myclass.print_str(Myclass.get_str())


# In[8]:


class circle:
    radius=int(input('enter the radius'))   
    def area(radius):
        a=3.14*radius*radius
        print('area of circle is',a)
    def peri(radius):
        p=2*3.14*radius
        print('perimeter of circle is',p)
    circle.area(radius)
    peri(radius)


# In[22]:


class circle: 
    def area(radius):
        a=3.14*radius*radius
        print('area of circle is',a)
    def peri(radius):
        p=2*3.14*radius
        print('perimeter of circle is',p)
c=circle()
clas=c.__class__
print('class name of object c',clas.__name__)


# # Lambda function
# 

# In[4]:


add=lambda x:x+15
print(add(10))


# In[5]:


mul=lambda x,y:x*y
print(mul(12,4))


# In[8]:


a=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
a.sort(key=lambda x:x[1])
a


# In[11]:


a=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
a1=sorted(a,key=lambda x:x['color'])
a1


# In[17]:


strt=lambda x,c:print('starts with ',x[0]) if x[0]==c else print('not starts with',x[0])
c=input("enter character ")
x=input("enter word ")
print(strt(x,c))


# In[23]:


strt=lambda x:print('number',x) if x[0].isdigit() else print('string',x)
c=input("enter string")
strt(c)


# In[33]:


a=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
x(a)
a1=lambda x: (for i in x:  if (i%19==0 or i%13==0) print(i))


# In[43]:


a=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
a1=lambda x:print(x[0]) 
a1(a)


# In[1]:


a=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 
a1=list(filter(lambda x:(x%13==0 or x%19),a))
print(a1)


# In[6]:


a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
sorts=sorted(a,key=lambda a1: sum(a1)) 
print(sorts)


# In[12]:


s=['red', 'black', 'white', 'green', 'orange'] 
sub=input('enter substring')
a=list(filter(lambda x:sub in x,s))
print(a)


# In[ ]:




