import cv2

# Read image
img = cv2.imread('img.jpg')

# Check image loaded or not
if img is None:
    print("Image not found!")
    exit()

# Average Blur
average = cv2.blur(img, (9, 9))

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (9, 9), 0)

# Median Blur
median = cv2.medianBlur(img, 9)

# Bilateral Filter
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Show outputs
cv2.imshow("Original Image", img)
cv2.imshow("Average Blur", average)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()