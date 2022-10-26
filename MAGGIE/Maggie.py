#llamar a la API
import requests
import csv
import time

while True:
   URL= 'https://thesimpsonsquoteapi.glitch.me/quotes'
  
  #Obtenemos el paquete/caja que nos viene de ahi con el get'
   respuesta = requests.get(url=URL)
   
  #extraemos los datos en formato JSON
   datos = respuesta.json()
   estado = respuesta.status_code
  #accedemos a datos, y especificamente a la clave donde esta el chiste
  #y lo guardamos en una variable
   frase_simpson:str = datos[0]['quote']
   autor:str = datos[0]['character']
   

   if autor == 'Lisa':
    #guardar la frase en csv de Lisa
    with open('lisa.csv', 'a', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow(frase_simpson)
    print(frase_simpson)
    print(autor)
    #guardar la imagen en carpeta de Lisa
    
    time.sleep(3)

   elif autor == 'Homer Simpson':
    with open('Homer_Simpson.csv', 'a', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow(frase_simpson)
    print(frase_simpson)
    print(autor)
    #guardar la frase en csv de Homer
    
    time.sleep(3)
  
   else:
    with open('General.csv', 'a', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow(frase_simpson)
    print(frase_simpson)
    print(autor)
    print('Es otro')
    #guardar la frase en csv de General
    
    time.sleep(3)