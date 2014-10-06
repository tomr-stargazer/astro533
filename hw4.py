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