import cv2 as cv
import numpy as np

from helper import rescaleFrame


img_org = cv.imread('../Photos/boston.jpg')
img = rescaleFrame(img_org, 0.4)

blank = np.zeros(img.shape[:2], np.uint8)

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Boston', img)
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(blank.shape)
print(b.shape)
print(g.shape)
print(r.shape)
print(blue.shape)
print(green.shape)
print(red.shape)

cv.waitKey(0)
