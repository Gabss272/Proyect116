import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Mercury", (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Venus", (150, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Earth", (250, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Mars", (350, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Jupiter", (450, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Saturn", (550, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Uranus", (650, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Neptune", (750, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

cv2.imshow("Output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_system_with_name.jpg", img)