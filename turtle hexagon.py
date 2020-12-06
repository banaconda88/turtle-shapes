#!/usr/bin/env python
# coding: utf-8

# In[9]:


import turtle
shelly=turtle.Turtle()
shelly.shape('turtle')
shelly.color('pink')
shelly.shapesize(1,0.5)


# In[10]:


def turtle_moving():
    shelly.forward(100)
    shelly.left(60)
for i in range (6):
    turtle_moving()


# In[ ]:




