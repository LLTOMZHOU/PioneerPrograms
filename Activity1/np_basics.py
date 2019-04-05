import numpy as np
import cv2

img = cv2.imread("chicago.jpg")
blankImg1 = np.zeros((10,10), np.uint8)
blankImg2 = np.ones((10,10), np.uint8) * 255

mat1 = np.array([1.3, 2.3333333, 3])
print("Dimensions:")
print(mat1.shape)
print(mat1.size)
print(mat1.dtype) #float64 is default
print("ItemSize:")
print(mat1.itemsize)

#Modifying mat1's shape
print("Reshape:")
print(mat1.reshape(3,1))

#Performing operation in numpy instead of list and iteration
print(mat1 * 3)
print(mat1 // 2)

#Very interesting trick
mat2 = mat1 < 2
print(mat2)
print("Dimensions:")
print(mat2.shape)
print(mat2.size)
print(mat2.dtype)
print("ItemSize:")
print(mat1.itemsize)

#Random array
a = np.random.random((2,3)) #random float from 0 to 1
print(a)
b = np.array([1,2,3])
print("Randomly chosen int from 1,2, and 3")
print(np.random.choice(b)) #randomly choose an element

#Creating multi-dimensional arrays
mat3 = np.array([(1.3, 2, 3), (2, 3, 4)], np.float32)
print("Dimensions:")
print(mat3.shape)
print(mat3.size)
print(mat3.dtype)
print("ItemSize:")
print(mat3.itemsize)
# cv2.waitKey()

#Accessing img array
print("values at row 20, col 30: ", img[20,30])
print("values at row 20, col 30: ", img[20,30,:])
print(img.shape)
print("Row 5:")
print(img[5])
print("Col 5:")
print(img[:,0,:])

cv2.imshow("cropped_img", img[:100, :340, :])
# tye print every row form 10 to 50
cv2.imshow("row", img[10:50])

# tye print every row form 10 to 50
cv2.imshow("cols", img[:, 20:80, :])

cv2.imshow("original image", img)

cv2.waitKey()

cv2.destroyAllWindows()



