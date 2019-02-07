# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:55:50 2019

@author: moust
"""
#Q1
import numpy as np
Npart = 25
m = np.zeros(Npart)
v = np.zeros(Npart)
q = np.ones(Npart)
x = np.linspace(0, (Npart-1)*0.2, Npart)
r = np.zeros((Npart ,Npart))

for i in range (0,Npart):
    m[i] = 1.0
    v[i] = 2.5
    
print ("printing array of masses: ",m)
print ("printing array of velocities: ",v)

T = 1/2 * m * v**2
print (T)

T_tot_sum = np.sum (T)

print ("Results from numpy sum is ",T_tot_sum)

#plot
from matplotlib import pyplot as plt

Npart_array = [5, 10, 15, 20, 25]
Kinetic_array = [15.625, 31.25, 46.875, 62.5, 78.125]

#plt.plot (Npart_array, Kinetic_array, 'red')
#plt.show

#Q2
for i in range (0,Npart):
    for j in range (0,Npart):
        r[i][j] = np.sqrt( (x[i]-x[j])**2 )
    
#print ("Printing array of charges",q)
#print ("Printing array of charges ",x)
#print ("Printing array of charges \n",r)

def Potential(sep_array, charge_array):
    N = len(charge_array)
    Pot = 0.
    for i in range (0,N):
        for j in range(0,N):
            if (i!=j):
                Pot = Pot +charge_array[i]*charge_array[j]/sep_array[i][j]
    return Pot

V_tot = Potential (r, q)

#print (V_tot) 
    
#plot
Potential_array = [64.166, 192.897, 347.734, 519.548, 703.990]

#plt.plot (Npart_array, Kinetic_array, 'red')
#plt.show

#Q3
import time

start = time.time()

x = Npart_array
y = Potential_array
#y = Kinetic_array

plt.plot (x, y, 'red')
plt.show

end = time.time()
how_long = end - start
print ("Total time to run in seconds is: ",how_long)
#kinetic total time in seconds = 0.013340950012207031
#KE scales linearly

#Potential total time = 0.0111680308227539
#Potential seems to scale quadratically, slightly curved




