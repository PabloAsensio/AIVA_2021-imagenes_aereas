# Tree Detector
En este repositorio se simula la experiencia empresarial entre un cliente (profesor) y empresa (alumnos).

Tree Detector es un sistema de visión artificial que resolverá el problema de conteo de árboles, así como el de detectarlos y saber su radio.

# Instalación
El equipo donde se quiera ejecutar el programa debe contar con:
* Python 3.6.x (comprobado en 3.6.13, posiblemente funcione en versiones posteriores)
* CUDA 11.2
* cuDNN v8.1.0 (January 26th, 2021), for CUDA 11.0,11.1 and 11.2
* Cuda Compilation tool 10.1
Los pasos a seguir para la ejecución del programa son los siguientes:

**1.** Clonar este repositorio.
~~~
git clone https://github.com/pasensio97/AIVA_2021-imagenes_aereas
~~~

**2.** Crear entorno virtual con virtualenv en la carpeta clonada.
~~~
virtualenv --python=python3.6 venv && source venv/bin/activate
~~~

**4.** Instalar las librerías indicadas en el archivo requirements.txt.
~~~
python -m pip install -r requirements.txt
~~~
Es posible que de algún error por falta de librerías o módulos. Pero son fácilmente solucionables.

**5.** Navegar en la ventana de comandos(cmd) hasta la carpeta ```./AIVA_20201-imagenes_aereas/src```.


**6.** Una vez dentro del entorno virtual, ejecutar la siguiente línea:
~~~
python setup.py build_ext --inplace
~~~


**7.** Descargar el modelo entrenado del siguiente enlace y guardarlo dentro de la carpeta 'src/model'. 

[Enlace a model.h5](https://urjc-my.sharepoint.com/:u:/g/personal/v_lomas_2020_alumnos_urjc_es/EacpLrcXskdKiNGxebzT-a0BuwnjOVyTQ0o0iaKJOjZzFQ?e=LYQbvI) 

**8.** En este punto ya se tienen todas las depencencias necesarias para la ejecución del servidor ```aplication.py```, que es el encargado de realizar la detección de árboles. 
~~~
python aplication.py
~~~

# Rendimiento del sistema
Para evaluar el rendimiento de la aplicación desarrollada se han calculado métricas, en particular la curva **Precision–Recall** y el valor de **Average Precision (AP)**, que son las métricas más populares que se utilizan para evaluar los modelos de detección de objetos. En concreto, se han utilizado las métricas que se utilizan en la conocida competición Pascal VOC, implementada en este [repositorio](https://github.com/rafaelpadilla/Object-Detection-Metrics).
Para ello, ha sido necesario realizar los siguientes pasos:
- Elaborar un conjunto de imágenes de test (no ‘vistas’ anteriormente por la red).
- Etiquetarlas manualmente para generar los archivos de ground truth para cada una de las imágenes de test.
- Pasar cada una de las imágenes de test por la red para obtener así los archivos con las detecciones realizadas.
- Calcular métricas a partir de los archivos de ground truth y las detecciones. 

La **curva Precicion - Recall** obtenida ha sido la siguiente:
<img src="../test/metrics/result_metrics/tree.png" width="550" class="center"> 
