import cv2
import numpy as np
import matplotlib.pyplot as plt

def localeq(img, window):
    img_salida = img.copy()
    img_padded = cv2.copyMakeBorder(img, window, window, window, window, borderType=cv2.BORDER_REPLICATE)
    N_rows, N_cols = img.shape
    fila, col = (0, 0)

    for ir in range(window, N_rows + window):
        for ic in range(window, N_cols + window):
            v = img_padded[ir - window:ir + window + 1, ic - window:ic + window + 1]
            v_heq = cv2.equalizeHist(v)
            img_salida[fila, col] = v_heq[window, window]
            col += 1
        fila += 1
        col = 0

    return img_salida

img = cv2.imread("Imagen_con_detalles_escondidos.tif", cv2.IMREAD_GRAYSCALE)
plt.imshow(localeq(img,13),cmap='gray')
