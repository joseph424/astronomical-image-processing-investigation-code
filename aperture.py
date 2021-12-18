import numpy as np

def square(mat,rows,columns,y_coord,x_coord,limit):
    """
        Function that estimates the size of the detected object; the edge of
        the object is defined at the pixel where its count is less than a
        defined limit
        """
    #starting from the coordinates of the pixel with maximum count (approximate centre)
    ys = [y_coord]
    xs = [x_coord]
    
    #pixels read in along positive x direction
    for m in range(x_coord,columns):
        if mat[y_coord][m] > limit:
            xs.append(m)
        else:
            break

    #pixels read in along positive y direction
    for n in range(0,y_coord):
        if mat[y_coord-n][x_coord] > limit:
            ys.append(y_coord-n)
        else:
            break

    #pixels read in along negative x direction        
    for o in range(0,x_coord):
        if mat[y_coord][x_coord-o] > limit:
            xs.append(x_coord-o)
        else:
            break

    #pixels read in along negative y direction
    for p in range(0,rows-y_coord):
        if mat[y_coord+p][x_coord] > limit:
            ys.append(y_coord+p)
        else:
            break

    #pixels read in along diagonal in the +x,+y direction
    for q in range(0,rows):
        if y_coord - q == 0:
            ys.append(0)
            xs.append(x_coord+q)
            break
        elif x_coord+q == columns-1:
            ys.append(y_coord-q)
            xs.append(columns-1)
            break
        elif mat[y_coord-q][x_coord+q] > limit:
            ys.append(y_coord-q)
            xs.append(x_coord+q)
        else:
            break

    #pixels read in along diagonal in the -x,+y direction
    for r in range(0,rows):
        if y_coord - r == 0:
            ys.append(0)
            xs.append(x_coord-r)
            break
        elif x_coord -r == 0:
            ys.append(y_coord-r)
            xs.append(0)
            break
        elif mat[y_coord-r][x_coord-r] > limit:
            ys.append(y_coord-r)
            xs.append(x_coord-r)
        else:
            break

    #pixels read in along diagonal in the -x,-y direction
    for s in range(0,rows):
        if y_coord+s == rows - 1:
            ys.append(rows-1)
            xs.append(x_coord-s)
            break
        elif x_coord-s == 0:
            ys.append(y_coord+s)
            xs.append(0)
            break
        elif mat[y_coord+s][x_coord-s] > limit:
            ys.append(y_coord+s)
            xs.append(x_coord-s)
        else:
            break
    
    #pixels read in along diagonal in the +x,-y direction
    for t in range(0,rows):
        if y_coord+t == rows-1:
            ys.append(rows-1)
            xs.append(x_coord+t)
            break
        elif x_coord+t == columns-1:
            ys.append(y_coord+t)
            xs.append(columns-1)
            break
        elif mat[y_coord+t][x_coord+t] > limit:
            ys.append(y_coord+t)
            xs.append(x_coord+t)
        else:
            break

    total_count = 0
    
    #square aperture where the counts of the contained pixels are summed
    for u in range(min(xs),max(xs)+1):
        for v in range(min(ys),max(ys)+1):
            total_count += mat[v][u]
            mat[v][u] = 0
    
    return total_count

def circular(mat,rows,columns,y_coord,x_coord,limit):
    """
        Function that estimates the size of the detected object; the edge of
        the object is defined at the pixel where its count is less than a
        defined limit
        """
    #starting from the coordinates of the pixel with maximum count (approximate centre)
    ys = [y_coord]
    xs = [x_coord]
    
    #pixels read in along positive x direction
    for m in range(x_coord,columns):
        if mat[y_coord][m] > limit:
            xs.append(m)
        else:
            break

    #pixels read in along positive y direction
    for n in range(0,y_coord):
        if mat[y_coord-n][x_coord] > limit:
            ys.append(y_coord-n)
        else:
            break

    #pixels read in along negative x direction        
    for o in range(0,x_coord):
        if mat[y_coord][x_coord-o] > limit:
            xs.append(x_coord-o)
        else:
            break

    #pixels read in along negative y direction
    for p in range(0,rows-y_coord):
        if mat[y_coord+p][x_coord] > limit:
            ys.append(y_coord+p)
        else:
            break

    #pixels read in along diagonal in the +x,+y direction
    for q in range(0,rows):
        if y_coord - q == 0:
            ys.append(0)
            xs.append(x_coord+q)
            break
        elif x_coord+q == columns-1:
            ys.append(y_coord-q)
            xs.append(columns-1)
            break
        elif mat[y_coord-q][x_coord+q] > limit:
            ys.append(y_coord-q)
            xs.append(x_coord+q)
        else:
            break

    #pixels read in along diagonal in the -x,+y direction
    for r in range(0,rows):
        if y_coord - r == 0:
            ys.append(0)
            xs.append(x_coord-r)
            break
        elif x_coord -r == 0:
            ys.append(y_coord-r)
            xs.append(0)
            break
        elif mat[y_coord-r][x_coord-r] > limit:
            ys.append(y_coord-r)
            xs.append(x_coord-r)
        else:
            break

    #pixels read in along diagonal in the -x,-y direction
    for s in range(0,rows):
        if y_coord+s == rows - 1:
            ys.append(rows-1)
            xs.append(x_coord-s)
            break
        elif x_coord-s == 0:
            ys.append(y_coord+s)
            xs.append(0)
            break
        elif mat[y_coord+s][x_coord-s] > limit:
            ys.append(y_coord+s)
            xs.append(x_coord-s)
        else:
            break
    
    #pixels read in along diagonal in the +x,-y direction
    for t in range(0,rows):
        if y_coord+t == rows-1:
            ys.append(rows-1)
            xs.append(x_coord+t)
            break
        elif x_coord+t == columns-1:
            ys.append(y_coord+t)
            xs.append(columns-1)
            break
        elif mat[y_coord+t][x_coord+t] > limit:
            ys.append(y_coord+t)
            xs.append(x_coord+t)
        else:
            break
    
    x_cent = int(0.5*(max(xs)+min(xs)))
    y_cent = int(0.5*(max(ys)+min(ys)))
        
    total_count = 0
    radius = 0
        
    if max(xs)-x_cent > max(ys)-y_cent:
        radius = max(xs)-x_cent
    else:
        radius = max(ys) - y_cent
        
    for u in range(min(xs),max(xs)+1):
        for v in range(min(ys),max(ys)+1):
            if radius >= np.sqrt((x_cent-u)*(x_cent-u)+(y_cent-v)*(y_cent-v)):
                total_count += mat[v][u]
            mat[v][u] = 0
        
    return total_count