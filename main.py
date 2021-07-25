import numpy as np
import cv2

#image input
img = cv2.imread("trialimage.jpg")

#defining edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartonization
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

#Output
cv2.imshow("Original Image: ", img)
cv2.imshow("After change: ", cartoon)

#keeping windows open
cv2.waitKey(0)