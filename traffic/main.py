import cv2
import imutils
# import object_detection

# cap = cv2.VideoCapture("Commonwealth_traffic.MOV")
# cap = cv2.VideoCapture("video1.mp4")

# input_file = '/Users/Henry/Desktop/personal_projects/traffic/cars.mp4'
input_file = '/Users/Henry/Desktop/personal_projects/traffic/Commonwealth_traffic.MOV'

cap = cv2.VideoCapture(input_file)
# od = object_detection()

object_detector = cv2.createBackgroundSubtractorMOG2()

while True: 
    ret, frame = cap.read()
    
    mask = object_detector.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()






# #Load the video (place it in the same path as the source code) 
# cap = cv2.VideoCapture('vid.mp4')
# while cap.isopened():
#      ret, image=cap.read()
#      if ret:
#         image= imutils.resize(image,width=min(400, image.shape[1])) 
#         #detect all the regions that has pedestrians 
#         (region,_) = hog.detectMultiscale(image,winStride=(4, 4),padding=(4, 4),scale=1.05) 
#         #draw the regions in the video
#         for (x,y,w,h) in region: 
#             cv2.rectangle(image, (x, y),(x, y + h),(0, 0, 255), 2)

#      cv2.imshow("Image", image)
#      if cv2.waitkey(25) & 0xFF== ord('q'):
#         break

# cv2.destroyAllwindows()
# #Done! Click Run.