"""
Code for Astro 533 HW#7.

"The goal of this homework is to help build intuition as to the drivers 
of chemical evolution.  In a short computer program, set up the chemical 
evolution equations, and numerically calculate the evolution of the 
metallicity of a mock galaxy. You may assume that the yield p is 0.02 
(i.e., ~solar)."

"""

from __future__ import division

import numpy as np

# yield
p = 0.02

# initial states
M_g = 1 # gas mass
M_s = 0 # stellar mass
M_zg = 0 # mass of metals in gas
M_zs = 0 # mass of metals in stars

M_g_array = [M_g]
M_s_array = [M_s]
M_zg_array =[M_zg]
M_zs_array =[M_zs]

i=0 
while M_g > 0:
    i+=1
    if i < 6 or i > 92:
        print "{4:02d} -- M_g: {0:.2f}    M_s: {1:.2f}    M_zg: {2:.2e}    M_zs: {3:.2e}".format(M_g, M_s, M_zg, M_zs, i)
    elif i == 10 or i==11:
        print ".. --  ...  ...    ...  ...     ...    ...        ...   ...".format(M_g, M_s, M_zg, M_zs, i)        

    # metallicity terms
    Z_g = M_zg / M_g
    try:
        Z_s = M_zs / M_s
    except ZeroDivisionError:
        Z_s = 0

    # relations between differential quantities

    dM_s = 0.01 # SFR per timestep
    dM_g = - dM_s
    dM_zg = p * dM_s - Z_g * dM_s
    dM_zs = Z_g * dM_s

    M_g += dM_g
    M_s += dM_s
    M_zg += dM_zg
    M_zs += dM_zs

    M_g_array.append(M_g)
    M_s_array.append(M_s)
    M_zg_array.append(M_zg)
    M_zs_array.append(M_zs)

M_g_array = np.array(M_g_array)
M_s_array = np.array(M_s_array)
M_zg_array =np.array(M_zg_array)
M_zs_array =np.array(M_zs_array)