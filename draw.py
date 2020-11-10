import cv2 as cv
import numpy as np


blank_img = np.zeros((500, 500, 3), dtype=np.uint8)
# cv.imshow('Blank Image', blank_img)

# 1. Paint a certain color, ex Green
# blank_img[:] = 0, 255, 0
# blank_img[200:300, 250:350] = 0, 255, 0
# cv.imshow('Green Image', blank_img)

# 2.Draw a rectangle
cv.rectangle(blank_img, (0, 0), (blank_img.shape[1]//2, blank_img.shape[0]//2),
             (0, 0, 255), thickness=-1)


# 3. Draw a circle
cv.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2),
          40, (0, 255, 0), thickness=-1)

# 4. D line
cv.line(blank_img, (0, 0),
        (blank_img.shape[1]//2, blank_img.shape[0]//2), (255, 255, 255), thickness=3)

# 5. Write text
cv.putText(blank_img, "Hello!", (255, 255), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (255, 255, 255), thickness=4)


cv.imshow('Green Image', blank_img)
cv.waitKey(0)
