import cv2 as cv
import numpy as np


img = cv.imread('../Photos/cats.jpg')
cv.imshow('Cats', img)


def translate(img, x, y):
    """Translate an image
    -x: left
    x: right
    -y: up
    y: down
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


def rotate(img, angle, rotPoint=None):
    """Rotate an image
    rotPoint: Rotation Point
    """
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)

# Flipping
flip = cv.flip(img, 1,)

# Cropping
cropped = img[200:400, 300:400]

translated = translate(img, 100, -100)
cv.imshow('Translated', translated)

rotated = rotate(img, -45,)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45,)
cv.imshow('Rotated Rotated', rotated_rotated)

cv.imshow('Resized', resized)

cv.imshow('Flipped', flip)

cv.imshow('Cropped', cropped)

cv.waitKey(0)
