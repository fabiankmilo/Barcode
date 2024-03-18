import cv2

def camaras():

    cam1 = cv2.VideoCapture(1, cv2.CAP_DSHOW) # camara de abajo # 1
    cam2 = cv2.VideoCapture(0, cv2.CAP_DSHOW) # camara del centro # 0
    cam3 = cv2.VideoCapture(3, cv2.CAP_DSHOW) # camara de arriba # 3
    cam3.set(cv2.CAP_PROP_FPS, 60)

    # cam3 = cv2.VideoCapture(1) # camara de arriba

    cam1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    cam2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    cam3.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam3.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


    if not cam1.isOpened():
        print('error camara 1')

    if not cam2.isOpened():
        print('error camara 2')

    if not cam3.isOpened():
        print('error camara 3')

    while True:

        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()
        ret3, frame3 = cam3.read()

        #frame = cv2.hconcat([frame1, frame2, frame3])
        cv2.imshow("Camera_1", frame1)
        cv2.imshow("Camera_2", frame2)
        cv2.imshow("Camera_3", frame3)
        cv2.waitKey(1)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            
            #cam1.release()
            #cam2.release()
            cam3.release()
            break

#cv2.destroyAllWindows()
camaras()