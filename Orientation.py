# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:39:41 2019

@author: moustafad
"""
#print ("hello world!")
### varibles for particle 1
import numpy as np
Npart = 10
### create empty lists for each quantity

m = np.zeros(Npart)
v = np.zeros(Npart)
q = np.zeros(Npart)
x = np.zeros(Npart)
T = np.zeros(Npart)
##prints a list of zeros because np.zeros of Npart (10) didnt assign values
print(m)

##can assign them values using for loop
for i in range(0,Npart): #incret by 1 until [i] reaches 10. i starts @ 0
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i #fixed spacing will get larger by * i incerement
    v[i] = 0.2 * i
    
    ### now that i have mass and velocity for the 
    ###ith particle, I can calculate the kinetic energy
    ### for the ith particle
    T[i] = 0.5 *m[i] * v[i]**2
print(T)
#print (m)
#print (q)
#print (x) 
#print (v)    
### Varibles for particle 2
#m2 = 1.0 
#v2 = 2.5
#q2 = 1.0
#x2 = 0.5

### Varibles for pair of particles
#r12 = np.sqrt((x1-x2)**2)
#V12 = q1*q2/r12
#print (" separation is ",r12)
#print ("Potential Energy is",V12) 
 #### used earlier to define T1, T2,T3,T4 are identicle
#T1 = 0.5*m*v**2
#T2 = 1/2 * m * v * v
#T3 = 0.5 * m * v * v
#T4 = m*v**2/2

#print (T1, T2, T3, T4)
