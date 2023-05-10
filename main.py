import cv2
import os
def caturing_images(i):
    #intializing webcam
    camera = cv2.VideoCapture(0)
    if not os.path.exists('faces'):
        os.makedirs('faces')
    while True:
        ret,frame = camera.read()
        if not ret:
            print("not captured")
            break
        cv2.imshow("source faces capturing",frame)
        key = cv2.waitKey(1)
        if key == 27:
            print("closing")
            break
        elif key==32:
            i += 1
            cv2.imwrite('faces/image{}.png'.format(i),frame)
            print('faces/image{}.png'.format(i),"is captured!")
    return i
    camera.release()
    cv2.destroyAllWindows()