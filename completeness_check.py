import numpy as np
import aperture
import maximum

def fake_sources(back_sigma,rows,columns,limit,max_limit):
    complete_percent = np.zeros(14)
    for mag in range(8,22):
        blank_image = np.zeros((rows, columns))
        image = blank_image + np.random.normal(0, back_sigma, blank_image.shape)
    
        source_sig = np.random.normal(2,0.3)
    
        y_cents = []
        x_cents = []
    
        max_count = 10^((25.3-mag)/2.5)
    
        for i in range(1,6):
            y_cents.append(80*i)
    
        for j in range(1,5):
            x_cents.append(52*j)
    
        for k in range(0,len(y_cents)):
            for l in range(y_cents[k]-10,y_cents[k]+10):
                for m in range(x_cents[k]-10,x_cents[k]+10):
                    image[l][m] += (max_count/(2*np.pi*source_sig*source_sig))*np.exp(-(1/(2*source_sig*source_sig))*((l-y_cents[k])*(l-y_cents[k])+(m-x_cents[k])*(m-x_cents[k])))
                
        fin = False
        object_counter = []
        while fin == False:
            
            maxCount, y_max, x_max = maximum.max_finder(image,rows,columns)
        
            if maxCount > max_limit:
                object_counter.append(aperture.circular(image,rows,columns,y_max,x_max,limit))
            else:
                fin = True
                
        if len(object_counter) >= 20:
            complete_percent[mag-8] = 1
        