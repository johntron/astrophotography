"""
The input images aren't great for this, because they can be perfectly aligned through a simple rotation and have no
WCS data
"""

import drizzle.util
from drizzle import drizzle
import cv2
import glob
import numpy as np

# Parameters
input_folder = './test_images/'  # Folder containing input images
output_image = 'stacked_image.fits'  # Output stacked image
image_list = glob.glob(f"{input_folder}*.png")

# Initialize output array (same size as input images)
first_image = cv2.imread(image_list[0], cv2.IMREAD_GRAYSCALE)
output_shape = first_image.shape
output_array = np.zeros(output_shape, dtype=first_image.dtype)

# Initialize weight map (same size as input images)
weight_map = np.zeros(output_shape, dtype=np.float64)

# Center of rotation for alignment
center_of_rotation = (256, 256)

driz = drizzle.Drizzle()
# Loop through each image, align and stack
for idx, image_file in enumerate(image_list):
    # Read image
    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

    # Find the coordinates of the star (white dot)
    star_coordinates = np.column_stack(np.where(img > 128))

    # Average coordinates if there are more than one
    star_x, star_y = np.mean(star_coordinates, axis=0)

    # Calculate angle to rotate the star back to its initial position
    dx = star_x - center_of_rotation[0]
    dy = star_y - center_of_rotation[1]
    angle = np.arctan2(dy, dx) * 180 / np.pi

    # Rotate the image to align the star
    M = cv2.getRotationMatrix2D(center_of_rotation, -angle, 1)
    img_aligned = cv2.warpAffine(img, M, output_shape[::-1])

    # Create weight map for this image (all ones)
    wgt = np.ones(img_aligned.shape, dtype=np.float64)

    # Generate transformation matrix (identity, since we have aligned the images)
    transform = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # Drizzle image onto output_array
    driz.add_image(img_aligned, transform, wgt, output_array, weight_map, 1.0, 'cps', 1.0, 1.0, 1)

# Normalize the output array based on the weight map
output_array = drizzle.util.drizzle_output(output_array, weight_map, out_units='cps')

# Save the stacked image
drizzle.util.writefits(output_image, output_array, None)

print("Stacking complete.")
