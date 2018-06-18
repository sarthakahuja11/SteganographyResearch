import cv2
import numpy as np

def convert_img_to_dct(img):
	b,g,r=cv2.split(img)
	dct_b=cv2.dct(np.float32(b)/255.0)
	dct_g=cv2.dct(np.float32(g)/255.0)
	dct_r=cv2.dct(np.float32(r)/255.0)
	array_to_nn=np.ndarray(img.shape, dtype=np.float32)
	array_to_nn[:,:,0]=dct_b
	array_to_nn[:,:,1]=dct_g
	array_to_nn[:,:,2]=dct_r
	return array_to_nn

def convert_dct_to_img(dct):
	b=cv2.dct(array_to_nn[:,:,0],flags=cv2.DCT_INVERSE)
	g=cv2.dct(array_to_nn[:,:,1],flags=cv2.DCT_INVERSE)
	r=cv2.dct(array_to_nn[:,:,2],flags=cv2.DCT_INVERSE)
	img=cv2.merge([b,g,r])
	return img


img=cv2.imread('0_img.jpg')
array_to_nn=convert_img_to_dct(img)
print(array_to_nn)
img2=convert_dct_to_img(array_to_nn)
cv2.imshow("Original image",img)
cv2.imshow("Returned image",img2)
cv2.waitKey()
