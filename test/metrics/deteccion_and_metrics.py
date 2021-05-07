##### DETECCIÓN DE ÁRBOLES EN IMÁGENES AÉREAS CON RETINANET #####

# Paquetes necesarios
import keras
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cv2
import os
import numpy as np
import time
import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('--images_test_path',
                    help='Ruta donde se encuentran las imágenes sobre las que se quiere hacer la detección',
                    required=False,
                    default='../../images/test_images',
                    type=str)
parser.add_argument('--output-path',
                    help='Ruta donde se van a guardar las imágenes con la detección',
                    required=False,
                    default='./results_test_images',
                    type=str)
parser.add_argument('--output-path2',
                    help='Ruta donde se van a guardar las imágenes con la detección+groundtruth',
                    required=False,
                    default='./results_test_images_and_gt',
                    type=str)
args = parser.parse_args()

images_path = args.images_test_path
output_path = args.output_path
output_path2 = args.output_path2

output_path_txt = './object_detection_metrics/detections'

# Seleccionar GPU
gpu = 0
setup_gpu(gpu)

###### LOAD RETINANET MODEL #####
# Cargar el modelo
#model_path = os.path.join('keras_retinanet','inference', 'model.h5')
model_path = os.path.join('..','..','src','model', 'model.h5')

# Cargar el modelo preentrenado
model = models.load_model(model_path, backbone_name='resnet50')

# Convertir etiquetas a nombres
labels_to_names = {0: 'tree'}

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

    # Se crea el archivo .txt para la imagen actual
    file = open(os.path.join(output_path_txt, img_name[0:-4] + '.txt'), 'w')

    # Visualizar las detecciones
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        # Bboxes con puntuaciones menores a 0.5 no se tienen en cuenta
        if score < 0.5:
            break
        else:
            file.write(
                'tree' + " " + str(score) + " " + str(box[0]) + " " + str(box[1]) + " " + str(box[2]) + " " + str(
                    box[3]) + '\n')

        color = label_color(label)
        b = box.astype(int)
        draw_box(draw, b, color=color)
        caption = "{} {:.3f}".format(labels_to_names[label], score)
        draw_caption(draw, b, caption)

    print('Tiempo ejecución ' + img_name + ':', str(round(time.time() - start_time, 3)), 'segundos')
    cv2.imwrite(os.path.join(output_path, img_name[0:-4] + '.png'), draw)

    # Se añaden las bbox de ground truth a la imagen
    xml_file=os.path.join('object_detection_metrics', 'groundtruths_xml',img_name[0:-4]+'.xml')
    with open(xml_file):
        root = ET.parse(xml_file).getroot()
        for obj in root.findall('object'):
            # obj_name = obj.find('name').text
            bndbox = obj.find('bndbox')
            left = int(bndbox.find('xmin').text)
            top = int(bndbox.find('ymin').text)
            right = int(bndbox.find('xmax').text)
            bottom = int(bndbox.find('ymax').text)

            #cv2.rectangle(draw, (left, top), (right, bottom), (0, 255, 0), 2)

            center = (int((left + right) / 2), int((top + bottom) / 2))
            radio = min(int((right - left) / 2), int((bottom - top) / 2))
            cv2.circle(draw, center, radio, (0,255,0), 2)
            cv2.circle(draw, center, 1, (0,255, 0), 2)

            cv2.imwrite(os.path.join(output_path2, img_name[0:-4] + '.png'), draw)

    #plt.show()

print('\n---------- DETECCCIÓN FINALIZADA ----------\n\n')
print('Tiempo total:', str(round(time.time() - time1, 3)), 'segundos')

# Cálculo de métricas
print('---------- CÁLCULO DE MÉTRICAS ----------')
os.system('python ./object_detection_metrics/pascalvoc.py --savepath ../results_metrics')