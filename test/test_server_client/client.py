import base64
import http.client
import json

import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path_input_img',
                    help='Path of the input image',
                    required=True,
                    type=str)
parser.add_argument('--path_output_img',
                    help='Path where the output image will be saved',
                    required=False,
                    default='./output_img.png',
                    type=str)

args = parser.parse_args()
path_input_img = args.path_input_img
path_output_img = args.path_output_img

if __name__ == "__main__":

    # Cargamos una imagen, luego va a base64, a un mapa y a un JSON
    img = cv2.imread(path_input_img)
    png_encoded_img = cv2.imencode('.jpg', img)

    base64_encoded_img = base64.b64encode(png_encoded_img[1])

    message = {'img': base64_encoded_img.decode('UTF-8')}
    json_message = json.dumps(message)

    # Creamos conexión, cabecera y enviamos el mensaje con un POST
    headers = {'Content-type': 'application/json'}

    connection = http.client.HTTPConnection('127.0.0.1', port=8000)
    connection.request('POST','', json_message, headers)

    # Esperamos la respuesta y la pintamos por pantalla
    resp = connection.getresponse()

    # decode img
    decode_resp=resp.read().decode()
    resp_dicc = json.loads(decode_resp)
    img_result=resp_dicc['result']

    jpg_img_result = base64.b64decode(img_result)
    img_final_decoded = cv2.imdecode( np.frombuffer( jpg_img_result, dtype=np.int8 ), 1)

    cv2.imwrite(path_output_img, img_final_decoded)
    cv2.imshow("Processed Image (press any key to exit)", img_final_decoded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

