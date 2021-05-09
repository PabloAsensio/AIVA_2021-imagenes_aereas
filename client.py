import argparse
import base64
import http.client
import json

import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--input',
                    help='Path of the input image',
                    required=True,
                    type=str)
parser.add_argument('--output',
                    help='Path where the output image will be saved',
                    required=False,
                    default='./output_img.png',
                    type=str)

args = parser.parse_args()
input = args.input
output = args.output

if __name__ == "__main__":

    # We load an image, then it goes to base64, a map and a JSON
    img = cv2.imread(input)

    # Encode image
    encoded_img = cv2.imencode('.jpg', img)

    # Image to Base64
    base64_encoded_img = base64.b64encode(encoded_img[1])

    # Base64 in a JSON
    message = {'img': base64_encoded_img.decode('UTF-8')}
    json_message = json.dumps(message)

    # We create connection, header and send the message with a POST
    headers = {'Content-type': 'application/json'}

    connection = http.client.HTTPConnection('127.0.0.1', port=8000)
    connection.request('POST','', json_message, headers)

    # We wait for the response and we paint it
    resp = connection.getresponse()

    # Decoding img
    decode_resp=resp.read().decode()
    resp_dicc = json.loads(decode_resp)
    img_result=resp_dicc['result']

    # Base64 decoding
    jpg_img_result = base64.b64decode(img_result)

    # Processed Image
    img_final_decoded = cv2.imdecode( np.frombuffer( jpg_img_result, dtype=np.int8 ), 1)

    cv2.imwrite(output, img_final_decoded)
    cv2.imshow("Processed Image (press any key to exit)", img_final_decoded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()