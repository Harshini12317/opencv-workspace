import cv2

img = cv2.imread("image.jpg",0)

adaptive = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow("Adaptive", adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()