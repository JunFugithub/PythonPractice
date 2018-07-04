import cv2

orignal = cv2.imread('cat_pikaqiu.jpg')

print(orignal.shape)
font = cv2.FONT_HERSHEY_DUPLEX
text = "+1"
cv2.circle(orignal, (770, 30), 20, (0, 0, 255), -1)
cv2.putText(orignal, text, org=(757, 35), fontFace=font, fontScale=0.6, color=(0, 0, 0), thickness=2, lineType= cv2.LINE_AA)

cv2.imshow("original", orignal)
cv2.imwrite('notification+1.jpg', orignal)