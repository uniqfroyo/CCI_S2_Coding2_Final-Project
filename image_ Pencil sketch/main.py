import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy

# num_down = 2       # number of downsampling steps
# num_bilateral = 7  # number of bilateral filtering steps
#
# img_rgb = cv2.imread("assets/londoneye.JPG")
#
# # downsample image using Gaussian pyramid
# img_color = img_rgb
# for _ in range(num_down):
#     img_color = cv2.pyrDown(img_color)
#
# # repeatedly apply small bilateral filter instead of
# # applying one large filter
# for _ in range(num_bilateral):
#     img_color = cv2.bilateralFilter(img_color, d=9,
#                                     sigmaColor=9,
#                                     sigmaSpace=7)
#
# # upsample image to original size
# for _ in range(num_down):
#     img_color = cv2.pyrUp(img_color)
#
# # convert to grayscale and apply median blur
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
# img_blur = cv2.medianBlur(img_gray, 7)
#
# # detect and enhance edges
# img_edge = cv2.adaptiveThreshold(img_blur, 255,
#                                  cv2.ADAPTIVE_THRESH_MEAN_C,
#                                  cv2.THRESH_BINARY,
#                                  blockSize=9,
#                                  C=2)
#
# # convert back to color, bit-AND with color image
# img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
# img_cartoon = cv2.bitwise_and(img_color, img_edge)
#
# # display
# cv2.imshow("cartoon", img_cartoon)

img = cv2.imread('assets/StPaul.JPG')

#Define the number of bilateral filters
num_bilateral = 7

#Reduce the sampling with the Gaussian pyramid
img_color = img

#Bilateral filtering
for i in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

#Grayscale image conversion
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#Median filtering
img_blur = cv2.medianBlur(img_gray, 7)

#Edge detection and adaptive threshold processing
img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,
                                 blockSize=15,
                                 C=2)

#Convert back to a color image
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

img_cartoon = cv2.bitwise_and(img_color, img_edge)

cv2.imshow('src', img)
cv2.imshow('dst', img_cartoon)
cv2.waitKey()
cv2.destroyAllWindows()