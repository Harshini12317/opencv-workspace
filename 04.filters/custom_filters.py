import cv2
import numpy as np

# Open Webcam
cap = cv2.VideoCapture(0)

while True:

    # Read frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to access webcam")
        break

    # -----------------------------
    # Blur Kernel
    # -----------------------------
    blur_kernel = np.ones((3, 3), np.float32) / 9

    blur = cv2.filter2D(frame, -1, blur_kernel)

    # -----------------------------
    # Sharpen Kernel
    # -----------------------------
    sharpen_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharpen = cv2.filter2D(frame, -1, sharpen_kernel)

    # -----------------------------
    # Edge Detection Kernel
    # -----------------------------
    edge_kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])

    edges = cv2.filter2D(frame, -1, edge_kernel)

    # -----------------------------
    # Emboss Kernel
    # -----------------------------
    emboss_kernel = np.array([
        [-2, -1, 0],
        [-1,  1, 1],
        [ 0,  1, 2]
    ])

    emboss = cv2.filter2D(frame, -1, emboss_kernel)

    # Show all outputs
    cv2.imshow("Original", frame)
    cv2.imshow("Blur", blur)
    cv2.imshow("Sharpen", sharpen)
    cv2.imshow("Edges", edges)
    cv2.imshow("Emboss", emboss)

    # Quit on pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()