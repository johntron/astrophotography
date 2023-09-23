## Usage

```bash
conda env create -f environment.yml --prefix ./.env
```

## Domain Models

- **`catalog_entry.py`**: Represents individual entries in a star or object catalog.
- **`image.py`**: Represents a single raw or processed image and associated metadata.
- **`image_set.py`**: Represents a collection of images, possibly a set of raw images for a particular observation.
- **`plate.py`**: Encapsulates the WCS and plate-solving functionalities.
- **`registration.py`**: Manages the registration or alignment of images.
- **`stack.py`**: Represents a set of aligned and stacked images.
- **`stars.py`**: Manages detected stars or features in images.
- **`telescope.py`**: Contains metadata and possibly control commands for the telescope.
- **`visualization.py`**: Manages the creation and properties of any visualizations or outputs that describe the images.

## Flow

- **`flow.py`**: Contains the Prefect flow that orchestrates the execution of tasks defined in the `ops` folder, making
  use of domain models for data storage and manipulation.

## Ops

Each sub-folder in `ops` corresponds to a specific operation or set of related operations in the image processing
pipeline:

- **`align`**: Contains tasks for aligning images, possibly based on detected stars or plate-solving.
- **`calibrate`**: Includes calibration tasks for bias, dark, and flat field corrections.
- **`catalog`**: Tasks for fetching and matching object catalogs.
- **`color`**: Color calibration and balancing tasks.
- **`contrast`**: Contrast adjustment tasks.
- **`deconvolve`**: Deconvolution algorithms like Richardson-Lucy or Wiener filtering.
- **`inspect`**: Tasks for inspecting image data, like generating histograms or statistics.
- **`meta`**: Metadata extraction and writing tasks.
- **`noise`**: Noise estimation and reduction tasks.
- **`read`**: Reading tasks for different image formats.
- **`stack`**: Image stacking tasks using different algorithms.
- **`stretch`**: Dynamic range stretching tasks.
- **`write`**: Writing tasks for different image formats.
