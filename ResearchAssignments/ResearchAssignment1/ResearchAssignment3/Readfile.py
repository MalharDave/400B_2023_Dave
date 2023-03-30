#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import astropy.units as u

def Read(filename):
    file=open(filename,'r')
    line1 = file.readline()
    label, value = line1.split()
    time = float(value)*u.Myr
    line2 = file.readline()
    label, value = line2.split()
    Number= float(value) #there is no unit for Number
    file.close()
     
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3)
    print(data)
    return time,Number, data


# In[25]:


#t,N,data = Read("MW_000.txt")

#print(N)
#print(t)
#print(data['type'][1:31])


# In[ ]:




