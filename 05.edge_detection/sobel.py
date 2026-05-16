import cv2
import numpy as np

img = cv2.imread("img.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(
    gray,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)

sobely = cv2.Sobel(
    gray,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)

combined = cv2.bitwise_or(
    cv2.convertScaleAbs(sobelx),
    cv2.convertScaleAbs(sobely)
)

cv2.imshow("Original",img)
cv2.imshow("Sobel X",cv2.convertScaleAbs(sobelx))
cv2.imshow("Sobel Y",cv2.convertScaleAbs(sobely))
cv2.imshow("Combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()