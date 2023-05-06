#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import astropy.units as u
import astropy.table as tbl

from ReadFile import Read
class MassProfile:
    def __init__(galaxy,snap):
        ''' Class to calculate the 6-D phase-space position of a galaxy's center of mass using
        a specified particle type. 
            
            PARAMETERS
            ----------
            filename : `str`
                snapshot file
            ptype : `int; 1, 2, or 3`
                particle type to use for COM calculations
        '''
        # read data in the given file using Read
        self.time, self.total, self.data = Read(filename)   
        # add a string of the filenumber to the value “000”
        ilbl = '000' + str(Snap)
        # remove all but the last 3 digits
        ilbl = ilbl[-3:]
        self.filename="%s "%(galaxy) + ilbl + '.txt'
        
                                                                                             

                                   
        

        # store the mass, positions of only the particles of the given type
        
        self.m = self.data['m'][self.index]
        self.x = self.data['x'][self.index]*u.kpc #Storing x,y,z positions in units of kpc
        self.y = self.data['y'][self.index]*u.kpc
        self.z = self.data['z'][self.index]*u.kpc
        self.r= np.sqrt(x**2+y**2+z**2)*u.kpc #compiling the total magnitude
        self.gname = galaxy #storing the galaxy 
#defining the mass enclosed function 
#Inputs: self, ptype, radius
#outputs: Mass_enclosed
    def Massenclosed(self,ptype,radius):
        #line to signify the particle type we are dealing with
        index = np.where(self.data['type'] == ptype)
        mass=COM_P(self.filename,delta) #calling our COM_P function from center of mass file
        xnew= self.x- mass  #defining the x,y, and z values with respect ti center of mass
        ynew= self.y - mass
        znew= self.z -mass 
        #now we compute the total magnitude as 
        rnew = np.sqrt (x**2+y**2+z**2)
        #creating a numpy array same size as radius before we begin our loop
        mass_= np.array(radius)
        mass_enclosed=np.copy(mass_)
        mass_enclosed.fill(1)
        for i in range (np.size(radius)):
            [index]= np.where (rnew<r)
            mass_enclosed[i]=np.sum(self.m[index])
            
        return mass_enclosed
  #defining total enclosed mass
  #inputs: self, radius
  #outputs:msum
    def massenclosedsum(self,radius):
        msum= Massenclosed(self,1,radius)+Massenclosed(self,2,radius)+Massenclosed(self,3,radius)
        return msum
#defining hernquist mass of given system
  #inputs: self, radius, a, Mhalo,
  #outputs:HM
    def HernquistMass(self,radius,a,Mhalo):
        return (Mhalo*radius**2/a+radius**2)
        
    


# In[ ]:




