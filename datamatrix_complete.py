import cv2
#from pylibdmtx import pylibdmtx
from pylibdmtx.pylibdmtx import decode
import os
import time
#import numpy as np

# this code read 27 labels, process and get the output 
# datamatrix with 3 cameras
def captura():

# define the capture for three cameras with parameter 4k 4096x2160 pixels
    cam_1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    cam_2 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam_3 = cv2.VideoCapture(3, cv2.CAP_DSHOW)  

# parameters high resolucion 4K
    
    #cam_1.set(cv2.CAP_PROP_FPS, 60)
    cam_1.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
    cam_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

    #cam_2.set(cv2.CAP_PROP_FPS, 60)
    cam_2.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
    cam_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

    #cam_3.set(cv2.CAP_PROP_FPS, 60)
    cam_3.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
    cam_3.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

    if not cam_1.isOpened():
        print('error camara 1')

    if not cam_2.isOpened():
        print('error camara 2')

    if not cam_3.isOpened():
        print('error camara 3')
 
    #while True:
    
    # define variable of capture with cam function
    ret_1, frame_1 = cam_1.read()
    ret_2, frame_2 = cam_2.read()
    ret_3, frame_3 = cam_3.read()

    img_name_1 = "image_test_arriba.png"
    img_name_2 = "image_test_centro.png"
    img_name_3 = "image_test_abajo.png"

    # write images
    cv2.imwrite(img_name_1, frame_1)
    cv2.imwrite(img_name_2, frame_2)
    cv2.imwrite(img_name_3, frame_3)
    print("{} written!".format(img_name_1))
    print("{} written!".format(img_name_2))
    print("{} written!".format(img_name_3))
    
    # ending cameras
    cam_1.release()
    cam_2.release()
    cam_3.release()
    cv2.destroyAllWindows()

def coordenadas():

    # joint the images for process
    image_1 = cv2.imread('image_test_arriba.png', cv2.IMREAD_UNCHANGED)
    image_2 = cv2.imread('image_test_centro.png', cv2.IMREAD_UNCHANGED)
    image_3 = cv2.imread('image_test_abajo.png', cv2.IMREAD_UNCHANGED)
   
# coordinates ROI for high camera
    # coordinates for box # 25 in image  
    (x1, y1, x2, y2) = (600, 200, 1000, 600)

    # coordinates for box # 26 in image  
    (x3, y3, x4, y4) = (1900, 200, 2300, 600)

    # coordinates for box # 27 in image  
    (x5, y5, x6, y6) = (3000, 200, 3400, 600)

    # coordinates for box # 22 in image
    (x7, y7, x8, y8) = (800, 900, 1200, 1300)

    # coordinates for box # 23 in image 
    (x9, y9, x10, y10) = (1900, 900, 2300, 1300)

    # coordinates for box # 24 in image 
    (x11, y11, x12, y12) = (3000, 900, 3400, 1300)

    # coordinates for box # 19 in image 
    (x13, y13, x14, y14) = (800, 1600, 1200, 2000)

    # coordinates for box # 20 in image 
    (x15, y15, x16, y16) = (1800, 1600, 2200, 2000)

    # coordinates for box # 21 in image 
    (x17, y17, x18, y18) = (3000, 1600, 3400, 2000)
#--------------------------------------------------------------------------------------
   
# Coordinates ROI for center camera
    # coordinates for box # 16 in image
    (x19, y19, x20, y20) = (700, 200, 1100, 600)

    # coordinates for box # 17 in image
    (x21, y21, x22, y22) = (1800, 200, 2200, 600)

    # coordinates for box # 18 in image
    (x23, y23, x24, y24) = (3000, 200, 3400, 600)

    # coordinates for box # 13 in image
    (x25, y25, x26, y26) = (700, 900, 1100, 1300)

    # coordinates for box # 14 in image
    (x27, y27, x28, y28) = (1800, 900, 2200, 1300)

    # coordinates for box # 15 in image
    (x29, y29, x30, y30) = (2900, 900, 3300, 1300)

    # coordinates for box # 10 in image
    (x31, y31, x32, y32) = (600, 1500, 1000, 1900)

    # coordinates for box # 11 in image
    (x33, y33, x34, y34) = (1800, 1500, 2200, 1900)

    # coordinates for box # 12 in image
    (x35, y35, x36, y36) = (2900, 1600, 3300, 2000)

