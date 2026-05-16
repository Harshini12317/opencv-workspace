import cv2


img= cv2.imread('img.jpg')

print(img.shape)
# gives height, width and channels
# channel =1 grayscale
# =3 means bgr

print(img.size)

resized = cv2.resize(img,(500,300))
# imp  here order is width and height
cv2.imwrite('resizedImg.jpg',resized)