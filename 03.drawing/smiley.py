import cv2
import numpy as np

img = np.zeros((500,500,3),dtype='uint8')

cv2.circle(img, (250,250),200,(0,255,255),-1)

cv2.circle(img,(165,150),20,(0,0,0),-1)
cv2.circle(img,(330,150),20,(0,0,0),-1)

cv2.ellipse(
    img,
    (250,250),      # center
    (140,120),      # radius in x and y
    0,              # rotation angle
    0,              # start angle
    180,            # end angle
    (0,0,0),        # color
    5               # thickness
)


cv2.imwrite('Smiley.jpg',img)