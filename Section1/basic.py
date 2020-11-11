import cv2 as cv

img = cv.imread('../Photos/cats.jpg')
cv.imshow('Cats', img)

# Convert to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edge', canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (400, 400), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 40:500]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
