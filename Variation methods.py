# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:58:23 2019

@author: moustafad
"""
import numpy as np

### Function to return integrals involving Hamiltonian and basis functions
def H_ij(i, j):
    a = (1/5) * np.sin((j * 5 * np.pi)/(10)) * np.sin((i*5*np.pi)/(10))  
    b = (np.pi**2 * j**2) / 200

    ham_int = a + b
    
    if i==j:
        ham_int = a + b

    else: 
        ham_int = a
        
    return ham_int

H_mat = np.zeros((3,3))

for i in range (1,4):
    for j in range (1,4):
        H_mat[i-1][j-1] = H_ij(i, j) 
        
print (H_mat)

