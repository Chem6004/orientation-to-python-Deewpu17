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
H_mat = np.zeros((3,3))

for i in range (1,4):
    for j in range (1,4):
        H_mat[i-1][j-1] = H_ij(i, j) 
        
#print (H_mat)


### create an empty numpy array for the c vector
c = np.zeros(3)
### assign c vector to be (1, 0, 0)
c[0] = 1
#after c is defined
norm = np.dot(np.transpose(c), c)

### compute H_mat * c and store it to a new array called Hc
#Hc (as before)
Hc = np.dot(H_mat,c)

### compute c^t * Hc and store it to a variable E
E = np.dot(np.transpose(c), Hc) #/norm energy expectation value



#print(E)

E_opt, c_opt = np.linalg.eig(H_mat)

print (E_opt[0])

print (c_opt[0])



### Questions Part 2
# is the energy calcuted higher or lower than the ground state energy 
# of the ordinary particle in a box system?