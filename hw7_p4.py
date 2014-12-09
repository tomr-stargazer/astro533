"""
Code for Astro 533 HW#7, Problem 3

"The goal of this homework is to help build intuition as to the drivers 
of chemical evolution.  In a short computer program, set up the chemical 
evolution equations, and numerically calculate the evolution of the 
metallicity of a mock galaxy. You may assume that the yield p is 0.02 
(i.e., ~solar)."

"""

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

def closedbox_with_outflow_and_infall(SFR_per_timestep=0.01, p_yield=0.02, outflow_relative_to_SFR=0.1, mass_cutoff=10):

    # yield
    p = p_yield

    # initial states
    M_g = 1 # gas mass
    M_s = 0 # stellar mass
    M_zg = 0 # mass of metals in gas
    M_zs = 0 # mass of metals in stars

    M_g_array = [M_g]
    M_s_array = [M_s]
    M_zg_array =[M_zg]
    M_zs_array =[M_zs]

    eta = outflow_relative_to_SFR

    i=0 
    # New condition: let the galaxy grow to ten times its initial mass
    while M_g + M_s < mass_cutoff:
        i+=1
        print "{4} -- M_g: {0}    M_s: {1}    M_zg: {2}    M_zs: {3}".format(M_g, M_s, M_zg, M_zs, i)

        # metallicity terms
        Z_g = M_zg / M_g
        try:
            Z_s = M_zs / M_s
        except ZeroDivisionError:
            Z_s = 0

        # relations between differential quantities

        dM_s = SFR_per_timestep
        dM_g = 0 # SFR plus outflow is balanced exactly by gas infall
        dM_zg = p * dM_s - Z_g*dM_s - Z_g*eta*dM_s # assumes infalling gas has zero metals; outflowing gas metallicity matches current metallicity
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

    return M_g_array, M_s_array, M_zg_array, M_zs_array

fig_gas = plt.figure()
ax_gas = fig_gas.add_subplot(111)
fig_star = plt.figure()
ax_star = fig_star.add_subplot(111)

for eta in np.arange(0.0, 1.1, 0.2):

    # calculate the values
    M_g_array, M_s_array, M_zg_array, M_zs_array = closedbox_with_outflow_and_infall(outflow_relative_to_SFR=eta)
    Z_s_array = M_zs_array / M_s_array
    Z_g_array = M_zg_array / M_g_array
    mu_array = M_g_array / (M_g_array + M_s_array)

    # make the plot
    ax_gas.plot(mu_array[:-1], Z_g_array[:-1], label=r"$\eta = {0}$".format(eta))

    ax_star.plot(mu_array[:-1], Z_s_array[:-1], label=r"$\eta = {0}$".format(eta))

ax_star.set_xlabel(r"$\mu$ (Gas mass fraction)")
ax_star.set_ylabel(r"$Z_*$ (Average metallicity of stars)")
ax_star.legend(loc='upper left')

ax_gas.set_xlabel(r"$\mu$ (Gas mass fraction)")
ax_gas.set_ylabel(r"$Z_g$ (Metallicity of gas)")
ax_gas.legend(loc='upper left')

ax_star.invert_xaxis()
ax_gas.invert_xaxis()

plt.show()
