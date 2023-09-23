from .domain_models import image
from .ops import io
from .ops import calibrate
import pathlib

# @task
# def calibrate_images(image_set: image_set.UnprocessedImageSet):
#     # Calibrate raw images (bias, dark, and flat field corrections)
#     return calibrate.(images)
#
# @task
# def align_images(calibrated_images):
#     # Align images using registration
#     return align.align_images(calibrated_images)
#
# @task
# def stack_aligned_images(aligned_images):
#     # Stack aligned images using a chosen stacking method
#     return stack.stack_images(aligned_images)
#
# @task
# def reduce_noise(stacked_image):
#     # Apply noise reduction to the stacked image
#     return noise.reduce_noise(stacked_image)
#
# @task
# def enhance_contrast(image_with_reduced_noise):
#     # Enhance contrast in the image
#     return contrast.adjust_contrast(image_with_reduced_noise)
#
# @task
# def stretch_image(contrast_enhanced_image):
#     # Stretch the dynamic range of the image
#     return stretch.linear_stretch(contrast_enhanced_image)
#
# @task
# def write_final_image(stretched_image):
#     # Write the final processed image to an output format
#     write.write_fits_image(stretched_image, "/path/to/output/final_image.fits")

def process_images():
    # uncalibrated_images = io.read_uncalibrated("../input/NGC 1365 Great Barred Galaxy")
    # calibrated_images = calibrate.passthrough(uncalibrated_images)
    i = image.ChannelSeparated(pathlib.Path("../input/NGC 1365 Great Barred Galaxy"))
    print(i.luminosity)
    # aligned_images = align_images(calibrated_images)
    # stacked_image = stack_aligned_images(aligned_images)
    # noise_reduced_image = reduce_noise(stacked_image)
    # contrast_enhanced_image = enhance_contrast(noise_reduced_image)
    # final_image = stretch_image(contrast_enhanced_image)
    # write_final_image(final_image)

if __name__ == "__main__":
    process_images()
