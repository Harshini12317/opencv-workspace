An edge is a place where pixel intensity changes suddenly

That boundary = edge

Examples:

Border of a face
Border of a car
Border of text
Shape boundaries


## Canny edge --> Detects all edgs
## Sobet  -->  Can detect horizontal and Vertical edges differently 
## Laplacian → detects edges in all directions at once


#### Thresholding before edges
Thresholding means:

Convert an image into only black and white based on a cutoff value

If threshold = 127

Pixel values:
50   100   140   220

After threshold:
0     0    255   255


If pixel > threshold → White (255)

If pixel ≤ threshold → Black (0)

### Flow

Image
   ↓
Grayscale
   ↓
Threshold
   ↓
Edge Detection

# Why do this before edge detection?
Because it removes unnecessary details and simplifies the image.