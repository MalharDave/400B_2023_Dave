#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #importing numpy library
import astropy.units as u #importing astropy's unit library to get our answers with their units
from Readfile import Read #importing Read function from the Readfile program we created

#defining a function to calculate the distance in 3-d space
#input a, b, c signifying 3 directions 
#returning total distance d 
def magd(a,b,c): 
    d= np.sqrt(a**2+b**2+c**2)  #squaring all the 3 directions and then taking their square root 
    return d 
#defining a function to calculate the velocity in 3-d space
#input d, e, f signifying 3 velocities
#returning total distance v 
def magv(d,e,f):
    v= np.sqrt(d**2+e**2+f**2) 
    return v


# In[42]:


# This function gives the magnitude of distance in kpc, magnitude of velocity in km/s,mass in units of M_Sun
# Inputs: filename; particle type ; particle number
# Returns: Sum of a, b, c in kpc
def ParticleInfo(filename,particle_type,particle_number):
    file=Read(filename) #using Read to get all the values from Readfile.py
    #data=file[2]
    t,N,data = Read("MW_000.txt")
    #using variables t for time, N for number of particles and data to get specifics 
    #about them from our text file
    index= np.where(data['type'] == particle_type)
    x=data['x'][index][particle_number] #taking distance in x direction
    x=x*u.kpc #converting it to kpc 
    y=data['y'][index][particle_number] # #taking distance in y direction
    y=y*u.kpc #converting it to kpc 
    z=data['z'][index][particle_number]  #taking distance in z direction
    
    z=z*u.kpc #converting it to kpc 
    m=data['m'][particle_number] #taking the mass of the given particle
    m=(m*10**-10)*u.solMass #converting the mass to be expressed in the form of solar masses, and multilying by 10^-10 since 
    #that is default in text file 
    m-np.round(m,3)
    vx=data['vx'][index][particle_number] #taking velocity in x direction 
    vx=vx*u.km/u.s #converting it to km/s
    vy=data['vy'] [index][particle_number]#taking velocity in y direction 
    vy=vy*u.km/u.s #converting it to km/s
    vz=data['vz'][index][particle_number]#taking velocity in z direction 
    vz=vz*u.km/u.s #converting it to km/s
    
    mag_d=magd(x,y,z) #Calling the distance magnitude function to calculate total 3d distance
    mag_d=np.round(mag_d,3) #rounding the 3d distance to the 3rd decimal value using numpy.round 
    mag_v=magv(vx,vy,vz) #Calling the velocity magnitude function to calculate total 3d velocity
    mag_v=np.round(mag_v,3) #rounding the 3d velocity to the 3rd decimal value using numpy.roun
    return m,mag_d,mag_v #returning the 3 things we need to calculate at the end, mass, and distance and velocity in 3d 

    


# In[48]:


calling = ParticleInfo("MW_000.txt",2,99) #We call our Particle info function , 2 is for disk stars so we enter that in
#NOTE: We call 99 instead of 100 because it starts from 0, so technically 100th particle is 99 in number 


# In[49]:


#printing out the mass, distance magnitude and velocity magnitude for designated galaxy in the units asked 

print("The mass of the given disk particle is:" ,calling[0]) #3.949*10-13 solMass
print("The distance of the given particle is: " ,calling[1])#4.245 kpc
print("The velocity of the given particle is: ", calling[2])#312.135 km / s

print("The distance of the given particle in light years is: " ,calling[1].to(u.lyr))#13845.338234075754 lyr


# In[ ]:





# In[ ]:





# In[ ]:




