#!/usr/bin/env python
# coding: utf-8

# In[13]:


def positive_numbers_in_range(*numbers):
    for num in numbers:
        if num >= 0:
            print(num)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

print("Positive numbers:")
positive_numbers_in_range(num1, num2, num3, num4)

