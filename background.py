import numpy as np

def background_remover(image,rows,columns,index):
    """
        Function that estimates the mean and standard deviation of the normally
        distributed background counts and subtracts the average background
        count from the input pixel data
        """
    background = []

    for i in range(0,rows):
        for j in range(0,columns):
            #global mean background = 3423 with standard deviation = 26
            if image[index][i][j] < (3423 + 5*26) and image[index][i][j] > (3423 - 5*26):
                background.append(image[index][i][j])

    background_mean = np.mean(background)
    background_stdev = np.std(background)
    
    image_no_back = image[index] - background_mean
    
    return image_no_back, background_stdev, background_mean

def fake_sources(back_sigma,rows,columns,max_limit):
    complete_percent = np.zeros(12*8)
    for mag in range(10*8,21*8):
        blank_image = np.zeros((rows, columns))
        image = blank_image + np.random.normal(0, back_sigma, blank_image.shape)
    
        y_cents = []
        x_cents = []
    
        max_count = 10**((25.3-float(mag/8))/2.5)
    
        for i in range(1,6):
            y_cents.append(80*i)
    
        for j in range(1,5):
            x_cents.append(52*j)
    
        for l in range(0,len(y_cents)):
            for m in range(0,len(x_cents)):
                source_sig = np.random.normal(2,0.3)
                image[y_cents[l]][x_cents[m]] += (max_count/(2*np.pi*source_sig*source_sig))
                if image[y_cents[l]][x_cents[m]] >= max_limit:
                    complete_percent[mag-(10*8)] += 1/20
    
    return complete_percent