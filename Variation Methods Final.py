# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:47:01 2019

@author: moust
"""
### Question Part 1
import numpy as np

### Function to return integrals involving Hamiltonian and basis functions
def H_ij(i, j):
    a = (1/5) * np.sin(j * 5 * np.pi/10) * np.sin(i*5*np.pi/10)  
    b = (np.pi**2 * j**2) / 200

    ham_int = a + b
    
    if i==j:
        ham_int = a + b

    else: 
        ham_int = a
        
    return ham_int

test = H_ij(1,1)
H_mat = np.zeros((6,6))

#for i in range (1,4):
#    for j in range (1,4):
#        H_mat[i-1][j-1] = H_ij(i, j) 

for i in range (1,7):
    for j in range (1,7):
        H_mat[i-1][j-1] = H_ij(i, j) 
        
print (H_mat)


### create an empty numpy array for the c vector
c = np.zeros(6)
### assign c vector to be ....
##c[0] = 1 #(1,0,0) 0.249348022
#c[1] = 1 (0,1,0) 0.197392088
#c[2] = 1 (0, 0, 2) 0.64413219
#c[0] = np.sqrt(1/2) (np.sqrt 1/2,0,0) 0.124674
#c[2] = np.sqrt(1/2) 
#c [3] = 1
#c[4] = 1
c[0] = 1
#after c is defined
norm = np.dot(np.transpose(c), c)

### compute H_mat * c and store it to a new array called Hc
#Hc (as before)
Hc = np.dot(H_mat,c)

### compute c^t * Hc and store it to a variable E
E = np.dot(np.transpose(c), Hc) #/norm energy expectation value



print(E)

E_opt, c_opt = np.linalg.eig(H_mat)

print (E_opt[0])

print (c_opt[0])

## increasing the contribution of excited states does not impact the enegy as expected
## changing the values of c vector resulted in the same value for energy



### Questions Part 2

## is the energy calcuted higher or lower than the 
## ground state energy of the ordinary particle in a box system?

## The ground state energy is lower than the energy of the 
## ordinary particle in a box system





##Why do you think mixing in functions that correspond 
#to excited states in the ordinary particle in a box 
#system actually helped to improve (i.e. lower) your energy 
#in the system with the delta function potential?

# Particle in a box has potential energy through out most of the box, meanwhile
# in the system with the delta function potential, potential energy spikes in one area and is zero
#  through out the rest of the box. Mixing in the functions will improve (lower)
# the energy of the overall system because average potential will be lower than the 
# delta function potential.






#Increase the number of basis functions to 6 (so that ${\bf H}$ is a 
#6x6 matrix and ${\bf c}$ is a vector with 6 entries) and repeat your calculation 
#of the variational estimate of the ground state energy. Does the energy improve 
#(lower) compared to what it was when 3 basis functions were used?

## The ground state energy of 3 basis function is -0.922618887 and the ground state energy 
## of the 6 basis function is -0.934136179. Therefore the energy improved (lowered) 
## with 6 basis functions

