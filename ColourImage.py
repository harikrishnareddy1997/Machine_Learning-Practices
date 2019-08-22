import cv2
import webcolors
import numpy as np
#import getpixel
import image as img1
cv2.imshow('hari.png')

'''
pixel=image[0,0]
print(len(pixel))
print("the most repeated is :",max(pixel))
print(pixel)'''
def find_center(image_file):
    img = cv2.open("hari.png")
    img_mtx = img.load()
    top = bottom = 0
    first_row = True
    # First we find the top and bottom border of the object
    for row in range(img.size[0]):
        for col in range(img.size[1]):
            if img_mtx[row, col][0:3] != (255, 255, 255):
                bottom = row
                if first_row:
                    top = row
                    first_row = False
    middle_row = (top + bottom) / 2  # Calculate the middle row of the object
    print(middle_row)

    left = right = 0
    first_col = True
    # Scan through the middle row and find the left and right border
    for col in range(img.size[1]):
        if img_mtx[middle_row, col][0:3] != (255, 255, 255):
            left = col
            if first_col:
                right = col
                first_col = False
    middle_col = (left + right) / 2  # Calculate the middle col of the object
    print(middle_col)

    return (middle_row, middle_col)
print(img1)











'''getpixel.enable(im)
r, g, b = im.getpixel(0,0)
print 'Red: %s, Green:%s, Blue:%s' % (r,g,b)'''