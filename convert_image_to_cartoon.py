import cv2 # pip install opencv-python
import numpy as np


img = cv2.imread("pic.png")

gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur (gray, 5)
edges = cv2.adaptiveThreshold (gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter( img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
# cartoon.save("pic1.png")

cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

# def Convert(image):
#     original_image = cv2.imread("pic.png")
#     Gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#     Blur_image = cv2.GaussianBlur(Gray_image, (3, 3), 0)
#     detect_edge = cv2.adaptiveThreshold(Blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

#     output = cv2.bitwise_and(image, image, mask=detect_edge)

#     cv2.imshow("Original picture", original_image)
#     cv2.imshow("Cartoon Effect", output)
#     cv2.waitKey(0)

# img = cv2.imread("pic.png")
# Convert(img)



