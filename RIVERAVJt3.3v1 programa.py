#RIVERA VARGAS JUAN
import numpy as np
import cv2
from matplotlib import pyplot as plt
 
# Cargamos la imagen
original = cv2.imread("img2.jpg")
originalcopy = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (9,9), 0)
 
# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 0, 254)
 


# Buscamos los contornos
(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Mostramos el número de monedas por consola
#print("He encontrado {} objetos".format(len(contornos)))
total=0
for c in contornos:
    area =  cv2.contourArea(c)
    if area >= 60:
      if area >= 138:
        total=total+5
      elif area >= 115:
        total=total+2
      elif area >= 95:
        total=total+1
      else:
        total=total+0.5

      #print(f'Area: {area}')

print(f'El total de dinero es {total} pesos')

cv2.drawContours(original,contornos,-1,(255,0,0), 7)
#cv2.imshow("contornos", original)

#cv2.waitKey(0)


titles = ['Original','Con bordes']
images = [originalcopy,original]
miArray = np.arange(2)
for i in miArray:
  plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
 
plt.show()