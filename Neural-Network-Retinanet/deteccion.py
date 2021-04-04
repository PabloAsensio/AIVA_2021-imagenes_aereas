###### LOAD NECESSARY MODULES ######

# show images inline
# %matplotlib inline

# automatically reload modules when they have changed
# %load_ext autoreload
# %autoreload 2

# import keras
import keras

# import keras_retinanet
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu

# import miscellaneous modules
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time

# use this to change which GPU to use
gpu = 0

# set the modified tf session as backend in keras
setup_gpu(gpu)

###### LOAD RETINANET MODEL #####
# adjust this to point to your downloaded/trained model
# models can be downloaded here: https://github.com/fizyr/keras-retinanet/releases
model_path = os.path.join('inference', 'model.h5')

# load retinanet model
model = models.load_model(model_path, backbone_name='resnet50')

# if the model is not converted to an inference model, use the line below
# see: https://github.com/fizyr/keras-retinanet#converting-a-training-model-to-inference-model
# model = models.convert_model(model)

# print(model.summary())

# load label to names mapping for visualization purposes
labels_to_names = {0: 'tree'}

##### RUN DETECTIION ON EXAMPLE #####
# load image
img_path = './test_images'
# txt_path='./deteccion/deteccion-0.5'
for idx, img_name in enumerate(sorted(os.listdir(img_path))):
    filepath = os.path.join(img_path, img_name)
    image = read_image_bgr(filepath)
    # copy to draw on
    draw = image.copy()
    # draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

    # preprocess image for network
    image = preprocess_image(image)
    image, scale = resize_image(image)

    # process image
    start = time.time()
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
    print("processing time: ", time.time() - start)

    # correct for image scale
    boxes /= scale

    #file = open(os.path.join(txt_path, img_name[0:-4] + '.txt'), 'w')
    # visualize detections
    for box, score, label in zip(boxes[0], scores[0], labels[0]):

        print(box)
        print(score)
        # scores are sorted so we can break
        if score < 0.5:
            break
        #else:
            #file.write('gun' + " " + str(score) + " " + str(box[0]) + " " + str(box[1]) + " " + str(box[2]) + " " + str(
            #box[3]) + '\n')

        color = label_color(label)

        b = box.astype(int)
        draw_box(draw, b, color=color)

        caption = "{} {:.3f}".format(labels_to_names[label], score)
        draw_caption(draw, b, caption)

    plt.figure(figsize=(15, 15))
    plt.axis('off')
    plt.imshow(draw)
    # plt.savefig('resultados/img_name')
    cv2.imwrite('./resultados-test/{}.png'.format(img_name[0:-4]), draw)
    # plt.show()
