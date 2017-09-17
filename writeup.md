

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:



My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I used Canny function of cv2 to get edges.

Third, I used  the mask function modified by me to get mask edges, then for these mask edges , I deal them with Hough Transform to find lane lines.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by the cv2'function with 2 pionts from last step Hough Transform ...




One potential shortcoming would be appear some strange lines  when there are some shadows or other big hollows on the road. And, the lanes_line is not continuityn sometime.

Another shortcoming could be these code are not good at for the bend roads .




A possible improvement would be to make the lane lines to become more continuityn ...


