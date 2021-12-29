import numpy as np
import imageio # pip install imageio
import cv2
import scipy.ndimage # pip install scipy
 
img = "pic.png"

def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
    result = front*255/(255-back)
    result[result>255] = 255
    return result.astype('uint8')

s = imageio.imread(img)
g = grayscale(s)
i= 255-g

b = scipy.ndimage.filters.gaussian_filter(i,sigma = 10)
r = dodge(b,g)
cv2.imshow("Image", r)
cv2.waitKey(0)
cv2.destroyAllWindows()




