# Automated Fruit Sorting System (Computer Vision Based)

## Project Overview

The **Automated Fruit Sorting System** is a real-time computer vision application that classifies and sorts fruits based on **color, size, and ripeness** using a **laptop webcam**. The project is built using **Python and OpenCV** and demonstrates how visual features can be used to automate agricultural sorting tasks.

This system is designed for **educational purposes, mini-projects, and prototypes**, and can be extended to real-world automation using hardware such as conveyor belts and servo motors.

---

## Features

*  Real-time fruit detection using webcam
* Color classification (Red, Yellow, Green)
* Size classification (Small, Medium, Large)
* Ripeness detection (Unripe, Ripe, Overripe)
* Automated sorting decision (Bin assignment)
* Live visualization with labels and mask output

---

## How It Works

1. Captures live video from the laptop camera
2. Preprocesses frames using Gaussian blur and HSV color space
3. Segments fruit from the background
4. Extracts features:

   * Hue → Color
   * Contour area → Size
   * Saturation → Ripeness
5. Applies sorting logic to assign a bin
6. Displays results in real time

---

## Technologies Used

* **Python 3.x**
* **OpenCV** (Computer Vision)
* **NumPy**
* **VS Code** (Recommended IDE)

---

## Project Structure

```
Fruit Sorting System/
│── main.py                 # Main application (webcam-based)
│── utils.py                # Image preprocessing & segmentation
│── color_detector.py       # Color classification logic
│── size_detector.py        # Size classification logic
│── ripeness_detector.py    # Ripeness detection logic
│── README.md               # Project documentation
```

---

##  Usage Instructions

* Place **one fruit at a time** in front of the webcam
* Use a **plain background** for best results
* Keep the fruit **30–50 cm** from the camera
* Avoid showing your face or other objects
* Press **Q** to quit the application

---

## Output

* Live camera feed with classification text
* Binary mask showing detected fruit
* Sorting bin decision displayed on screen

Example output:

```
Color: Yellow | Size: Medium | Ripeness: Ripe → BIN 2
```
---

## Advantages

* Low-cost solution
* Real-time processing
* Easy to understand and modify
* Suitable for academic projects
* Hardware integration ready

---

## Limitations

* Detects only one fruit at a time
* Sensitive to lighting conditions
* Fixed camera distance required
* Not trained on all fruit varieties

---

## Future Enhancements

* Integration with conveyor belt and servo motors
* Machine learning / deep learning models
* Multi-fruit detection
* Mobile camera support
* Accuracy evaluation dashboard

---

## Applications

* Agricultural automation
* Fruit grading and quality control
* Educational demonstrations
* Computer vision learning projects

---

## Installation & Setup

### Clone or Download the Project

```bash
git clone git@github.com:engalaagabr/Fruit-Sorting-System.git
cd Fruit-Sorting-System
```

### Install Required Libraries

```bash
pip install opencv-python numpy
```

### Run the Application

```bash
python main.py
```
---
THX
