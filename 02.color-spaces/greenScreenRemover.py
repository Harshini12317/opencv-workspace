import cv2
import numpy as np

# Load images
person = cv2.imread("green.jpg")
background = cv2.imread("background.jpg")

# Resize background to match person image
background = cv2.resize(background, (person.shape[1], person.shape[0]))

# Convert person image to HSV
hsv = cv2.cvtColor(person, cv2.COLOR_BGR2HSV)

# Green color range
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

# Create mask for green background
mask = cv2.inRange(hsv, lower_green, upper_green)

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Extract the person
foreground = cv2.bitwise_and(person, person, mask=mask_inv)

# Extract background where green exists
bg = cv2.bitwise_and(background, background, mask=mask)

# Combine both images
final = cv2.add(foreground, bg)

# Show output
cv2.imshow("Original", person)
cv2.imshow("Mask", mask)
cv2.imshow("Final Output", final)

# Save result
cv2.imwrite("output.jpg", final)

cv2.waitKey(0)
cv2.destroyAllWindows()