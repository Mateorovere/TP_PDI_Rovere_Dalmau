
import cv2
import numpy as np

imagen = cv2.imread('formulario_05.png', cv2.IMREAD_GRAYSCALE)
umbral = 110
imagen_binarizada = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('imagen binarizada',imagen_binarizada)

suma_filas = np.sum(imagen_binarizada, axis=1)//255
suma_columnas = np.sum(imagen_binarizada, axis=0)//255
umbral_filas = 100
umbral_columnas = 100
filas_divisorias = list(np.where(suma_filas < umbral_filas)[0])
columnas_divisorias = list(np.where(suma_columnas < umbral_columnas)[0])
#print(filas_divisorias)
#print(columnas_divisorias)

celdas = {}
cant_caracteres = []
cant_palabras = []
for i in range(len(filas_divisorias)-1):
  celdas[i] = (filas_divisorias[i], filas_divisorias[i+1], columnas_divisorias[1], columnas_divisorias[2])
#print(celdas)
for i in range(len(celdas)):
  word_count = 1
  roi = imagen_binarizada[celdas[i][0]+5:celdas[i][1]-5, celdas[i][2]+5:celdas[i][3]-5]
  roi_invertido = 255- roi
  transposed_roi = np.transpose(roi_invertido)
  #lo tuve que hacer transpuesta dado que connectedComponentsWithStats funciona, selecionando primero las de menor valor en el eje Y,
  #entonces asi selecciona las de menor valor en el eje X
  retval, labels, stats, centroids = cv2.connectedComponentsWithStats(transposed_roi, 8, cv2.CV_32S)
  ix_area = (stats[:, -1] > 5) & (stats[:, -1] < 5000)
  stats = stats[ix_area,:]
  #print(stats)
  cant_caracteres.append(len(stats))
  for j in range(len(stats)-1):
     if (stats[j+1][1] - (stats[j][1] + stats[j][3])) > 8:
        word_count +=1
  cant_palabras.append(word_count)
  cv2.imshow('roi invertido', transposed_roi)
  cv2.waitKey()
     
cv2.destroyAllWindows()

print(cant_caracteres)
print(cant_palabras)

12346789

if (cant_caracteres[1] + cant_palabras[1] - 1) <= 25 and cant_palabras[1] >= 2:
   print('Nombre y apellido: OK')
else:
   print('Nombre y apellido: MAL')

if 1 < (cant_caracteres[2] + cant_palabras[2] - 1) < 4:
   print('Edad: OK')
else:
   print('Edad: Mal')

if cant_caracteres[3] <= 25 and cant_palabras[3] == 1:
   print('Mail: OK')
else:
   print('Mail: MAL')

if cant_caracteres[4] == 8 and cant_palabras[4] == 1:
   print('Legajo: OK')
else:
   print("Legajo: MAL")

if cant_caracteres[6] == 2:
   print('Pregunta 1: OK')
else:
   print('Pregunta 1: MAL')

if cant_caracteres[7] == 2:
   print('Pregunta 2: OK')
else:
   print('Pregunta 2: MAL')

if cant_caracteres[8] == 2:
   print('Pregunta 3: OK')
else:
   print('Pregunta 3: MAL')

if (cant_caracteres[9] + cant_palabras[9] - 1) <= 25:
   print('Comentarios: OK')
else:
   print('Comentarios: MAL')