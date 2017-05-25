import collections

import numpy as np
import cv2

# Params
sensitivity = 80
max_aspect = 0.5

# Setup Constructs
lower_white = np.array([0, 0, 255 - sensitivity])
upper_white = np.array([255, sensitivity, 255])
kernel = np.ones((5, 5), np.uint8)
bigkernel = np.ones((10, 10), np.uint8)
out_data = collections.namedtuple('out_data', 'uv theta p a mu')


frame = cv2.imread("data\\506.jpg")
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
	if max(wh) * max_aspect > min(wh):
		continue
	w, h = wh
	box = cv2.boxPoints((tl, wh, theta))
	ouput_contours.append(np.int0(box))

	# Confidence is the percent of the roi that is not black
	cmask = np.zeros(mask.shape, dtype=np.uint8)
	cv2.fillPoly(cmask, [np.int32(box)], 255)
	cmask = cv2.bitwise_and(cmask, mask)
	found_tags.append(
		out_data(uv=tl, theta=theta, p=2 * w + 2 * h, a=w * h,
				mu=1 - abs((h * w - np.count_nonzero(cmask)) / (h * w))))

contours = ouput_contours

mask = cv2.merge((mask, mask, mask))

mask = cv2.drawContours(mask, contours, -1, (0, 255, 0), 3)
frame = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

for item in found_tags:
	print item

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)

cv2.imwrite('frame2.png', frame)
cv2.imwrite('mask2.png', mask)

cv2.waitKey(0)
