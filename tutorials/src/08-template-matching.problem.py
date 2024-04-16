# Exercise #8
# -----------
#
# Demonstrating how to do template matching in OpenCV.

# Template matching, originally with objects from the image. Typical example
# is counting blood cells
import cv2
import numpy as np

use_color = False

if use_color:
    """"""
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image
    image_color = cv2.imread(r'C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\chewing_gum_balls01.jpg', cv2.IMREAD_COLOR)
    template_color = cv2.imread(r'C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\cgb_red.jpg', cv2.IMREAD_COLOR)
    # TODO Read shape of the template and original image
    img_h, img_w, _ = image_color.shape
    template_h, template_w, _ = template_color.shape

else:
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image
    image_color = cv2.imread(r'C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\chewing_gum_balls01.jpg', cv2.IMREAD_COLOR)
    template_color = cv2.imread(r'C:\Users\micro\Documents\GitHub\tutorials\tutorials\data\images\cgb_green.jpg', cv2.IMREAD_COLOR)
    template_h, template_w, _ = template_color.shape

    # TODO Read shape of the template and original image

    # TODO Define template matching methods,
    # See https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the
    # math behind each method
    methods = [
        cv2.TM_CCORR_NORMED
    ]
    # TODO Loop over all methods in order to compare them
    for method in methods:
       img = image_color.copy()
       match_img = cv2.matchTemplate(img, template_color, method)
       match_bin = cv2.threshold(match_img, 0.90, 1.0, cv2.THRESH_BINARY)[1]
       match_bin = np.uint8(match_bin*255)
       connectivity = 8
       (numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(match_bin, connectivity, cv2.CV_16F)
       for i in range(1, numLabels):
           pos_x = stats[i, cv2.CC_STAT_LEFT]
           pos_y = stats[i, cv2.CC_STAT_TOP]
           size_x = stats[i, cv2.CC_STAT_WIDTH]
           size_y = stats[i, cv2.CC_STAT_HEIGHT]
           cv2.rectangle(img,(pos_x, pos_y), (pos_x + template_w, pos_y + template_h), (0,255,0))

       #result = cv2.bitwise_and(img, img, mask = match_bin)
       cv2.imshow("Template matching result", match_bin)
       cv2.imshow("Original Image", img)


       cv2.waitKey(0)


        # TODO (In loop) work on a new image each time
        # TODO (In loop) do the template matching

    # TODO (In loop) get the best match location

    # TODO (In loop) draw rectangle at found location

    # TODO (In loop) show original image with found location

    # TODO (In loop) show image with the template matching result for all pixels

    # (in loop) just press any key to show the next image
    

cv2.destroyAllWindows()
