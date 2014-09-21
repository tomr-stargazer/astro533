"""
Code for Homework 3 in Astro 533.

"""

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

def compute_ptmass_arrays(length=100, a=50):

	a_conversion = a/length

	x_over_a_array = np.arange(length) * a_conversion

	density_array = np.zeros(length)
	density_array[0] = 1

	mass_array = np.ones(length)

	velocity_array = 1/np.sqrt(x_over_a_array)

	return density_array, mass_array, velocity_array, x_over_a_array

def plot_on_paper():

	fig = plt.figure()

	subplot_density = fig.subplot(311)
	subplot_mass = fig.subplot(312)
	subplot_velocity = fig.subplot(313)

	ptmass_density, ptmass_mass, ptmass_velocity, ptmass_radius = compute_ptmass_arrays()
	sis_density, sis_mass, sis_velocity, sis_radius = compute_sis_arrays()
	constantrho_density, constantrho_mass, constantrho_velocity, constantrho_radius = compute_constantrho_arrays()

	subplot_density.plot()

	return fig



