# RETO SIMPSON
![](https://i.pinimg.com/originals/31/9c/08/319c08b4f69445ad6270a4a2d46b9f14.jpg)
## 1º RETO: MAGGIE

Los objetivos de este reto son:
- Usando google colab crear un notebook que consuma la api de los simpson y haga una consulta cada 30s a la API.
- El codigo debe guardar cada quote en un csv dentro de una carpeta con el nombre del personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos).
- Generar un fichero Docjer que copue el codigo dentro del contenedor y se ejecute de manera autonoma. El Docker que copie el codigo en una carpeta app.
- El fichero docher dbe crear al menos las carpetas Lisa y Homer e inicialmente solo coger citas de ellos dos.

### Primer paso
Acceder a la herramienta Google Colab
![Descripción de la imagen](https://www.marketing-branding.com/wp-content/uploads/2020/07/google-colaboratory-colab-guia-completa.jpg)
[ pinchando vaya al enlace]
...
### SEGUNDO PASO
A continuación pasamos a la codificación, para ello usaremos el lenguaje Pyhton
![Descripción de la imagen](https://seovalladolid.es/wp-content/uploads/2021/02/python.png)

#### Primera parte: importar las librerias necesarias
```
import requests
import csv
import time
```
A continuación pasamos a comentar que significa cada una de ellas:
- import requests: allows you to send HTTP requests using Python.
- import csv: Import plugin allows users to import items from a simple CSV (comma-separated values) file, and then map the CSV column data to multiple elements, files, and/or tags.
- import time: provides many ways of representing time in code, such as objects, numbers, and strings

#### Segunda parte: Bucle continuo + GET
Comenzamos con un While: True. De esta manera mantenemos el programa siempre en ejecución ya que el objetivo del ejercicio es que haga peticiones cada 30 segundos "él solo", sin tener que inicializarlo nosotros

Ahora bien, para hacer esta PETICIÓN es necesario usar una de los MÓDULOS que hemos importado anteriormente. Este es el REQUESTS.

Antes de nada, comentar como la API nos da la información. Esto es clave para poder extraer la información posteriormente

```
[
  {
    "quote": "Why are you pleople avoiding me? Does my withered face remind you of the grim specter of death?",
    "character": "Abe Simpson",
    "image": "https://cdn.glitch.com/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2FAbrahamSimpson.png?1497567511593",
    "characterDirection": "Right"
  }
]
```
Guardamos en una VARIABLE, la URL donde se va a hacer la PETICIÓN.
```
URL= 'https://thesimpsonsquoteapi.glitch.me/quotes'
```
Una vez eso, hacemos la PETICIÓN mediante un GET para que nos devuelva el JSON donde tendremos toda la información.
> GET: is used to request data from a specified resource.
```
   respuesta = requests.get(url=URL)
``` 
Después, extraemos el JSON y lo guardamos en una VARIABLE de nuestro código
```
   datos = respuesta.json()
   estado = respuesta.status_code
```
Finalmente, de nuestra VARIABLE donde está el JSON, accedemos específicamente al dato que queremos.
```
   frase_simpson:str = datos[0]['quote']
   autor:str = datos[0]['character']
```

#### Tercer parte: Crear un archivo CSV
Para ello vamos a utilizar el siguiente trozo de código:

```
with open('General/general.csv', 'a', newline='') as csvfile:
      spamwriter = csv.writer(csvfile)
      spamwriter.writerow(frase_simpson)
```
Es importante saber las partes que lo componen, por ello las vamos a detallar:
- with open : es una función que en función de los parametros que les demos hará determinadas acciones.
- 'General/general.csv': se divide en dos partes principalmente:
    - General/: esta es la ruta donde queremos que se cree el archivo CSV
    - general.csv: es el nombre que le queremos dar al archivo CSV
- 'a': en esta parte de la función se indica las diferentes opciones a la hora de crear el archivo. Las principales opciones son:
    - a (append): con ello añadimos frases al archivo CSV. Si no está creado, se crea automáticamente, en caso contrario, añadirá al documento lo que le hemos dicho.
    - w (write): con ello escribimos en el archivo CSV. En caso de que no exista anteriormente, lo creará de nuevas, en caso contrario **SOBREESCRIBIRÁ** lo que haya anteriormente.
    - r (read): con ello nos permite leer el archivo CSV.
- csvfile: en este caso, puede ser cualquier cosa, ya sea f, o lo que queramos pero se ha de mantener para el resto del código
- spamwriter = es una variable que puede tener cualquier nombre, pero se ha de mantener dentro de la función
- csv.writer()= en esta parte definimos como queremos que nos añada las frases. Por ejemplo si queremos separarlo por || y otros estilos.
- spamwriter.writerow(frase_simpson): aquí le decimos a la función que queremos que nos añada al archivo CSV previamente creado

#### Cuarte parte: Bucle condicional 'if'
Cuando el codigo haga la peticion a la API nos devolverá una frase con un autor, y como para el ejercicio nos pide que separemos en función de Lisa y Homer es necesario que pensemos en un pseudocódigo de esta manera 'si el autor es Lisa, guardalo en lisa y si es Homer, guardalo en Homer'

Entonces el bucle condicional que necesitamos es if con un elif ya que si no es uno será el otro.

Dentro del bucle habrá que escribir la frase del autor, por tanto el trozo de codigo quedará de esta manera

- En el caso de Lisa
```
if autor == 'Lisa':
    #guardar la frase en csv de Lisa
    with open('Lisa/lisa.csv', 'a', newline='') as csvfile:
     spamwriter = csv.writer(csvfile)
     spamwriter.writerow(frase_simpson)
```
- En el caso de Homer
```
 elif autor == 'Homer Simpson':
    with open('Homer/homer.csv', 'a', newline='') as csvfile:
     spamwriter = csv.writer(csvfile)
     spamwriter.writerow(frase_simpson)
    #guardar la frase en csv de Homer 
```

#### Quinta parte: Hacer una petición cada 30 segundos
Para ello usaremos uno de los modulos que hemos importado,time
Quedando de la siguiente manera:
```
timesleep(30)
```

