import cv2 as cv


img = cv.imread('../Photos/cats.jpg')
cv.imshow('Cats', img)

# Average
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gausian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gausian Blur', gauss)

# Median
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)
