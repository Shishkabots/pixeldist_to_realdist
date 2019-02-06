'''
Formula and calculations for final r and theta.

Conventions for theta:
Theta counterclockwise is negative, clockwise is positive.

Note that there is no theta offset for the camera relative to the robot, i.e. camera theta is robot theta; we can always orient it
properly and it is terrible if we need to do the offset.

Also, pixel_delta_y should never be negative (we are assuming that the object is on the top half of the image)

precalculated:
tape_offset_x, tape_offset_y.
tape_offset_r, tape_offset_theta (by extension).
robot_offset_x, robot_offset_y.

need functions:
find_center(img)
convert_dist(pixel_r, height)
get_cameraToTape_theta(img)

pixel_delta_x, pixel_delta_y = find_center(img)
camera_r = convert_dist(dist(pixel_delta_x, pixel_delta_y), height)
camera_theta = atan(pixel_delta_y/pixel_delta_x)	# for negative pixel_delta_x, should take return a negative angle

camera_delta_x = camera_r * cos(camera_theta)
camera_delta_y = camera_r * sin(camera_theta)

cameraToTape_theta = get_cameraToTape_Theta()

tape_delta_x = tape_offset_r * cos(cameraToTape_theta + tape_offset_theta)
tape_delta_y = tape_offset_r * sin(cameraToTape_theta + tape_offset_theta)

delta_y = robot_offset_y + camera_delta_y + tape_delta_y
delta_x = robot_offset_x + camera_delta_x + tape_delta_x
r = sqrt(delta_y ** 2 + delta_x ** 2)
theta = atan(delta_y/delta_x)

Send theta to gyro code, and send r to encoder code. Turn -theta (i.e. if theta here is negative, turn positive theta under cartesian coordinates, i.e. turn counterclockwise).
Then move forward r.

Step 3 handles the final turn.
'''

import cv2

def convert_dist(pixel_dist, height):

def get_cameraToTape_Theta(img):

def find_center(img):




tape_offset_x = 0
tape_offset_y = 0
tape_offset_r = sqrt(tape_offset_x ** 2, tape_offset_y ** 2)
tape_offset_theta = atan(tape_offset_y / tape_offset_x)
robot_offset_x = 0
robot_offset_y = 0

pixel_delta_x, pixel_delta_y = find_center(img)
camera_r = convert_dist(dist(pixel_delta_x, pixel_delta_y), height)
camera_theta = atan(pixel_delta_y/pixel_delta_x)	# for negative pixel_delta_x, should take return a negative angle

camera_delta_x = camera_r * cos(camera_theta)
camera_delta_y = camera_r * sin(camera_theta)

cameraToTape_theta = get_cameraToTape_Theta(img)

tape_delta_x = tape_offset_r * cos(cameraToTape_theta + tape_offset_theta)
tape_delta_y = tape_offset_r * sin(cameraToTape_theta + tape_offset_theta)

delta_y = robot_offset_y + camera_delta_y + tape_delta_y
delta_x = robot_offset_x + camera_delta_x + tape_delta_x
r = sqrt(delta_y ** 2 + delta_x ** 2)
theta = atan(delta_y/delta_x)