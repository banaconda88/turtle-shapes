#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
shelly=turtle.Turtle()
shelly.shape('turtle')
shelly.color('purple')
shelly.shapesize(1,0.5)


# In[2]:


def turtle_circles():
    shelly.circle(100)
    shelly.right(10)
for i in range (26):
    turtle_circles()

