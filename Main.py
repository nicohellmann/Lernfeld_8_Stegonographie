from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
im = Image.open(r"Lernfeld_8_Stegonographie\rhinozelfant1.png")
im2arr = np.array(im)
img = mpimg.imread(r'Lernfeld_8_Stegonographie\rhinozelfant2.png')

newimg = []
for i in range(0,len(img)-1):
    temp1_row = []
    for j in range(0,len(img[0])-1):
        temp2_pixel = []
        
        if (img[i][j][0] == img[i+1][j][0] or img[i][j][0] == img[i-1][j][0] or img[i][j][0] == img[i][j+1][0] or img[i][j][0] == img[i][j-1][0]) and (img[i][j][1] == img[i+1][j][1] or img[i][j][1] == img[i-1][j][1] or img[i][j][1] == img[i][j+1][1] or img[i][j][1] == img[i][j-1][1]) and (img[i][j][2] == img[i+1][j][2] or img[i][j][2] == img[i-1][j][2] or img[i][j][2] == img[i][j+1][2] or img[i][j][2] == img[i][j-1][2]) :
            temp2_pixel =[1,1,1]
        else:
            temp2_pixel = img[i][j]
        
        temp1_row.append(temp2_pixel)
    newimg.append(temp1_row)



plt.imshow(newimg)
plt.show()

