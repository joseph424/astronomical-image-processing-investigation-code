def data_sorter(mag,mag_limits,no_galaxy):
    """
        Function that measures the number of galaxies brighter than defined
        magntiude limits.
        """
    for i8 in range(0,len(mag)):
        if mag[i8] >= 9 and mag[i8] < 10:
            for j3 in range(0,len(mag_limits)):
                no_galaxy[j3] += 1
        elif mag[i8] >= 10 and mag[i8] < 11:
            for j4 in range(1,len(mag_limits)):
                no_galaxy[j4] += 1
        elif mag[i8] >=11 and mag[i8] < 12:
            for j5 in range(2,len(mag_limits)):
                no_galaxy[j5] += 1
        elif mag[i8] >=12 and mag[i8] < 13:
            for j6 in range(3,len(mag_limits)):
                no_galaxy[j6] += 1
        elif mag[i8] >= 13 and mag[i8] < 14:
            for j7 in range(4,len(mag_limits)):
                no_galaxy[j7] += 1
        elif mag[i8] >=14 and mag[i8] < 15:
            for j8 in range(5,len(mag_limits)):
                no_galaxy[j8] += 1
        elif mag[i8] >=15 and mag[i8] < 16:
            for j9 in range(6,len(mag_limits)):
                no_galaxy[j9] += 1
        elif mag[i8] >=16 and mag[i8] < 17:
            for j10 in range(7,len(mag_limits)):
                no_galaxy[j10] += 1
        elif mag[i8] >=17 and mag[i8] < 18:
            for j11 in range(8,len(mag_limits)):
                no_galaxy[j11] += 1
        elif mag[i8] >= 18 and mag[i8] < 19:
            for j12 in range(9,len(mag_limits)):
                no_galaxy[j12] += 1
        elif mag[i8] >= 19 and mag[i8] < 20:
            for j13 in range(10,len(mag_limits)):
                no_galaxy[j13] += 1
        else:
            no_galaxy[11] += 1
    
    return no_galaxy