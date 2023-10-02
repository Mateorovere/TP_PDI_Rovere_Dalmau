# TP_PDI_Rovere_Dalmau
Nuestro Trabajo Practico para Procesamiento De Imagenes:<br>
Integrantes:<br>
Mateo Rovere<br>
Valentin Dalmau<br>

Para el primer ejercicio nos dimos cuenta que una ventana de entre 10 y 15 pixeles era lo que mejor funcionaba para este problema <br>
En el segundo ejercicio, intentamos resolverlo con cv2.connectedComponentsWithStats(), pero luego nos dimos cuenta de que el problema de diferenciar palabras era más fácil resolverlo con pytesseract. Realizamos el ejercicio primero en Google Colab y luego lo pasamos a Visual Studio Code. Nos dimos cuenta de que pytesseract detectaba un carácter menos (probablemente un espacio) en VSCODE que en Colab, por lo cual tuvimos que ajustar el código para que funcione en VSCODE. Por último, al probar en todos los formularios, descubrimos que en el formulario 4, pytesseract detecta de manera errónea la pregunta uno (mientras que en Google Colab lo hace bien).

<h2>INSTRUCIONES:</h2>
Ejercicio 2)<br>
Instalar tesseract:  https://github.com/UB-Mannheim/tesseract/wiki<br>
Agregar el tesseract al PATH: C:\Program Files\Tesseract-OCR\tesseract.exe<br>
Luego ejecutar el siguiente comando en la terminal: pip install pytesseract <br>

