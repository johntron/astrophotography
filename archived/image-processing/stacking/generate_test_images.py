import pathlib

import cv2
import numpy as np
import math

# Parameters
num_images = 50  # Number of images to generate
image_size = (512, 512)  # Size of the image
center = (256, 256)  # Center of rotation
radius = 100  # Radius of rotation
star_size = 5  # Size of the star (white dot)
output_folder = pathlib.Path("./test_images/")

output_folder.mkdir()

# Loop to generate images
for i in range(num_images):
    # Initialize a black image
    img = np.zeros((image_size[1], image_size[0], 3), dtype=np.uint8)

    # Calculate the position of the star considering field rotation
    angle = 2 * np.pi * i / num_images
    x = int(center[0] + radius * math.cos(angle))
    y = int(center[1] + radius * math.sin(angle))

    # Draw the star (white dot)
    cv2.circle(img, (x, y), star_size, (255, 255, 255), -1)

    # Save the image
    dest = output_folder / f"image_{i + 1}.png"
    cv2.imwrite(str(dest), img)

    print(f"Generated image {i + 1} at {dest}")

print("All images generated.")
