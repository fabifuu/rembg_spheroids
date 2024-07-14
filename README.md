# rembg + CellProfiler = Hassle-free 3D image area analysis for Cell-IQ dataset using U2-Net / ISNet machine learning model

This repository provides a pipeline for improving image quality from Cell-IQ source images (cancer spheroids using `rembg` and machine learning models. When source images have poor quality due to low contrast, non-homogenous backgrounds, or out-of-focus imaging, performing area measurements with CellProfiler can be challenging. To address this, we use a machine learning model (ISNet or U2-Net) to distinguish spheroids (objects) from the background before applying the CellProfiler pipeline. The images produced were then used as inputs for the CellProfiler pipeline with simpler thresholding methods (like manual thresholding) due to the clear separation of foreground (spheroid) and background. An illustration of the pipeline that incorporates the segmentation ML model, featuring an example image with non-homogenous background (e.g., drug precipitation), is provided.

## Background
The aim of proliferation experiment is to measure the change of cell proliferation over time, by measuring its area. To measure the area, we need to separate the object with background. Usually, it was done using thresholding method. However, since the thresholding method is very sensitive to the exposure, brightness, and grayscale (gray-ness level) of surrounding object, the area is not perfectly captured. This problem also worsened by the precipitation of drugs/inhibitor or dried well. Thus, the quality of original images are important

## Pipeline

## Example
Time-lapse of spheroids growth (original)
![Before](Asset/before.gif)

Time-lapse of spheroids growth after running the pipeline
![After](Asset/After.gif)
