import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('partage3clair.png')
img2 = cv.imread('keyA.png')
img3 = cv.imread('keyB.png')
img4 = cv.imread('keyC.png')
img5 = cv.bitwise_xor(img1,img2)
cv.imwrite("resA.png",img5)
img6 = cv.bitwise_xor(img5,img3)
cv.imwrite("resAB.png",img6)
img7 = cv.bitwise_xor(img6,img4)
cv.imwrite("partage3crypte.png",img7)


cv.imwrite("partage3decodee.png",cv.bitwise_xor(cv.bitwise_xor(cv.bitwise_xor(img7,img2),img3),img4))

