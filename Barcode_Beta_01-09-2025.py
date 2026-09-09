import cv2
from pylibdmtx.pylibdmtx import decode
from concurrent.futures import ThreadPoolExecutor
import os

# True para guardar recortes y verificar imagenes
guardar_recortes = True
pruebas = (1000, 200, 2500, 2000) 
if guardar_recortes:
    os.makedirs("C:/pythonFiles/files", exist_ok=True)

ruta_txt = os.path.join("C:/pythonFiles/datamatrix_result.txt")
# x1 y1 x2 y2
A9 = (500, 50, 1400, 650) #A9 
B9 = (1650, 50, 2800, 650) #B9
C9 = (2800, 50, 3800, 650) #C9 
A8 = (400, 700, 1200, 1400) #A8
B8 = (1650, 700, 2800, 1400) #B8
C8 = (2800, 700, 3800, 1400) #C8
A7 = (400, 1500, 1200, 2900) #A7
B7 = (1650, 1450, 2800, 2900) #B7
C7 = (2800, 1500, 3800, 2900) #C7

A6 = (400, 50, 1200, 650) #A6
B6 = (1650, 50, 2800, 650) #B6
C6 = (2800, 50, 3600, 650) #C6
A5 = (400, 700, 1200, 1500)#A5
B5 = (1650, 700, 2800, 1500)#B5
C5 = (2800, 700, 3600, 1500) #C5
A4 = (400, 1400, 1200, 2400) #A4
B4 = (1650, 1400, 2800, 2400) #B4
C4 = (2800, 1400, 3600, 2400) #C4

A3 = (400, 50, 1200, 750) #A3
B3 = (1650, 50, 2800, 750) #B3
C3 = (2800, 50, 3600, 750) #C3
A2 = (400, 800, 1200, 1400) #A2
B2 = (1650, 800, 2800, 1400) #B2
C2 = (2800,800, 3600, 1400) #C2
A1 = (400, 1300, 1200, 2900) #A1
B1 = (1650, 1300, 2800, 2900) #B1
C1 = (2800, 1300, 3600, 2900) #C1

# ROIs por cámara (mismo orden: A, B, C)
ROIS = {

    # 'cam2': [ A6, B6, C6,
    #           A5, B5, C5,
    #           A4, B4, C4],

    'cam1': [ A6, B6, C6,
              A5, B5, C5,
              A4, B4, C4],

    'cam2': [ A9, B9, C9,
              A8, B8, C8,
              A7, B7, C7], 

    'cam3': [ A3, B3, C3,
              A2, B2, C2,
              A1, B1, C1] 
 

    # 'cam1': [pruebas, pruebas, pruebas,
    #          pruebas, pruebas, pruebas,
    #          pruebas, pruebas, pruebas],
    # 'cam2': [pruebas, pruebas, pruebas,
    #          pruebas, pruebas, pruebas,
    #          pruebas, pruebas, pruebas],
    # 'cam3': [pruebas, pruebas, pruebas,
    #          pruebas, pruebas, pruebas,
    #          pruebas, pruebas, pruebas],

}



# Esta lista se crea para organizar las ROIs segun el orden de las lecturas 
# tener en cuenta el orden de la lista de arriba
nombres_rois = [
    "A6", "B6", "C6", "A5", "B5", "C5", "A4", "B4", "C4", # camara 2
    "A9", "B9", "C9", "A8", "B8", "C8", "A7", "B7", "C7",  # camara 3
    "A3", "B3", "C3", "A2", "B2", "C2", "A1", "B1", "C1" # camara 1
    
    
]

def capturar_imagenes():
    frames = []
    for i in range(0, 3):  # camaras 0 a 3
        cam = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
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
        ruta = os.path.join("C:/pythonFiles/files", f"{nombre_recorte}.png")
        cv2.imwrite(ruta, crop)
    result = decode(crop)
    return result[0].data.decode('utf-8') if result else "0"

def procesar_todo():
    frames = capturar_imagenes()
    if len(frames) != 3:
        print("no se capturaron todas las imagenes")
        return

    resultados_codigos = []
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
            # print(combinado)

        # Guardar en archivo .txt separado por comas, sin saltos de línea
        with open(ruta_txt, "a", encoding="utf-8") as f:
            # f.write(",".join(resultados_con_nombres))
            f.write(f"{resultados_con_nombres}" + ",")

    return resultados_con_nombres

if __name__ == "__main__":
    # resultados = procesar_todo()
    lista2 = procesar_todo()
    print(lista2)