# Google Arts & Culture Image Collection Pipeline

**Developed:** August 2020

**Related project:** Recommend Art Museum (October 2020)

## Overview

This repository documents a historical Python workflow developed
to collect and prepare artwork images and page-derived information
from Google Arts & Culture.

The work supported the development of Recommend Art Museum,
an artwork and museum recommendation application developed
in October 2020.

## Implementation

The repository includes:

1. Partner page discovery using Selenium.
2. Artwork URL extraction using Scrapy Shell.
3. Image downloading and collection of page-derived text.
4. Dataset organization and JPEG conversion using Pillow.
5. Image cropping and resizing to 224 × 224 pixels.
6. Correlation-based detection of visually similar images.
7. Image renumbering and metadata alignment.

The similarity analysis uses Pearson correlation between grayscale
image vectors, with a threshold of 0.85.

## Technologies

- Python
- Selenium
- Scrapy
- pandas
- NumPy
- Pillow
- Jupyter Notebook
- Conda

## Project Status and Limitations

This is a historical implementation from August 2020.

The scripts and notebooks document a partly interactive workflow,
not a fully automated end-to-end application.

Some processing steps are implemented without independently
verified execution results.

The code depends on historical library versions and website-specific
selectors. Compatibility with the current Google Arts & Culture
website has not been verified.

## Data and Third-Party Content

This repository does not distribute collected artwork images
or metadata datasets.

Artwork images and other third-party content remain subject
to their respective rights and applicable usage conditions.

The availability of this historical source code does not grant
permission to collect, reproduce, or redistribute third-party
content. Any reuse of the collection methods requires independent
review of applicable laws, website policies, and permissions.

This project is not affiliated with or endorsed by Google.
