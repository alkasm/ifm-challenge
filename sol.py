import numpy as np
import cv2

# Params
sensitivity = 80
max_aspect = 0.5

# Setup Constructs
lower_white = np.array([0, 0, 255-sensitivity])
upper_white = np.array([255, sensitivity, 255])
kernel = np.ones((5, 5), np.uint8)
bigkernel = np.ones((10, 10), np.uint8)


frame = cv2.imread("data\216.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_white, upper_white)

# Remove noise
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# Fill blobs
mask = cv2.dilate(mask, bigkernel, iterations=2)
# Close blobs
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, bigkernel)

_, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours for tags
ouput_contours = []
found_tags = []
for i, e in enumerate(contours):
	# Throw out small blobs
	if cv2.contourArea(e) < mask.size * 0.001:
		continue
	# Throw out big blobs
	if cv2.contourArea(e) > mask.size * 0.1:
		continue
	e = cv2.convexHull(e)
	tl, wh, theta = cv2.minAreaRect(e)
	# Throw out high aspect ratio blobs
	if max(wh)*max_aspect > min(wh):
		continue
	found_tags.append((tl, wh, theta))
	box = cv2.boxPoints((tl, wh, theta))
	ouput_contours.append(np.int0(box))

contours = ouput_contours

mask = cv2.merge((mask, mask, mask))

mask = cv2.drawContours(mask, contours, -1, (0, 255, 0), 3)
frame = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)

cv2.waitKey(0)
