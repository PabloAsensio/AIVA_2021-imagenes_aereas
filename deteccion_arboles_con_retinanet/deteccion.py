##### DETECCIÓN DE ÁRBOLES EN IMÁGENES AÉREAS CON RETINANET #####

# Paquetes necesarios
import keras
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--images_test_path",
    help="Ruta donde se encuentran las imágenes sobre las que se quiere hacer la detección",
    required=True,
    type=str,
)
parser.add_argument(
    "--output-path",
    help="Ruta donde se van a guardar las imágenes con la detección",
    required=True,
    type=str,
)
args = parser.parse_args()

images_path = args.images_test_path
output_path = args.output_path

# Seleccionar GPU
gpu = 0
setup_gpu(gpu)

###### LOAD RETINANET MODEL #####
# Cargar el modelo
model_path = os.path.join("inference", "model.h5")

# Cargar el modelo preentrenado
model = models.load_model(model_path, backbone_name="resnet50")

# Convertir etiquetas a nombres
labels_to_names = {0: "tree"}

time1 = time.time()
for idx, img_name in enumerate(sorted(os.listdir(images_path))):
    start_time = time.time()
    filepath = os.path.join(images_path, img_name)
    image = read_image_bgr(filepath)
    draw = image.copy()

    # Preprocesar la imagen para la red
    image = preprocess_image(image)
    image, scale = resize_image(image)

    # Se procesa la imagen
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))

    # Se escalan las bbox
    boxes /= scale

    # Visualizar las detecciones
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        # Bboxes con puntuaciones menores a 0.5 no se tienen en cuenta,
        # estan ordenadas de mayor a menor, por eso break
        if score < 0.5:
            break

        color = label_color(label)
        b = box.astype(int)
        draw_box(draw, b, color=color)
        caption = "{} {:.3f}".format(labels_to_names[label], score)
        draw_caption(draw, b, caption)

    print(
        "Tiempo ejecución " + img_name + ":",
        str(round(time.time() - start_time, 3)),
        "segundos",
    )
    cv2.imwrite(os.path.join(output_path, img_name[0:-4] + ".png"), draw)

print("\n---------- DETECCCIÓN FINALIZADA ----------")
print("Tiempo total:", str(round(time.time() - time1, 3)), "segundos")
