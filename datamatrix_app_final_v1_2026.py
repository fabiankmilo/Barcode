 
# # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Nueva versión JUNIO
# # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import cv2
from pylibdmtx.pylibdmtx import decode
from concurrent.futures import ThreadPoolExecutor
import os

# True para guardar recortes y verificar imagenes
guardar_recortes = True
# pruebas = (400, 200, 600, 700) 
if guardar_recortes:
    # os.makedirs("C:/Proyectos/pythonFiles/files", exist_ok=True) # ruta anterior
    os.makedirs("C:/Proyectos/Barcode/files", exist_ok=True) # nueva ruta nuevo PC

ruta_txt = os.path.join("C:/Proyectos/Barcode/datamatrix_result.txt")


A9 = (400, 30, 1200, 650) #A9 
B9 = (1700, 10, 2600, 600) #B9
C9 = (2600, 10, 3600, 700) #C9 
A8 = (400, 700, 1200, 1300) #A8
B8 = (1700, 650, 2500, 1350) #B8
C8 = (2550, 650, 3450, 1350) #C8
A7 = (400, 1350, 1200, 2250) #A7
B7 = (1550, 1300, 2700, 2700) #B7
C7 = (2750, 1300, 3750, 2750) #C7

A6 = (450, 200, 1300, 950) #A6
B6 = (1550, 150, 2700, 800) #B6
C6 = (2800, 200, 3600, 850) #C6
A5 = (450, 850, 1250, 1650)#A5
B5 = (1550, 800, 2700, 1600)#B5
C5 = (2800, 800, 3600, 1600) #C5
A4 = (600, 1600, 1400, 3000) #A4
B4 = (1550, 1500, 2700, 2500) #B4
C4 = (2800, 1550, 3600, 2550) #C4

A3 = (500, 50, 1300, 800) #A3
B3 = (1550, 50, 2700, 800) #B3
C3 = (2800, 50, 3600, 800) #C3
A2 = (500, 750, 1300, 1450) #A2
B2 = (1550, 750, 2700, 1450) #B2
C2 = (2800, 750, 3600, 1450) #C2
A1 = (600, 1400, 1400, 2900) #A1
B1 = (1500, 1350, 2600, 2950) #B1
C1 = (2800, 1400, 3600, 2900) #C1



# ROIs por cámara (mismo orden: A, B, C)
ROIS = {

    'cam1': [ A3, B3, C3,
              A2, B2, C2,
              A1, B1, C1], 

    'cam2': [ A6, B6, C6,
              A5, B5, C5,
              A4, B4, C4],

    'cam3': [ A9, B9, C9,
              A8, B8, C8,
              A7, B7, C7]   

}

# Esta lista se crea para organizar las ROIs segun el orden de las lecturas 
# tener en cuenta el orden de la lista de arriba
nombres_rois = [
    "A3", "B3", "C3", "A2", "B2", "C2", "A1", "B1", "C1", # camara 1
    "A6", "B6", "C6", "A5", "B5", "C5", "A4", "B4", "C4", # camara 2
    "A9", "B9", "C9", "A8", "B8", "C8", "A7", "B7", "C7",  # camara 3

]

def capturar_imagenes():
    frames = []
    for i in range(0, 3):  # camaras 0 a 3
        cam = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
        cam.set(cv2.CAP_PROP_AUTOFOCUS, 1)
        if not cam.isOpened():
            print(f"Error al abrir la camara {i}")
        else:
            ret, frame = cam.read()
            if ret:
                # print(f"camara {i} capturada correctamente")
                frames.append(frame)
            else:
                print(f"no se pudo capturar imagen de la camara {i}")
            cam.release()
    return frames

def decodificar_roi(imagen, roi, nombre_recorte):
    x1, y1, x2, y2 = roi
    crop = imagen[y1:y2, x1:x2]
    if guardar_recortes:
        ruta = os.path.join("C:/Proyectos/Barcode/files", f"{nombre_recorte}.png")
        cv2.imwrite(ruta, crop)
    result = decode(crop)
    return result[0].data.decode('utf-8') if result else "0"

def procesar_todo():
    frames = capturar_imagenes()
    if len(frames) != 3:
        print("no se capturaron todas las imagenes")
        return

    # resultados_codigos = []
    with ThreadPoolExecutor() as executor:
        tareas = []

        all_rois = list(ROIS['cam1']) + list(ROIS['cam2']) + list(ROIS['cam3'])
        all_frames = [frames[0]] * 9 + [frames[1]] * 9 + [frames[2]] * 9

        for frame, roi, nombre in zip(all_frames, all_rois, nombres_rois):
            tareas.append(executor.submit(decodificar_roi, frame, roi, nombre))

        resultados_con_nombres = []
        for i, tarea in enumerate(tareas):
            
            # resultado = tarea.result()
            resultado = tarea.result().strip().replace(" ", "")
            combinado = f"{resultado}-{nombres_rois[i]}"
            resultados_con_nombres.append(combinado)
            print(combinado)

        # Guardar en archivo .txt separado por comas, sin saltos de línea
        with open(ruta_txt, "a", encoding="utf-8") as f:
            # f.write(",".join(resultados_con_nombres))
            f.write(f"{resultados_con_nombres}" + ",")

    return resultados_con_nombres

if __name__ == "__main__":
    # resultados = procesar_todo()
    lista2 = procesar_todo()
    print(lista2)
