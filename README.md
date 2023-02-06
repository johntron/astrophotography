# Astrophotography image processing

## Curriculum

* [Introduction to astrophotography](#introduction-to-astrophotography)
* [Image acquisition](#image-acquisition)
* [Image calibration](#image-calibration)
* [Image stacking](#image-stacking)
* [Image enhancement](#image-enhancement)
* [Color processing](#color-processing)
* [Advanced techniques](#advanced-techniques)
* [Image analysis](#image-analysis)

## Introduction to astrophotography

Learn the basics of astrophotography, including the equipment used, camera settings, and exposure times.

## Image acquisition

Learn how to capture images of the night sky using a digital camera or a telescope.

## Image calibration

Learn how to process raw astronomical images, including dark frame subtraction, flat field correction, and bias
correction.

### 1. Introduction to image calibration

Learn the importance of image calibration in astrophotography and its impact on the final image quality.

<dl>
   <dt>Bias frames</dt>
   <dd>Used to capture electronic bias inherent in sensor (zero point), so it can be removed from light frames. Does not capture or account for read noise.</dd>

   <dt>Dark frames</dt>
   <dd>Used to capture noise caused by heat generated during exposures and amplifiers (dark current), so it can be removed from light frames. Includes electronic bias, so bias frames must be subtracted from dark frames, or only dark frames should be used (no bias frames) - <em>❓ is this true❓</em></dd>

   <dt>Flat frames</dt>
   <dd>Used to capture optical imperfections in imaging path, so it can be corrected for. Can correct for minor vignette, sensor mottling (if any), as well as dust and other stray particles. Captured when all pixels are irradiated the same amount. During image processing, light frames are divided by flat frames. This effectively normalizes the range of each pixel by reducing the brightness of pixels with few optical obstructions.</dd>

   <dt>Flat dark frames</dt>
   <dd>Alternative to bias and dark frames for sensors that can't capture these types of calibration frames effectively.</dd>
</dl>

Reference:

* https://telescope.live/blog/learning-about-amp-glow#:~:text=Amplifier%20glow%20refers%20to%20a,circuitry%20of%20the%20imaging%20chip.

### 2. Capturing calibration frames

Dark and flat frames should be captured using same exposure as light frames. Dust can accumulate on the sensor during imaging, and jostling the instrument can dislodge dist. For these reasons, flat frames should be taken immediately after capturing light frames. Bias frames - if used - should be taken with minimal exposure.

### 2. Dark frame subtraction

Dark bias correction (includes sensor bias):

```python
dark_corrected_image = raw_image - reference_dark_image
```

Reference:

* https://prancer.physics.louisville.edu/astrowiki/index.php/Image_processing_with_Python_and_SciPy#Correcting_and_Combining_Images


### 3. Flat field correction

Flat field correction:

```python
final_image = dark_corrected_image / reference_flat_image
```

Reference:

* https://www.macobservatory.com/blog/2018/11/3/how-to-take-easy-flats-using-an-inexpensive-light-source
* https://prancer.physics.louisville.edu/astrowiki/index.php/Image_processing_with_Python_and_SciPy#Correcting_and_Combining_Images
* https://homepages.inf.ed.ac.uk/rbf/HIPR2/pixdiv.htm

### 4. Bias correction

This isn't necessary when using dark frames, because dark frames include electronic bias; however, if bias frames were used, the correction would use subtraction.

### 6. Image calibration techniques

Individual calibration frames can be combined to create a "master" calibration frame - e.g. master dark frame. These master frames should be combined with light frames of the same exposure.

To save time, a library of calibration frames can be created ahead of time. This avoids the time-consuming process of creating calibration frames during an imaging session. Most (all?) calibration frames can be created while the sun is up; however, accounting for temperature would be hard.

### 7. Image calibration settings

Learn how to adjust image calibration settings to produce the best final image, including choosing the right number of
images to use and the best calibration technique.

### 8. Outstanding questions

* If creating a calibration frame library, how do you account for temperature?
* How many calibration frames should be included in a master frame?

## Image stacking

Learn how to combine multiple images to increase the signal-to-noise ratio and produce a final image
with greater detail.

1. Introduction to image stacking: Learn the basics of image stacking and its importance in astrophotography.
1. Image acquisition: Learn how to capture images of the night sky using a digital camera or a telescope.
1. Image calibration: Learn how to process raw astronomical images, including dark frame subtraction, flat field
   correction, and bias correction.
1. Registration: Learn how to align and register multiple images to be stacked, including techniques for eliminating
   field rotation, field curvature, and focal plane distortion.
2. Methods: Learn about different image stacking methods, including average stacking, median stacking, and sigma
   clipping.
3. Settings: Learn how to adjust image stacking settings to produce the best final image, including choosing the
   right number of images to stack and the best stacking method.
4. Post-processing: Learn how to post-process the final stacked image using techniques such as histogram stretching,
   noise reduction, and sharpening.

## Image enhancement

Learn how to process and enhance final images using techniques such as histogram stretching, noise
reduction, and sharpening.

1. Introduction to image enhancement: Learn the importance of image enhancement in astrophotography and its impact
   on the final image quality.
2. Image processing software: Learn how to use image processing software, such as Adobe Photoshop, GIMP, or
   PixInsight, to enhance astrophotographic images.
2. Histogram stretching: Learn how to adjust the image brightness and contrast using histogram stretching to bring
   out faint details in the image.
2. Noise reduction: Learn how to reduce the noise in an image using techniques such as wavelet processing, selective
   smoothing, and median filtering.
2. Sharpening: Learn how to sharpen the details in an image using techniques such as unsharp masking, high-pass
   filtering, and deconvolution.
2. Color processing: Learn how to adjust the colors in an image to bring out the best representation of the night
   sky, including techniques for color balancing, color correction, and color grading.
2. Layer masks: Learn how to use layer masks to selectively apply image processing techniques to specific areas of
   an image.

## Color processing

Learn how to create a color image from a set of monochrome images captured through different
filters.

1. Introduction to color processing: Learn the importance of color processing in astrophotography and its impact on the
   final image quality.
1. Color theory: Learn the basics of color theory and how it applies to astrophotography.
1. Image processing software: Learn how to use image processing software, such as Adobe Photoshop, GIMP, or PixInsight,
   to process the colors in astrophotographic images.
1. Color balancing: Learn how to balance the colors in an image to achieve a natural-looking representation of the night
   sky.
1. Color correction: Learn how to correct the colors in an image to bring out the best representation of the celestial
   objects, including techniques for removing color casts, fixing white balance, and adjusting saturation.
1. Color grading: Learn how to adjust the colors in an image for artistic effect, including techniques for color grading
   and creating color-lookup tables.
1. Layer masks: Learn how to use layer masks to selectively apply color processing techniques to specific areas of an
   image.

## Advanced techniques

Learn about advanced techniques such as luminance layering, layer masks, and star tracking for
capturing sharp images of the night sky.

1. Advanced image processing techniques: Learn about advanced image processing techniques, including non-linear image
   processing, HDR imaging, and advanced color processing.
1. Advanced stacking techniques: Learn about advanced stacking techniques, including median stacking, sigma clipping,
   and multiscale processing.
1. Image restoration: Learn about techniques for restoring images, including removing artifacts, correcting distortion,
   and repairing damage.
1. Astrophotography with telescopes: Learn how to capture astrophotographic images using a telescope, including
   techniques for focusing, guiding, and stacking.
1. Astrophotography with specialized cameras: Learn how to capture astrophotographic images using specialized cameras,
   such as CCD or CMOS cameras.
1. Astrophotography with narrowband filters: Learn how to capture images using narrowband filters, including
   hydrogen-alpha, oxygen-iii, and sulfur-ii filters.
1. Image integration: Learn how to integrate multiple images captured under different conditions or with different
   equipment to produce a final image with improved quality and detail.

## Image analysis

Learn how to analyze astrophotographic images to extract scientific information, such as determining
the position and brightness of stars, the size of galaxies, and the presence of nebulae.

1. Introduction to image analysis: Learn about the importance of image analysis in astrophotography and its role in
   extracting scientific information from images.
1. Image processing software: Learn how to use image processing software, such as PixInsight or IRAF, for image
   analysis.
1. Photometry: Learn how to measure the brightness of celestial objects in an image, including techniques for aperture
   photometry, PSF photometry, and profile fitting.
1. Astrometry: Learn how to measure the positions of celestial objects in an image, including techniques for plate
   solving and world coordinate systems.
1. Image statistics: Learn how to extract information about the distribution and properties of the data in an image,
   including techniques for computing mean, median, mode, standard deviation, and skewness.
1. Image visualization: Learn how to visualize the data in an image, including techniques for creating histograms,
   contour plots, and surface plots.
1. Object detection: Learn how to detect celestial objects in an image, including techniques for source extraction,
   deblending, and false detection removal.