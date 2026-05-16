import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    # Read frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Average Blur
    average = cv2.blur(frame, (9, 9))

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(frame, (9, 9), 0)

    # Median Blur
    median = cv2.medianBlur(frame, 9)

    # Bilateral Filter
    bilateral = cv2.bilateralFilter(frame, 9, 75, 75)

    # Show all outputs
    cv2.imshow("Original", frame)
    cv2.imshow("Average Blur", average)
    cv2.imshow("Gaussian Blur", gaussian)
    cv2.imshow("Median Blur", median)
    cv2.imshow("Bilateral Filter", bilateral)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()