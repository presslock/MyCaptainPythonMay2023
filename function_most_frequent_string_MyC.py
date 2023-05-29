#!/usr/bin/env python
# coding: utf-8

# In[12]:


def most_frequent():
    string = input("Enter a string: ")

    frequency = {}
    for letter in string:
        frequency[letter] = frequency.get(letter, 0) + 1

    sorted_letters = sorted(frequency, key=frequency.get, reverse=True)

    for letter in sorted_letters:
        print(letter, frequency[letter])

most_frequent()


# In[ ]:




