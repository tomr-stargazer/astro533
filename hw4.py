"""
Code to do Eric's HW.

You will be using the NYU Value-Added Galaxy Catalog (the low-z version) 
from Mike Blanton for today's homework. The catalog is described at 
sdss.physics.nyu.edu/vagc/ 
and can be downloaded from ctools homework area in resources (this 
link takes you to the data file) (25MB)

You will read in the .fits file (in IDL using mrdfits), and the columns
of interest are absmag (an array of 8 values, ugrizJHK absolute 
magnitudes assuming H_0 = 100km/s), sersic_n (5 values of sersic index in 
ugriz, use the r-band value), and zdist (the redshift).

"""

from __future__ import division

import os.path

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
import astropy.units as u
import astropy.constants as c

data_path = os.path.expanduser("~/Dropbox/Grad School/Courses/galaxies_astro533/")

sdss_table = Table.read(data_path+'lowz_catalog.dr4.fits')

absmag = sdss_table['ABSMAG'] #absolute magnitude 
g_column = absmag[:,1]
r_column = absmag[:,2]

sersic = sdss_table['SERSIC_N']
spirals = sersic[:,2] < 2
ellipticals = sersic[:,2] >= 2

z_column = sdss_table['ZDIST']

H_0 = 100 * u.km / u.s / u.Mpc
distance = (c.c * z_column / H_0).to(u.Mpc)

def magnitude_bin_stuff(n_bins=10):

    hist, bin_edges = np.histogram(r_column, bins=n_bins)
 
    max_distance = np.zeros_like(hist) * u.Mpc
    bin_centers = np.zeros_like(hist, dtype='float')

    bin_width = np.abs(bin_edges[0] - bin_edges[1])

    for i in range(len(hist)):

        bin_min = bin_edges[i]
        bin_max = bin_edges[i+1]

        bin_centers[i] = np.mean((bin_max, bin_min))

        max_distance[i] = np.max( distance [((r_column > bin_min) & (r_column < bin_max))])

    V_max = 4/3 * np.pi * max_distance**3

    luminosity_function = hist / (V_max * bin_width)

    return luminosity_function, bin_centers, V_max, max_distance, hist
