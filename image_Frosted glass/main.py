import cv2
import numpy as np
import matplotlib.pyplot as plt

# # read the image
# img = cv2.imread("assets/Londoneye.JPG", cv2.IMREAD_UNCHANGED)
# rows, cols, chn = img.shape
#
# # add noise
# for i in range(50000):
#     x = np.random.randint(0, rows)
#     y = np.random.randint(0, cols)
#     img[x, y, :] = 255
#
# cv2.imshow("noise", img)
#
# # Wait for the show
# cv2.waitKey(0)
# cv2.destroyAllWindows() //噪点
#
# src = cv2.imread('assets/Londoneye.JPG', cv2.IMREAD_UNCHANGED)
#
# #Set the convolution kernel
# kernel = np.ones((20,20), np.uint8)
#
# #图像顶帽运算
# result = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)
#
# cv2.imshow("src", src)
# cv2.imshow("result", result)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # Read the original image grayscale color
# img = cv2.imread('assets/CityofLondon.JPG', 0)
# print(img.shape)
#
# #Gets the height and width of the image
# rows, cols = img.shape[:]
#
# #Convert the image from two dimensional pixels to one dimensional pixels
# data = img.reshape((rows * cols, 1))
# data = np.float32(data)
#
# #Define the center (type,max_iter,epsilon)
# criteria = (cv2.TERM_CRITERIA_EPS +
#             cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#
# #set the label
# flags = cv2.KMEANS_RANDOM_CENTERS
#
# #K-means clustering aggregates into 4 categories
# compactness, labels, centers = cv2.kmeans(data, 4, None, criteria, 10, flags)
#
# #Generate the final image
# dst = labels.reshape((img.shape[0], img.shape[1]))
#
# #Used to display Chinese labels normally
# plt.rcParams['font.sans-serif']=['SimHei']
#
# #show the image
# titles = [u'原始图像', u'聚类图像']
# images = [img, dst]
# for i in range(2):
#    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray'),
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
# plt.show()




#read the image
src = cv2.imread('assets/CityofLondon.JPG')

# New target image
dst = np.zeros_like(src)

# Gets the image rows and columns
rows, cols = src.shape[:2]

# Define offsets and random numbers
offsets = 70
random_num = 10

#Frosted glass effect: the color of the random pixel in the neighborhood of the pixel is replaced by the color of the current pixel
for y in range(rows - offsets):
    for x in range(cols - offsets):
        random_num = np.random.randint(0,offsets)
        dst[y,x] = src[y + random_num,x + random_num]

#show the image
cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()