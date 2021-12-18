def max_finder(pixels,rows,columns):
    """
        Function that finds the pixel with the maximum count and returns the
        count and the coordiantes of the maximum-count pixel
        """
    max_count = 0
    x_coord = 0
    y_coord = 0

    for k in range(0,rows):
        for l in range(0,columns):
            if pixels[k][l] > max_count:
                max_count = pixels[k][l]
                x_coord = l
                y_coord = k
    
    return max_count, y_coord, x_coord