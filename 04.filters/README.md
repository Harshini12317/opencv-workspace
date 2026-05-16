### Filters in OpenCV



Filters are used for:
- noise reduction
- smoothing images
- preprocessing before edge detection
- beauty filters
- preserving important structures

---

# Topics Covered

## 1. Average Blur
Simple averaging of nearby pixels.

*parameter is m*n  kernal size
*kernal size is prop to blur
* kernal size should be odd, because centre should exist
### Features
- Fast
- Simple
- Destroys edges heavily

### Uses
- Basic smoothing
- Lightweight applications

---

## 2. Gaussian Blur
Weighted blur using Gaussian distribution.

parameter are kernal size 
and blur intensity distribution level



### Features
- Smooth natural blur
- Most commonly used
- Good preprocessing step

### Uses
- Edge detection
- Face detection
- Computer vision pipelines

---

## 3. Median Blur
Uses median value instead of average.

```python
cv2.medianBlur()
```

here kernal is always a square matrix ,so only one parameter,  the size should be odd

### Features
- Excellent for salt-and-pepper noise
- Preserves edges better than average blur

### Uses
- OCR preprocessing
- Old image restoration
- Noise removal

---

## 4. Bilateral Filter
Smooths image while preserving edges.

```python
cv2.bilateralFilter()
```

### Features
- Keeps edges sharp
- Advanced smoothing

### Uses
- Beauty filters
- Cartoon effects
- Portrait enhancement

---

# Files

| File | Description |
|---|---|
| compare_filters.py | Applies and compares all filters |

---

# Concepts Learned

- Image smoothing
- Noise reduction
- Kernel size
- Edge preservation
- Preprocessing techniques

---

# Output

The program displays:
- Original Image
- Average Blur
- Gaussian Blur
- Median Blur
- Bilateral Filter

Each filter produces different smoothing behavior.

---

# Next Chapter

06-edge-detection/

Topics:
- Canny Edge Detection
- Sobel Operator
- Laplacian
- Real-time edge detection