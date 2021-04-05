# Tree Detector
En este repositorio se simula la experiencia empresarial entre un cliente (profesor) y empresa (alumnos).
Tree Detector es un sistema de visión artificial que resolverá el problema de conteo de árboles, así como el de detectarlos y saber su radio.

# Instalación
El equipo donde se quiera ejecutar el programa debe contar con:
* Python 3.7
* CUDA 10.0
* cuDNN 7.4

Los pasos a seguir para la ejecución del programa son los siguientes:
1. Clonar este repositorio
~~~
git clone https://github.com/pasensio97/AIVA_2021-imagenes_aereas
~~~

2. Navegar en la ventana de comandos(cmd) hasta la carpeta './AIVA_20201-imagenes_aereas/deteccion_arboles_con_retinanet'
3. Crear entorno virtual con virtualenv
~~~
virtualenv venv
~~~
4. Activar el entorno virtual
~~~
venv\Scripts\activate
~~~
5. Una vez dentro del entorno virtual, instalar las librerías indicadas en el archivo requirements.txt
~~~
pip install -r requirements
~~~
6. En este punto ya se tienen todas las librerías necesarias para la ejecución del archivo 'deteccion.py', que es el encargado de realizar la detección de árboles. Como argumentos de entrada se le pasa la ruta de la carpeta donde estén guardadas las imágenes de test y la ruta de la carpeta de salida donde se guardarán las imágenes con la detección realizada.
~~~
python deteccion.py --images_test_path ./test_images --output-path ./resultados_test
~~~
