import numpy as np
import matplotlib.pyplot as plt
import fragmenter
import background
import maximum
import aperture
import magntiudes
import pandas as pd
import astropy.io
from astropy.io import fits

#this section plots a histogram of the noise
hdulist = fits.open("A1_mosaic.fits")
hdulist[0].header
hdulist[0].data

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
plt.title('Histogram of background intensities',fontsize=16)
plt.xlabel('Intensity/arbitrary units',fontsize=12)
plt.ylabel('Counts',fontsize=12)
plt.grid(True)
plt.savefig("Histogram of background intensities.jpg", dpi=300,bbox_inches='tight')
plt.show()
hdulist.close()

#for the image processing
row = 401
column = 237

position_x = []
position_y = []
backgrounds = []

#splits the processed image into sections with (rows, columns)
segs, ind = fragmenter.fragment(row,column)

#list to store the total counts of each object detected
object_counts = []

comp_per = np.zeros(12*8)

#loop with iterations for each image section
for a in range(0, ind):
    
    #function applied to estimate parameters of bakground signal and subtracts mean background count from all pixels
    im_wo_back, sigma, mean = background.background_remover(segs,row,column,a)
    finished = False
    
    #sets the count minimum limits at for the edge and (approximate) centre of the object
    lim = 3*sigma
    max_lim = 6*sigma
    
    #loop that repeats until no more objects are found
    while finished == False:
        
        #function identifies the pixel with the maximum count value
        maxCount, y_max, x_max = maximum.max_finder(im_wo_back,row,column)
        
        if maxCount > max_lim:
            #function that estimates the size of the object and uses a square aperture to sum the total counts of the pixels within
            object_counts.append(aperture.circular(im_wo_back,row,column,y_max,x_max,lim))
            position_y.append(y_max)
            position_x.append(x_max)
            backgrounds.append(mean)
        else:
            #terminates loop as no more objects present
            finished = True
    
    comp_per = np.add(comp_per,background.fake_sources(sigma,row,column,max_lim)/ind)

#magntiudes of objects measured as a function of the CCD counts
count_errors = np.sqrt(object_counts)
mags = 25.3 - 2.5*np.log10(object_counts)




df = pd.DataFrame({"x-coordinate" : position_x, "y_coordinate" : position_y, "Total counts" : object_counts, "Total counts uncertainty" : count_errors, "Mean background count" : backgrounds})
df.to_csv("Catalogue.csv", index=False)

mag_points = np.linspace(10,21,12)
no_galaxies = np.zeros(12)

#function calculates the number of galaxies brighter than the given magntiude limits
no_galaxies = magntiudes.data_sorter(mags,mag_points,no_galaxies)

error_upper = np.log10(no_galaxies+np.sqrt(no_galaxies)) - np.log10(no_galaxies)
error_lower = np.log10(no_galaxies) - np.log10(no_galaxies-np.sqrt(no_galaxies))

mag_lim_fit = mag_points[:7]
no_gal_fit = no_galaxies[:7]

#fits and plots data with the linear model
fit, cov = np.polyfit(mag_lim_fit,np.log10(no_gal_fit),1,w=1/(error_upper[:7]+error_lower[:7]),cov=True)
x = np.linspace(9,17.3,10000)
y = fit[0]*x + fit[1]
plt.plot(mag_points,np.log10(no_galaxies),'.')
plt.plot(x,y)
plt.xlabel('Magnitude',fontsize=12)
plt.ylabel('log$_{10}$(N)',fontsize=12)
plt.title("Log number count plot",fontsize=16)
plt.xlim([8,22])
plt.ylim([0.5,3.5])
plt.errorbar(mag_points,np.log10(no_galaxies),yerr=(error_lower, error_upper),fmt='.',capsize=3, color='k')
plt.grid()
plt.savefig("Log number count plot.jpg", dpi=300,bbox_inches='tight')
plt.show()

print('Gradient: ',fit[0], ' +/- ',np.sqrt(cov[0][0]))
print('Intercept: ',fit[1], ' +/- ',np.sqrt(cov[1][1]))

complete_mags = np.linspace(10,21,96)

plt.plot(complete_mags,comp_per,'.')
plt.grid()
plt.title('Fraction of fabricated objects detected',fontsize=16)
plt.xlabel('Magnitude',fontsize=12)
plt.ylabel('Fraction detected',fontsize=12)
plt.xlim([14,18])
plt.savefig("Fraction of fabricated objects detected plot.jpg",dpi=300,bbox_inches='tight')
plt.show()
