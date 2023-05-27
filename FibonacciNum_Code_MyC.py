#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("Enter the count of Fibonacci numbers to be seen in the series"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


# In[ ]:




