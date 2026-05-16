import cv2
import numpy as np

img = cv2.imread("shapes.png",0)

_, thresh = cv2.threshold(
    img,
    127,
    255,
    cv2.THRESH_BINARY
)

kernel = np.ones((5,5),np.uint8)

eroded = cv2.erode(
    thresh,
    kernel,
    iterations=1
)

cv2.imshow("Original",thresh)
cv2.imshow("Eroded",eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()