from astropy.io import fits

def fragment(rows,columns):
    p1 = fits.getdata('bled.fits')

    def blockshaped(arr, nrows, ncols):
        """
        Function that receives a 2D array and splits it into segments with a
        defined number of rows and columns.
        
        Returns an array containing each 2D segment and returns the value of 
        the number of segments within the array
        """
        h, w = arr.shape
        assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
        assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
        return (arr.reshape(h//nrows, nrows, -1, ncols)
                .swapaxes(1,2)
                .reshape(-1, nrows, ncols))
    
    segments = blockshaped(p1,rows,columns)
    index = int((4411/rows)*(2370/columns)-1)
    
    return segments, index