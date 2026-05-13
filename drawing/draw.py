import cv2
import numpy as np


img= np.zeros((500,500,3),dtype='uint8')

cv2.line(img,(0,0),(499,499),(0,255,0),2)
cv2.rectangle(img, (50,50), (300,200), (255,0,0), 3)
#cv2.rectangle(image, top_left, bottom_right, color, thickness)

cv2.rectangle(img, (0,0), (50,50), (255,0,0), -1)
# thickness =-1 means solid shape
cv2.circle(img, (250,250), 50, (0,0,255), 3)
#cv2.circle(image, center, radius, color, thickness)

cv2.putText(img,
            "Hello OpenCV",
            (50,450),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,255),
            2)

# # cv2.putText(image,
#             text,
#             position,
#             font,
#             font_scale,
#             color,
#             thickness)
cv2.imshow("Drawing",img)

cv2.waitKey(0)
cv2.destroyAllWindows()