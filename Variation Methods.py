
### Function to return integrals involving Hamiltonian and basis functions
def H_ij(i, j):
    
    
         
    ### if i==j, you need to worry about kinetic and potential
    ### if i!=j, you only need to worry about potential...
    ### so check if i==j and handle the two cases accordingly
    ### store the result in the variable called ham_int
    import numpy as np
    H_mat = np.zeros ((3,3))

#how to make matrix
Matrix = [[0 for i in range ]]

for n in range(0,2):
   #for j in range(0,3):
   i[n] = range (0,2)
   j [n] = rang (0,2)
H_mat[i][j] = H_ij(i, j) 
        
Print (H_mat)

    
   # if i==j:
        
Print ((np.pi **2 * j ** 2) / 200) + (1/5) * np.sin ((j * 5 * np.pi)/(10)) * sin ((i * 5 * np. pi) (10))
        ### code to evaluate integral H_ii here!
 
    
    #else:
        ### code to evaluate H_ij here!

    #return ham_int
#Create an array called $H_mat$ that can be used to store the Hamiltonian 
