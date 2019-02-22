# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:14:41 2019

@author: moustafad
"""

def BBK(r_curr, v_curr, rp_curr, gamma_val, temperature_val, mu, f_interp, dt):
    
    ### get acceleration at current time: (force + current perturbation on force)/mass - drag
    a_curr = (-1*f_interp(r_curr) + rp_curr)/mu - gamma_val*v_curr
    ### THE ABOVE IS EQUATION 6 IN THE ASSIGNMENT DAS POSTED
    
    ### update velocity for half time step, for such a small time step can approximate dv = adt
    ### THINK ABOUT IT: DO YOU REALLY HAVE TO DO THIS STEP?
    
   
    ### use current acceleration and velocity to update position
    ### WRITE CODE IMPLEMENTING THE FORMULA YOU OBTAINED, AS PART OF EXERCISE 1, FOR r(t+dt) HERE
    
    ### calculate the rp_future
    
    rp_fut = np.sqrt(2*temperature_val*gamma_val*mu/dt)*np.random.normal(0,1)
    
    ### use rp_fut to get future acceleration a_fut (a_tilde at the future time in the assignment), 
    ### note that we cannot take future drag into account as we have not calculated our future velocity yet
    ### CODE IMPLEMENTING EQUATION 7 IN THE ASSIGNMENT DAS POSTED GOES HERE
    
    ### use current and future acceleration to get future velocity v_fut
    ### note that we have to "correct" our formula relative to the formula for velocity Verlet
    ### as we have not included our future drag in our future acceleration
    
    # v_fut = (v_halftime + 0.5*a_fut*dt)/(1+0.5*gamma_val*dt)
    ### WRITE CODE IMPLEMENTING THE FORMULA YOU OBTAINED, AS PART OF EXERCISE 1, FOR r(t+dt) HERE
    
    result = [r_fut, v_fut, rp_fut]
    
    return result

### how many updates do you want to perform?
N_updates = 200000

### Now use r_init and v_init and run velocity verlet update N_updates times, plot results
### these arrays will store the time, the position vs time, and the velocity vs time
r_vs_t = np.zeros(N_updates)
v_vs_t = np.zeros(N_updates)
e_vs_t = np.zeros(N_updates)
t_array = np.zeros(N_updates)

### first entry is the intial position and velocity
r_vs_t[0] = r_init
v_vs_t[0] = v_init
e_vs_t[0] = (sE(r_init)-minE)+0.5*mu*result_array[1]**2

### first BBK update
result_array = BBK(r_init, v_init, rp_init, gamma, temperature, mu, fE, dt)

### do the update N_update-1 more times
for i in range(1,N_updates):
    tmp = BBK(result_array[0], result_array[1], result_array[2], gamma, temperature, mu, fE, dt)
    result_array = tmp
    t_array[i] = dt*i
    r_vs_t[i] = result_array[0]
    v_vs_t[i] = result_array[1]
    e_vs_t[i] = (sE(result_array[0])-minE)+0.5*mu*result_array[1]**2

### Plot the trajectory of bondlength vs time:
plt.plot(t_array, r_vs_t, 'red')
plt.show()

### plot the phase space trajectory of position vs momentum
plt.plot(mu*v_vs_t, r_vs_t, 'blue')
plt.show()

### plot the total energy vs. time: does the average energy seem to converge?
plt.plot(t_array,e_vs_t,'magenta')
plt.show()

### mean energy for next to last and last ten thousand time steps: does each equal k_B*T? are they similar to each other?
print("Mean Energy for next to last 100000 time steps of the trajectory is ",np.mean(e_vs_t[(N_updates-20000):(N_updates-10000)])," Hartrees")
print("Mean Energy for last 100000 time steps of the trajectory is ",np.mean(e_vs_t[(N_updates-10000):N_updates])," Hartrees")