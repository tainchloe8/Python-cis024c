
# coding: utf-8

# In[1]:

def addAll(inList):
    return sum(inList)
def diffAll(inList):
    return reduce(lambda x,y: x-y,inList)
def multiplyAll(inList):
    return reduce(lambda x,y: x*y,inList)
def greatestAll(inList):
    return max(inList)

