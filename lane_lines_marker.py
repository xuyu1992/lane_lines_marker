# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 00:14:14 2017

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:10:11 2017

@author: admin
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def gray_f(img):
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    kernel_size = 3 # Must be an odd number (3, 5, 7...)
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0) 
    return blur_gray

def canny_edge(img):
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(img, low_threshold, high_threshold)
    return edges

def mask_f(img):
    img0 = np.copy(img)
    mask = np.zeros_like(img0)   
    ignore_mask_color = 255   
    
    # This time we are defining a five sided polygon to mask
    imshape = img.shape
    if imshape[1] == 1280:    
        vertices = np.array([[(210,670),(615, 460), (670, 430), (1090,670),(640,655)]], dtype=np.int32)
    #For the challenge.mp4
    else :
        vertices = np.array([[(0,imshape[0]),(450,330), (490, 310), (imshape[1],imshape[0])]], dtype=np.int32)
    #For 540p videos
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    masked_edges = cv2.bitwise_and(img, mask)
    return masked_edges

def hough_linesp(img):
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15    # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 30 #minimum number of pixels making up a line
    max_line_gap = 20    # maximum gap in pixels between connectable line segments
    line_image = np.copy(image)*0 # creating a blank to draw lines on
    
    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)
    return lines

def draw_lines(lines):
    line_image = np.copy(image)*0
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    lines_edges = cv2.addWeighted(frame, 0.8, line_image, 1, 0) 
    return lines_edges
# Create a "color" binary image to combine with line image
# =============================================================================
#     color_edges = np.dstack((edges, edges, edges)) 
# =============================================================================
    
    # Draw the lines on the edge image
    
stream = cv2.VideoCapture('solidYellowLeft.mp4')
if stream.isOpened() == False:
    print "Cannot open input video"
    exit()
size = (int(stream.get(3)),int(stream.get(4)))
print size
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 25.0, size)
count = 1
# =============================================================================
ret, frame = stream.read()
while ret:
    image = np.copy(frame)
    gary_img = gray_f(image)
    edge_img = canny_edge(gary_img)
    mask_region = mask_f(edge_img)
    hough_lines = hough_linesp(mask_region)
    lane_line = draw_lines(hough_lines)
    out.write(lane_line)
    print 'Writing the ',count ,'th frame '
    count += 1 
    ret, frame = stream.read()
stream.release()
out.release()
print 'end'













