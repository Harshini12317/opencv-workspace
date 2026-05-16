import cv2

img = cv2.imread("img.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(
    gray,
    cv2.CV_64F
)

lap = cv2.convertScaleAbs(lap)

cv2.imshow("Original", img)
cv2.imshow("Laplacian", lap)

cv2.waitKey(0)
cv2.destroyAllWindows()