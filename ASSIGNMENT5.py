#!/usr/bin/env python
# coding: utf-8

# In[2]:


n1=1500
n2=2700
for i in range (n1,n2+1):
    if(i%7==0 and i%5==0):
        print(i,'is divisible by 7 and multiple of 5')


# In[4]:


for i in range (51):
    if(i%3==0 and i%5==0):
        print('FIZZBUZZ')
    elif(i%3==0):
        print('FIZZ')
    elif(i%5==0):
        print('BUZZ')
    else:
        print(i)


# In[5]:


for i in range(7):
    if(i==3 or i==6):
        continue
    print(i)


# In[7]:


a,b,c=input('enter the length of triangles a,b,c').split()
if(a==b==c):
    print('equilateral triangle')
elif(a==b or b==c or a==c):
    print('isosceles triangle')
else:
    print('scalene triangle')


# In[16]:


a=int(input('enter the number'))
sum=0
c=0
for i in range(0,a+1):
    sum+=i
    c+=1
avg=sum/c
print('average is',avg)
print('sum is', sum)


# In[30]:


for i in range(0,10):
    for j in range(0,i):
        print(i,end='')
    print('')


# In[2]:


lst=[10,80,900,67,8,45]                                                                                                                               
c=0
for i in lst:
    if(i>30):
        c+=1
print(c)


# In[6]:


a,b=input('enter the length and breadth').split()
if(a==b):
    print('square')
else:
    print("rectangle")


# In[7]:


a=int(input('enter the quantity'))
cost=a*100
print('cost is',cost)
if(cost>1000):
    discount=0.1*cost
    cost-=discount
    print('total cost after discount is',cost)


# In[1]:


y=int(input('enter the year of service'))
s=int(input('enter the salary per year'))
print('salary per year is',s)
if(y>5):
    b=s*0.5
    s+=b
    print('bonus is ',b, 'and total amount is',s)


# In[6]:


g=int(input('enter the marks out of 100'))
if (g>=80):
    print('a')
elif(g>=60 and g<80):
    print('b')
elif(g>=50 and g<60):
    print('c')
elif(g>=45 and g<50):
    print('d')
else:
    print('e')


# In[13]:


tc=int(input('enter the no of classes held'))
pc=int(input('enter the no of classes attended'))
per=(pc/tc)*100
print(per)
if(per>=75):
    print('Attendence is more than 75% and Allowed to write exam ')
else:
    print('Attendence is less than 75% and NOT Allowed to write exam')


# In[6]:


i=1
sum=0
while(i<=10):
    num=int(input('enter the integer'))
    i+=1
    sum+=num
avg=sum/10
print(avg)


# In[18]:


for i in range(1,11):
    print('24*',i,' =',(24*i),  '  ','50*',i,'=',(50*i), '    ', '29*',i,'=',(29*i)  )


# In[14]:


num=0
sum=0
i=0
pro=1
while(num!='q'):
    num=input('enter the integer')
    if(num=='q'):
        break 
    else:
        i+=1
        sum+=int(num)
        pro*=int(num)
       
avg=sum/i
print('average is',avg)
print('product is',pro)


# In[4]:


lst=input('enter the list elements').split()
print('list elements are',lst)
key=input('enter element to be searched')
for i in lst:
    if(key == i):
        lst.remove(i)
        print('element found')
        print('list elements after deleting',lst)
    else:
        print('element not found')
        


# In[17]:


lst1=[]
lst2=[]
lst3=[]
flag=False
for i in range(1,101):
    if(i%2==0):
        lst1.append(i)
    if(i%2!=0):
        lst2.append(i)
    for j in range(2,101):
        if(i==j):
            flag=False
        elif(i%j==0):
            flag=True
            break
       
    if(flag==False):
        lst3.append(i)
            
print('even numbers',lst1)
print(' ')
print('odd numbers',lst2)
print(' ')
print('prime numbers',lst3)
print(' ')


# In[10]:


lst1=[]
lst2=[]
lst3=[]
flag=False
for i in range(1,101):
    if(i%2==0):
        lst1.append(i)
    if(i%2!=0):
        lst2.append(i)
    for j in range(2,101):
        if(i==j):
            flag=False
        elif(i%j==0):
            flag=True
            break
       
    if(flag==False):
        lst3.append(i)
            
print('even numbers',lst1)
print(' ')
print('odd numbers',lst2)
print(' ')
print('prime numbers',lst3)
print(' ')
d4=[]
d6=[]
d8=[]
d3=[]
d5=[]
d7=[]
lst=lst1+lst2+lst3
print(lst)
for k in lst:
    if(int(k)%4==0):
        d4.append(k)
    if(int(k)%6==0):
        d6.append(k)
    if(int(k)%8==0):
        d8.append(k)
    if(int(k)%3==0):
        d3.append(k)
    if(int(k)%5==0):
        d5.append(k)
    if(int(k)%7==0):
        d7.append(k)
print('d4',d4)
print(' ')
print('d6',d6)
print(' ')
print('d8',d8)
print(' ')
print('d3',d3)
print(' ')
print('d5',d5)
print(' ')
print('d7',d7)
print(' ')


# In[15]:


a=['hi','hello',3, 7,'welcome',3.4,'bit',2]
nlst=[]
flst=[]
slst=[]
for i in a:
    if(type(i)==str):
        slst.append(i)
    elif(type(i)==int):
        nlst.append(i)
    else:
        flst.append(i)
print('sring list',slst)
print('integer list',nlst)
print('float list',flst)


# In[16]:


a=[2,3,4,6,8]
s=[]
for i in a:
    s.append(i*i)
print(s)


# In[ ]:




