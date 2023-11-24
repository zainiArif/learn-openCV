import cv2

filePath = 'utility\children.jpg'
img = cv2.imread(filePath)

#resize image
wResize = 500
hResize = 500
resizeDimensions = (wResize, hResize)
resizeImg = cv2.resize(img, resizeDimensions, interpolation=cv2.INTER_AREA)

#reclace image
scale = 0.50
wRescale = img.shape[1]*scale
hRescale = img.shape[0]*scale
rescaleDimensions = (int(wRescale,), int(hRescale))
rescaleImg = cv2.resize(img, rescaleDimensions, interpolation=cv2.INTER_AREA)

cv2.imshow('original image', img)
cv2.waitKey(0)

cv2.imshow('resize image', resizeImg)
cv2.waitKey(0)

cv2.imshow('rescale image', rescaleImg)
cv2.waitKey(0)