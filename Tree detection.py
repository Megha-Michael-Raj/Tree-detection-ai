
import cv2

# Load the image
image = cv2.imread('tree_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 100, 200)

# Find contours of the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area to remove small objects
min_area = 1000
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Draw bounding boxes around the detected trees
for cnt in filtered_contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv2.imshow('Tree Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
  