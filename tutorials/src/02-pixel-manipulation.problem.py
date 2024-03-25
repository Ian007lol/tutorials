# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color
img_gray= cv2.imread(r"C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\nl_clown.jpg", cv2.IMREAD_GRAYSCALE)
img_color= cv2.imread(r"C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\nl_clown.jpg", cv2.IMREAD_COLOR)

# TODO Do some print out about the loaded data using type, dtype and shape
print (type(img_gray))
print (type(img_color))
print (img_color.dtype)
print (img_gray.dtype)
print (img_color.dtype)
print (img_gray.shape)
print (img_color.shape)
# TODO Continue with the grayscale image

# TODO Extract the size or resolution of the image
img_gray_h, img_gray_w = img_gray.shape

# TODO Resize image
img_gray.resize(400,400)
# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row
print(img_gray[0, :])
# TODO Print first column
print(img_gray[:, 0])
# TODO Continue with the color image

# TODO Set an area of the image to black
img_color = cv2.resize(img_color, [400, 400])

img_changed = np.copy(img_color)
img_changed[50:200,50:200] = 0 


# TODO Show the image and wait until key pressed
cv2.imshow("My image view", img_color)
cv2.waitKey(0)
# TODO Find all used colors in the image

# TODO Copy one part of an image into another one
img_test = cv2.imread(r"C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\Noisy_Smithsonian_Castle.jpg", cv2.IMREAD_COLOR)
img_final = cv2.imread(r"C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\Bumbu_Rawon.jpg", cv2.IMREAD_COLOR)
img_test = cv2.resize(img_test,[400, 400])
img_final = cv2.resize(img_final,[400, 400])
img_final[50:200,50:200] = img_test[50:200,50:200]
# TODO Save image to a file
cv2.imwrite('img_final.jpg', img_final)
# TODO Show the image again
cv2.imshow("My image view", img_final)
cv2.waitKey(0)

# TODO Show the original image (copy demo)
cv2.imshow("My image view", img_color)