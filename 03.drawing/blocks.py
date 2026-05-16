import cv2
import numpy as np
import random

img =np.zeros((1000,1000,3),dtype='uint8')

for i in range(5):
    for j in range(5):
        k=i*200
        l=j*200

        b=random.randint(0, 255)
        g=random.randint(0, 255)
        r=random.randint(0, 255)

        cv2.rectangle(img,(k,l),(k+200,l+200),(b,g,r),-1)


cv2.imwrite('Blocks.jpg',img)



