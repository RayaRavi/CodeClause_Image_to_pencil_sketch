import cv2

# Load the image
img = cv2.imread('r.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray_img = 255 - gray_img

# Blur the inverted image using a Gaussian filter
blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

# Invert the blurred image
inverted_blurred_img = 255 - blurred_img

# Create the pencil sketch image by combining the grayscale image with the inverted blurred image
pencil_sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256)

# Save the output image
cv2.imwrite('pencil_sketch_output.jpg', pencil_sketch_img)
#print(pencil_sketch_img)