#--------------------------------------------------------------------------------------
# Coordinates ROI for low camera
    # coordinates for box # 7 in image ==========> image 1 in camera
    (x37, y37, x38, y38) = (700, 200, 1100, 600)

    # coordinates for box # 8 in image ==========> image 2 in camera
    (x39, y39, x40, y40) = (1800, 200, 2300, 600)

    # coordinates for box # 9 in image ==========> image 3 in camera
    (x41, y41, x42, y42) = (3000, 200, 3500, 600)

    # coordinates for box # 4 in image ==========> image 4 in camera
    (x43, y43, x44, y44) = (700, 900, 1100, 1300)

    # coordinates for box # 5 in image ==========> image 5 in camera
    (x45, y45, x46, y46) = (1800, 900, 2200, 1300)

    # coordinates for box # 6 in image ==========> image 6 in camera
    (x47, y47, x48, y48) = (3000, 900, 3400, 1300)

    # coordinates for box # 1 in image ==========> image 7 in camera
    (x49, y49, x50, y50) = (700, 1600, 1100, 2000)

    # coordinates for box # 2 in image ==========> image 8 in camera
    (x51, y51, x52, y52) = (1800, 1600, 2200, 2000)

    # coordinates for box # 3 in image ==========> image 9 in camera
    (x53, y53, x54, y54) = (3000, 1600, 3400, 2000)

    cropped_image_1 = image_1[y1:y2, x1:x2]
    cropped_image_2 = image_1[y3:y4, x3:x4]
    cropped_image_3 = image_1[y5:y6, x5:x6]
    cropped_image_4 = image_1[y7:y8, x7:x8]
    cropped_image_5 = image_1[y9:y10, x9:x10]
    cropped_image_6 = image_1[y11:y12, x11:x12]
    cropped_image_7 = image_1[y13:y14, x13:x14]
    cropped_image_8 = image_1[y15:y16, x15:x16]
    cropped_image_9 = image_1[y17:y18, x17:x18]

    cropped_image_10 = image_2[y19:y20, x19:x20]
    cropped_image_11 = image_2[y21:y22, x21:x22]
    cropped_image_12 = image_2[y23:y24, x23:x24]
    cropped_image_13 = image_2[y25:y26, x25:x26]
    cropped_image_14 = image_2[y27:y28, x27:x28]
    cropped_image_15 = image_2[y29:y30, x29:x30]
    cropped_image_16 = image_2[y31:y32, x31:x32]
    cropped_image_17 = image_2[y33:y34, x33:x34]
    cropped_image_18 = image_2[y35:y36, x35:x36]

    cropped_image_19 = image_3[y37:y38, x37:x38]
    cropped_image_20 = image_3[y39:y40, x39:x40]
    cropped_image_21 = image_3[y41:y42, x41:x42]
    cropped_image_22 = image_3[y43:y44, x43:x44]
    cropped_image_23 = image_3[y45:y46, x45:x46]
    cropped_image_24 = image_3[y47:y48, x47:x48]
    cropped_image_25 = image_3[y49:y50, x49:x50]
    cropped_image_26 = image_3[y51:y52, x51:x52]
    cropped_image_27 = image_3[y53:y54, x53:x54]

    # we crop the images according to ROI
    # high camera
    # cropped_image_25 = image_1[y1:y2, x1:x2]
    # cropped_image_26 = image_1[y3:y4, x3:x4]
    # cropped_image_27 = image_1[y5:y6, x5:x6]
    # cropped_image_22 = image_1[y7:y8, x7:x8]
    # cropped_image_23 = image_1[y9:y10, x9:x10]
    # cropped_image_24 = image_1[y11:y12, x11:x12]
    # cropped_image_19 = image_1[y13:y14, x13:x14]
    # cropped_image_20 = image_1[y15:y16, x15:x16]
    # cropped_image_21 = image_1[y17:y18, x17:x18]

    # # center camera
    # cropped_image_16 = image_2[y19:y20, x19:x20]
    # cropped_image_17 = image_2[y21:y22, x21:x22]
    # cropped_image_18 = image_2[y23:y24, x23:x24]
    # cropped_image_13 = image_2[y25:y26, x25:x26]
    # cropped_image_14 = image_2[y27:y28, x27:x28]
    # cropped_image_15 = image_2[y29:y30, x29:x30]
    # cropped_image_10 = image_2[y31:y32, x31:x32]
    # cropped_image_11 = image_2[y33:y34, x33:x34]
    # cropped_image_12 = image_2[y35:y36, x35:x36]

    # # low camera
    # cropped_image_7 = image_3[y37:y38, x37:x38]
    # cropped_image_8 = image_3[y39:y40, x39:x40]
    # cropped_image_9 = image_3[y41:y42, x41:x42]
    # cropped_image_4 = image_3[y43:y44, x43:x44]
    # cropped_image_5 = image_3[y45:y46, x45:x46]
    # cropped_image_6 = image_3[y47:y48, x47:x48]
    # cropped_image_1 = image_3[y49:y50, x49:x50]
    # cropped_image_2 = image_3[y51:y52, x51:x52]
    # cropped_image_3 = image_3[y53:y54, x53:x54]

    lista_1 = [cropped_image_1, cropped_image_2, cropped_image_3, cropped_image_4, cropped_image_5, 
              cropped_image_6, cropped_image_7, cropped_image_8, cropped_image_9,cropped_image_10, cropped_image_11, cropped_image_12, cropped_image_13, cropped_image_14, 
              cropped_image_15, cropped_image_16, cropped_image_17, cropped_image_18, cropped_image_19, cropped_image_20, cropped_image_21, cropped_image_22, cropped_image_23, 
              cropped_image_24, cropped_image_25, cropped_image_26, cropped_image_27]
    
