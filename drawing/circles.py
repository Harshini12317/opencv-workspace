import cv2
import numpy as np
import random

img =np.zeros((1000,1000,3),dtype='uint8')

for i in range(1000):  
        

    b=random.randint(0, 255)
    g=random.randint(0, 255)
    r=random.randint(0, 255)

    rad1=random.randint(0,1000)
    rad2=random.randint(0,1000)

    radius=random.randint(0,100)

    cv2.circle(img,(rad1,rad2),radius,(b,g,r),-1)


        


cv2.imwrite('circles.jpg',img)

# cv2.imshow('wallpaper',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


