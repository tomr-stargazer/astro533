"""
Code for Homework 3 in Astro 533.

"""

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

def compute_ptmass_arrays(length=100, a=50):

	x_over_a_array = np.arange(length) / a

	density_array = np.zeros(length)
	density_array[0] = 1000 # arbitrary constant
	density_array[1] = 1000

	mass_array = np.cumsum(density_array*2*np.pi*(x_over_a_array)**2)

	velocity_array = np.sqrt(mass_array/x_over_a_array)

	return density_array, mass_array, velocity_array, x_over_a_array

def compute_sis_arrays(length=100, a=50):

	x_over_a_array = np.arange(length) / a

	density_array = (1/x_over_a_array)**2 / 100 # arbitrary constant
	density_array[a:] = 0
	density_array[0] = density_array[1]

	mass_array = np.cumsum(density_array*2*np.pi*(x_over_a_array)**2)

	velocity_array = np.sqrt(mass_array/x_over_a_array)

	return density_array, mass_array, velocity_array, x_over_a_array

def compute_constantrho_arrays(length=100, a=50):

	x_over_a_array = np.arange(length) / a

	density_array = np.ones(length) / 40 # arbitrary constant
	density_array[a:] = 0

	mass_array = np.cumsum(density_array*2*np.pi*(x_over_a_array)**2)

	velocity_array = np.sqrt(mass_array/x_over_a_array)

	return density_array, mass_array, velocity_array, x_over_a_array



def plot_on_paper():

	fig = plt.figure(figsize=(8.5,11), dpi=100)

	subplot_density = fig.add_subplot(311)
	subplot_mass = fig.add_subplot(312)
	subplot_velocity = fig.add_subplot(313)

	ptmass_density, ptmass_mass, ptmass_velocity, ptmass_radius = compute_ptmass_arrays()
	sis_density, sis_mass, sis_velocity, sis_radius = compute_sis_arrays()
	constantrho_density, constantrho_mass, constantrho_velocity, constantrho_radius = compute_constantrho_arrays()

	subplot_density.plot(ptmass_radius, ptmass_density, label="point mass")
	subplot_density.plot(sis_radius, sis_density, label="SIS")
	subplot_density.plot(constantrho_radius, constantrho_density, label=r"$\rho_0$")
	subplot_density.legend()
	subplot_density.set_yscale('log')
	subplot_density.text(0.1, 0.75, "Density profile", fontsize=24, transform=subplot_density.transAxes)
	subplot_density.set_ylabel(r"$\rho (r)$", fontsize=24)
	subplot_density.set_title("Astro 533. Homework 3. Tom Rice", fontsize=18)

	subplot_mass.plot(ptmass_radius, ptmass_mass)
	subplot_mass.plot(sis_radius, sis_mass)
	subplot_mass.plot(constantrho_radius, constantrho_mass)
	subplot_mass.set_yscale('log')
	subplot_mass.set_ylabel(r"$M (<r)$", fontsize=24)
	subplot_mass.text(0.6, 0.2, "Mass profile", fontsize=24, transform=subplot_mass.transAxes)

	subplot_velocity.plot(ptmass_radius, ptmass_velocity)
	subplot_velocity.plot(sis_radius, sis_velocity)
	subplot_velocity.plot(constantrho_radius, constantrho_velocity)
	subplot_velocity.set_yscale('log')
	subplot_velocity.set_ylim(0.05, 12)
	subplot_velocity.set_ylabel(r"$v_{circ} (r)$", fontsize=24)
	subplot_velocity.set_xlabel('$r / a$', fontsize=24)
	subplot_velocity.text(0.6, 0.2, "Rotation curve", fontsize=24, transform=subplot_velocity.transAxes)

	fig.show()

	return fig



