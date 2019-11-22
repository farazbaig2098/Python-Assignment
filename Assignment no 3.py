#!/usr/bin/env python
# coding: utf-8

# In[1]:


''' QNO 1 '''

a = int(input("Enter 1st number  "))
b = int( input("Enter 2nd number  "))
operator = input("Enter operator  ")

if operator == "*":
    print(a*b)
    
elif operator == '+':
    pritn(a+b)

elif operator == '-':
    print(a-b)
    
elif operator == '/':
    print(a/b)
    
elif operator == 'p':
    print(a**b)


# In[2]:


''' QNO 2 '''
arr = [12,"asf","qwe","power","lol",13]
for aa in arr:
    if type(aa) == int or type(aa) == float:
        print(f"Numeric value is found = {aa} At Index={arr.index(aa)}")


# In[3]:


'''QNO 3 '''
dtio = {"firstName":"FARAZ", "lastName":"BAIG"}
print(dtio)

dtio.update({"mid":"lol"})
print(dtio)


# In[4]:


'''QNO 4'''
def sumdic(dtio):
        sum = 0
        for i in dtio.values():
            sum = sum + i
        return sum

ndtio = {0:12 , 1:41, 2:123 }

print("sum :: ",sumdic(ndtio))


# In[5]:


'''Qno 5 '''
lst1 = ["hhh","aaa", "abc","aaa","ccc",1,1]
def dup(lst):
    lst1dup = []
    for val in lst:
        if val not in lst1dup:
            lst1dup.append(val)
        elif val in lst1dup:
            print("duplicate value is found ",val)
    return lst1dup

print(dup(lst1))


# In[6]:


'''Qno 6'''
dic = {
    1: 30,
    2: 50,
    3: 20,
    4: 50,
    5: 90,
    6: 60}
def is_key_present(x):
    if x in dic:
        print('Key is present in the dictionary')
    else: 
        print('Key is not present in the dictionary')
            
            
is_key_present(6)
is_key_present(99)


# In[ ]:




