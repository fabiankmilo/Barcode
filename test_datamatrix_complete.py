#import numpy as np
import cv2
from pylibdmtx import pylibdmtx
from pylibdmtx.pylibdmtx import decode
import os
import time

# codigo de prueba para test de imagenes 
# este cod lee las 27 etiquetas, procesa y obtiene la salida con 3 camaras

def coordenadas():

    # usamos la imagen tomada desde la camara para procesarla
    image_1 = cv2.imread('image_test_arriba.png', cv2.IMREAD_UNCHANGED)
    image_2 = cv2.imread('image_test_centro.png', cv2.IMREAD_UNCHANGED)
    image_3 = cv2.imread('image_test_abajo.png', cv2.IMREAD_UNCHANGED)
   
# Coordenadas para camara de arriba
    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 1
    (x1, y1, x2, y2) = (650, 200, 1050, 600)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 2
    (x3, y3, x4, y4) = (1800, 200, 2200, 600)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 3
    (x5, y5, x6, y6) = (3000, 200, 3400, 600)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 4
    (x7, y7, x8, y8) = (700, 900, 1100, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 5
    (x9, y9, x10, y10) = (1800, 900, 2200, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 6
    (x11, y11, x12, y12) = (3000, 900, 3400, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 7
    (x13, y13, x14, y14) = (700, 1700, 1100, 2100)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 8
    (x15, y15, x16, y16) = (1850, 1700, 2250, 2100)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 9
    (x17, y17, x18, y18) = (3000, 1700, 3400, 2100)
#--------------------------------------------------------------------------------------
   
    # Coordenadas para camara de centro
    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 1
    (x19, y19, x20, y20) = (600, 100, 1000, 500)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 2
    (x21, y21, x22, y22) = (1800, 100, 2200, 500)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 3
    (x23, y23, x24, y24) = (3000, 100, 3400, 500)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 4
    (x25, y25, x26, y26) = (600, 900, 1000, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 5
    (x27, y27, x28, y28) = (1750, 900, 2150, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 6
    (x29, y29, x30, y30) = (2950, 900, 3350, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 7
    (x31, y31, x32, y32) = (650, 1500, 1050, 1900)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 8
    (x33, y33, x34, y34) = (1750, 1600, 2150, 2000)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 9
    (x35, y35, x36, y36) = (2900, 1600, 3300, 2000)

#--------------------------------------------------------------------------------------
    # Coordenadas para camara de abajo
    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 1
    (x37, y37, x38, y38) = (750, 200, 1150, 600)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 2
    (x39, y39, x40, y40) = (1850, 200, 2250, 600)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 3
    (x41, y41, x42, y42) = (3000, 200, 3400, 600)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 4
    (x43, y43, x44, y44) = (700, 900, 1100, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 5
    (x45, y45, x46, y46) = (1800, 900, 2200, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 6
    (x47, y47, x48, y48) = (2900, 900, 3300, 1300)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 7
    (x49, y49, x50, y50) = (750, 1600, 1150, 2000)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 8
    (x51, y51, x52, y52) = (1800, 1600, 2200, 2000)

    # coordenadas para el primer cuadro datamatrix de foto de pack 9 - 9
    (x53, y53, x54, y54) = (2950, 1600, 3350, 2000)

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

    # recortamos las imagenes segun las ROI
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

    lista_1 = [cropped_image_1, cropped_image_2, cropped_image_3, cropped_image_4, cropped_image_5, 
              cropped_image_6, cropped_image_7, cropped_image_8, cropped_image_9,cropped_image_10, cropped_image_11, cropped_image_12, cropped_image_13, cropped_image_14, 
              cropped_image_15, cropped_image_16, cropped_image_17, cropped_image_18, cropped_image_19, cropped_image_20, cropped_image_21, cropped_image_22, cropped_image_23, 
              cropped_image_24, cropped_image_25, cropped_image_26, cropped_image_27]
    
    # para cada elemento de la lista genero una imagen recortada (ROI) y la enumero de 1 a 27
    
    count_1 = 1
    for i in lista_1:
        cv2.imwrite("cropped_image_{}.png".format(count_1), i)
        count_1 += 1

def crop(decoded, image):

    x1 = int(decoded.rect.left - 20)
    y1 = int(decoded.rect.top - decoded.rect.top)
    x2 = int(decoded.rect.left + decoded.rect.width + 20)
    #y2 = int(decoded.rect.height + decoded.rect.top + 300)
    y2 = int(400)


    im_crop = image[y1:y2, x1:x2]
    #cv2.imshow("imagen_a.png", im_crop)
    
    return im_crop

#esta funcion decodifica las imagenes recortadas y en la salida muestra la lectura del datamatrix

# funcion que decodifica imagenes
def decoder(thresh):
    # decodes all datamatrix from an image
    datamatrix = pylibdmtx.decode(thresh)
    #list_data = []

    if not datamatrix:
        print("Datamatrix Not Detected")
        with open("datamatrix_result.txt", mode ='a') as file:
                file.write("datamatrix_not_detected" + "\n")
    else:
        
        #for i in datamatrix:
        for i in range(len(datamatrix)):
            # print(decoded_objects[i].data)
            datamtx = str(datamatrix[i].data, "utf-8")
            #print(str(datamatrix[i].data, "utf-8")) #removes the b'... formatting
            print(datamtx)
            #creo archivo txt para LOG de lecturas
            with open("datamatrix_result.txt", mode ='a') as file:
                file.write(datamtx + "\n")
                #list_data.append(datamtx) # nueva linea para entregar data a desarrollo sistemas
            return thresh
        #print(list_data)

if __name__ == "__main__":

    # acceso a las camaras (activar cuando las camaras esten conectadas)
    from glob import glob

    # cam_1 = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    # cam_2 = cv2.VideoCapture(3, cv2.CAP_DSHOW) 
    # cam_3 = cv2.VideoCapture(1, cv2.CAP_DSHOW) 

    # cam_1.set(cv2.CAP_PROP_FPS, 60)
    # cam_1.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    # cam_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

    # cam_2.set(cv2.CAP_PROP_FPS, 60)
    # cam_2.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    # cam_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

    # cam_3.set(cv2.CAP_PROP_FPS, 60)
    # cam_3.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    # cam_3.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)


    # if not cam_1.isOpened():
    #     print('error camara 1')

    # if not cam_2.isOpened():
    #     print('error camara 2')

    # if not cam_3.isOpened():
    #     print('error camara 3')
 
    # while True:

    #     ret_1, frame_1 = cam_1.read()
    #     ret_2, frame_2 = cam_2.read()
    #     ret_2, frame_3 = cam_2.read()
    #     # cv2.imshow("test", frame)
    #     time.sleep(2)

    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #     # save when using 'q' key
    #     #cv2.imwrite("testing_webcam.jpg", frame)
    #         break

    #     elif cam_1.isOpened() and cam_2.isOpened() and cam_3.isOpened:

    #         img_name_1 = "image_test_abajo.png"
    #         img_name_2 = "image_test_centro.png"
    #         img_name_3 = "image_test_arriba.png"

    #         cv2.imwrite(img_name_1, frame_1)
    #         cv2.imwrite(img_name_2, frame_2)
    #         cv2.imwrite(img_name_3, frame_3)
    #         print("{} written!".format(img_name_1))
    #         print("{} written!".format(img_name_2))
    #         print("{} written!".format(img_name_3))

    #         cam_1.release()
    #         cam_2.release()
    #         cam_3.release()
    #         cv2.destroyAllWindows()
    #         break
        
    coordenadas()
    #print("listo !")
    
    # con glob nos desplazamos por las imagenes

    datamtx = sorted(glob('cropped_image_*.png'), key=os.path.getmtime)
        
    try:
        count = 1
        for datamatrixs in datamtx:

            # cargo imagenes a decodificar
            img = cv2.imread(datamatrixs)
            #img = cv2.convertScaleAbs(img, alpha=0.5, beta=30) # linea para modificar contraste
            #gray_a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # lineas para binarizar imagen
            #ret, thresh = cv2.threshold(gray_a, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            print("decodificando imagen {}".format(count))

            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # blurred = cv2.GaussianBlur(gray, (7, 7), 0)
            # T, thresh = cv2.threshold(blurred, 190, 255, cv2.THRESH_BINARY)

            count += 1
            # decodificando imagen
            img = decoder(img)
        
            #return list_data
    except:
        print("No se ha podido procesar la imagen")
        #break
    
    # os.remove("cropped_image_1.png")
    # os.remove("cropped_image_2.png")
    # os.remove("cropped_image_3.png")
    # os.remove("cropped_image_4.png")
    # os.remove("cropped_image_5.png")
    # os.remove("cropped_image_6.png")
    # os.remove("cropped_image_7.png")
    # os.remove("cropped_image_8.png")
    # os.remove("cropped_image_9.png")
    # os.remove("cropped_image_10.png")
    # os.remove("cropped_image_11.png")
    # os.remove("cropped_image_12.png")
    # os.remove("cropped_image_13.png")
    # os.remove("cropped_image_14.png")
    # os.remove("cropped_image_15.png")
    # os.remove("cropped_image_16.png")
    # os.remove("cropped_image_17.png")
    # os.remove("cropped_image_18.png")
    # os.remove("cropped_image_19.png")
    # os.remove("cropped_image_20.png")
    # os.remove("cropped_image_21.png")
    # os.remove("cropped_image_22.png")
    # os.remove("cropped_image_23.png")
    # os.remove("cropped_image_24.png")
    # os.remove("cropped_image_25.png")
    # os.remove("cropped_image_26.png")
    # os.remove("cropped_image_27.png")