# OCR Recognition System Using OpenCV and Tesseract

## Project Overview

This project was developed as part of an AI internship assignment.

The system extracts text from images using Optical Character Recognition (OCR) techniques and validates the extracted results using confidence scores.

The project includes:

* Image preprocessing
* OCR text extraction
* Confidence evaluation
* Bounding-box visualization
* Batch dataset processing
* Interactive Gradio interface

---

## Objectives

The project satisfies the following requirements:

* OCR library integration (Tesseract OCR)
* Grayscale conversion
* Gaussian blur preprocessing
* Adaptive thresholding
* Confidence score analysis
* Minimum confidence validation (80%)
* Visual confirmation using bounding boxes

---

## Technologies Used

* Python
* OpenCV
* Tesseract OCR
* Pandas
* NumPy
* Gradio

---

## Project Structure

OCR-Recognition-Project/

dataset/

output/

annotated/

extracted_text/

reports/

src/

preprocess.py

ocr_engine.py

confidence.py

visualize.py

batch_processor.py

main.py

gradio_app.py

requirements.txt

README.md

---

## Processing Pipeline

Input Image

↓

Grayscale Conversion

↓

Gaussian Blur

↓

Adaptive Thresholding

↓

OCR Recognition

↓

Confidence Analysis

↓

PASS / FAIL Validation

↓

Output Generation

---

## Features

### Image Preprocessing

* Grayscale conversion
* Gaussian blur
* Adaptive thresholding

### OCR Extraction

* Text extraction using Tesseract OCR
* Bounding-box detection

### Confidence Analysis

* Average OCR confidence calculation
* Automatic PASS/FAIL validation

Validation rule:

Confidence ≥ 80% → PASS

Confidence < 80% → FAIL

### Batch Processing

Process all images inside the dataset folder automatically.

Outputs:

* Annotated images
* Extracted text files
* Summary CSV report
* Statistics report

### Gradio Interface

Users can:

* Upload an image
* View OCR text
* View confidence score
* View validation result
* View bounding boxes

---

## Dataset

The project was tested using OCR image datasets containing printed text and document images.

Best performance was achieved on:

* Printed documents
* Book pages
* Typed text
* Clean scans

Lower performance may occur on:

* Handwritten text
* Low-resolution images
* Complex scene text
* Blurred images

---

## Example Outputs

For each image:

* Extracted text
* Confidence score
* PASS/FAIL status
* Annotated image with bounding boxes

---

## Generated Reports

### summary.csv

Contains:

filename

confidence

status

### statistics.txt

Contains:

* Total images processed
* Average confidence
* PASS count
* FAIL count
* Pass rate

---

## Running the Project

### Batch Processing

python main.py

### Gradio Interface

python gradio_app.py

---

## Future Improvements

* Handwritten text recognition
* PDF support
* Real-time webcam OCR
* Arabic OCR support
* Deep-learning OCR models (EasyOCR, PaddleOCR)

---

## Author

Montaha Otify
AI Intern at DecodeLaps
