import cv2
img=cv2.imread('vikas.jpg')
cv2.imshow('vikasFriend',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
gray=cv2.imread('vikas.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('vikasFriend',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()