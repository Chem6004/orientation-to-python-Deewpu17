

import numpy as np

### Function to return integrals involving Hamiltonian and basis functions
def H_ij(i, j):
    a = 2 * np.sin (np.pi * 0.25) * np.sin (np.pi * 0.25) 
    b = 2 * (0.25 - 0.5)
   
    ham_int = a * b 
    
    if i==j:
        ham_int = a * b

    else: 
        ham_int = a
        
    return ham_int


H_mat = np.zeros((3,3))

for i in range (1,4):
    for j in range (1,4):
        H_mat[i-1][j-1] = H_ij(i, j) 

 
        
print ('Print H_mat is')


### create an empty numpy array for the c vector
c = np.zeros(3)

c[0] = 1

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
