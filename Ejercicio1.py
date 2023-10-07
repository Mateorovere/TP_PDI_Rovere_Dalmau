import cv2
import numpy as np
import matplotlib.pyplot as plt

def localeq(img, window_rows, window_cols):
    img_salida = img.copy()
    img_padded = cv2.copyMakeBorder(img, window_rows, window_rows, window_cols, window_cols, borderType=cv2.BORDER_REPLICATE)
    N_rows, N_cols = img.shape
    fila, col = (0, 0)

    for ir in range(window_rows, N_rows + window_rows):
        for ic in range(window_cols, N_cols + window_cols):
            v = img_padded[ir - window_rows:ir + window_rows + 1, ic - window_cols:ic + window_cols + 1]
            v_heq = cv2.equalizeHist(v)
            img_salida[fila, col] = v_heq[window_rows, window_cols]
            col += 1
        fila += 1
        col = 0

    return img_salida

img = cv2.imread("Imagen_con_detalles_escondidos.tif", cv2.IMREAD_GRAYSCALE)
window_rows = 15 # Número de filas de la ventana
window_cols = 15  # Número de columnas de la ventana
cv2.imshow('imagen ecualizada', localeq(img, window_rows, window_cols))
cv2.waitKey(0)
