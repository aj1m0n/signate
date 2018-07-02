img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
tmp = img[:, :]
height, width = img.shape[:2]
if(height > width):
	size = height
	limit = width
else:
	size = width
	limit = height
start = int((size - limit) / 2)
fin = int((size + limit) / 2)
new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (size, size))
if(size == height):
	new_img[:, start:fin] = tmp
else:
	new_img[start:fin, :] = tmp
