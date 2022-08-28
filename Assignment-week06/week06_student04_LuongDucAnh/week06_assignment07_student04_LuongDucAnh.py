import numpy as np

#Load grid from txt file 
grid = np.loadtxt("C:/Users/imlda/Desktop/week06_student04_LuongDucAnh/additionalFolder/Problem11.txt", dtype = int, delimiter=' ')

maxProduct = 0
for i in range (0, 20):
    for j in range (0, 17):
        hProduct = grid[i, j] * grid[i, j + 1] * grid[i, j + 2] * grid[i, j + 3] #horizontal
        vProduct = grid[j, i] * grid[j + 1, i] * grid[j + 2, i] * grid[j + 3, i] #verticle
        #Update maxProduct if hProduct or vProduct is greater than maxProduct
        if hProduct > maxProduct:
            maxProduct = hProduct
        if vProduct > maxProduct:
            maxProduct = vProduct
        
for i in range (0, 17):
    for j in range (0, 17):
        dlProduct = grid[i, j] * grid[i + 1, j + 1] * grid[i + 2, j + 2] * grid[i + 3, j + 3] #diagonal left
        drProduct = grid[i, j + 3] * grid[i + 1, j + 2] * grid[i + 2, j + 1] * grid[i + 3, j] #diagonal right
        #Update maxProduct if dlProduct or drProduct is greater than maxProduct
        if dlProduct > maxProduct:
            maxProduct = dlProduct
        if drProduct > maxProduct:
            maxProduct = drProduct
            
print (maxProduct) #70600674