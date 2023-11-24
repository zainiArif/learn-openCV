# to instal : pip install opencv-python
# or : pip install opencv-contrib-python --> more complete : main module and contribution module all install
import cv2 

filePath = 'utility/children.jpg' #file image location
img = cv2.imread(filePath) #image read
#print(type(img)) #img data type numpy array (BGR pixel information)
# print(img.shape) # result (size vertical image, size horizontal image. deep image ) deep image = BGR

cv2.imshow('image', img) #image open / show

cv2.waitKey(0) # Always open image until user close