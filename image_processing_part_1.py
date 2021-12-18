# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:29:07 2021

@author: jmcan
"""

import astropy.io
from astropy.io import fits
import numpy as np
import scipy as sp
import math as math
import matplotlib.pyplot as plt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
import matplotlib.cm as cm
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import axes3d
import plotly.figure_factory as ff
hdulist = fits.open("A1_mosaic.fits")
hdulist[0].header
hdulist[0].data
#plots a histogram of the noise
p1 = fits.getdata('A1_mosaic.fits')
pixels = p1.flatten()
noise = []
for i in range(0,len(pixels)):
    if pixels[i] < 3700 and pixels[i] > 0:
        noise.append(pixels[i])

a, b, c = plt.hist(noise,bins=50)
bins = np.zeros(len(a))
for j in range(0,len(a)):
    bins[j] = b[j+1] - b[j]
    
    
plt.hist(noise,bins=50,color='b')
plt.grid(True)
plt.savefig("cycle3plot1.jpg", dpi=300,bbox_inches='tight')
plt.show()
hdulist.close()