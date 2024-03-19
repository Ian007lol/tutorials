# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.
# TODO First step is to import the opencv module which is called 'cv2'
import cv2
# TODO Check the opencv version
print(cv2.__version__)

# TODO Load an image with image reading modes using 'imread'
image = cv2.imread(r'C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\bumbu_rawon.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.

# TODO Resize image with 'resize'
desired_size = (300, 200)
resized_image = cv2.resize(image, desired_size)
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# TODO Rotate image (but keep it rectangular) with 'rotate'
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# TODO Save image with 'imwrite'
cv2.imwrite('first_test.jpg', rotated_image)
# TODO Show the image with 'imshow'