# for each element of list, write an image of an number (indicator)
    count_1 = 1
    for i in lista_1:
        cv2.imwrite("cropped_image_{}.png".format(count_1), i)
        count_1 += 1

# this function decode the images croped and in the out read datamatrix code

def decode_data(thresh):
    # decodes all datamatrix from an image
    datamatrix = decode(thresh)
    #list_data = []

    if not datamatrix:
        print("Datamatrix Not Detected")
        with open("datamatrix_result.txt", mode ='a') as file:
                file.write("datamatrix_not_detected" + "\n")
    else:
        for i in range(len(datamatrix)):
            # print(decoded_objects[i].data)
            datamtx = str(datamatrix[i].data, "utf-8")
            #print(str(datamatrix[i].data, "utf-8")) #removes the b'... formatting
            print(datamtx)
            #creo archivo txt para LOG de lecturas
            #list_data.append(i) # nueva linea para entregar data a desarrollo sistemas (en prueba)
            #print(list_data)
            with open("datamatrix_result.txt", mode ='a') as file:
                file.write(datamtx + "\n")
            return thresh
# start functions
        
if __name__ == "__main__":

    # API glob allows you to scroll through each of the cropped images
    from glob import glob
    #import os
    
    time.sleep(1)
    captura()
    time.sleep(1)
    coordenadas()

    #datamtx = glob("cropped_image_*.png")
    datamtx = sorted(glob('cropped_image_*.png'), key=os.path.getmtime)
            
    try:
        count = 1
        for datamatrixs in datamtx:
            # charge images for decopder
            img = cv2.imread(datamatrixs)
            #img = cv2.convertScaleAbs(img, alpha=0.5, beta=50)
            #gray_a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #ret, thresh = cv2.threshold(gray_a, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            
            print("decodificando imagen {}".format(count))
            count += 1
            # decode image
            #img = decode_data(thresh)
            img = decode_data(img)


    except:
        print("No se ha podido procesar la imagen")
        #break

os.remove("cropped_image_1.png")
os.remove("cropped_image_2.png")
os.remove("cropped_image_3.png")
os.remove("cropped_image_4.png")
os.remove("cropped_image_5.png")
os.remove("cropped_image_6.png")
os.remove("cropped_image_7.png")
os.remove("cropped_image_8.png")
os.remove("cropped_image_9.png")
os.remove("cropped_image_10.png")
os.remove("cropped_image_11.png")
os.remove("cropped_image_12.png")
os.remove("cropped_image_13.png")
os.remove("cropped_image_14.png")
os.remove("cropped_image_15.png")
os.remove("cropped_image_16.png")
os.remove("cropped_image_17.png")
os.remove("cropped_image_18.png")
os.remove("cropped_image_19.png")
os.remove("cropped_image_20.png")
os.remove("cropped_image_21.png")
os.remove("cropped_image_22.png")
os.remove("cropped_image_23.png")
os.remove("cropped_image_24.png")
os.remove("cropped_image_25.png")
os.remove("cropped_image_26.png")
os.remove("cropped_image_27.png")