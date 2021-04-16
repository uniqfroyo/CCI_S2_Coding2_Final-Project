import cv2
import math
import numpy as np

# Read the original image
img = cv2.imread('assets/Regent street.JPG')

# Gets the image rows and columns
rows, cols = img.shape[:2]

# New target image
dst = np.zeros((rows, cols, 3), dtype="uint8")

# define wave parameters
wavelength = 20
amplitude = 30
phase = math.pi / 4

# get the center point
centreX = 0.5
centreY = 0.5
radius = min(rows, cols) / 2

# set wave cover area
icentreX = cols * centreX
icentreY = rows * centreY

# wave effects
for i in range(rows):
    for j in range(cols):
        dx = j - icentreX
        dy = i - icentreY
        distance = dx * dx + dy * dy

        if distance > radius * radius:
            x = j
            y = i
        else:
            # calculate wave area
            distance = math.sqrt(distance)
            amount = amplitude * math.sin(distance / wavelength * 2 * math.pi - phase)
            amount = amount * (radius - distance) / radius
            amount = amount * wavelength / (distance + 0.0001)
            x = j + dx * amount
            y = i + dy * amount

        # border judgement
        if x < 0:
            x = 0
        if x >= cols - 1:
            x = cols - 2
        if y < 0:
            y = 0
        if y >= rows - 1:
            y = rows - 2

        p = x - int(x)
        q = y - int(y)

        # wave assignment
        dst[i, j, :] = (1 - p) * (1 - q) * img[int(y), int(x), :] + p * (1 - q) * img[int(y), int(x), :]
        + (1 - p) * q * img[int(y), int(x), :] + p * q * img[int(y), int(x), :]

# show image
cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()