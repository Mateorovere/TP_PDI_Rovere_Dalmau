
#!apt-get install tesseract-ocr
#!pip install pytesseract

import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

imagen = cv2.imread('formulario_01.png', cv2.IMREAD_GRAYSCALE)

umbral = 110
_, imagen_binarizada = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)

cv2.imshow('Image', imagen_binarizada)


suma_filas = np.sum(imagen_binarizada, axis=1)//255
suma_columnas = np.sum(imagen_binarizada, axis=0)//255

umbral_filas = 100
umbral_columnas = 100
filas_divisorias = list(np.where(suma_filas < umbral_filas)[0])
columnas_divisorias = list(np.where(suma_columnas < umbral_columnas)[0])
print(filas_divisorias)
print(columnas_divisorias)

celdas = {}
for i in range(len(filas_divisorias)-1):
  celdas[i] = (filas_divisorias[i], filas_divisorias[i+1], columnas_divisorias[1], columnas_divisorias[2])
print(celdas)

pytesseract.pytesseract.lang = 'spanish'
custom_config = r'--oem 3 --psm 6'

# Función para validar el campo de Nombre y Apellido
def validar_nombre_apellido(texto):
    palabras = texto.split()
    if len(palabras) < 2 or len(texto) > 26:
        return "MAL"
    else:
        return "OK"

# Función para validar el campo de Edad
def validar_edad(texto):
    if len(texto) not in [3, 4]:
        #print(texto)
        return "MAL"
    else:
        return "OK"

# Función para validar el campo de Mail
def validar_mail(texto):
    if len(texto) > 26 or "@" not in texto or "." not in texto:
        return "MAL"
    else:
        return "OK"

# Función para validar el campo de Legajo
def validar_legajo(texto):
    palabras = texto.split()
    if len(texto) != 9 or len(palabras) != 1:
        return "MAL"
    else:
        return "OK"

# Función para validar el campo de Pregunta (SI o NO)
def validar_pregunta(texto):
    palabras = texto.split()
    texto = texto.replace("|", "")
    #print(len(texto))
    if len(texto) != 2+len(palabras)-1:
        return "MAL"
    else:
        return "OK"


# Función para validar el campo de Comentarios
def validar_comentarios(texto):
    if len(texto) > 26:
        return "MAL"
    else:
        return "OK"

for i in range(len(celdas)):
  if i==5:
    continue
  roi = imagen_binarizada[celdas[i][0]+1:celdas[i][1], celdas[i][2]+1:celdas[i][3]]
  cv2.imshow('roi', roi)
  #output = cv2.connectedComponentsWithStats(roi, 8, cv2.CV_32S)
  #print(output[0])
  text = pytesseract.image_to_string(roi, config=custom_config)
  if i == 0:
        print("Tipo de formulario:", text)
  elif i == 1:
      print("Nombre y Apellido:", validar_nombre_apellido(text))
  elif i == 2:
      print("Edad:", validar_edad(text))
  elif i == 3:
      print("Mail:", validar_mail(text))
  elif i == 4:
      print("Legajo:", validar_legajo(text))
  elif i >= 6 and i <= 8:
      print(f"Pregunta {i - 5}:", validar_pregunta(text))
  elif i == 9:
      print("Comentarios:", validar_comentarios(text))

