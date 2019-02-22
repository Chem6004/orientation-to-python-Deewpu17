# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:06:21 2019

@author: moust
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

### create an array of 20 bond lengths spanning 0.5 - 3.5 angstroms
### but store in atomic units of length... note 1 angstrom = 1.88973 a.u. of length
r_array = np.linspace(0.5,3.5,20)*1.88973
print(r_array)

### fill in this array with your actual energy values... there should be 20 values in total!!!
E_array = [-107.141,-110.874, -112.204, -112.622, -112.699, -112.653, -112.570, 
          -112.484, -112.410, -112.361, -112.333, -112.315, -112.304, -112.069,
          -112.291, -112.287, -112.001, -111.948, -111.927, -112.280]


# TO see the plot of the PES, uncomment the following lines
plt.plot(r_array, E_array, 'red')
plt.show()

### use cubic spline interpolation
order = 3
### form the interpolator object for the data
sE = InterpolatedUnivariateSpline(r_array, E_array, k=order)
### form a much finer grid
r_fine = np.linspace(1.06,5.0,200)
### compute the interpolated/extrapolated values for E on this grid
E_fine = sE(r_fine)
### plot the interpolated data
plt.plot(r_fine, E_fine, 'blue')
plt.show()

### take the derivative of potential
fE = sE.derivative()
### force is the negative of the derivative
F_fine = -1*fE(r_fine)

### plot the forces
plt.plot(r_fine, np.abs(F_fine), 'black')
plt.xlim(1,5)
plt.show()

### Find index of the PES where it has its global minimum
r_eq_idx = np.argmin(E_fine)

### find the value of the separation corresponding to that index
r_eq = r_fine[r_eq_idx]

### print equilibrium bond-length in atomic units and in angstroms
print("Equilibrium bond length is ",r_eq," atomic units")
print("Equilibrium bond length is ",r_eq*0.529," Angstroms")


### get second derivative of potential energy curve... recall that we fit a spline to
### to the first derivative already and called that spline function fE.
cE = fE.derivative()

### evaluate the second derivative at r_eq to get k
k = cE(r_eq)


### define "ground-state" velocity:
v = np.sqrt( np.sqrt(k/mu)/(2*mu))

### get random position and velocity for CO within a reasonable range
r_init = np.random.uniform(0.75*r_eq,2*r_eq)
v_init = np.random.uniform(-2*v,2*v)

### print initial position and velocity
print("Initial separation is ",r_init, "atomic units")
print("Initial velocity is   ",v_init, "atomic units")
### establish time-step for integration to be 0.2 atomic units... this is about 0.01 femtoseconds
dt = 0.02

### get force on particle 
F_init = -1*fE(r_init)


def Velocity_Verlet(r_curr, v_curr, mu, f_interp, dt):
    ### get acceleration at current time
    a_curr = -1*f_interp(r_curr)/mu
    
    ### use current acceleration and velocity to update position
    r_fut = r_curr + v_curr * dt + 0.5 * a_curr * dt**2
    
    ### use r_fut to get future acceleration a_fut
    
    
    a_fut = -1*f_interp(r_curr)/mu
    ### use current and future acceleration to get future velocity v_fut
    
    v_fut = v_curr + 0.5 * (a_curr + a_fut) * dt
    
    result = [r_fut, v_fut]
    
    return result

### how many updates do you want to perform?
N_updates = 200000

### Now use r_init and v_init and run velocity verlet update N_updates times, plot results
### these arrays will store the time, the position vs time, and the velocity vs time
r_vs_t = np.zeros(N_updates)
v_vs_t = np.zeros(N_updates)
t_array = np.zeros(N_updates)

### first entry is the intial position and velocity
r_vs_t[0] = r_init
v_vs_t[0] = v_init

### first Velocity Verlet update
result_array = Velocity_Verlet(r_init, v_init, mu, fE, dt)

### do the update N_update-1 more times
for i in range(1,N_updates):
    tmp = Velocity_Verlet(result_array[0], result_array[1], mu, fE, dt)
    result_array = tmp
    t_array[i] = dt*i
    r_vs_t[i] = result_array[0]
    v_vs_t[i] = result_array[1]

### Plot the trajectory of bondlength vs time:
plt.plot(t_array, r_vs_t, 'red')
plt.show()

### plot the phase space trajectory of position vs momentum
plt.plot(mu*v_vs_t, r_vs_t, 'blue')
plt.show()

###Question 1 
# what is the reduced mass of the CO molecule in atomic units
m_C = 12.0 * 1836 #1836 au conversion
m_O = 16.0 * 1836
m_CO = m_C * m_O / (m_C + m_O)
print ('reduced mass is ',(m_CO))
### 12589.7

### define reduced mass of CO as m_C * m_O /(m_C + m_O) where mass is in atomic units (electron mass = 1)
## 
mu = 12589.7

### Question 2
## calculated mu = 1.13856*10**-26
## Dr. Foley mu = 13625
vf = np.sqrt (k/mu)
print ('vibrational frequency', vf)
### 0.010308461206176322 atomic units

## Question 3 

a = -1*fE(3)/mu
print ('acceleration is ', a)
### -2.2187115023362023 * 10**5 atomic units





