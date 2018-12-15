import cv2
import numpy as np

image = cv2.imread("./kir.png")

def erode(im, struct_elem_w, struct_elem_h):
    x, y, rgb = im.shape
    from_around_px_x = -(struct_elem_w - 1) // 2
    to_around_px_x = ((struct_elem_w - 1) // 2) + 1
    from_around_px_y = -(struct_elem_h - 1) // 2
    to_around_px_y = ((struct_elem_h - 1) // 2) + 1
    res_img = np.zeros((x, y, 3))
    for c in range(rgb):
        for i in range(x):
            for j in range(y):
                min_pixel = 255
                for k in range(from_around_px_x, to_around_px_x):
                    for l in range(from_around_px_y, to_around_px_y):
                        if 0 > i + k or i + k >= x or 0 > j + l or j + l >= y:
                            continue
                        test_pixel = float(im[i + k, j + l, c])
                        if min_pixel > test_pixel:
                            min_pixel = test_pixel
                res_img[i, j, c] = min_pixel
    return res_img

def dilate(im, struct_elem_w, struct_elem_h):
    x, y, rgb = im.shape
    from_around_px_x = -(struct_elem_w - 1) // 2
    to_around_px_x = ((struct_elem_w - 1) // 2) + 1
    from_around_px_y = -(struct_elem_h - 1) // 2
    to_around_px_y = ((struct_elem_h - 1) // 2) + 1
    res_img = np.zeros((x, y, 3))
    for c in range(rgb):
        for i in range(x):
            for j in range(y):
                max_pixel = 0
                for k in range(from_around_px_x, to_around_px_x):
                    for l in range(from_around_px_y, to_around_px_y):
                        if 0 > i + k or i + k >= x or 0 > j + l or j + l >= y:
                            continue
                        test_pixel = float(im[i + k, j + l, c])
                        if max_pixel < test_pixel:
                            max_pixel = test_pixel
                res_img[i, j, c] = max_pixel
    return res_img


e = erode(image, 5, 5)
d = dilate(image, 5, 5)

cv2.imshow("eroded", e)
cv2.imshow("dilated", d)
cv2.waitKey()
